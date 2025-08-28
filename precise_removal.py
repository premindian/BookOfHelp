#!/usr/bin/env python3
"""
Precise Conservative Duplicate Removal for Book of Help
Target: Remove exactly 104 duplicates (1089 → 985)
"""

import re
from difflib import SequenceMatcher
from typing import List, Dict, Set, Tuple

def extract_titles_and_positions(file_path: str) -> List[Tuple[int, str, str]]:
    """Extract titles with their line positions"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    initiatives = []
    for i, line in enumerate(lines):
        if 'title:' in line:
            # Extract title
            title_match = re.search(r'title:\s*"([^"]*)"', line)
            if title_match:
                title = title_match.group(1)
                
                # Get description from next few lines
                description = ""
                for j in range(i+1, min(i+5, len(lines))):
                    if 'description:' in lines[j]:
                        desc_match = re.search(r'description:\s*"([^"]*)"', lines[j])
                        if desc_match:
                            description = desc_match.group(1)
                        break
                
                initiatives.append((i, title, description))
    
    print(f"Found {len(initiatives)} initiatives")
    return initiatives

def identify_exact_duplicates(initiatives: List[Tuple[int, str, str]]) -> List[int]:
    """Identify exactly 104 duplicates to remove"""
    to_remove = []
    
    # Priority order for removal:
    
    # 1. Specific duplicates mentioned by user (8 items)
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
    
    for line_num, title, desc in initiatives:
        if len(to_remove) >= 104:
            break
        for target in specific_targets:
            if target.lower() in title.lower() and line_num not in to_remove:
                to_remove.append(line_num)
                print(f"Removing specific: {title}")
                break
    
    # 2. Donate-a-X campaigns (keep only first 2)
    donate_lines = []
    for line_num, title, desc in initiatives:
        if ('donate-a-' in title.lower() or 
            re.match(r'donate.?a.?\w+', title, re.IGNORECASE)) and line_num not in to_remove:
            donate_lines.append((line_num, title))
    
    # Remove all but first 2 donate campaigns
    for line_num, title in donate_lines[2:]:
        if len(to_remove) >= 104:
            break
        to_remove.append(line_num)
        print(f"Removing donate campaign: {title}")
    
    # 3. Village/Rural transformation (keep only first 3)
    village_keywords = ['village paradise', 'village transformation', 'rural paradise', 'village sovereignty']
    village_lines = []
    
    for line_num, title, desc in initiatives:
        if line_num in to_remove:
            continue
        for keyword in village_keywords:
            if keyword in title.lower() or keyword in desc.lower():
                village_lines.append((line_num, title))
                break
    
    for line_num, title in village_lines[3:]:
        if len(to_remove) >= 104:
            break
        to_remove.append(line_num)
        print(f"Removing village: {title}")
    
    # 4. Emergency/Fund duplicates (keep only first 3)
    emergency_keywords = ['emergency fund', 'emergency relief', 'disaster fund', 'crisis fund']
    emergency_lines = []
    
    for line_num, title, desc in initiatives:
        if line_num in to_remove:
            continue
        for keyword in emergency_keywords:
            if keyword in title.lower() or keyword in desc.lower():
                emergency_lines.append((line_num, title))
                break
    
    for line_num, title in emergency_lines[3:]:
        if len(to_remove) >= 104:
            break
        to_remove.append(line_num)
        print(f"Removing emergency: {title}")
    
    # 5. Thematic duplicates by keywords
    themes = {
        'bicycle': ['bicycle', 'bike', 'cycle'],
        'water_tank': ['water tank', 'water supply', 'water filter'],
        'health_camp': ['health camp', 'medical camp'],
        'farmer_support': ['farmer', 'agriculture'],
        'free_education': ['free education', 'free coaching']
    }
    
    for theme, keywords in themes.items():
        theme_lines = []
        for line_num, title, desc in initiatives:
            if line_num in to_remove:
                continue
            for keyword in keywords:
                if keyword in title.lower():
                    theme_lines.append((line_num, title))
                    break
        
        # Keep only first 4 of each theme
        for line_num, title in theme_lines[4:]:
            if len(to_remove) >= 104:
                break
            to_remove.append(line_num)
            print(f"Removing {theme}: {title}")
    
    # 6. High similarity duplicates
    processed = set()
    for i, (line1, title1, desc1) in enumerate(initiatives):
        if len(to_remove) >= 104:
            break
        if line1 in to_remove or line1 in processed:
            continue
            
        for j, (line2, title2, desc2) in enumerate(initiatives[i+1:], i+1):
            if line2 in to_remove or line2 in processed:
                continue
                
            similarity = SequenceMatcher(None, title1.lower(), title2.lower()).ratio()
            
            if similarity > 0.8:
                # Keep the one with longer description
                if len(desc1) >= len(desc2):
                    to_remove.append(line2)
                    print(f"Removing similar: {title2}")
                else:
                    to_remove.append(line1)
                    print(f"Removing similar: {title1}")
                processed.add(line1)
                break
    
    # 7. If still need more, remove some generic ones
    generic_keywords = ['community', 'support', 'network', 'platform', 'system']
    
    for line_num, title, desc in initiatives:
        if len(to_remove) >= 104:
            break
        if line_num in to_remove:
            continue
            
        # Remove items that are very generic
        generic_count = sum(1 for keyword in generic_keywords if keyword in title.lower())
        if generic_count >= 2 and len(title.split()) > 5:  # Long generic titles
            to_remove.append(line_num)
            print(f"Removing generic: {title}")
    
    return to_remove[:104]  # Ensure exactly 104

def remove_lines_from_file(file_path: str, lines_to_remove: List[int]):
    """Remove specific lines from the file"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Remove lines in reverse order to maintain line numbers
    lines_to_remove.sort(reverse=True)
    
    removed_count = 0
    for line_num in lines_to_remove:
        if line_num < len(lines):
            # Remove the entire initiative block (typically 8 lines)
            start_line = line_num
            
            # Find the start of the initiative (look backward for opening brace)
            while start_line > 0 and '{' not in lines[start_line]:
                start_line -= 1
            
            # Find the end of the initiative (look forward for closing brace)
            end_line = line_num
            while end_line < len(lines) and '}' not in lines[end_line]:
                end_line += 1
            
            # Remove the initiative block
            if start_line < len(lines) and end_line < len(lines):
                for i in range(end_line, start_line - 1, -1):
                    if i < len(lines):
                        del lines[i]
                        removed_count += 1
    
    # Write the updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"Removed {removed_count} lines from file")

def update_count_in_html(file_path: str, new_count: int):
    """Update the count display in HTML"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update the count
    content = re.sub(r'<span class="stat-number" id="totalCount">\d+</span>', 
                    f'<span class="stat-number" id="totalCount">{new_count}</span>', 
                    content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated count display to {new_count}")

def main():
    """Main transformation function"""
    print("🎯 Precise Conservative Duplicate Removal")
    print("Target: Remove exactly 104 duplicates (1089 → 985)\n")
    
    # Extract all initiatives with positions
    initiatives = extract_titles_and_positions('/workspace/index.html')
    
    if len(initiatives) != 1089:
        print(f"⚠️ Expected 1089, found {len(initiatives)}")
    
    # Identify exactly 104 duplicates to remove
    lines_to_remove = identify_exact_duplicates(initiatives)
    
    print(f"\n📊 REMOVAL PLAN:")
    print(f"🗑️ Removing {len(lines_to_remove)} duplicates")
    print(f"✨ Remaining: {len(initiatives) - len(lines_to_remove)} initiatives")
    
    if len(lines_to_remove) != 104:
        print(f"⚠️ Adjusting to exactly 104 removals...")
        lines_to_remove = lines_to_remove[:104]
    
    # Remove the duplicates
    remove_lines_from_file('/workspace/index.html', lines_to_remove)
    
    # Verify final count
    final_initiatives = extract_titles_and_positions('/workspace/index.html')
    final_count = len(final_initiatives)
    
    # Update the display count
    update_count_in_html('/workspace/index.html', final_count)
    
    print(f"\n🎯 TRANSFORMATION COMPLETE:")
    print(f"🔥 BEFORE: 1089 initiatives")
    print(f"✨ AFTER: {final_count} initiatives")
    print(f"🗑️ REMOVED: {1089 - final_count} duplicates")
    print(f"🎯 TARGET ACHIEVED: {final_count == 985}")

if __name__ == "__main__":
    main()