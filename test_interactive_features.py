import json
import time
import subprocess
import urllib.request
import websocket
import sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_dir = r"C:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi\.cdp_test_profile"
port = 9444

def test_features():
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
        time.sleep(2)
        with urllib.request.urlopen(f"http://localhost:{port}/json") as r:
            tabs = json.loads(r.read())
            page_tab = next(t for t in tabs if "localhost:8888" in t.get("url", ""))

        ws = websocket.create_connection(page_tab["webSocketDebuggerUrl"])

        def send_cmd(method, params=None):
            req_id = int(time.time() * 1000) % 100000
            msg = {"id": req_id, "method": method, "params": params or {}}
            ws.send(json.dumps(msg))
            while True:
                res = json.loads(ws.recv())
                if res.get("id") == req_id:
                    return res.get("result", {})

        send_cmd("Page.enable")
        send_cmd("Runtime.enable")
        # Set to mobile width 375px
        send_cmd("Emulation.setDeviceMetricsOverride", {
            "width": 375,
            "height": 812,
            "deviceScaleFactor": 1,
            "mobile": True
        })
        send_cmd("Page.reload", {"ignoreCache": True})
        time.sleep(1.5)

        def eval_js(js_code):
            res = send_cmd("Runtime.evaluate", {"expression": js_code, "returnByValue": True})
            return res.get("result", {}).get("value")

        print("=== TESTING INTERACTIVE FEATURES ON 375px MOBILE ===")

        # 1. Mobile Menu Toggle
        menu_test = eval_js("""
        (() => {
            const btn = document.getElementById('btnMobileMenu');
            const menu = document.getElementById('navMenu');
            btn.click();
            const isOpenAfterClick = menu.classList.contains('open');
            btn.click();
            const isClosedAfterSecondClick = !menu.classList.contains('open');
            return { isOpenAfterClick, isClosedAfterSecondClick };
        })()
        """)
        print("1. Mobile Menu Toggle:", menu_test)

        # 2. Language Switcher
        lang_test = eval_js("""
        (() => {
            const sel = document.getElementById('langSelector');
            sel.value = 'hi';
            sel.dispatchEvent(new Event('change'));
            const brandTag = document.getElementById('i18n-brand-tag').textContent;
            sel.value = 'en';
            sel.dispatchEvent(new Event('change'));
            return { hindiTag: brandTag, restored: document.getElementById('i18n-brand-tag').textContent };
        })()
        """)
        print("2. Language Switcher:", lang_test)

        # 3. Accessibility Controls (Contrast & Low Data)
        a11y_test = eval_js("""
        (() => {
            const cBtn = document.getElementById('btnToggleContrast');
            const dBtn = document.getElementById('btnToggleLowData');
            cBtn.click();
            const hasContrast = document.body.classList.contains('high-contrast');
            cBtn.click();
            dBtn.click();
            const hasLowData = document.body.classList.contains('low-data');
            dBtn.click();
            return { hasContrast, hasLowData };
        })()
        """)
        print("3. Accessibility Controls:", a11y_test)

        # 4. Quick Voice Scenario Click & Entity Extraction
        eval_js("""
        (() => {
            const presetBtn = document.querySelector('.qvc-btn');
            if (presetBtn) presetBtn.click();
        })()
        """)
        time.sleep(1.8) # Allow stepper animation & extraction to finish

        voice_test = eval_js("""
        (() => {
            return {
                origin: document.getElementById('entityOrigin').value,
                dest: document.getElementById('entityDest').value,
                sector: document.getElementById('entitySector').value,
                transcript: document.getElementById('voiceTranscriptText').textContent
            };
        })()
        """)
        print("4. Quick Voice Check-in & Extraction:", voice_test)

        # 5. Confirm Check-in & Timeline Event Prepend
        timeline_test = eval_js("""
        (() => {
            const initialCount = document.querySelectorAll('.timeline-event-card').length;
            const btn = document.getElementById('btnConfirmCheckin');
            btn.click();
            const newCount = document.querySelectorAll('.timeline-event-card').length;
            return { initialCount, newCount, added: newCount > initialCount };
        })()
        """)
        print("5. Timeline Submission:", timeline_test)

        # 6. What-if Scenario Simulator
        whatif_test = eval_js("""
        (() => {
            const slider = document.getElementById('whatIfVolumeSlider');
            slider.value = 35000;
            slider.dispatchEvent(new Event('input'));
            return {
                volume: document.getElementById('whatIfVolumeBadge').textContent,
                surge: document.getElementById('whatIfSurgePercent').textContent,
                activity: document.getElementById('whatIfCorridorActivity').textContent,
                pressure: document.getElementById('whatIfPlanningPressure').textContent
            };
        })()
        """)
        print("6. What-if Simulator:", whatif_test)

        # 7. Corridor Selection & Drawer
        corridor_test = eval_js("""
        (() => {
            // Select first corridor pill in hero or map
            const pill = document.querySelector('.corridor-pill') || document.querySelector('.qvc-btn');
            if (typeof selectCorridor === 'function') {
                selectCorridor('bihar-gujarat');
            }
            return {
                corridorTitle: document.getElementById('drawerCorridorTitle')?.textContent,
                corridorVol: document.getElementById('drawerCorridorVolume')?.textContent
            };
        })()
        """)
        print("7. Corridor Selection:", corridor_test)

        # 8. Forecast Selector
        forecast_test = eval_js("""
        (() => {
            const sel = document.getElementById('forecastCorridorSelect');
            sel.value = 'bihar-gujarat';
            sel.dispatchEvent(new Event('change'));
            return { activeVal: sel.value };
        })()
        """)
        print("8. Forecast Selector:", forecast_test)

        # 9. Guided Demo Journey Step
        demo_test = eval_js("""
        (() => {
            const nextBtn = document.getElementById('btnDemoNext');
            nextBtn.click();
            return {
                stepText: document.getElementById('demoProgressText').textContent,
                title: document.getElementById('demoStageTitle').textContent
            };
        })()
        """)
        print("9. Guided Demo Journey Step:", demo_test)

        ws.close()
    finally:
        proc.terminate()

if __name__ == "__main__":
    test_features()
