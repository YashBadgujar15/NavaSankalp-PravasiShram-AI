import re
import os
import subprocess

base_dir = r"c:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi"
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    full_html = f.read()

head_m = re.search(r"(<head>.*?</head>)", full_html, re.DOTALL | re.IGNORECASE)
head = head_m.group(1) if head_m else ""

start_idx = full_html.find('id="whatIfScenarioCard"')
start_tag = full_html.rfind("<div", 0, start_idx)
end_tag = full_html.find("</section>", start_tag)
whatif_html = full_html[start_tag:end_tag]

page = f"""<!DOCTYPE html>
<html lang="en">
{head}
<body style="background:#060A18; padding:1.5rem; margin:0;">
  <div class="content-container" style="max-width:1200px; margin:0 auto;">
    {whatif_html}
  </div>
  <script src="js/app.js"></script>
</body>
</html>"""

html_path = os.path.join(base_dir, "snap_whatif.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(page)

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_dir = os.path.expandvars(r"%TEMP%\chrome_snap_whatif")
out_png = os.path.join(base_dir, "snap_whatif.png")

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={temp_dir}",
    f"--screenshot={out_png}",
    "--window-size=1280,680",
    "http://localhost:8888/snap_whatif.html"
]
subprocess.run(cmd, capture_output=True, timeout=15)
print("snap_whatif.png created:", os.path.exists(out_png), "size:", os.path.getsize(out_png) if os.path.exists(out_png) else 0)
