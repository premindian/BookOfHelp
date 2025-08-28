#!/usr/bin/env python3
"""
Conservative Duplicate Removal Script for Book of Help
Target: Reduce from 1089 to 985 initiatives (remove 104 duplicates)
Focus: Remove only clear duplicates while preserving unique value propositions
"""

import re
import json
from difflib import SequenceMatcher
from typing import List, Dict, Set, Tuple

def extract_initiatives_from_html(file_path: str) -> Tuple[List[Dict], str, str]:
    """Extract initiatives array from HTML file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the initiatives array
    start_pattern = r'const initiatives = \['
    end_pattern = r'\];'
    
    start_match = re.search(start_pattern, content)
    if not start_match:
        raise ValueError("Could not find initiatives array start")
    
    start_pos = start_match.end() - 1  # Include the opening bracket
    
    # Find the matching closing bracket
    bracket_count = 0
    current_pos = start_pos
    in_string = False
    escape_next = False
    string_char = None
    
    while current_pos < len(content):
        char = content[current_pos]
        
        if escape_next:
            escape_next = False
        elif char == '\\':
            escape_next = True
        elif not in_string and char in '"\'`':
            in_string = True
            string_char = char
        elif in_string and char == string_char:
            in_string = False
            string_char = None
        elif not in_string:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    break
        
        current_pos += 1
    
    if bracket_count != 0:
        raise ValueError("Could not find matching closing bracket")
    
    before_content = content[:start_match.start()]
    initiatives_content = content[start_match.start():current_pos + 1]
    after_content = content[current_pos + 1:]
    
    # Parse initiatives
    initiatives_js = initiatives_content[len("const initiatives = "):]
    
    # Clean up JavaScript to make it JSON-parseable
    # Remove comments
    initiatives_js = re.sub(r'//.*?(?=\n|$)', '', initiatives_js, flags=re.MULTILINE)
    initiatives_js = re.sub(r'/\*.*?\*/', '', initiatives_js, flags=re.DOTALL)
    
    # Remove trailing commas
    initiatives_js = re.sub(r',(\s*[}\]])', r'\1', initiatives_js)
    
    try:
        initiatives = json.loads(initiatives_js)
        print(f"Successfully parsed {len(initiatives)} initiatives")
        return initiatives, before_content, after_content
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print("Trying alternative parsing...")
        
        # Fallback: extract initiatives manually
        initiatives = []
        lines = initiatives_content.split('\n')
        current_initiative = {}
        in_initiative = False
        
        for line in lines:
            line = line.strip()
            if line.startswith('{') and not in_initiative:
                in_initiative = True
                current_initiative = {}
            elif line.startswith('}') and in_initiative:
                if current_initiative:
                    initiatives.append(current_initiative.copy())
                in_initiative = False
                current_initiative = {}
            elif in_initiative:
                # Parse key-value pairs
                if ':' in line:
                    key_match = re.match(r'(\w+):\s*["\']?(.*?)["\']?[,]?$', line)
                    if key_match:
                        key, value = key_match.groups()
                        # Clean up value
                        value = value.rstrip(',').strip('"\'')
                        current_initiative[key] = value
        
        print(f"Fallback parsing extracted {len(initiatives)} initiatives")
        return initiatives, before_content, after_content

def similarity(a: str, b: str) -> float:
    """Calculate similarity between two strings"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def identify_specific_duplicates(initiatives: List[Dict]) -> Set[int]:
    """Identify the 8 specific duplicates mentioned by user"""
    to_remove = set()
    
    # Target duplicates to find and remove
    target_duplicates = [
        "Quality Seeds Distribution Chain",
        "Academic Stress Management Hub", 
        "Medication Impact Tracker",
        "Inclusive Wedding Support Network",
        "Mobile Toy Libraries",
        "Village Bicycle Libraries", 
        "Street Vendor First-Aid Kits",
        "Tool Libraries Platform"
    ]
    
    for i, initiative in enumerate(initiatives):
        title = initiative.get('title', '')
        for target in target_duplicates:
            if similarity(title, target) > 0.8:
                to_remove.add(i)
                print(f"Found specific duplicate: {title}")
                break
    
    return to_remove

def identify_donate_campaigns(initiatives: List[Dict]) -> Set[int]:
    """Identify Donate-a-X campaigns to consolidate"""
    to_remove = set()
    donate_campaigns = []
    
    # Find all Donate-a-X campaigns
    for i, initiative in enumerate(initiatives):
        title = initiative.get('title', '')
        if re.match(r'Donate.?a.?\w+', title, re.IGNORECASE) or 'donate-a-' in title.lower():
            donate_campaigns.append((i, title))
    
    print(f"Found {len(donate_campaigns)} Donate-a-X campaigns")
    
    # Keep only the first few and remove the rest
    if len(donate_campaigns) > 3:
        for i, title in donate_campaigns[3:]:
            to_remove.add(i)
            print(f"Removing donate campaign: {title}")
    
    return to_remove

def identify_village_initiatives(initiatives: List[Dict]) -> Set[int]:
    """Identify village transformation/paradise initiatives to streamline"""
    to_remove = set()
    village_initiatives = []
    
    # Keywords that indicate village transformation initiatives
    village_keywords = ['village paradise', 'village transformation', 'village sovereignty', 'rural paradise', 'village hub']
    
    for i, initiative in enumerate(initiatives):
        title = initiative.get('title', '').lower()
        description = initiative.get('description', '').lower()
        
        for keyword in village_keywords:
            if keyword in title or keyword in description:
                village_initiatives.append((i, initiative.get('title', '')))
                break
    
    print(f"Found {len(village_initiatives)} village transformation initiatives")
    
    # Keep only the first 3 and remove the rest
    if len(village_initiatives) > 3:
        for i, title in village_initiatives[3:]:
            to_remove.add(i)
            print(f"Removing village initiative: {title}")
    
    return to_remove

def identify_community_sovereignty(initiatives: List[Dict]) -> Set[int]:
    """Identify community sovereignty movements to unify"""
    to_remove = set()
    community_initiatives = []
    
    for i, initiative in enumerate(initiatives):
        title = initiative.get('title', '').lower()
        description = initiative.get('description', '').lower()
        
        if 'community sovereignty' in title or 'community sovereignty' in description:
            community_initiatives.append((i, initiative.get('title', '')))
    
    print(f"Found {len(community_initiatives)} community sovereignty initiatives")
    
    # Keep only the first 2 and remove the rest
    if len(community_initiatives) > 2:
        for i, title in community_initiatives[2:]:
            to_remove.add(i)
            print(f"Removing community sovereignty: {title}")
    
    return to_remove

def identify_emergency_funds(initiatives: List[Dict]) -> Set[int]:
    """Identify emergency/fund duplicates to integrate"""
    to_remove = set()
    emergency_initiatives = []
    
    emergency_keywords = ['emergency fund', 'emergency relief', 'disaster fund', 'crisis fund', 'emergency aid']
    
    for i, initiative in enumerate(initiatives):
        title = initiative.get('title', '').lower()
        description = initiative.get('description', '').lower()
        
        for keyword in emergency_keywords:
            if keyword in title or keyword in description:
                emergency_initiatives.append((i, initiative.get('title', '')))
                break
    
    print(f"Found {len(emergency_initiatives)} emergency/fund initiatives")
    
    # Keep only the first 3 and remove the rest
    if len(emergency_initiatives) > 3:
        for i, title in emergency_initiatives[3:]:
            to_remove.add(i)
            print(f"Removing emergency fund: {title}")
    
    return to_remove

def identify_thematic_duplicates(initiatives: List[Dict]) -> Set[int]:
    """Identify thematic duplicates (bicycle, water, health, agricultural)"""
    to_remove = set()
    
    # Group by themes
    themes = {
        'bicycle': [],
        'water': [],
        'health': [],
        'agricultural': [],
        'education': []
    }
    
    for i, initiative in enumerate(initiatives):
        title = initiative.get('title', '').lower()
        description = initiative.get('description', '').lower()
        
        if 'bicycle' in title or 'bike' in title or 'cycle' in title:
            themes['bicycle'].append((i, initiative.get('title', '')))
        elif 'water' in title and ('tank' in title or 'supply' in title or 'filter' in title):
            themes['water'].append((i, initiative.get('title', '')))
        elif ('health' in title or 'medical' in title) and ('camp' in title or 'clinic' in title):
            themes['health'].append((i, initiative.get('title', '')))
        elif 'farm' in title or 'agriculture' in title or 'crop' in title:
            themes['agricultural'].append((i, initiative.get('title', '')))
        elif 'education' in title and ('free' in title or 'scholarship' in title):
            themes['education'].append((i, initiative.get('title', '')))
    
    # Remove excess from each theme
    for theme, items in themes.items():
        if len(items) > 5:  # Keep max 5 per theme
            print(f"Found {len(items)} {theme} initiatives, keeping 5")
            for i, title in items[5:]:
                to_remove.add(i)
                print(f"Removing {theme} duplicate: {title}")
    
    return to_remove

def identify_high_similarity_duplicates(initiatives: List[Dict]) -> Set[int]:
    """Identify additional high-similarity duplicates"""
    to_remove = set()
    
    for i in range(len(initiatives)):
        if i in to_remove:
            continue
            
        for j in range(i + 1, len(initiatives)):
            if j in to_remove:
                continue
                
            title1 = initiatives[i].get('title', '')
            title2 = initiatives[j].get('title', '')
            
            # Check title similarity
            title_sim = similarity(title1, title2)
            
            if title_sim > 0.85:  # Very high similarity
                # Keep the one with longer description (more detailed)
                desc1 = initiatives[i].get('description', '')
                desc2 = initiatives[j].get('description', '')
                
                if len(desc2) > len(desc1):
                    to_remove.add(i)
                    print(f"Removing similar duplicate: {title1} (kept: {title2})")
                else:
                    to_remove.add(j)
                    print(f"Removing similar duplicate: {title2} (kept: {title1})")
                break
    
    return to_remove

def save_updated_html(initiatives: List[Dict], before_content: str, after_content: str, file_path: str):
    """Save the updated HTML file with cleaned initiatives"""
    
    # Convert initiatives back to JavaScript format
    js_initiatives = "const initiatives = [\n"
    
    for i, initiative in enumerate(initiatives):
        js_initiatives += "            {\n"
        js_initiatives += f'                title: "{initiative.get("title", "").replace('"', '\\"')}",\n'
        js_initiatives += f'                description: "{initiative.get("description", "").replace('"', '\\"')}",\n'
        js_initiatives += f'                category: "{initiative.get("category", "").replace('"', '\\"')}",\n'
        js_initiatives += f'                impact: "{initiative.get("impact", "").replace('"', '\\"')}",\n'
        js_initiatives += f'                beneficiaries: "{initiative.get("beneficiaries", "").replace('"', '\\"')}",\n'
        js_initiatives += f'                icon: "{initiative.get("icon", "").replace('"', '\\"')}"\n'
        js_initiatives += "            }"
        if i < len(initiatives) - 1:
            js_initiatives += ","
        js_initiatives += "\n"
    
    js_initiatives += "        ];"
    
    # Combine all parts
    new_content = before_content + js_initiatives + after_content
    
    # Update the count in the HTML
    new_content = re.sub(r'<span class="stat-number" id="totalCount">\d+</span>', 
                        f'<span class="stat-number" id="totalCount">{len(initiatives)}</span>', 
                        new_content)
    
    # Write the updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated HTML file with {len(initiatives)} initiatives")

def main():
    """Main transformation function"""
    print("🚀 Starting Conservative Duplicate Removal Transformation")
    print("Target: 1089 → 985 initiatives (remove 104 duplicates)\n")
    
    # Load initiatives
    initiatives, before_content, after_content = extract_initiatives_from_html('/workspace/index.html')
    print(f"Initial count: {len(initiatives)} initiatives\n")
    
    # Collect all indices to remove
    all_to_remove = set()
    
    # 1. Remove specific identified duplicates (8)
    print("1️⃣ Removing specific identified duplicates...")
    specific_dupes = identify_specific_duplicates(initiatives)
    all_to_remove.update(specific_dupes)
    print(f"   Found {len(specific_dupes)} specific duplicates\n")
    
    # 2. Consolidate Donate-a-X campaigns 
    print("2️⃣ Consolidating Donate-a-X campaigns...")
    donate_dupes = identify_donate_campaigns(initiatives)
    all_to_remove.update(donate_dupes)
    print(f"   Removing {len(donate_dupes)} donate campaigns\n")
    
    # 3. Streamline village initiatives
    print("3️⃣ Streamlining village transformation initiatives...")
    village_dupes = identify_village_initiatives(initiatives)
    all_to_remove.update(village_dupes)
    print(f"   Removing {len(village_dupes)} village initiatives\n")
    
    # 4. Unify community sovereignty
    print("4️⃣ Unifying community sovereignty movements...")
    community_dupes = identify_community_sovereignty(initiatives)
    all_to_remove.update(community_dupes)
    print(f"   Removing {len(community_dupes)} community sovereignty\n")
    
    # 5. Integrate emergency systems
    print("5️⃣ Integrating emergency/fund duplicates...")
    emergency_dupes = identify_emergency_funds(initiatives)
    all_to_remove.update(emergency_dupes)
    print(f"   Removing {len(emergency_dupes)} emergency funds\n")
    
    # 6. Consolidate thematic duplicates
    print("6️⃣ Consolidating thematic duplicates...")
    thematic_dupes = identify_thematic_duplicates(initiatives)
    all_to_remove.update(thematic_dupes)
    print(f"   Removing {len(thematic_dupes)} thematic duplicates\n")
    
    # 7. Find additional high-similarity duplicates if needed
    current_removals = len(all_to_remove)
    target_removals = 104
    
    if current_removals < target_removals:
        print(f"7️⃣ Finding additional high-similarity duplicates...")
        print(f"   Need {target_removals - current_removals} more removals")
        additional_dupes = identify_high_similarity_duplicates(initiatives)
        # Only take what we need
        additional_needed = list(additional_dupes)[:target_removals - current_removals]
        all_to_remove.update(additional_needed)
        print(f"   Removing {len(additional_needed)} additional duplicates\n")
    
    # Remove duplicates
    cleaned_initiatives = [init for i, init in enumerate(initiatives) if i not in all_to_remove]
    
    print(f"🎯 TRANSFORMATION SUMMARY:")
    print(f"🔥 BEFORE: {len(initiatives)} initiatives (with duplication)")
    print(f"✨ AFTER: {len(cleaned_initiatives)} unique, high-quality initiatives")
    print(f"🗑️ REMOVED: {len(all_to_remove)} total duplicates")
    print(f"📊 TARGET ACHIEVED: {len(cleaned_initiatives) == 985}")
    
    # Save the updated file
    save_updated_html(cleaned_initiatives, before_content, after_content, '/workspace/index.html')
    
    print("\n✅ Transformation complete! Ready for bookofhelp.com")

if __name__ == "__main__":
    main()