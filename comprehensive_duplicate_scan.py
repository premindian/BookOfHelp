#!/usr/bin/env python3
"""
Comprehensive scan for any remaining duplicates
Final quality assurance for the catalog
"""

import re
from difflib import SequenceMatcher
from collections import defaultdict

def extract_all_initiatives():
    """Extract all initiatives from the current file"""
    with open('/workspace/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract initiative objects
    pattern = r'\{[^{}]*?title:\s*"([^"]*)"[^{}]*?description:\s*"([^"]*)"[^{}]*?\}'
    matches = re.findall(pattern, content, re.DOTALL)
    
    initiatives = []
    for i, (title, description) in enumerate(matches):
        initiatives.append({
            'index': i,
            'title': title.strip(),
            'description': description.strip()[:200] + "..." if len(description.strip()) > 200 else description.strip()
        })
    
    return initiatives

def find_exact_duplicates(initiatives):
    """Find initiatives with identical titles"""
    title_groups = defaultdict(list)
    
    for init in initiatives:
        title_groups[init['title']].append(init)
    
    return {title: inits for title, inits in title_groups.items() if len(inits) > 1}

def find_highly_similar(initiatives, threshold=0.9):
    """Find initiatives with very similar titles"""
    similar_pairs = []
    
    for i, init1 in enumerate(initiatives):
        for j, init2 in enumerate(initiatives[i+1:], i+1):
            similarity = SequenceMatcher(None, init1['title'].lower(), init2['title'].lower()).ratio()
            if similarity >= threshold:
                similar_pairs.append((init1, init2, similarity))
    
    return similar_pairs

def main():
    """Main scan function"""
    print("🔍 COMPREHENSIVE DUPLICATE SCAN")
    print("Scanning current catalog for any remaining duplicates...\n")
    
    initiatives = extract_all_initiatives()
    print(f"📊 Scanning {len(initiatives)} initiatives\n")
    
    # Check for exact duplicates
    exact_dupes = find_exact_duplicates(initiatives)
    print("1️⃣ EXACT DUPLICATE TITLES:")
    if exact_dupes:
        for title, inits in exact_dupes.items():
            print(f"   🔴 '{title}' appears {len(inits)} times")
            for init in inits:
                print(f"      - Index {init['index']}: {init['description']}")
    else:
        print("   ✅ No exact duplicate titles found")
    
    print()
    
    # Check for highly similar titles
    similar_pairs = find_highly_similar(initiatives, 0.9)
    print("2️⃣ HIGHLY SIMILAR TITLES (>90% similarity):")
    if similar_pairs:
        for init1, init2, similarity in similar_pairs:
            print(f"   🟡 {similarity:.1%} similarity:")
            print(f"      - '{init1['title']}'")
            print(f"      - '{init2['title']}'")
    else:
        print("   ✅ No highly similar titles found")
    
    print()
    
    # Summary
    total_issues = len(exact_dupes) + len(similar_pairs)
    if total_issues == 0:
        print("🎉 EXCELLENT QUALITY!")
        print(f"✅ All {len(initiatives)} initiatives are unique")
        print("🚀 Catalog is optimally curated for bookofhelp.com!")
    else:
        print(f"📝 Found {total_issues} potential quality issues to address")
    
    return exact_dupes, similar_pairs

if __name__ == "__main__":
    main()