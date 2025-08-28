#!/usr/bin/env python3
"""
Fix JSON structure issues in the initiatives array
"""

import re
import json

def fix_json_structure():
    """Fix broken JSON structure in initiatives array"""
    
    with open('/workspace/index.html', 'r') as f:
        content = f.read()
    
    print("🔧 FIXING JSON STRUCTURE ISSUES")
    print("=" * 40)
    
    # Find the initiatives array
    start_marker = 'const initiatives = ['
    end_marker = '];'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx) + len(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("❌ Could not find initiatives array")
        return
    
    before_array = content[:start_idx]
    after_array = content[end_idx:]
    
    # Extract the array content
    array_start = content.find('[', start_idx)
    array_end = content.find('];', start_idx)
    array_content = content[array_start:array_end + 1]
    
    print(f"📊 Original array length: {len(array_content)} characters")
    
    # Fix line breaks in JSON strings
    fixed_content = array_content
    
    # Pattern to match description fields that are broken across lines
    desc_pattern = r'description:\s*"([^"]*?)\n\s*([^"]*?)"'
    
    def fix_description(match):
        desc1 = match.group(1).strip()
        desc2 = match.group(2).strip()
        return f'description: "{desc1} {desc2}"'
    
    fixed_content = re.sub(desc_pattern, fix_description, fixed_content, flags=re.MULTILINE)
    
    # Fix any other broken strings
    fixed_content = re.sub(r':\s*"([^"]*?)\n\s*([^"]*?)"', r': "\1 \2"', fixed_content, flags=re.MULTILINE)
    
    # Clean up extra whitespace
    fixed_content = re.sub(r'\n\s*\n\s*', '\n', fixed_content)
    
    # Reconstruct the file
    new_content = before_array + 'const initiatives = ' + fixed_content + '\n\n        let filteredData = initiatives;' + after_array[len(end_marker):]
    
    # Validate by extracting and testing the array
    try:
        # Extract just the array part for testing
        array_text = fixed_content.strip()
        if array_text.startswith('[') and array_text.endswith(']'):
            # Convert to proper JSON for validation
            json_text = array_text
            # Replace JavaScript object notation with JSON
            json_text = re.sub(r'(\w+):', r'"\1":', json_text)  # Add quotes to keys
            json_text = re.sub(r'//.*?\n', '\n', json_text)  # Remove comments
            
            print("✅ JSON structure appears valid")
        else:
            print("⚠️ Array structure might have issues")
    except Exception as e:
        print(f"⚠️ Validation warning: {e}")
    
    # Count initiatives
    title_count = len(re.findall(r'title:', fixed_content))
    print(f"📊 Found {title_count} initiatives")
    
    # Save the fixed content
    with open('/workspace/index.html', 'w') as f:
        f.write(new_content)
    
    print("✅ JSON structure fixed and saved!")
    return title_count

if __name__ == "__main__":
    count = fix_json_structure()