#!/usr/bin/env python3
"""
Targeted Duplicate Removal Script
Removes specific duplicates identified in the analysis
"""

import re

def remove_specific_duplicates():
    """Remove specific duplicate entries"""
    
    with open('/workspace/index.html', 'r') as f:
        content = f.read()
    
    print("🎯 REMOVING SPECIFIC DUPLICATES")
    print("=" * 40)
    
    # Specific duplicates to remove (keep the first, remove the second)
    duplicates_to_remove = [
        {
            'title': 'Quality Seeds Distribution Chain',
            'keep_description': 'Platform to create supply chain distributing quality seeds',
            'remove_description': 'Advanced agricultural supply chain platform ensuring distribution of certified high-quality seeds'
        },
        {
            'title': 'Academic Stress',
            'keep_pattern': 'Academic Stress Reduction Platform',
            'remove_pattern': 'Academic Stress Management Hub'
        },
        {
            'title': 'Medication',
            'keep_pattern': 'Medication Side Effects Tracker',
            'remove_pattern': 'Medication Impact Tracker'
        }
    ]
    
    removed_count = 0
    
    # Remove the second Quality Seeds Distribution Chain entry
    print("🗑️ Removing duplicate: Quality Seeds Distribution Chain (Advanced version)")
    pattern1 = r'\s*{\s*title:\s*"Quality Seeds Distribution Chain",\s*description:\s*"Advanced agricultural supply chain platform.*?\n\s*},?\s*'
    content = re.sub(pattern1, '', content, flags=re.DOTALL)
    removed_count += 1
    
    # Remove Academic Stress Management Hub (keep Academic Stress Reduction Platform)
    print("🗑️ Removing duplicate: Academic Stress Management Hub")
    pattern2 = r'\s*{\s*title:\s*"Academic Stress Management Hub",.*?\n\s*},?\s*'
    content = re.sub(pattern2, '', content, flags=re.DOTALL)
    removed_count += 1
    
    # Remove Medication Impact Tracker (keep Medication Side Effects Tracker)
    print("🗑️ Removing duplicate: Medication Impact Tracker")
    pattern3 = r'\s*{\s*title:\s*"Medication Impact Tracker",.*?\n\s*},?\s*'
    content = re.sub(pattern3, '', content, flags=re.DOTALL)
    removed_count += 1
    
    # Remove other similar pairs mentioned
    similar_removals = [
        "Inclusive Wedding Support Network",
        "Mobile Toy Libraries", 
        "Village Bicycle Libraries",
        "Street Vendor First-Aid Kits",
        "Tool Libraries Platform"
    ]
    
    for title in similar_removals:
        print(f"🗑️ Removing similar duplicate: {title}")
        pattern = rf'\s*{{\s*title:\s*"{re.escape(title)}",.*?\n\s*}},?\s*'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        removed_count += 1
    
    # Clean up any double commas or formatting issues
    content = re.sub(r',\s*,', ',', content)
    content = re.sub(r',\s*\]', ']', content)
    
    # Update the count
    current_count = len(re.findall(r'title:\s*"', content))
    print(f"\n📊 REMOVAL SUMMARY")
    print("-" * 20)
    print(f"Specific duplicates removed: {removed_count}")
    print(f"New initiative count: {current_count}")
    
    # Save the cleaned content
    with open('/workspace/index.html', 'w') as f:
        f.write(content)
    
    # Update the stat display
    updated_content = content.replace(
        '<span class="stat-number" id="totalCount">1091</span>',
        f'<span class="stat-number" id="totalCount">{current_count}</span>'
    )
    
    with open('/workspace/index.html', 'w') as f:
        f.write(updated_content)
    
    print(f"✅ File updated with {current_count} unique initiatives")
    return current_count

if __name__ == "__main__":
    final_count = remove_specific_duplicates()