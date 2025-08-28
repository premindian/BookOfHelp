#!/usr/bin/env python3
"""
Comprehensive Duplicate Analysis Script
Identifies duplicates between original 1250+ list and current 1091 catalog
"""

import re
from difflib import SequenceMatcher
import json

def normalize_text(text):
    """Normalize text for comparison"""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
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
    # Common keywords that indicate similar concepts
    keywords = set()
    
    # Add important terms
    for word in normalized.split():
        if len(word) > 3 and word not in ['with', 'from', 'this', 'that', 'will', 'have', 'been', 'they', 'them', 'their', 'these', 'those']:
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

def find_comprehensive_duplicates():
    """Comprehensive duplicate analysis"""
    
    # Read original initiatives (now comprehensive)
    with open('/workspace/full_original_list.txt', 'r') as f:
        original_full = [line.strip() for line in f if line.strip()]
    
    # Read current initiatives
    with open('/workspace/current_initiatives.txt', 'r') as f:
        current = [line.strip() for line in f if line.strip()]
    
    print(f"📊 COMPREHENSIVE DUPLICATE ANALYSIS")
    print(f"=" * 50)
    print(f"Original list: {len(original_full)} initiatives")
    print(f"Current catalog: {len(current)} initiatives")
    print(f"Estimated duplicates removed: {len(original_full) - len(current)}")
    print()
    
    # Find matches
    exact_matches = []
    high_similarity = []
    medium_similarity = []
    keyword_matches = []
    
    matched_current_indices = set()
    
    for i, orig in enumerate(original_full):
        best_matches = []
        
        for j, curr in enumerate(current):
            similarity = similarity_score(orig, curr)
            keyword_sim = keyword_overlap(orig, curr)
            
            if similarity >= 0.7 or keyword_sim >= 0.6:
                best_matches.append((j, curr, similarity, keyword_sim))
        
        # Sort by best similarity
        best_matches.sort(key=lambda x: max(x[2], x[3]), reverse=True)
        
        if best_matches:
            j, curr, sim, kw_sim = best_matches[0]
            
            if sim >= 0.95:  # Exact match
                exact_matches.append((i, orig, j, curr, sim, kw_sim))
                matched_current_indices.add(j)
            elif sim >= 0.8 or kw_sim >= 0.8:  # High similarity
                high_similarity.append((i, orig, j, curr, sim, kw_sim))
                matched_current_indices.add(j)
            elif sim >= 0.7 or kw_sim >= 0.6:  # Medium similarity
                medium_similarity.append((i, orig, j, curr, sim, kw_sim))
                matched_current_indices.add(j)
    
    # Display results
    print("🎯 EXACT MATCHES (95%+ similarity)")
    print("-" * 40)
    for i, (orig_idx, orig, curr_idx, curr, sim, kw_sim) in enumerate(exact_matches, 1):
        print(f"{i}. ORIGINAL: {orig}")
        print(f"   CURRENT:  {curr}")
        print(f"   SIMILARITY: {sim:.1%} | KEYWORDS: {kw_sim:.1%}")
        print()
    
    print("🔍 HIGH SIMILARITY MATCHES (80-95% similarity)")
    print("-" * 40)
    for i, (orig_idx, orig, curr_idx, curr, sim, kw_sim) in enumerate(high_similarity[:20], 1):  # Show first 20
        print(f"{i}. ORIGINAL: {orig}")
        print(f"   CURRENT:  {curr}")
        print(f"   SIMILARITY: {sim:.1%} | KEYWORDS: {kw_sim:.1%}")
        print()
    
    if len(high_similarity) > 20:
        print(f"   ... and {len(high_similarity) - 20} more high similarity matches")
        print()
    
    print("📋 SUMMARY OF DUPLICATES IDENTIFIED")
    print("-" * 40)
    print(f"✅ Exact matches: {len(exact_matches)}")
    print(f"🎯 High similarity: {len(high_similarity)}")
    print(f"📊 Medium similarity: {len(medium_similarity)}")
    print(f"📈 Total potential duplicates: {len(exact_matches) + len(high_similarity) + len(medium_similarity)}")
    print()
    print(f"📉 ESTIMATED CONSOLIDATION IMPACT")
    print("-" * 40)
    total_matches = len(exact_matches) + len(high_similarity) + len(medium_similarity)
    estimated_removed = len(original_full) - len(current)
    print(f"Original initiatives: {len(original_full)}")
    print(f"Current unique catalog: {len(current)}")
    print(f"Initiatives consolidated/removed: {estimated_removed}")
    print(f"Match detection accuracy: {(total_matches/estimated_removed)*100:.1f}%" if estimated_removed > 0 else "N/A")
    
    # Create a report of removed/consolidated items
    print(f"\n🗑️ SAMPLE OF LIKELY CONSOLIDATED INITIATIVES")
    print("-" * 40)
    
    matched_originals = {item[0] for item in exact_matches + high_similarity + medium_similarity}
    unmatched_originals = [orig for i, orig in enumerate(original_full) if i not in matched_originals]
    
    print(f"These {len(unmatched_originals)} initiatives from your original list appear to have been")
    print(f"consolidated, merged, or refined during catalog creation:")
    print()
    
    for i, initiative in enumerate(unmatched_originals[:30], 1):  # Show first 30
        print(f"{i}. {initiative}")
    
    if len(unmatched_originals) > 30:
        print(f"... and {len(unmatched_originals) - 30} more initiatives")
    
    return {
        'exact_matches': exact_matches,
        'high_similarity': high_similarity, 
        'medium_similarity': medium_similarity,
        'unmatched_originals': unmatched_originals,
        'total_original': len(original_full),
        'total_current': len(current),
        'estimated_removed': estimated_removed
    }

if __name__ == "__main__":
    results = find_comprehensive_duplicates()