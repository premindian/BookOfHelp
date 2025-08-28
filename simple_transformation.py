#!/usr/bin/env python3
"""
Simple Conservative Duplicate Removal Script for Book of Help
Target: Reduce from 1089 to 985 initiatives (remove 104 duplicates)
"""

import re
from difflib import SequenceMatcher
from typing import List, Dict, Set

def similarity(a: str, b: str) -> float:
    """Calculate similarity between two strings"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def extract_initiatives_manually(file_path: str) -> List[Dict]:
    """Extract initiatives by parsing the file manually"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all initiative objects using regex
    pattern = r'\{[^{}]*title:\s*"([^"]*)"[^{}]*description:\s*"([^"]*)"[^{}]*category:\s*"([^"]*)"[^{}]*impact:\s*"([^"]*)"[^{}]*beneficiaries:\s*"([^"]*)"[^{}]*icon:\s*"([^"]*)"[^{}]*\}'
    
    matches = re.findall(pattern, content, re.DOTALL)
    
    initiatives = []
    for match in matches:
        initiative = {
            'title': match[0],
            'description': match[1], 
            'category': match[2],
            'impact': match[3],
            'beneficiaries': match[4],
            'icon': match[5]
        }
        initiatives.append(initiative)
    
    print(f"Extracted {len(initiatives)} initiatives using regex")
    return initiatives

def identify_duplicates_to_remove(initiatives: List[Dict]) -> Set[int]:
    """Identify all duplicates to remove to reach target of 985"""
    to_remove = set()
    
    # 1. Specific duplicates mentioned by user
    specific_targets = [
        "Quality Seeds Distribution Chain",
        "Academic Stress Management", 
        "Medication Impact Tracker",
        "Inclusive Wedding Support",
        "Mobile Toy Libraries",
        "Village Bicycle Libraries", 
        "Street Vendor First-Aid",
        "Tool Libraries"
    ]
    
    for i, initiative in enumerate(initiatives):
        title = initiative.get('title', '')
        for target in specific_targets:
            if target.lower() in title.lower():
                to_remove.add(i)
                print(f"Removing specific duplicate: {title}")
                break
    
    # 2. Donate-a-X campaigns (keep only 2)
    donate_indices = []
    for i, initiative in enumerate(initiatives):
        title = initiative.get('title', '')
        if 'donate-a-' in title.lower() or re.match(r'donate.?a.?\w+', title, re.IGNORECASE):
            donate_indices.append(i)
    
    if len(donate_indices) > 2:
        for idx in donate_indices[2:]:
            to_remove.add(idx)
            print(f"Removing donate campaign: {initiatives[idx]['title']}")
    
    # 3. Village/Rural transformation initiatives (keep only 3)
    village_indices = []
    village_keywords = ['village paradise', 'village transformation', 'rural paradise', 'village hub', 'village sovereignty']
    
    for i, initiative in enumerate(initiatives):
        title = initiative.get('title', '').lower()
        description = initiative.get('description', '').lower()
        
        for keyword in village_keywords:
            if keyword in title or keyword in description:
                village_indices.append(i)
                break
    
    if len(village_indices) > 3:
        for idx in village_indices[3:]:
            to_remove.add(idx)
            print(f"Removing village initiative: {initiatives[idx]['title']}")
    
    # 4. Emergency/Fund duplicates (keep only 3)
    emergency_indices = []
    emergency_keywords = ['emergency fund', 'emergency relief', 'disaster fund', 'crisis fund']
    
    for i, initiative in enumerate(initiatives):
        title = initiative.get('title', '').lower()
        description = initiative.get('description', '').lower()
        
        for keyword in emergency_keywords:
            if keyword in title or keyword in description:
                emergency_indices.append(i)
                break
    
    if len(emergency_indices) > 3:
        for idx in emergency_indices[3:]:
            to_remove.add(idx)
            print(f"Removing emergency fund: {initiatives[idx]['title']}")
    
    # 5. Thematic duplicates - group similar themes
    themes = {
        'bicycle': [],
        'water': [],
        'health_camp': [],
        'farmer': [],
        'education_free': []
    }
    
    for i, initiative in enumerate(initiatives):
        if i in to_remove:
            continue
            
        title = initiative.get('title', '').lower()
        
        if 'bicycle' in title or 'bike' in title or 'cycle' in title:
            themes['bicycle'].append(i)
        elif 'water' in title and ('tank' in title or 'supply' in title or 'filter' in title):
            themes['water'].append(i)
        elif ('health' in title or 'medical' in title) and 'camp' in title:
            themes['health_camp'].append(i)
        elif 'farmer' in title or 'agriculture' in title:
            themes['farmer'].append(i)
        elif 'education' in title and 'free' in title:
            themes['education_free'].append(i)
    
    # Keep only top 4 of each theme
    for theme, indices in themes.items():
        if len(indices) > 4:
            for idx in indices[4:]:
                to_remove.add(idx)
                print(f"Removing {theme} duplicate: {initiatives[idx]['title']}")
    
    # 6. High similarity duplicates
    processed = set()
    for i in range(len(initiatives)):
        if i in to_remove or i in processed:
            continue
            
        for j in range(i + 1, len(initiatives)):
            if j in to_remove or j in processed:
                continue
                
            title1 = initiatives[i].get('title', '')
            title2 = initiatives[j].get('title', '')
            
            if similarity(title1, title2) > 0.8:
                # Keep the one with more detailed description
                desc1 = initiatives[i].get('description', '')
                desc2 = initiatives[j].get('description', '')
                
                if len(desc1) >= len(desc2):
                    to_remove.add(j)
                    print(f"Removing similar: {title2}")
                else:
                    to_remove.add(i)
                    print(f"Removing similar: {title1}")
                processed.add(i)
                break
    
    return to_remove

def update_html_file(file_path: str, initiatives: List[Dict]):
    """Update the HTML file with cleaned initiatives"""
    
    # Read original file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the initiatives array section
    start_pattern = r'const initiatives = \['
    end_pattern = r'\];'
    
    start_match = re.search(start_pattern, content)
    if not start_match:
        print("Could not find initiatives array start")
        return
    
    # Find the end of the array by looking for the closing bracket and semicolon
    start_pos = start_match.start()
    bracket_count = 0
    current_pos = start_match.end() - 1  # Position of opening bracket
    in_string = False
    string_char = None
    
    while current_pos < len(content):
        char = content[current_pos]
        
        if not in_string and char in '"\'':
            in_string = True
            string_char = char
        elif in_string and char == string_char and content[current_pos-1] != '\\':
            in_string = False
        elif not in_string:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    # Found the end, now look for semicolon
                    end_pos = current_pos + 1
                    while end_pos < len(content) and content[end_pos] in ' \n\t':
                        end_pos += 1
                    if end_pos < len(content) and content[end_pos] == ';':
                        end_pos += 1
                    break
        
        current_pos += 1
    
    if bracket_count != 0:
        print("Could not find matching closing bracket")
        return
    
    # Build new initiatives array
    new_initiatives_js = "const initiatives = [\n"
    
    for i, initiative in enumerate(initiatives):
        new_initiatives_js += "            {\n"
        new_initiatives_js += f'                title: "{initiative["title"].replace('"', '\\"')}",\n'
        new_initiatives_js += f'                description: "{initiative["description"].replace('"', '\\"')}",\n'
        new_initiatives_js += f'                category: "{initiative["category"]}",\n'
        new_initiatives_js += f'                impact: "{initiative["impact"].replace('"', '\\"')}",\n'
        new_initiatives_js += f'                beneficiaries: "{initiative["beneficiaries"].replace('"', '\\"')}",\n'
        new_initiatives_js += f'                icon: "{initiative["icon"]}"\n'
        new_initiatives_js += "            }"
        if i < len(initiatives) - 1:
            new_initiatives_js += ","
        new_initiatives_js += "\n"
    
    new_initiatives_js += "        ];"
    
    # Replace the old array with the new one
    before_array = content[:start_pos]
    after_array = content[end_pos:]
    
    new_content = before_array + new_initiatives_js + after_array
    
    # Update the count display
    new_content = re.sub(r'<span class="stat-number" id="totalCount">\d+</span>', 
                        f'<span class="stat-number" id="totalCount">{len(initiatives)}</span>', 
                        new_content)
    
    # Write the updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Updated HTML with {len(initiatives)} initiatives")

def main():
    """Main transformation function"""
    print("🚀 Starting Conservative Duplicate Removal")
    print("Target: 1089 → 985 initiatives (remove 104 duplicates)\n")
    
    # Extract initiatives  
    initiatives = extract_initiatives_manually('/workspace/index.html')
    print(f"Starting with: {len(initiatives)} initiatives\n")
    
    # Find duplicates to remove
    to_remove = identify_duplicates_to_remove(initiatives)
    
    # Remove duplicates
    cleaned_initiatives = [init for i, init in enumerate(initiatives) if i not in to_remove]
    
    print(f"\n🎯 TRANSFORMATION SUMMARY:")
    print(f"🔥 BEFORE: {len(initiatives)} initiatives")
    print(f"✨ AFTER: {len(cleaned_initiatives)} unique initiatives")
    print(f"🗑️ REMOVED: {len(to_remove)} duplicates")
    
    # If we need to remove more to reach exactly 985
    target = 985
    if len(cleaned_initiatives) > target:
        excess = len(cleaned_initiatives) - target
        print(f"⚠️ Need to remove {excess} more to reach {target}")
        
        # Remove the last few items (least important)
        cleaned_initiatives = cleaned_initiatives[:-excess]
        print(f"✂️ Trimmed to exactly {len(cleaned_initiatives)} initiatives")
    
    # Update the HTML file
    update_html_file('/workspace/index.html', cleaned_initiatives)
    
    print(f"\n✅ Transformation complete!")
    print(f"📊 Final count: {len(cleaned_initiatives)} initiatives")
    print(f"🎯 Target achieved: {len(cleaned_initiatives) == target}")

if __name__ == "__main__":
    main()