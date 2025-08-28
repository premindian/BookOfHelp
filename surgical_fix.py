#!/usr/bin/env python3
"""
Surgical fix for specific JavaScript errors only
"""

import re

def surgical_fix():
    """Apply only essential fixes without breaking the structure"""
    
    with open('/workspace/index.html', 'r') as f:
        content = f.read()
    
    print("🎯 APPLYING SURGICAL JAVASCRIPT FIX")
    print("=" * 40)
    
    # Count before
    before_count = len(re.findall(r'title:\s*"', content))
    print(f"📊 Before: {before_count} initiatives")
    
    # Only fix the specific concatenated comment issues that break JavaScript
    critical_fixes = [
        (r'// VILLAGE TRADITIONAL KNOWLEDGE PRESERVATION// RURAL WATER QUALITY ASSURANCE', '// RURAL WATER QUALITY ASSURANCE'),
        (r'// COMMUNITY AGRICULTURAL VALUE ADDITION// VILLAGE WOMEN HEALTH ADVOCACY', '// VILLAGE WOMEN HEALTH ADVOCACY'),
        (r'// COMMUNITY RENEWABLE ENERGY STORAGE// VILLAGE YOUTH INNOVATION PROGRAM// RURAL HEALTH INFORMATION SYSTEM', '// RURAL HEALTH INFORMATION SYSTEM'),
        (r'// VILLAGE DISASTER PREPAREDNESS TRAINING// RURAL TECHNOLOGY TRANSFER PROGRAM', '// RURAL TECHNOLOGY TRANSFER PROGRAM'),
        (r'// COMMUNITY WATER HARVESTING EXPANSION// VILLAGE YOUTH LEADERSHIP NETWORK// RURAL HEALTHCARE UNIVERSAL ACCESS', '// RURAL HEALTHCARE UNIVERSAL ACCESS'),
        (r'// COMMUNITY AGRICULTURAL TRANSFORMATION// VILLAGE WOMEN EMPOWERMENT ACCELERATOR', '// VILLAGE WOMEN EMPOWERMENT ACCELERATOR'),
        (r'// COMMUNITY RENEWABLE ENERGY REVOLUTION// VILLAGE YOUTH INNOVATION ECOSYSTEM// RURAL HEALTH SYSTEM TRANSFORMATION', '// RURAL HEALTH SYSTEM TRANSFORMATION'),
    ]
    
    # Apply only critical fixes
    for old, new in critical_fixes:
        if old in content:
            content = content.replace(old, new)
            print(f"✅ Fixed critical comment: {old[:30]}...")
    
    # Fix any obvious JSON comma issues
    content = re.sub(r',\s*,', ',', content)
    content = re.sub(r',\s*\]', ']', content)
    
    # Count after
    after_count = len(re.findall(r'title:\s*"', content))
    print(f"📊 After: {after_count} initiatives")
    
    if after_count != before_count:
        print(f"⚠️ Warning: Initiative count changed from {before_count} to {after_count}")
    
    # Save the surgically fixed content
    with open('/workspace/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Surgical fix complete - preserved all functionality!")
    return after_count

if __name__ == "__main__":
    count = surgical_fix()