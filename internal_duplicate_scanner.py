#!/usr/bin/env python3
"""
Internal Duplicate Scanner for Current Catalog
Identifies duplicates within the existing 1091 initiatives
"""

import re
from difflib import SequenceMatcher
from collections import defaultdict

def normalize_text(text):
    """Normalize text for comparison"""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    # Remove common prefixes/suffixes
    text = re.sub(r'^(to |platform to |app to |initiative to |create |provide |support |distribute |sponsor |fund |organize |build |install |set up |establish )', '', text)
    text = re.sub(r'(platform|app|initiative|program|system|network|bank|support|hub|tracker|fund|leaderboard)$', '', text)
    text = text.strip()
    return text

def similarity_score(a, b):
    """Calculate similarity between two strings"""
    return SequenceMatcher(None, normalize_text(a), normalize_text(b)).ratio()

def extract_keywords(text):
    """Extract key concepts from text"""
    normalized = normalize_text(text)
    keywords = set()
    
    # Add important terms
    for word in normalized.split():
        if len(word) > 3 and word not in ['with', 'from', 'this', 'that', 'will', 'have', 'been', 'they', 'them', 'their', 'these', 'those', 'poor', 'rich', 'family', 'families', 'children', 'people']:
            keywords.add(word)
    
    return keywords

def keyword_overlap(text1, text2):
    """Calculate keyword overlap between two texts"""
    keywords1 = extract_keywords(text1)
    keywords2 = extract_keywords(text2)
    
    if not keywords1 or not keywords2:
        return 0
    
    intersection = len(keywords1.intersection(keywords2))
    union = len(keywords1.union(keywords2))
    
    return intersection / union if union > 0 else 0

def find_internal_duplicates():
    """Find duplicates within current catalog"""
    
    # Read current initiatives
    with open('/workspace/current_initiatives.txt', 'r') as f:
        initiatives = [line.strip() for line in f if line.strip()]
    
    print(f"🔍 INTERNAL DUPLICATE ANALYSIS")
    print(f"=" * 50)
    print(f"Scanning {len(initiatives)} initiatives for internal duplicates...")
    print()
    
    # Find duplicates
    duplicates = []
    processed = set()
    
    for i, init1 in enumerate(initiatives):
        if i in processed:
            continue
            
        similar_group = [(i, init1)]
        
        for j, init2 in enumerate(initiatives[i+1:], i+1):
            if j in processed:
                continue
                
            similarity = similarity_score(init1, init2)
            keyword_sim = keyword_overlap(init1, init2)
            
            # More aggressive duplicate detection
            if similarity >= 0.75 or keyword_sim >= 0.7:
                similar_group.append((j, init2))
                processed.add(j)
        
        if len(similar_group) > 1:
            duplicates.append(similar_group)
            for idx, _ in similar_group:
                processed.add(idx)
    
    # Display results
    print("🎯 DUPLICATE GROUPS FOUND")
    print("-" * 40)
    
    total_duplicates = 0
    removal_candidates = []
    
    for group_num, group in enumerate(duplicates, 1):
        print(f"\n📦 GROUP {group_num} ({len(group)} similar initiatives):")
        print("-" * 30)
        
        # Sort by length (keep the most comprehensive)
        group.sort(key=lambda x: len(x[1]), reverse=True)
        
        for i, (idx, text) in enumerate(group):
            status = "✅ KEEP (Most comprehensive)" if i == 0 else f"🗑️ REMOVE (Duplicate {i})"
            print(f"{status}")
            print(f"   {idx}: {text[:100]}{'...' if len(text) > 100 else ''}")
            
            if i > 0:  # Mark for removal
                removal_candidates.append((idx, text))
                total_duplicates += 1
        print()
    
    # Check for theme-based consolidation opportunities
    print("🔍 THEME-BASED CONSOLIDATION OPPORTUNITIES")
    print("-" * 40)
    
    themes = {
        'eye': [],
        'dental': [],
        'bicycle': [],
        'solar': [],
        'water': [],
        'housing': [],
        'education': [],
        'medical': [],
        'food': [],
        'clothing': [],
        'widow': [],
        'orphan': [],
        'sewing': [],
        'farmers': [],
        'street vendor': [],
        'ambulance': [],
        'toilet': [],
        'library': []
    }
    
    for i, text in enumerate(initiatives):
        text_lower = text.lower()
        for theme in themes:
            if theme in text_lower:
                themes[theme].append((i, text))
    
    consolidation_opportunities = 0
    for theme, items in themes.items():
        if len(items) > 3:  # More than 3 initiatives in same theme
            print(f"\n🎨 {theme.upper()} THEME ({len(items)} initiatives):")
            for idx, text in items[:5]:  # Show first 5
                print(f"   {idx}: {text[:80]}{'...' if len(text) > 80 else ''}")
            if len(items) > 5:
                print(f"   ... and {len(items) - 5} more")
            consolidation_opportunities += max(0, len(items) - 2)  # Keep 2, consolidate rest
    
    print(f"\n📊 DUPLICATE REMOVAL SUMMARY")
    print("-" * 40)
    print(f"Current initiatives: {len(initiatives)}")
    print(f"Exact/near duplicates found: {total_duplicates}")
    print(f"Theme consolidation opportunities: {consolidation_opportunities}")
    print(f"Total potential removals: {total_duplicates + consolidation_opportunities}")
    print(f"Optimized catalog size: {len(initiatives) - total_duplicates - consolidation_opportunities}")
    
    return removal_candidates, duplicates, themes

if __name__ == "__main__":
    removal_candidates, duplicates, themes = find_internal_duplicates()