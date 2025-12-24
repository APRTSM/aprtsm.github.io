import requests
import yaml
import json
import os
from datetime import datetime

# Configuration
# Selected conferences
TARGET_CONFS = ['ase', 'ease', 'esem', 'fse', 'icpc', 'icse', 'icsme', 'issta', 'msr', 'saner']
BASE_URL = "https://raw.githubusercontent.com/ccfddl/ccf-deadlines/main/conference/SE/{}.yml"
OUTPUT_FILE = "pages/data.json"

def fetch_conf_data(conf_id):
    url = BASE_URL.format(conf_id)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return yaml.safe_load(response.text)
        else:
            print(f"Failed to fetch {conf_id}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching {conf_id}: {e}")
        return None

def main():
    deadlines = []
    
    print("Fetching deadlines...")
    for conf_id in TARGET_CONFS:
        data = fetch_conf_data(conf_id)
        if not data:
            continue
            
        # Parse logic to get the *next* deadline
        # The YAML contains a list of 'confs' (years). We want the relevant one.
        # Usually the last one or one with a future deadline.
        
        # Flattened list of all deadlines
        # We want to format it as: { "name": "MSR 2025", "deadline": "2024-11-09", "url": "..." }
        
        # Handle list vs dict (CCF YAMLs seem to be a list with one item)
        conf_data = data
        if isinstance(data, list):
            if len(data) > 0:
                conf_data = data[0]
            else:
                continue

        for conf_instance in conf_data.get('confs', []):
            year = conf_instance.get('year')
            link = conf_instance.get('link')
            timeline = conf_instance.get('timeline', [])
            
            # Find the main deadline (usually the last 'deadline' entry)
            # Some entries have multiple (abstract, paper). We usually want 'deadline'.
            
            final_deadline = None
            for t in timeline:
                if 'deadline' in t:
                    final_deadline = t['deadline']
            
            if final_deadline:
                # Clean date string "YYYY-MM-DD HH:MM:SS" -> "YYYY-MM-DD"
                date_str = str(final_deadline).split(' ')[0]
                pass

        # Strategy: Get the latest year available in the file.
        # Check specific field (like 'confs' array).
        if conf_data.get('confs'):
             # Sort by year
             sorted_confs = sorted(conf_data['confs'], key=lambda x: x['year'])
             latest_conf = sorted_confs[-1]
             
             # Extract deadline
             timeline = latest_conf.get('timeline', [])
             final_deadline = None
             # Prioritize 'deadline' key
             for t in timeline:
                 if 'deadline' in t:
                     final_deadline = t['deadline']
             
             if not final_deadline:
                 # Fallback to abstract_deadline ??
                 for t in timeline:
                     if 'abstract_deadline' in t:
                         final_deadline = t['abstract_deadline']
            
             if final_deadline:
                 entry = {
                     "name": f"{conf_data['title']} {latest_conf['year']}",
                     "deadline": str(final_deadline).split(' ')[0],
                     "url": latest_conf.get('link', '')
                 }
                 deadlines.append(entry)
                 print(f"Added {entry['name']}")

    # Write to JSON
    # IMPORTANT: Jekyll reads this, so we need Front Matter? 
    # "page/data.json" in the previous implementation had front matter:
    # ---
    # layout: null
    # permalink: /data.json
    # ---
    # [ ... ]
    
    print(f"Writing {len(deadlines)} entries to {OUTPUT_FILE}...")
    
    with open(OUTPUT_FILE, 'w') as f:
        f.write("---\nlayout: null\npermalink: /data.json\n---\n")
        json.dump(deadlines, f, indent=4)
        
    print("Done.")

if __name__ == "__main__":
    main()
