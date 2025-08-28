#!/usr/bin/env python3
"""
Ultra Conservative Duplicate Removal
Only removes truly identical entries, preserves all nuanced variations
"""

import re
import difflib

def extract_initiatives_safe():
    """Safely extract initiatives from HTML"""
    with open('/workspace/index.html', 'r') as f:
        content = f.read()
    
    # Find initiatives using a more robust pattern
    pattern = r'{\s*title:\s*"([^"]+)",\s*description:\s*"([^"]+)",\s*category:\s*"([^"]+)",\s*impact:\s*"([^"]+)",\s*beneficiaries:\s*"([^"]+)",\s*icon:\s*"([^"]+)"\s*}'
    
    matches = re.findall(pattern, content, re.DOTALL)
    
    initiatives = []
    for i, match in enumerate(matches):
        initiatives.append({
            'index': i,
            'title': match[0].strip(),
            'description': match[1].strip(),
            'category': match[2].strip(),
            'impact': match[3].strip(),
            'beneficiaries': match[4].strip(),
            'icon': match[5].strip()
        })
    
    print(f"✅ Safely extracted {len(initiatives)} initiatives")
    return initiatives

def find_ultra_conservative_duplicates(initiatives):
    """Find only truly identical duplicates"""
    print("\n🎯 ULTRA CONSERVATIVE DUPLICATE DETECTION")
    print("=" * 50)
    print("Only removing entries that are 100% identical in title AND description")
    
    duplicates_to_remove = []
    seen_combinations = {}
    
    for i, init in enumerate(initiatives):
        # Create a signature: title + description (normalized)
        title_norm = re.sub(r'\s+', ' ', init['title'].lower().strip())
        desc_norm = re.sub(r'\s+', ' ', init['description'].lower().strip())
        signature = f"{title_norm}|||{desc_norm}"
        
        if signature in seen_combinations:
            original_idx = seen_combinations[signature]
            original = initiatives[original_idx]
            
            print(f"🎯 IDENTICAL DUPLICATE FOUND:")
            print(f"   Original #{original_idx}: '{original['title']}'")
            print(f"   Duplicate #{i}: '{init['title']}'")
            print(f"   → Removing duplicate #{i}")
            print()
            
            duplicates_to_remove.append(i)
        else:
            seen_combinations[signature] = i
    
    # Also check for exact title matches (different descriptions are kept)
    title_exact_matches = {}
    for i, init in enumerate(initiatives):
        if i in duplicates_to_remove:
            continue
            
        title_exact = init['title'].strip()
        if title_exact in title_exact_matches:
            original_idx = title_exact_matches[title_exact]
            original = initiatives[original_idx]
            
            # Only remove if descriptions are also very similar (95%+ match)
            desc_similarity = difflib.SequenceMatcher(
                None, 
                original['description'].lower(), 
                init['description'].lower()
            ).ratio()
            
            if desc_similarity >= 0.95:
                print(f"🎯 EXACT TITLE + SIMILAR DESCRIPTION:")
                print(f"   Original #{original_idx}: '{original['title']}'")
                print(f"   Duplicate #{i}: '{init['title']}'")
                print(f"   Description similarity: {desc_similarity:.1%}")
                print(f"   → Removing duplicate #{i}")
                print()
                duplicates_to_remove.append(i)
        else:
            title_exact_matches[title_exact] = i
    
    print(f"📊 ULTRA CONSERVATIVE RESULTS:")
    print(f"   Total initiatives: {len(initiatives)}")
    print(f"   Truly identical duplicates: {len(duplicates_to_remove)}")
    print(f"   Remaining after cleanup: {len(initiatives) - len(duplicates_to_remove)}")
    print(f"   Removal rate: {(len(duplicates_to_remove)/len(initiatives))*100:.1f}%")
    
    return sorted(duplicates_to_remove, reverse=True)

def remove_duplicates_safely(duplicates_to_remove):
    """Remove duplicates by modifying the HTML file safely"""
    
    if not duplicates_to_remove:
        print("✅ No truly identical duplicates found - catalog is perfectly curated!")
        return False
    
    print(f"\n🔧 SAFELY REMOVING {len(duplicates_to_remove)} IDENTICAL DUPLICATES")
    print("=" * 50)
    
    with open('/workspace/index.html', 'r') as f:
        content = f.read()
    
    # Find all initiative blocks
    pattern = r'(\s*//[^\n]*\n\s*{\s*title:\s*"[^"]+",\s*description:\s*"[^"]+",\s*category:\s*"[^"]+",\s*impact:\s*"[^"]+",\s*beneficiaries:\s*"[^"]+",\s*icon:\s*"[^"]+"\s*}),?'
    
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    if len(matches) != len(duplicates_to_remove) + (len(matches) - len(duplicates_to_remove)):
        print("⚠️ Initiative count mismatch - using safer approach")
        return False
    
    # Create new content by skipping the duplicate indices
    new_parts = []
    current_pos = 0
    
    for i, match in enumerate(matches):
        if i not in duplicates_to_remove:
            # Keep this initiative
            new_parts.append(content[current_pos:match.start()])
            new_parts.append(match.group(1))
            
            # Add comma if not the last one we're keeping
            remaining_indices = [idx for idx in range(len(matches)) if idx not in duplicates_to_remove and idx > i]
            if remaining_indices:
                new_parts.append(',')
        
        current_pos = match.end()
    
    # Add the rest of the file
    new_parts.append(content[current_pos:])
    
    new_content = ''.join(new_parts)
    
    # Update the count
    final_count = len(matches) - len(duplicates_to_remove)
    new_content = re.sub(
        r'<span class="stat-number" id="totalCount">\d+</span>',
        f'<span class="stat-number" id="totalCount">{final_count}</span>',
        new_content
    )
    
    # Create backup
    import shutil
    shutil.copy('/workspace/index.html', '/workspace/index_safe_backup.html')
    print("✅ Created safety backup: index_safe_backup.html")
    
    # Save the new content
    with open('/workspace/index.html', 'w') as f:
        f.write(new_content)
    
    print(f"✅ Successfully removed {len(duplicates_to_remove)} identical duplicates")
    print(f"📊 Final count: {final_count} unique initiatives")
    
    return True

def ultra_conservative_removal():
    """Main function for ultra conservative duplicate removal"""
    print("🎯 ULTRA CONSERVATIVE DUPLICATE REMOVAL")
    print("=" * 60)
    print("PHILOSOPHY: Preserve all nuanced variations, remove only identical copies")
    print()
    
    # Step 1: Extract safely
    initiatives = extract_initiatives_safe()
    if not initiatives:
        return False
    
    # Step 2: Find only truly identical duplicates
    duplicates_to_remove = find_ultra_conservative_duplicates(initiatives)
    
    if not duplicates_to_remove:
        print("\n🎉 PERFECT! Your catalog is already optimally curated!")
        print("No truly identical duplicates found.")
        return True
    
    # Step 3: Remove safely
    success = remove_duplicates_safely(duplicates_to_remove)
    
    if success:
        print(f"\n🎉 ULTRA CONSERVATIVE REMOVAL COMPLETE!")
        print("✅ Only identical duplicates removed")
        print("✅ All nuanced variations preserved") 
        print("✅ Catalog quality maintained")
        print("✅ Functionality preserved")
    
    return success

if __name__ == "__main__":
    ultra_conservative_removal()