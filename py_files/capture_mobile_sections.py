import urllib.request, json, time, websocket, base64, subprocess, os

port = 9777
temp_dir = r"C:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi\.cdp_sections"
out_dir = r"c:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi"

cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    f"--remote-debugging-port={port}",
    "--remote-allow-origins=*",
    f"--user-data-dir={temp_dir}",
    "--no-first-run",
    "--disable-gpu",
    "http://localhost:8888"
]
proc = subprocess.Popen(cmd)
time.sleep(2)
try:
    with urllib.request.urlopen(f"http://localhost:{port}/json") as r:
        tabs = json.loads(r.read())
        page_tab = next(t for t in tabs if "localhost:8888" in t.get("url", ""))

    ws = websocket.create_connection(page_tab["webSocketDebuggerUrl"])
    def send(method, params=None):
        msg = {"id": 1, "method": method, "params": params or {}}
        ws.send(json.dumps(msg))
        while True:
            res = json.loads(ws.recv())
            if res.get("id") == 1:
                return res.get("result", {})

    send("Page.enable")
    send("Emulation.setDeviceMetricsOverride", {"width": 375, "height": 812, "deviceScaleFactor": 1, "mobile": True})
    send("Page.reload", {"ignoreCache": True})
    time.sleep(1.5)

    targets = [
        ("mobile_shot_worker.png", "document.getElementById('worker').scrollIntoView();"),
        ("mobile_shot_consent.png", "document.getElementById('consent').scrollIntoView();"),
        ("mobile_shot_map.png", "document.getElementById('intelligence').scrollIntoView();"),
        ("mobile_shot_forecast.png", "document.getElementById('forecast').scrollIntoView();"),
        ("mobile_shot_authority.png", "document.getElementById('authority').scrollIntoView();"),
        ("mobile_shot_whatif.png", "document.getElementById('whatIfScenarioCard').scrollIntoView();"),
        ("mobile_shot_footer.png", "document.querySelector('.master-footer').scrollIntoView();")
    ]

    for fname, scroll_code in targets:
        send("Runtime.evaluate", {"expression": scroll_code})
        time.sleep(0.5)
        shot = send("Page.captureScreenshot", {"format": "png"})
        img_data = base64.b64decode(shot["data"])
        fpath = os.path.join(out_dir, fname)
        with open(fpath, "wb") as f:
            f.write(img_data)
        print(f"Captured {fname}: {len(img_data)} bytes")

    ws.close()
finally:
    proc.terminate()
