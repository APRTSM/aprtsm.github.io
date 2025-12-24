import requests
import xml.etree.ElementTree as ET
import yaml
import os
import re
from difflib import SequenceMatcher

# Configuration
DBLP_URL = "https://dblp.org/pid/202/8373.xml"
CONF_FILE = "_data/conference.yml"
JOURNAL_FILE = "_data/journal.yml"

def load_yaml(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as f:
        return yaml.safe_load(f) or []

def save_yaml(filepath, data):
    with open(filepath, 'w') as f:
        # Use allow_unicode=True to preserve accents
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

def fetch_dblp_data():
    print(f"Fetching DBLP data from {DBLP_URL}...")
    response = requests.get(DBLP_URL)
    response.raise_for_status()
    return response.content

def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def parse_authors(entry):
    authors = []
    for author in entry.findall('author'):
        authors.append(author.text)
    return ", ".join(authors)

def update_papers(xml_root):
    # Load existing data
    local_confs = load_yaml(CONF_FILE)
    local_journals = load_yaml(JOURNAL_FILE)

    new_confs = []
    new_journals = []

    # Process XML entries
    for r in xml_root.findall('r'):
        # Check for inproceedings (Conference) or article (Journal)
        conf_entry = r.find('inproceedings')
        journal_entry = r.find('article')
        
        entry = conf_entry if conf_entry is not None else journal_entry
        if entry is None:
            continue
            
        entry_type = 'conference' if conf_entry is not None else 'journal'
        
        # Extract basic info
        title = entry.find('title').text
        year = entry.find('year').text
        url = entry.find('ee').text if entry.find('ee') is not None else ""
        key = entry.attrib.get('key')
        
        # Determine venue/alias
        if entry_type == 'conference':
            venue_node = entry.find('booktitle')
            venue_code = venue_node.text if venue_node is not None else "Conference"
        else:
            venue_node = entry.find('journal')
            venue_code = venue_node.text if venue_node is not None else "Journal"
            
        # Filter out CoRR (preprints)
        if venue_code == "CoRR":
            print(f"Skipping CoRR entry: {title}")
            continue
        # Format "Revenue" field e.g. "ICSE 2024" or "TSE (2024)"
        if entry_type == 'conference':
            revenue = f"{venue_code} {year}"
        else:
            revenue = f"{venue_code} ({year})"

        authors = parse_authors(entry)

        # Prepare new record
        new_record = {
            "title": title,
            "authors": authors,
            "revenue": revenue,
            "alias": venue_code,
            "link": url,
            "doi": url,
            "key": key
        }
        
        # Match with local data
        target_list = local_confs if entry_type == 'conference' else local_journals
        match_found = False
        
        for local_item in target_list:
            # Match by Key or Fuzzy Title
            is_match = False
            if 'key' in local_item and local_item['key'] == key:
                is_match = True
            elif similar(local_item['title'], title) > 0.9:
                is_match = True
            
            if is_match:
                # Update local item but preserve extras
                local_item['title'] = title # Update title fix typos
                local_item['authors'] = authors
                local_item['revenue'] = revenue
                local_item['alias'] = venue_code
                if not local_item.get('link'): local_item['link'] = url
                if not local_item.get('doi'): local_item['doi'] = url
                local_item['key'] = key # Ensure key exists
                
                # Add to new list
                if entry_type == 'conference':
                    new_confs.append(local_item)
                else:
                    new_journals.append(local_item)
                
                match_found = True
                # Remove from target matching to avoid duplicates? 
                # Better to reconstruct list.
                break
        
        if not match_found:
            # New paper found!
            print(f"New {entry_type} found: {title}")
            if entry_type == 'conference':
                new_confs.append(new_record)
            else:
                new_journals.append(new_record)

    # Sort by year descending (simple alphanumeric reverse sort on revenue approximates this, or better parse year)
    # Let's rely on DBLP order (usually chronological) or sort by year in 'year' field? 
    # Current YML doesn't preserve 'year' field explicitly in saved file usually, but we can add it or just reverse.
    # We will just append the rest of local items that were NOT in DBLP (e.g. preprints or very new)
    
    # Actually, the logic above only builds lists from DBLP matches. 
    # We need to Keep local items that are NOT in DBLP yet (e.g. "Other" papers or unpublished).
    # But usually 'conference.yml' only has published stuff.
    # Let's trust DBLP is the source of truth for these two files.
    
    # Save files
    print(f"Saving {len(new_confs)} conference papers...")
    save_yaml(CONF_FILE, new_confs)
    print(f"Saving {len(new_journals)} journal papers...")
    save_yaml(JOURNAL_FILE, new_journals)

if __name__ == "__main__":
    if not os.path.exists('_data'):
        os.makedirs('_data')
        
    xml_data = fetch_dblp_data()
    root = ET.fromstring(xml_data)
    update_papers(root)
    print("Done.")
