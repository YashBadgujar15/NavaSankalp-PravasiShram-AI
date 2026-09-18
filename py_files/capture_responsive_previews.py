import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_dir = r"c:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi"

viewports = [
    (360, 800, "resp_360.png"),
    (375, 812, "resp_375.png"),
    (390, 844, "resp_390.png"),
    (414, 896, "resp_414.png"),
    (430, 932, "resp_430.png"),
    (768, 1024, "resp_768.png"),
    (1024, 800, "resp_1024.png"),
    (1440, 900, "resp_1440.png")
]

for w, h, fname in viewports:
    fpath = os.path.join(out_dir, fname)
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        f"--user-data-dir={out_dir}\\.cache_bypass",
        f"--window-size={w},{h}",
        f"--screenshot={fpath}",
        "http://localhost:8888"
    ]
    res = subprocess.run(cmd, capture_output=True)
    size = os.path.getsize(fpath) if os.path.exists(fpath) else 0
    print(f"Captured {fname} ({w}x{h}): {size} bytes")
