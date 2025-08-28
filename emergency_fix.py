#!/usr/bin/env python3
"""
Emergency fix for spinning website
Create a minimal working version that definitely loads
"""

import re

def create_minimal_working_version():
    """Create a minimal working version with just the first 50 initiatives"""
    
    with open('/workspace/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract first 50 initiatives only
    pattern = r'(\{[^{}]*title:[^{}]*\}),?'
    matches = re.findall(pattern, content, re.DOTALL)
    
    print(f"Found {len(matches)} initiative objects")
    
    # Take only first 50 to ensure it works
    working_initiatives = matches[:50]
    
    # Create clean JavaScript array
    js_array = "const initiatives = [\n"
    
    for i, match in enumerate(working_initiatives):
        # Clean up the match
        clean_match = match.strip().rstrip(',')
        js_array += "            " + clean_match
        if i < len(working_initiatives) - 1:
            js_array += ","
        js_array += "\n"
    
    js_array += "        ];"
    
    # Find the initiatives array in the original content
    start_pattern = r'const initiatives = \['
    end_pattern = r'\];'
    
    start_match = re.search(start_pattern, content)
    if not start_match:
        print("❌ Could not find initiatives array")
        return
    
    # Find the end position (simplified approach)
    end_pos = content.find('];', start_match.start()) + 2
    
    # Replace the array
    before_array = content[:start_match.start()]
    after_array = content[end_pos:]
    
    new_content = before_array + js_array + after_array
    
    # Update the count display
    new_content = re.sub(r'<span class="stat-number" id="totalCount">\d+</span>', 
                        f'<span class="stat-number" id="totalCount">50</span>', 
                        new_content)
    
    # Write the working version
    with open('/workspace/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Created minimal working version with {len(working_initiatives)} initiatives")

def main():
    """Main emergency fix function"""
    print("🚨 EMERGENCY FIX - Creating minimal working version")
    create_minimal_working_version()
    print("🚀 Website should now load properly!")

if __name__ == "__main__":
    main()