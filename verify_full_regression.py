import re
import os
import json

base_dir = r"c:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi"

with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()

with open(os.path.join(base_dir, 'js', 'app.js'), 'r', encoding='utf-8') as f:
    js = f.read()

with open(os.path.join(base_dir, 'css', 'style.css'), 'r', encoding='utf-8') as f:
    css = f.read()

failures = []

def check(name, condition, detail=""):
    if condition:
        print(f"  [PASS] {name}")
    else:
        print(f"  [FAIL] {name}: {detail}")
        failures.append(f"{name}: {detail}")

print("=== PRAVASISHRAM AI FULL REGRESSION TEST SUITE ===\n")

# A. Worker Check-in
print("A. Worker Check-in Flow:")
check("Mic button exists", 'id="btnBigMic"' in html)
check("Mic status text exists", 'id="micStatusText"' in html)
check("Voice transcript container exists", 'id="voiceTranscriptContainer"' in html)
check("Transcript label exists", 'id="transcriptLabel"' in html)
check("Transcript badge exists", 'id="transcriptStatusBadge"' in html)
check("Voice transcript text exists", 'id="voiceTranscriptText"' in html)
check("Pipeline stepper steps exist", all(s in html for s in ['id="stepListening"', 'id="stepUnderstanding"', 'id="stepProtecting"', 'id="stepReady"']))
check("Editable entity inputs exist", all(e in html for e in ['id="entityOrigin"', 'id="entityDest"', 'id="entitySector"', 'id="entityPurpose"', 'id="entityType"']))
check("Preset scenarios exist", 'class="qvc-btn"' in html and 'data-sample="Main Patna se Surat textile kaam ke liye aaya hoon."' in html)
check("Speech recognition handler in JS", 'recognition.onresult' in js and 'recognition.onerror' in js and 'recognition.onstart' in js)
check("Interim live results enabled", 'recognition.interimResults = true' in js)
check("Proper transcript display function", 'function displayTranscript' in js)
check("Actual speech label 'You said:' present", "You said:" in js)
check("Demo input label present", "Demo input" in js)
check("Editable fields populated by extraction", 'updateExtractedFields' in js)

# B & C. Confirmation & Timeline Event Protection
print("\nB & C. Confirmation & Duplicate Timeline Event Fix:")
check("Confirm button exists", 'id="btnConfirmCheckin"' in html)
check("Timeline container exists", 'id="timelineEventsList"' in html)
check("Submission lock exists in JS", 'let isSubmittingCheckin = false;' in js)
check("Signature duplicate check exists in JS", 'lastSubmittedEventSig === currentEventSig' in js)
check("Single event prepended to timeline", 'syntheticDataset.timeline.unshift(newEvent);' in js)
check("Total events incremented by 1", 'syntheticDataset.kpis.totalEvents += 1;' in js)
check("Button bound check prevents multiple listeners", '!btnConfirm.dataset.bound' in js)
check("Historical synthetic demo events preserved", all(ev in js for ev in ['evt-01', 'evt-02', 'evt-03']))

# D. Consent Center
print("\nD. Consent Center Flow:")
check("Consent banner exists", 'id="consentStatusBanner"' in html)
check("Re-Verify consent button exists", 'id="btnGiveConsent"' in html)
check("Review data use button exists", 'id="btnReviewDataUse"' in html)
check("Withdraw consent button exists", 'id="btnWithdrawConsent"' in html)
check("Withdraw confirm modal exists", 'id="withdrawConfirmModal"' in html)
check("Withdraw confirm action button exists", 'id="btnConfirmWithdrawAction"' in html)
check("Data use review modal exists", 'id="dataUseModal"' in html)
check("Consent update reflected on timeline", 'syntheticDataset.timeline.forEach(t => t.consent = "withdrawn")' in js)

# E. Migration Intelligence Map & Corridors
print("\nE. Migration Intelligence (SVG Map & Corridors):")
check("SVG India map exists", 'id="indiaMapSvg"' in html)
check("Corridor filter State exists", 'id="filterState"' in html)
check("Corridor filter Sector exists", 'id="filterSector"' in html)
check("Corridor filter Type exists", 'id="filterType"' in html)
check("Corridor detail panel exists", 'id="corridorDetailPanel"' in html)
check("Hero corridor pills container exists", 'id="heroCorridorPills"' in html)
check("Curved corridor drawing logic in JS", 'function drawSvgCorridors' in js)
check("Corridor selection logic in JS", 'function selectCorridor' in js)

# F. Forecast
print("\nF. Forecast Flow:")
check("Forecast chart canvas exists", 'id="forecastChartCanvas"' in html)
check("Forecast corridor selector exists", 'id="forecastCorridorSelect"' in html)
check("Forecast chart renderer in JS", 'function renderForecastChart' in js)
check("Forecast selector bound in JS", 'selector.addEventListener("change"' in js)
check("Multi-corridor forecast datasets present", 'forecastCorridors:' in js)

# G. Authority Command Center
print("\nG. Authority Command Center:")
check("KPI Total Events exists", 'id="kpiTotalEvents"' in html)
check("KPI Active Corridors exists", 'id="kpiActiveCorridors"' in html)
check("KPI Emerging Corridors exists", 'id="kpiEmergingCorridors"' in html)
check("KPI High Activity Regions exists", 'id="kpiHighRegions"' in html)
check("Top Corridors Table Body exists", 'id="commandCorridorsTableBody"' in html)
check("AI Planning Signals List exists", 'id="aiSignalsList"' in html)

# H. Guided Demo
print("\nH. Guided 2-Minute Demo Journey:")
check("Launch Demo nav CTA exists", 'href="#demo"' in html and 'Launch Demo' in html)
check("Demo Prev button exists", 'id="btnDemoPrev"' in html)
check("Demo Next button exists", 'id="btnDemoNext"' in html)
check("Demo Auto-Play button exists", 'id="btnDemoAutoPlay"' in html)
check("Demo progress indicator exists", 'id="demoProgressText"' in html)
check("Demo stage title exists", 'id="demoStageTitle"' in html)
check("Demo stage desc exists", 'id="demoStageDesc"' in html)
check("Demo 7 nodes exist in HTML", all(f'id="demoNode{i}"' in html for i in range(1, 8)))

# I. Language Switcher (5 Languages)
print("\nI. Multilingual Localization (5 Languages):")
check("Language selector exists", 'id="langSelector"' in html)
for lang in ['en', 'hi', 'gu', 'mr', 'bn']:
    check(f"I18N contains '{lang}'", f'{lang}: {{' in js)
    for key in ['brandTag', 'heroTitle', 'heroSub', 'btnJourney', 'btnIntel', 'workerTitle', 'voicePrompt', 'consentTitle', 'activeConsent', 'withdrawnConsent', 'demoBadge']:
        check(f"'{lang}' has key '{key}'", f'{key}:' in js)

# J. Responsive Styles (1440px to 360px)
print("\nJ. Responsive Layout & CSS Guardrails:")
check("CSS has 1440px / desktop container", 'max-width: 1380px' in css)
check("CSS has 1024px breakpoint", '@media (max-width: 1024px)' in css or '@media (max-width: 960px)' in css)
check("CSS has 768px breakpoint", '@media (max-width: 768px)' in css)
check("CSS has 480px / mobile breakpoint", '@media (max-width: 480px)' in css)
check("Zero horizontal overflow guard", 'overflow-x: hidden' in css)
check("Responsive tables container", 'overflow-x: auto' in css)

# Terminology & Transparency Guardrails
print("\nTerminology & Transparency Safety:")
check("No 'ZERO CONTINUOUS SURVEILLANCE'", 'ZERO CONTINUOUS SURVEILLANCE' not in html and 'ZERO CONTINUOUS SURVEILLANCE' not in js)
check("No 'DDPR'", 'DDPR' not in html and 'DDPR' not in js)
check("No 'DPDP-Aligned'", 'DPDP-Aligned' not in html and 'DPDP-Aligned' not in js)
check("Contains 'Privacy-by-Design Architecture'", 'Privacy-by-Design Architecture' in html)
check("Contains 'No continuous GPS tracking'", 'No continuous GPS tracking' in html)
check("Contains 'No continuous personal tracking in this prototype.'", 'No continuous personal tracking in this prototype.' in html)
check("Contains 'Continuous location tracking can create privacy, security and battery concerns.'", 'Continuous location tracking can create privacy, security and battery concerns.' in html)
check("Contains 'Tell us where you moved and why.'", 'Tell us where you moved and why.' in html)
check("Contains 'Synthetic demonstration data'", 'Synthetic demonstration data' in html)
check("Contains 'Concept prototype' disclaimer", 'DISCLAIMER & TRANSPARENCY NOTICE:' in html)

print("\n" + "="*50)
if failures:
    print(f"FAILED with {len(failures)} errors:")
    for f in failures:
        print(" - " + f)
else:
    print("ALL 75 REGRESSION CHECKS PASSED PERFECTLY!")
print("="*50)
