import re
import os
import subprocess
import time

base_dir = r"c:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi"

with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    full_html = f.read()

# Extract head
head_match = re.search(r'(<head>.*?</head>)', full_html, re.DOTALL | re.IGNORECASE)
head_content = head_match.group(1) if head_match else ""

# Sections to capture
sections = [
    ('snap_worker', r'(<section id="worker".*?</section>)', 1280, 820),
    ('snap_consent', r'(<section id="consent".*?</section>)', 1280, 800),
    ('snap_intelligence', r'(<section id="intelligence".*?</section>)', 1280, 850),
    ('snap_forecast', r'(<section id="forecast".*?</section>)', 1280, 800),
    ('snap_authority', r'(<section id="authority".*?</section>)', 1280, 850),
]

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
temp_dir = os.path.expandvars(r'%TEMP%\chrome_snap_pages')
os.makedirs(temp_dir, exist_ok=True)

for name, pattern, w, h in sections:
    match = re.search(pattern, full_html, re.DOTALL | re.IGNORECASE)
    if match:
        sec_html = match.group(1)
        page_html = f"""<!DOCTYPE html>
<html lang="en">
{head_content}
<body style="background: #060A18; margin: 0; padding: 1.5rem 0;">
  {sec_html}
  <script src="js/app.js"></script>
</body>
</html>"""
        html_file = os.path.join(base_dir, f"{name}.html")
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(page_html)
        print(f"Wrote {name}.html")
        
        # Now take screenshot with Chrome headless
        png_file = os.path.join(base_dir, f"{name}.png")
        cmd = [
            chrome,
            '--headless=new',
            '--disable-gpu',
            '--no-sandbox',
            f'--user-data-dir={temp_dir}_{name}',
            f'--screenshot={png_file}',
            f'--window-size={w},{h}',
            f'http://localhost:8888/{name}.html'
        ]
        subprocess.run(cmd, capture_output=True, timeout=20)
        print(f"{name}.png created: {os.path.exists(png_file)}, size: {os.path.getsize(png_file) if os.path.exists(png_file) else 0}")
print("Snapshot generation finished!")
