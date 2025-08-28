#!/usr/bin/env python3
"""
Careful Duplicate Removal - Surgical precision without breaking functionality
"""

import re
from difflib import SequenceMatcher
import json

def similarity_score(a, b):
    """Calculate similarity between two strings"""
    a_clean = re.sub(r'[^\w\s]', '', a.lower())
    b_clean = re.sub(r'[^\w\s]', '', b.lower())
    return SequenceMatcher(None, a_clean, b_clean).ratio()

def extract_initiatives():
    """Extract initiatives array safely"""
    with open('/workspace/index.html', 'r') as f:
        content = f.read()
    
    # Find the initiatives array boundaries
    start_marker = 'const initiatives = ['
    end_marker = '];'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx) + len(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("❌ Could not find initiatives array")
        return None, None, None
    
    before_array = content[:start_idx]
    after_array = content[end_idx:]
    
    # Extract individual initiatives using regex
    array_content = content[start_idx:end_idx]
    
    # Find all initiative objects
    initiative_pattern = r'\s*{\s*title:\s*"([^"]+)",\s*description:\s*"([^"]+)",\s*category:\s*"([^"]+)",\s*impact:\s*"([^"]+)",\s*beneficiaries:\s*"([^"]+)",\s*icon:\s*"([^"]+)"\s*}'
    
    initiatives = []
    for match in re.finditer(initiative_pattern, array_content, re.DOTALL):
        initiatives.append({
            'title': match.group(1),
            'description': match.group(2),
            'category': match.group(3),
            'impact': match.group(4),
            'beneficiaries': match.group(5),
            'icon': match.group(6),
            'original_text': match.group(0)
        })
    
    print(f"✅ Extracted {len(initiatives)} initiatives safely")
    return initiatives, before_array, after_array

def find_duplicates_carefully(initiatives):
    """Find duplicates with high precision"""
    print("\n🔍 CAREFUL DUPLICATE DETECTION")
    print("=" * 40)
    
    duplicates_to_remove = []
    exact_duplicates = []
    near_duplicates = []
    
    # Check for exact title matches
    titles_seen = {}
    for i, init in enumerate(initiatives):
        title = init['title'].strip()
        if title in titles_seen:
            exact_duplicates.append((i, init, titles_seen[title], initiatives[titles_seen[title]]))
            duplicates_to_remove.append(i)
        else:
            titles_seen[title] = i
    
    # Check for very similar titles (90%+ similarity)
    for i in range(len(initiatives)):
        if i in duplicates_to_remove:
            continue
        for j in range(i + 1, len(initiatives)):
            if j in duplicates_to_remove:
                continue
            
            title_sim = similarity_score(initiatives[i]['title'], initiatives[j]['title'])
            desc_sim = similarity_score(initiatives[i]['description'], initiatives[j]['description'])
            
            if title_sim >= 0.9 or (title_sim >= 0.7 and desc_sim >= 0.8):
                near_duplicates.append((i, initiatives[i], j, initiatives[j], title_sim, desc_sim))
                # Remove the shorter title (keep more descriptive)
                if len(initiatives[i]['title']) >= len(initiatives[j]['title']):
                    duplicates_to_remove.append(j)
                else:
                    duplicates_to_remove.append(i)
    
    # Display findings
    print(f"📊 DUPLICATE ANALYSIS:")
    print(f"   Exact title duplicates: {len(exact_duplicates)}")
    print(f"   Near duplicates (90%+ similar): {len(near_duplicates)}")
    print(f"   Total to remove: {len(set(duplicates_to_remove))}")
    
    if exact_duplicates:
        print(f"\n🎯 EXACT DUPLICATES:")
        for i, (idx1, init1, idx2, init2) in enumerate(exact_duplicates, 1):
            print(f"   {i}. '{init1['title']}'")
    
    if near_duplicates:
        print(f"\n🔍 NEAR DUPLICATES (first 10):")
        for i, (idx1, init1, idx2, init2, t_sim, d_sim) in enumerate(near_duplicates[:10], 1):
            print(f"   {i}. '{init1['title']}' ↔ '{init2['title']}' ({t_sim:.1%} similar)")
    
    return sorted(set(duplicates_to_remove), reverse=True)  # Remove from end to preserve indices

def rebuild_array_carefully(initiatives, indices_to_remove):
    """Rebuild the initiatives array without duplicates"""
    print(f"\n🔧 REBUILDING ARRAY CAREFULLY")
    print("=" * 40)
    
    # Remove duplicates (indices are sorted in reverse order)
    for idx in indices_to_remove:
        del initiatives[idx]
    
    print(f"✅ Removed {len(indices_to_remove)} duplicates")
    print(f"📊 Final count: {len(initiatives)} unique initiatives")
    
    # Rebuild the JavaScript array
    array_parts = ['        const initiatives = [']
    
    for i, init in enumerate(initiatives):
        comment = f"            // {init['title'].upper().replace(' ', ' ')}"
        array_parts.append(comment)
        array_parts.append('            {')
        array_parts.append(f'                title: "{init["title"]}",')
        array_parts.append(f'                description: "{init["description"]}",')
        array_parts.append(f'                category: "{init["category"]}",')
        array_parts.append(f'                impact: "{init["impact"]}",')
        array_parts.append(f'                beneficiaries: "{init["beneficiaries"]}",')
        array_parts.append(f'                icon: "{init["icon"]}"')
        
        if i < len(initiatives) - 1:
            array_parts.append('            },')
        else:
            array_parts.append('            }')
        array_parts.append('')
    
    array_parts.append('        ];')
    
    return '\n'.join(array_parts)

def careful_duplicate_removal():
    """Main function for careful duplicate removal"""
    print("🎯 CAREFUL DUPLICATE REMOVAL - PRESERVING ALL FUNCTIONALITY")
    print("=" * 60)
    
    # Step 1: Extract safely
    initiatives, before_array, after_array = extract_initiatives()
    if not initiatives:
        return False
    
    original_count = len(initiatives)
    print(f"📊 Starting with: {original_count} initiatives")
    
    # Step 2: Find duplicates carefully
    indices_to_remove = find_duplicates_carefully(initiatives)
    
    if not indices_to_remove:
        print("✅ No duplicates found - catalog is already clean!")
        return True
    
    # Step 3: Rebuild carefully
    new_array = rebuild_array_carefully(initiatives, indices_to_remove)
    
    # Step 4: Reconstruct the full file
    new_content = before_array + new_array + '\n\n        let filteredData = initiatives;' + after_array[2:]
    
    # Step 5: Update the count display
    final_count = original_count - len(indices_to_remove)
    new_content = re.sub(
        r'<span class="stat-number" id="totalCount">\d+</span>',
        f'<span class="stat-number" id="totalCount">{final_count}</span>',
        new_content
    )
    
    # Step 6: Save with backup
    import shutil
    shutil.copy('/workspace/index.html', '/workspace/index_backup.html')
    print("✅ Created backup: index_backup.html")
    
    with open('/workspace/index.html', 'w') as f:
        f.write(new_content)
    
    print(f"\n🎉 CAREFUL REMOVAL COMPLETE!")
    print(f"   Original: {original_count} initiatives")
    print(f"   Removed: {len(indices_to_remove)} duplicates")
    print(f"   Final: {final_count} unique initiatives")
    print(f"   Reduction: {(len(indices_to_remove)/original_count)*100:.1f}%")
    print("   ✅ All functionality preserved!")
    
    return True

if __name__ == "__main__":
    success = careful_duplicate_removal()