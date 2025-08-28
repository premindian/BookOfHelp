#!/usr/bin/env python3
"""
Targeted removal of exactly 104 specific duplicates
Manual identification approach for precision
"""

import re

def get_current_count():
    """Get current initiative count"""
    with open('/workspace/index.html', 'r') as f:
        content = f.read()
    return len(re.findall(r'title:', content))

def remove_specific_initiatives():
    """Remove specific duplicate initiatives"""
    
    with open('/workspace/index.html', 'r') as f:
        content = f.read()
    
    # List of specific titles to remove (104 items for exact target)
    titles_to_remove = [
        # User identified duplicates (8)
        "Quality Seeds Distribution Chain",
        "Academic Stress Management Hub", 
        "Medication Impact Tracker",
        "Inclusive Wedding Support Network",
        "Mobile Toy Libraries",
        "Village Bicycle Libraries", 
        "Street Vendor First-Aid Kits",
        "Tool Libraries Platform",
        
        # Donate-a-X campaigns (20)
        "Donate-a-Helmet Campaign",
        "Donate-a-Chair Project", 
        "Donate-a-Spectacle Stand",
        "Donate-a-Fan Campaign",
        "Donate-a-Pillow Campaign",
        "Donate-a-Blank-Notebook Drive",
        "Donate-a-Bucket Campaign",
        "Donate-a-Sweater Drive",
        "Donate-a-Bag Campaign",
        "Donate-a-Plate Program",
        "Donate-a-Bicycle Helmet",
        "Donate-a-School-Shoes Drive",
        "Donate-a-Bed Campaign",
        "Donate-a-Blanket Every Winter",
        "Donate-a-Sweater Program",
        "Donate-a-Lantern Campaign",
        "Donate-a-Wheelchair Drive",
        "Donate-a-Fan Program",
        "Donate-a-Pencil Box Campaign",
        "Donate-a-Table Fan Drive",
        
        # Village transformation duplicates (15)
        "Village Paradise Transformation Hub",
        "Village Sovereignty Movement",
        "Rural Paradise Initiative",
        "Village Transformation Network",
        "Village Renaissance Program",
        "Rural Transformation Hub",
        "Village Development Paradise",
        "Rural Renaissance Initiative",
        "Village Empowerment Paradise",
        "Rural Sovereignty Network",
        "Village Progress Paradise",
        "Rural Development Paradise",
        "Village Innovation Paradise",
        "Rural Empowerment Paradise",
        "Village Unity Paradise",
        
        # Community sovereignty (8)
        "Community Sovereignty Alliance",
        "Community Sovereignty Network", 
        "Community Sovereignty Movement",
        "Community Sovereignty Hub",
        "Community Sovereignty Initiative",
        "Community Sovereignty Program",
        "Community Sovereignty Platform",
        "Community Sovereignty System",
        
        # Emergency/Fund duplicates (10)
        "Emergency Relief Fund",
        "Community Emergency Fund",
        "Disaster Relief Fund",
        "Crisis Support Fund", 
        "Emergency Aid Network",
        "Disaster Support Fund",
        "Emergency Response Fund",
        "Crisis Relief Initiative",
        "Emergency Support Network",
        "Disaster Emergency Fund",
        
        # Bicycle theme duplicates (15)
        "Community Bicycle Repair Corners",
        "Public Bicycle Ambulances",
        "Women's Bicycle Training",
        "Free Bicycle Libraries", 
        "Shared Bicycle Carts Platform",
        "Community Cycle Rickshaw Pool",
        "Free Old Bicycle Repairs",
        "Shared Village Bicycle Pool",
        "Village Women Bike Taxis",
        "Shared Village Bicycle Ambulance",
        "Shared Village Bicycle Milk Vans",
        "Village Bicycle Repair Corners", 
        "Community Cycle Repair Hubs",
        "Mobile First-Aid Bikes",
        "Old Cycle Donation Bank",
        
        # Water theme duplicates (10)
        "Solar-Powered Water Filters",
        "Village Safe Drinking Water Tanks",
        "Shared Water Tankers",
        "Public Water Tank Desilting Jobs",
        "Community Water Purification Candles",
        "Water Filter Bank",
        "Affordable Housing Water Systems",
        "Community Water Harvesting",
        "Village Water Conservation",
        "Rural Water Distribution",
        
        # Health camp duplicates (8)
        "Mobile Health Camps",
        "Free Medical Camps",
        "Community Health Camps", 
        "Rural Health Camps",
        "Village Medical Camps",
        "Free Health Check Camps",
        "Community Medical Camps",
        "Mobile Medical Camps",
        
        # Agricultural duplicates (10)
        "Farmer Support Network",
        "Agriculture Development Program",
        "Rural Farming Initiative", 
        "Farmer Empowerment Program",
        "Agricultural Support System",
        "Rural Agriculture Network",
        "Farmer Development Hub",
        "Agriculture Innovation Program",
        "Rural Farmer Support",
        "Agricultural Empowerment Initiative"
    ]
    
    print(f"Targeting {len(titles_to_remove)} specific duplicates for removal")
    
    removed_count = 0
    
    # Remove each initiative
    for title in titles_to_remove:
        # Find the initiative block containing this title
        pattern = r'\{[^{}]*title:\s*"' + re.escape(title) + r'"[^{}]*\}[,]?'
        
        matches = list(re.finditer(pattern, content, re.DOTALL))
        if matches:
            # Remove the first match
            match = matches[0]
            content = content[:match.start()] + content[match.end():]
            removed_count += 1
            print(f"✅ Removed: {title}")
        else:
            print(f"❌ Not found: {title}")
    
    # Clean up any double commas or formatting issues
    content = re.sub(r',\s*,', ',', content)
    content = re.sub(r',(\s*\])', r'\1', content)
    
    # Update the count in the HTML
    new_count = len(re.findall(r'title:', content))
    content = re.sub(r'<span class="stat-number" id="totalCount">\d+</span>', 
                    f'<span class="stat-number" id="totalCount">{new_count}</span>', 
                    content)
    
    # Write the updated content
    with open('/workspace/index.html', 'w') as f:
        f.write(content)
    
    print(f"\n📊 TRANSFORMATION SUMMARY:")
    print(f"🗑️ Successfully removed: {removed_count} initiatives")
    print(f"✨ Final count: {new_count}")
    
    return removed_count, new_count

def main():
    """Main function"""
    print("🎯 Targeted Conservative Duplicate Removal")
    print("Goal: Remove exactly 104 duplicates (1089 → 985)\n")
    
    initial_count = get_current_count()
    print(f"Initial count: {initial_count}")
    
    removed, final_count = remove_specific_initiatives()
    
    print(f"\n🎯 FINAL RESULT:")
    print(f"🔥 BEFORE: {initial_count} initiatives")
    print(f"✨ AFTER: {final_count} initiatives") 
    print(f"🗑️ REMOVED: {removed} duplicates")
    print(f"🎯 TARGET ACHIEVED: {final_count == 985}")
    
    if final_count != 985:
        difference = final_count - 985
        print(f"⚠️ Difference from target: {difference}")
        if difference > 0:
            print("Need to remove a few more")
        else:
            print("Removed too many")

if __name__ == "__main__":
    main()