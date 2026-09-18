import re
import os

base_dir = r"c:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi"

with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()

with open(os.path.join(base_dir, 'js', 'app.js'), 'r', encoding='utf-8') as f:
    js = f.read()

with open(os.path.join(base_dir, 'css', 'style.css'), 'r', encoding='utf-8') as f:
    css = f.read()

errors = []

def test(desc, cond, detail=""):
    if cond:
        print(f"  [PASS] {desc}")
    else:
        print(f"  [FAIL] {desc}: {detail}")
        errors.append(f"{desc}: {detail}")

print("=== VERIFY WHAT-IF MIGRATION SCENARIO FEATURE ===\n")

# 1. UI Structure & Elements
print("1. UI Structure & Required Elements:")
test("What-if Scenario Card exists", 'id="whatIfScenarioCard"' in html)
test("Title 'What-if Migration Scenario' exists", "What-if Migration Scenario" in html)
test("Subtitle 'Simulate a sudden increase in migration volume for planning purposes.' exists",
     "Simulate a sudden increase in migration volume for planning purposes." in html)
test("Volume slider exists with id 'whatIfVolumeSlider'", 'id="whatIfVolumeSlider"' in html)
test("Slider min is 5000", 'min="5000"' in html)
test("Slider max is 50000", 'max="50000"' in html)
test("Volume badge element exists", 'id="whatIfVolumeBadge"' in html)
test("Surge percent element exists", 'id="whatIfSurgePercent"' in html)

# 2. Four Required Indicators
print("\n2. Four Required Indicators:")
test("Indicator 1: Estimated Corridor Activity", 'id="whatIfCorridorActivity"' in html and 'id="whatIfCorridorBadge"' in html)
test("Indicator 2: Planning Pressure", 'id="whatIfPlanningPressure"' in html and 'id="whatIfPressureBadge"' in html)
test("Indicator 3: Service Capacity Response", 'id="whatIfServiceCapacity"' in html and 'id="whatIfCapacityBadge"' in html)
test("Indicator 4: Emerging Corridor Signal", 'id="whatIfEmergingSignal"' in html and 'id="whatIfSignalBadge"' in html)

# 3. Recommendation Planning Message
print("\n3. Recommendation Planning Message:")
test("Recommendation container/text element exists", 'id="whatIfRecommendationText"' in html)
test("Planning Recommendation label exists", "Planning Recommendation" in html)

# 4. Required Transparency Wording
print("\n4. Required Transparency Wording:")
test("Contains 'Prototype Simulation'", "Prototype Simulation" in html or "PROTOTYPE SIMULATION" in html)
test("Contains 'Synthetic Demonstration Data'", "Synthetic Demonstration Data" in html or "SYNTHETIC DEMONSTRATION DATA" in html)
test("Contains 'Planning scenario — not a live government forecast'", "Planning scenario — not a live government forecast" in html)

# 5. JavaScript Implementation & Safeguards
print("\n5. JavaScript Implementation & Safeguards:")
test("Function initWhatIfScenario exists in JS", "function initWhatIfScenario()" in js)
test("initWhatIfScenario called in renderAuthorityDashboard", "initWhatIfScenario();" in js)
test("Listener bound guard prevents duplicate listeners", "slider.dataset.bound" in js)
test("Deterministic thresholds implemented in JS", "volume < 18000" in js and "volume < 35000" in js)
test("Low / Moderate threshold output present", "Low / Moderate" in js)
test("Moderate / High threshold output present", "Moderate / High" in js)
test("High / Critical threshold output present", "High / Critical" in js)
test("Planning recommendation recommendation present", "Consider reviewing service capacity along high-volume corridors" in js)

# 6. Prohibitions
print("\n6. Strict Negative Constraints (Prohibitions):")
test("No PDS integration claim", "PDS integration" not in html and "PDS Integration" not in html)
test("No ESIC integration claim", "ESIC integration" not in html and "ESIC Integration" not in html)
test("No Aadhaar verification", "Aadhaar verification" not in html and "Aadhaar Verification" not in html)
test("No WhatsApp integration", "WhatsApp integration" not in html and "WhatsApp Integration" not in html)
test("No JanParichay SSO", "JanParichay" not in html)
test("No official MoLE orders generated", "MoLE order" not in html and "official MoLE" not in html)
test("No continuous GPS tracking claimed", "No continuous GPS tracking" in html and "Continuous GPS tracking enabled" not in html)

print("\n" + "="*50)
if errors:
    print(f"FAILED: {len(errors)} checks failed!")
    for e in errors:
        print(" - " + e)
else:
    print(f"SUCCESS: ALL {24} WHAT-IF SCENARIO CHECKS PASSED!")
print("="*50)
