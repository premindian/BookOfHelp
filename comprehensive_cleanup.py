#!/usr/bin/env python3
"""
Comprehensive Cleanup Script
Removes the major duplicates found in the internal analysis
"""

import re

def comprehensive_cleanup():
    """Remove all identified duplicates"""
    
    with open('/workspace/index.html', 'r') as f:
        content = f.read()
    
    print("🚀 COMPREHENSIVE DUPLICATE CLEANUP")
    print("=" * 50)
    
    # Priority duplicates to remove (keeping the most comprehensive versions)
    major_duplicates = [
        # Donate-a-X Campaign duplicates (keep only Donate-a-Pencil Box Campaign)
        "Donate-a-Helmet Campaign",
        "Donate-a-Pillow Campaign", 
        "Donate-a-Fan Campaign",
        "Donate-a-Bucket Campaign",
        "Donate-a-Bag Campaign",
        "Donate-a-Bed Campaign",
        "Donate-a-Lantern Campaign",
        
        # Village Sovereignty/Paradise duplicates (keep main transformation hubs)
        "Village Health Sovereignty Council",
        "Village Technology Sovereignty Council", 
        "Village Employment Sovereignty Council",
        "Village Food Sovereignty Alliance",
        "Village Universal Sovereignty Platform",
        "Village Youth Sovereignty Program",
        "Village Ultimate Paradise Platform",
        "Village Health Paradise Ecosystem",
        "Village Food Paradise Ecosystem",
        "Rural Health Paradise Ecosystem",
        "Rural Food Paradise Ecosystem",
        
        # Community Sovereignty duplicates
        "Community Social Sovereignty Movement",
        "Community Food Sovereignty Movement", 
        "Community Health Sovereignty Program",
        "Community Employment Sovereignty Hub",
        "Community Skill Sovereignty Network",
        "Community Technology Sovereignty",
        "Community Disaster Sovereignty Network",
        
        # Emergency/Fund duplicates
        "Community Emergency Harmony Network",
        "Community Emergency Medicines Bank",
        "Community Emergency Fund",
        
        # Village Innovation duplicates
        "Village Youth Innovation Ecosystem",
        "Village Youth Innovation Program", 
        "Village Perfect Innovation Hub",
        "Village Innovation Lab",
        
        # Renewable Energy duplicates
        "Community Renewable Energy Revolution",
        "Village Renewable Energy Cooperative",
        "Community Renewable Energy Education",
        "Community Renewable Energy Storage",
        
        # Health duplicates
        "Community Health Volunteer Network",
        "Community Health Equity Initiative",
        "Community Health Abundance Network",
        "Community Health Emergency Fund",
        
        # Financial duplicates
        "Village Financial Sovereignty Program",
        "Village Financial Literacy Program",
        "Village Digital Literacy Program", 
        "Rural Financial Literacy Program",
        "Rural Women Financial Literacy",
        "Village Financial Harmony Hub",
        
        # Leadership duplicates
        "Village Women Leadership Revolution",
        "Village Women Leadership Training",
        "Village Women Leadership Council",
        "Village Youth Leadership Network",
        
        # Agricultural duplicates
        "Community Agricultural Research Network",
        "Community Agricultural Value Addition",
        "Community Agricultural Transformation",
        "Rural Agricultural Innovation Network",
        "Community Agricultural Wisdom Network",
        "Community Agricultural Innovation Lab",
        
        # Disaster duplicates
        "Community Disaster Shelter Network",
        "Community Disaster Risk Reduction",
        "Community Disaster Recovery Fund",
        "Village Disaster Preparedness Training",
        "Community Disaster Recovery Training",
        
        # Infrastructure duplicates
        "Rural Infrastructure Crowdfunding Platform",
        "Rural Infrastructure Planning Platform", 
        "Rural Infrastructure Smart Development",
        "Village Infrastructure Intelligence System",
        
        # Women empowerment duplicates
        "Village Women Economic Empowerment",
        "Village Women Empowerment Center",
        "Rural Women Entrepreneurship Hub",
        "Rural Women Leadership Program",
        
        # Water theme duplicates (keep main water security platform)
        "Village Water Abundance Initiative",
        "Village Water Paradise Initiative",
        "Rural Water Wisdom Network",
        "Community Water Harvesting Expansion",
        
        # Wisdom/Traditional duplicates
        "Village Traditional Knowledge Preservation",
        "Village Traditional Knowledge Database",
        "Village Traditional Wisdom Preservation",
        "Village Food Wisdom Preservation",
        "Village Wisdom Council Network",
        "Rural Wisdom Sovereignty Network",
        
        # Multiple bicycle-related duplicates (keeping core bicycle network)
        "Shared Village Bicycle Ambulance",
        "Shared Village Bicycle Milk Vans", 
        "Shared Village Bicycle Pool",
        "Community Cycle Repair Hubs",
        "Village Bicycle Repair Corners",
        
        # Perfect/Ultimate/Infinite duplicates
        "Community Perfect Wellness System",
        "Community Perfect Life Ecosystem",
        "Village Ultimate Miracle Platform",
        "Village Ultimate Unity Platform",
        "Community Infinite Peace Ecosystem",
        "Community Infinite Love Ecosystem",
        "Community Infinite Potential Activator",
        "Rural Infinite Wisdom Network",
        
        # Transformation duplicates
        "Community Transformation Sovereignty Movement",
        "Community Youth Transformation Program",
        "Village Ultimate Transformation Platform",
        "Village Health Transformation Initiative",
        
        # Renaissance/Paradise duplicates
        "Community Technological Renaissance",
        "Community Agricultural Renaissance",
        "Community Technological Paradise",
        "Village Environmental Renaissance",
        "Rural Complete Paradise Ecosystem"
    ]
    
    removed_count = 0
    
    for duplicate_title in major_duplicates:
        print(f"🗑️ Removing: {duplicate_title}")
        # Create a regex pattern to match the entire initiative block
        pattern = rf'\s*{{\s*title:\s*"{re.escape(duplicate_title)}",.*?\n\s*}},?\s*'
        before_count = len(re.findall(r'title:\s*"', content))
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        after_count = len(re.findall(r'title:\s*"', content))
        
        if before_count > after_count:
            removed_count += 1
    
    # Clean up formatting issues
    content = re.sub(r',\s*,', ',', content)
    content = re.sub(r',\s*\]', ']', content)
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)  # Remove excessive blank lines
    
    # Count final initiatives
    final_count = len(re.findall(r'title:\s*"', content))
    
    print(f"\n📊 COMPREHENSIVE CLEANUP SUMMARY")
    print("-" * 40)
    print(f"Major duplicates targeted for removal: {len(major_duplicates)}")
    print(f"Successfully removed: {removed_count}")
    print(f"Final optimized count: {final_count}")
    print(f"Total reduction: {1082 - final_count} initiatives")
    
    # Update the stat display
    content = re.sub(
        r'<span class="stat-number" id="totalCount">\d+</span>',
        f'<span class="stat-number" id="totalCount">{final_count}</span>',
        content
    )
    
    # Save the optimized content
    with open('/workspace/index.html', 'w') as f:
        f.write(content)
    
    print(f"✅ Catalog optimized to {final_count} unique, high-quality initiatives!")
    return final_count

if __name__ == "__main__":
    final_count = comprehensive_cleanup()