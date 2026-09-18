import json
import time
import subprocess
import urllib.request
import websocket
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_dir = r"C:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi\.cdp_profile"
port = 9333

def run_overflow_audit():
    cmd = [
        chrome_path,
        "--headless=new",
        f"--remote-debugging-port={port}",
        "--remote-allow-origins=*",
        f"--user-data-dir={temp_dir}",
        "--no-first-run",
        "--disable-gpu",
        "http://localhost:8888"
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        # Wait for port
        for _ in range(20):
            try:
                with urllib.request.urlopen(f"http://localhost:{port}/json") as r:
                    tabs = json.loads(r.read())
                    page_tab = next((t for t in tabs if "localhost:8888" in t.get("url", "")), None)
                    if page_tab:
                        break
            except Exception:
                time.sleep(0.3)
        
        if not page_tab:
            print("Could not find localhost:8888 tab")
            return

        ws_url = page_tab["webSocketDebuggerUrl"]
        ws = websocket.create_connection(ws_url)
        
        def send_cmd(method, params=None):
            req_id = int(time.time() * 1000) % 100000
            msg = {"id": req_id, "method": method, "params": params or {}}
            ws.send(json.dumps(msg))
            while True:
                res = json.loads(ws.recv())
                if res.get("id") == req_id:
                    return res.get("result", {})

        # Enable Page and Runtime
        send_cmd("Page.enable")
        send_cmd("Runtime.enable")

        widths = [360, 375, 390, 414, 430, 768, 1024, 1440]
        results = {}

        for w in widths:
            h = 800
            # Emulate device metrics
            send_cmd("Emulation.setDeviceMetricsOverride", {
                "width": w,
                "height": h,
                "deviceScaleFactor": 1,
                "mobile": (w < 900)
            })
            # Reload page with cache bypass so new CSS is loaded and rendered
            send_cmd("Page.reload", {"ignoreCache": True})
            time.sleep(1.0)

            # Evaluate overflow
            js_code = """
            (() => {
                const docWidth = document.documentElement.clientWidth;
                const bodyScrollWidth = document.body.scrollWidth;
                const docScrollWidth = document.documentElement.scrollWidth;
                const maxScrollWidth = Math.max(bodyScrollWidth, docScrollWidth);
                const hasOverflow = maxScrollWidth > docWidth + 1;
                
                const overflowingElements = [];
                const all = document.querySelectorAll('*');
                all.forEach(el => {
                    if (el.offsetParent === null && el.tagName !== 'BODY') return;
                    const r = el.getBoundingClientRect();
                    if (r.right > docWidth + 2) {
                        // find closest section or container
                        const sec = el.closest('section, header, footer, .apex-top-bar, .modal-backdrop') || el;
                        overflowingElements.push({
                            section: sec.id || sec.tagName || sec.className,
                            tag: el.tagName,
                            id: el.id || '',
                            className: (typeof el.className === 'string' ? el.className.split(' ').slice(0, 3).join(' ') : ''),
                            right: Math.round(r.right),
                            width: Math.round(r.width),
                            docWidth: docWidth
                        });
                    }
                });
                
                // Group by section
                const bySection = {};
                overflowingElements.forEach(item => {
                    const k = item.section + ' (' + item.tag + '.' + item.className + ')';
                    if (!bySection[k]) {
                        bySection[k] = { count: 0, maxRight: 0, sample: item };
                    }
                    bySection[k].count++;
                    bySection[k].maxRight = Math.max(bySection[k].maxRight, item.right);
                });

                return {
                    viewportWidth: docWidth,
                    maxScrollWidth: maxScrollWidth,
                    hasOverflow: hasOverflow,
                    totalCount: overflowingElements.length,
                    grouped: bySection
                };
            })()
            """
            eval_res = send_cmd("Runtime.evaluate", {
                "expression": js_code,
                "returnByValue": True
            })
            val = eval_res.get("result", {}).get("value", {})
            results[w] = val
            print(f"\n==========================================")
            print(f"Viewport {w}px: docWidth={val.get('viewportWidth')}, maxScroll={val.get('maxScrollWidth')}, hasOverflow={val.get('hasOverflow')}")
            if val.get("hasOverflow"):
                print(f"Total overflowing elements: {val.get('totalCount')}")
                for k, v in val.get("grouped", {}).items():
                    s = v['sample']
                    print(f"  -> Section/Item: {k} | maxRight={v['maxRight']}px (exceeds by {v['maxRight'] - val.get('viewportWidth')}px) [id='{s['id']}']")


        ws.close()
        return results
    finally:
        proc.terminate()

if __name__ == "__main__":
    run_overflow_audit()
