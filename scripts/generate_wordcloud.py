import yaml
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

def generate_svg_wordcloud():
    # Paths
    data_dir = '_data'
    output_path = 'assets/img/wordcloud.svg'
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 1. Gather all raw text
    text_data = []

    # Parse publications
    for filename in ['journal.yml', 'conference.yml', 'paper.yml']:
        path = os.path.join(data_dir, filename)
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = yaml.safe_load(f)
                if data:
                    for item in data:
                        text_data.append(item.get('title', ''))
                        text_data.append(item.get('alias', ''))

    # Parse team members
    for filename in ['team_members.yml', 'alumni.yml']:
        path = os.path.join(data_dir, filename)
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = yaml.safe_load(f)
                if data:
                    for item in data:
                        if 'keywords' in item:
                            text_data.extend(item['keywords'])

    full_text = " ".join([str(t) for t in text_data if t])

    # 2. Filtering / Preprocessing
    stop_words = {'a', 'an', 'the', 'and', 'or', 'of', 'in', 'on', 'at', 'to', 'for', 'with', 'by', 'as', 'is', 'are', 'was', 'were', 'it', 'its', 'from', 'into', 'using', 'based', 'towards', 'beyond', 'through', 'under', 'between', 'during', 'research', 'software', 'engineering', 'automated', 'program', 'repair', 'group', 'tools', 'maintenance', 'system', 'systems', 'problem', 'approach', 'model', 'analysis', 'data'}
    
    # Custom color palette (ACM Inspired)
    def acm_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        colors = ['#008080', '#2E8B57', '#800000', '#D2691E', '#696969', '#2F4F4F', '#4682B4']
        import random
        return random.choice(colors)

    # 3. Create WordCloud
    wc = WordCloud(
        width=800,
        height=400,
        background_color=None, # Transparent
        mode="RGBA",
        max_words=60,
        stopwords=stop_words,
        color_func=acm_color_func,
        font_path=None, # System default or can specify a path to Inter/Roboto
        prefer_horizontal=0.7,
        repeat=False
    )

    wc.generate(full_text)

    # 4. Export to SVG
    svg_content = wc.to_svg(embed_font=True)
    with open(output_path, 'w') as f:
        f.write(svg_content)
    
    print(f"Successfully generated word cloud: {output_path}")

if __name__ == "__main__":
    generate_svg_wordcloud()
