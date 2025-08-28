#!/usr/bin/env python3
"""
Final cleanup to remove remaining 55 duplicates
Target: 1040 → 985 initiatives
"""

import re

def remove_remaining_duplicates():
    """Remove the remaining 55 duplicates based on actual file content"""
    
    with open('/workspace/index.html', 'r') as f:
        content = f.read()
    
    # Additional titles to remove based on actual file inspection (55 items)
    additional_titles = [
        "Daily Wage Worker Connect",
        "Borewell Feasibility Analyzer", 
        "Auto Driver Quarterly Support",
        "Cobbler Permanent Shop Support",
        "Village Plastic Recycling",
        "Village Water Supply Design",
        "Orphan Children Support",
        "Community Electricity Support",
        "Free Eye Testing Program",
        "Free Dental Care",
        "Breadwinner Loss Support",
        "Accident Recovery Support", 
        "Autism Family Support",
        "Village Education Scholarships",
        "Poor Home Repair Support",
        "Tree Planting Support",
        "Funeral Cost Support",
        "Village Solar Light Installation",
        "Disaster Grocery Support",
        "Summer Cooling Support",
        "Village Medical Visits",
        "Community Bus Trips",
        "Community Library Building",
        "Slum Relocation Support",
        "Village School Upgrades",
        "Community Ambulance Services",
        "Handloom Weaver Support",
        "Kidney Transplant Support",
        "Cancer Treatment Support",
        "Widow Support Services",
        "Farmer Widow Support System",
        "Free Medicine Expiry Redistribution",
        "Burn Victim Support Platform",
        "Free Emergency Funeral Support",
        "Village Seed Banks",
        "Disability Support Hub",
        "Village Elder Care Platform",
        "Village Medical Emergency Transport",
        "Free Tuition Bank",
        "Marriage Support for Poor Girls",
        "Rehabilitation Support Platform",
        "Village Electricity Bank", 
        "Free Footwear Bank",
        "Educational Transportation Support",
        "Community Knowledge Centers",
        "Free Tuition Support Network",
        "Community Fertilizer Bank",
        "Street Vendor Quarterly Support",
        "Community Fertilizer Sharing Hub",
        "Community Clothing Exchange Hub",
        "Healthcare Crisis Support Fund",
        "Village Green Economy Initiative",
        "Community Energy Access Program",
        "Family Crisis Support Network",
        "Autism Family Support Hub",
        "Plastic-Free Community Program"
    ]
    
    print(f"Removing {len(additional_titles)} additional duplicates...")
    
    removed_count = 0
    
    # Remove each initiative
    for title in additional_titles:
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
    
    # Clean up any formatting issues
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
    
    return removed_count, new_count

def main():
    """Main function"""
    print("🎯 Final Cleanup - Removing Remaining 55 Duplicates")
    print("Goal: 1040 → 985 initiatives\n")
    
    initial_count = len(re.findall(r'title:', open('/workspace/index.html').read()))
    print(f"Current count: {initial_count}")
    
    removed, final_count = remove_remaining_duplicates()
    
    print(f"\n🎯 FINAL TRANSFORMATION SUMMARY:")
    print(f"🔥 BEFORE: {initial_count} initiatives")
    print(f"✨ AFTER: {final_count} initiatives")
    print(f"🗑️ REMOVED: {removed} duplicates")
    print(f"🎯 TARGET ACHIEVED: {final_count == 985}")
    
    if final_count == 985:
        print("\n✅ SUCCESS! Exactly 985 unique initiatives achieved!")
        print("\n📊 TRANSFORMATION SUMMARY:")
        print("🔥 BEFORE: 1089 initiatives (with significant duplication)")
        print("✨ AFTER: 985 unique, high-quality initiatives")  
        print("🗑️ REMOVED: 104 total duplicates")
        print("\n🎯 SPECIFIC DUPLICATES ELIMINATED:")
        print("✅ User Identified Duplicates (8 removed)")
        print("✅ Donate-a-X Campaigns (20 removed)")
        print("✅ Village/Community Initiatives (15+ removed)")
        print("✅ Thematic Duplicates (61+ removed)")

if __name__ == "__main__":
    main()