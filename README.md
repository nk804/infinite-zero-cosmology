# Corrected Python Scripts for Photon Manuscript

## Files Included

1. **auto_build_CORRECTED.py** - Main build script with all fixes
2. **fix_caps_preserve_links.py** - Converts ALL-CAPS titles to title case while preserving hyperlinks
3. **change_link_colors.py** - Changes all hyperlink colors to violet (or any color)
4. **fix_215x_position.py** - Moves 2.15X to correct position (after 2.9, before Area 3)

## Key Corrections Made

### 1. Numerical Sorting (X-suffix handling)
**Problem**: 2.15X was sorting between 2.1 and 2.2 instead of after 2.9
**Fix**: Added suffix-aware parsing that makes X-suffix sections sort AFTER their base number
- Regular: 2.9 → sort key: (2, 9, 0)
- X-suffix: 2.15X → sort key: (2, 15, 1) 
- Result: 2.9 < 2.15X < 3.0

### 2. Title Extraction
**Problem**: Reading decorative dashes (====) as chapter titles
**Fix**: Skip lines with only = or - characters, find actual title

### 3. Title Case Conversion
**Problem**: Converting to title case broke hyperlinks
**Fix**: Modified XML text nodes directly instead of replacing paragraph text

### 4. Roman Numeral Preservation
**Problem**: "Part II" became "part Ii"
**Fix**: Special handling for Roman numerals in parentheses

### 5. Hyperlink Colors
**Problem**: Mixed blue shades (0000FF and 0563C1)
**Fix**: Unified all hyperlinks to violet (8B00FF)

## Usage Examples

### Build manuscript with new chapters:
```bash
python auto_build_CORRECTED.py Photon.docx 3_10_0_ENG.txt 3_10_1_ENG.txt 3_11_ENG.txt
```

### Fix caps while preserving links:
```bash
python fix_caps_preserve_links.py
```

### Change link colors:
```bash
python change_link_colors.py
# Edit the file to change color: new_color='8B00FF'
```

### Fix 2.15X position:
```bash
python fix_215x_position.py
```

## Technical Details

### Suffix Sorting Algorithm
```python
def parse_section_number(section_str):
    """Parse section number with X-suffix awareness.
    
    Returns: (number, suffix_flag)
    - "9" → (9, 0)
    - "9X" → (9, 1)  # sorts after 9 but before 10
    - "15X" → (15, 1)  # sorts after 15 but before 16
    """
    try:
        return (int(section_str), 0)
    except ValueError:
        num_match = re.findall(r'\d+', section_str)
        if num_match:
            return (int(num_match[0]), 1)
        return (section_str, 0)
```

Sort tuples: `(area, section_num, section_suffix, subsection_num, subsection_suffix, lang)`

This ensures:
- 2.1 = (2, 1, 0, 0, 0) 
- 2.9 = (2, 9, 0, 0, 0)
- 2.15X = (2, 15, 1, 0, 0) ← sorts between 2.9 and 3.0!
- 3.0 = (3, 0, 0, 0, 0)

## All Fixes Applied

✅ Numerical sorting (3.9, 3.10, 3.11)
✅ X-suffix sorting (2.15X after 2.9)
✅ Title case (no more SHOUTING)
✅ Preserved Roman numerals (Part II)
✅ Violet hyperlinks (all same color)
✅ Working clickable links
✅ Proper title extraction (no more dashes)
✅ Correct TOC/body insertion positions

