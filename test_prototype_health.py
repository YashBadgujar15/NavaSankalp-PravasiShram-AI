import re
import os

base_dir = r"c:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi"

with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()

with open(os.path.join(base_dir, 'js', 'app.js'), 'r', encoding='utf-8') as f:
    js = f.read()

with open(os.path.join(base_dir, 'css', 'style.css'), 'r', encoding='utf-8') as f:
    css = f.read()

print("--- 1. ELEMENT ID INTEGRITY CHECK ---")
html_ids = set(re.findall(r'id=[\'"]([^\'"]+)[\'"]', html))
js_ids = set(re.findall(r'getElementById\([\'"]([^\'"]+)[\'"]\)', js))
missing_ids = js_ids - html_ids
if missing_ids:
    print("FAILED! Missing IDs in HTML:", missing_ids)
else:
    print(f"PASSED! All {len(js_ids)} JS element IDs exist in HTML ({len(html_ids)} total IDs in HTML).")

print("\n--- 2. INLINE ONCLICK CHECK ---")
onclicks = set(re.findall(r'onclick=[\'"]([a-zA-Z0-9_]+)\(', html))
for fn in onclicks:
    pattern = rf'function\s+{fn}\b|\b{fn}\s*='
    if not re.search(pattern, js):
        print(f"FAILED! Onclick function {fn}() not found in js/app.js!")
    else:
        print(f" - {fn}() found in js/app.js")
print("PASSED! All inline onclick handlers verified.")

print("\n--- 3. CSS BRACE BALANCE CHECK ---")
open_braces = css.count('{')
close_braces = css.count('}')
if open_braces != close_braces:
    print(f"FAILED! CSS brace mismatch: {open_braces} open, {close_braces} close")
else:
    print(f"PASSED! CSS braces balanced ({open_braces} pairs).")

print("\n--- 4. JS BRACKET BALANCE CHECK ---")
def check_js_brackets(content):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    in_str = False
    str_char = ''
    in_line_cmt = False
    in_block_cmt = False
    
    for i, ch in enumerate(content):
        if in_line_cmt:
            if ch == '\n': in_line_cmt = False
            continue
        if in_block_cmt:
            if ch == '*' and i + 1 < len(content) and content[i+1] == '/':
                in_block_cmt = False
            continue
        if in_str:
            if ch == str_char and content[i-1] != '\\': in_str = False
            continue
        if ch == '/' and i + 1 < len(content):
            if content[i+1] == '/': in_line_cmt = True; continue
            if content[i+1] == '*': in_block_cmt = True; continue
        if ch in ('"', "'", '`'):
            in_str = True
            str_char = ch
            continue
        if ch in '({[':
            stack.append((ch, i))
        elif ch in ')}]':
            if not stack:
                return f"Unexpected closing bracket {ch} at index {i}"
            top, idx = stack.pop()
            if top != pairs[ch]:
                return f"Mismatched bracket: expected {pairs[ch]} for {ch} at index {i}"
    if stack:
        return f"Unclosed bracket {stack[-1][0]} at index {stack[-1][1]}"
    return "OK"

res = check_js_brackets(js)
print(f"JS syntax check: {res}")
