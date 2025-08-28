#!/usr/bin/env python3
"""
Duplicate Analysis Script for Social Impact Initiatives
Compares original 1250+ list with current 1091 catalog
"""

import re
from difflib import SequenceMatcher
from collections import defaultdict

def normalize_text(text):
    """Normalize text for comparison"""
    # Convert to lowercase
    text = text.lower()
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove common prefixes/suffixes
    text = re.sub(r'^(to |platform to |app to |initiative to )', '', text)
    text = re.sub(r'(platform|app|initiative)$', '', text)
    text = text.strip()
    return text

def similarity_score(a, b):
    """Calculate similarity between two strings"""
    return SequenceMatcher(None, normalize_text(a), normalize_text(b)).ratio()

def parse_original_list():
    """Parse the original user list into individual initiatives"""
    original_text = """Facilitate the distribution of used textbooks at the school level—free or at a small price—from seniors to juniors, promoting reuse, affordability, and eco-conscious education.
To digitally connect daily wage workers with task givers, enabling a dignified, decentralized employment network across towns and villages with fairness in wages, transparency, and mutual respect.
To reduce stress levels in school systems especially like intermediate college where students go through severe stress to crack engineering or medicine seat
Humongous real time tracking on a given medication where in users can login side affects that they experience.
Give a helping hand to physically disabled and economically disadvantaged bride and bridegroom at their marriage venue
create a supply chain to distribute quality seeds for various crops like paddy, groundnut, millets etc for poor disadvantaged farmers
Enter soil composition and other metrics to see the feasibility for borewell and digging borewell for disadvantaged farmers..
Managing Agri-Clinics support at individual farmer level involving Soil health, Cropping practices, Plant protection, Post-harvest technology, Prices for various crops etc, include your ideas and make it one stop robust
Create a fertilizers bank for disadvantaged farmers
 provide street cart vendors a gift per quarter from willing rich people.
 provide auto drivers a gift per quarter from willing rich people.
 redistribute used toys (ages 2–5 & 5–9) to disadvantaged kids.
 Distribute surplus fruits from shops/street vendors to disadvantaged/orphanages/homeless.
 Track & distribute used clothes via drop boxes.
 Platform for poor to request money, rich to give, leaderboard for donors.
 Donation logging leaderboard for ultra-rich NGOs.
 Support cobblers on roads to get permanent small shops.
 Raise citizen issues to MLA/MLC/MP via ticketing .
 Mobilize small funds for patient caretakers, memorial services, books, travel, sporting goods.
 Receive already donated blood from local bank, leaderboard for donors.
 Recycling plastic/paper at village level with incentive system.
 Design safe drinking water supply for villages.
 Education fund for poor children sponsored by rich, leaderboard.
 Identify places needing public toilets, get funds from rich, leaderboard.
 Support young children who lost both parents, leaderboard.
 Mobilize small funds to buy push carts for new vendors, leaderboard.
 List rural road potholes and track resolution.
 Rich to pay poor communities' electricity bills as a group.
 Support poor fishermen with basic living fund in off-season, leaderboard.
 Sponsor cleft surgery for poor children.
 Lottery-based holiday adventure trip for poor children by rich sponsors, leaderboard.
 Sponsor a cooking gas cylinder to a poor family, leaderboard.
 Distribute school uniforms to children from poor neighborhoods, sponsors leaderboard.
 Distribute non-smartphones to elderly poor with 1-year subscription, sponsors leaderboard.
 Distribute sporting shoes to underprivileged village youth, sponsors leaderboard.
 Provide 6-month sewing machine training and donate machines to unemployed poor.
 Distribute mosquito nets to poor neighborhoods.
 Support free eye testing and spectacles donation for poor, sponsors leaderboard.
 Provide free dental checkups and procedures to poor, sponsors leaderboard.
 Provide free wheelchairs (motorized/non-motorized) to handicapped poor, sponsors leaderboard.
 Sponsor hearing aids for disadvantaged with hearing loss, sponsors leaderboard.
 Sponsor sports equipment for rural poor kids, sponsors leaderboard.
 Support families in poor communities who lose their breadwinner, sponsors leaderboard.
 Support poor families to overcome accident injury costs, sponsors leaderboard.
 Support poor families affected by autism, sponsors leaderboard.
 Scholarship for bright village poor children for higher education, sponsors leaderboard.
 Support repair of poor homes in backward communities, sponsors leaderboard.
 Support charities listed on leaders board across various help networks.
 Provide legal support to disadvantaged poor.
 Support tree planting with resources/funds, sponsors leaderboard.
 Support poor communities working to eradicate plastic bags with degradable alternatives.
 Support poor families with funeral costs for a tragic death, sponsors leaderboard.
 Provide extra medical funds to poor apart from government aid, sponsors leaderboard.
 Distribute free basic water filters to poor neighborhoods, sponsors leaderboard.
 Support old govt hospitals' ICU upgrades: cots, outlets, dustbins, sponsors leaderboard.
 Fund prosthetic devices for limb loss patients, sponsors leaderboard.
 Distribute blankets, raincoats, and sleeping mats to homeless poor, sponsors leaderboard.
 Install benches in parks in poor neighborhoods, sponsors leaderboard.
 Provide solar light installation in villages without electricity, sponsors leaderboard.
 Supply 1-month essential grocery packages to poor after natural disasters, sponsors leaderboard.
 Celebrate orphan child's birthday with cake from orphanage/bakery, fraud prevention checks.
 Distribute diapers to economically poor parents for newborns/toddlers, sponsors leaderboard.
 Set up mobile food delivery for homeless/underprivileged in areas lacking govt canteens, sponsors leaderboard.
 Provide summer coolers/fans to poor households with disabled or elderly, sponsors leaderboard.
 Sponsor agricultural experts to educate poor farmers on new technologies, sponsors leaderboard.
 Sponsor doctor/nurse visits to poor villages, leaderboard for sponsors & medics.
 Sponsor bus trips for 50 people from poor neighborhoods for picnics, sponsors leaderboard.
 Pay unemployed youth to clean poor neighborhoods, sponsors & helpers leaderboard.
 Provide water tanks/hand pumps for underprivileged communities, sponsors leaderboard.
 Support unemployed village youth with 3-month stipend in cities to find jobs, sponsors leaderboard.
 Fund solar/electric street lamps in poorly lit poor neighborhoods, sponsors leaderboard.
 Build/support community library with tech/books for poor neighborhoods, sponsors leaderboard.
 Provide quick aid to farmers after crop damage from disasters, sponsors leaderboard.
 Relocate families in slums/dump yards to better housing via govt/private aid, sponsors leaderboard.
 Randomly give gift cheque to poor disabled individuals, sponsors leaderboard.
 Encourage school dropouts to return via scholarships/books/uniforms & counseling, sponsors leaderboard.
 Upgrade poor village school infrastructure, sponsors leaderboard.
 Sponsor picnics & science tours for village school kids, sponsors leaderboard.
 Sponsor inter-school sports event in poor neighborhoods, sponsors leaderboard.
 Prevent farmer suicides via counseling, emergency aid, govt scheme links, sponsors leaderboard.
 Organize job fairs in poor neighborhoods, sponsors leaderboard.
 Procure and fund ambulance + driver for poor neighborhoods, sponsors leaderboard.
 Empower girls in poor neighborhoods for education & equality, sponsors leaderboard.
 Install dry/wet dustbins & regular clean-up in poor neighborhoods, sponsors leaderboard.
 Support manual handloom weavers with raw materials, tools, and market access, sponsors leaderboard."""
    
    # Split into individual lines and clean
    initiatives = []
    for line in original_text.strip().split('\n'):
        line = line.strip()
        if line and not line.startswith('#'):
            # Remove leading numbers, dots, dashes
            line = re.sub(r'^\d+[\.\)\-\s]*', '', line)
            # Remove leading bullet points
            line = re.sub(r'^[\-\*\•]\s*', '', line)
            initiatives.append(line.strip())
    
    return initiatives

def read_current_initiatives():
    """Read current initiatives from the generated file"""
    try:
        with open('/workspace/current_initiatives.txt', 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Current initiatives file not found")
        return []

def find_duplicates():
    """Find duplicates between original and current lists"""
    original = parse_original_list()
    current = read_current_initiatives()
    
    print(f"Original list: {len(original)} initiatives")
    print(f"Current catalog: {len(current)} initiatives")
    print()
    
    # Find exact and near matches
    exact_matches = []
    near_matches = []
    threshold = 0.8  # 80% similarity
    
    for i, orig in enumerate(original):
        best_match = None
        best_score = 0
        
        for j, curr in enumerate(current):
            score = similarity_score(orig, curr)
            if score > best_score:
                best_score = score
                best_match = (j, curr, score)
        
        if best_match and best_match[2] >= threshold:
            if best_match[2] >= 0.95:  # Exact match
                exact_matches.append((i, orig, best_match))
            else:  # Near match
                near_matches.append((i, orig, best_match))
    
    print("=== EXACT MATCHES (95%+ similarity) ===")
    for i, (orig_idx, orig_text, (curr_idx, curr_text, score)) in enumerate(exact_matches, 1):
        print(f"{i}. ORIGINAL: {orig_text}")
        print(f"   CURRENT:  {curr_text}")
        print(f"   SIMILARITY: {score:.2%}")
        print()
    
    print("=== NEAR MATCHES (80-95% similarity) ===")
    for i, (orig_idx, orig_text, (curr_idx, curr_text, score)) in enumerate(near_matches, 1):
        print(f"{i}. ORIGINAL: {orig_text}")
        print(f"   CURRENT:  {curr_text}")
        print(f"   SIMILARITY: {score:.2%}")
        print()
    
    total_matches = len(exact_matches) + len(near_matches)
    print(f"=== SUMMARY ===")
    print(f"Exact matches: {len(exact_matches)}")
    print(f"Near matches: {len(near_matches)}")
    print(f"Total duplicates found: {total_matches}")
    print(f"Estimated removed duplicates: {len(original) - len(current)} initiatives")
    
    return exact_matches, near_matches

if __name__ == "__main__":
    find_duplicates()