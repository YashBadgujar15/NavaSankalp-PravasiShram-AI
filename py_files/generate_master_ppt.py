import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# 1. Colors & Design Palette
BG_DARK = RGBColor(6, 10, 24)          # Deep Midnight Navy #060A18
CARD_BG = RGBColor(15, 23, 42)         # Surface Card Navy #0F172A
CARD_BORDER = RGBColor(30, 58, 95)     # Subtle Border
SAFFRON = RGBColor(249, 115, 22)       # Brand Saffron #F97316
SAFFRON_LIGHT = RGBColor(251, 146, 60) # Light Saffron #FB923C
EMERALD = RGBColor(16, 185, 129)       # Privacy/DPDP Emerald #10B981
BLUE_LIGHT = RGBColor(56, 189, 248)    # Intelligence Blue #38BDF8
INDIGO_ACCENT = RGBColor(99, 102, 241) # Modern Indigo #6366F1
WHITE = RGBColor(255, 255, 255)        # Text Primary #FFFFFF
TEXT_MUTED = RGBColor(148, 163, 184)   # Text Secondary #94A3B8
TEXT_DIM = RGBColor(100, 116, 139)     # Subtle Gray #64748B

def set_slide_bg(slide):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = BG_DARK

def add_header(slide, category_text, title_text, subtitle_text=""):
    # Category badge
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
    tf_cat = cat_box.text_frame
    tf_cat.word_wrap = True
    tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(9.5)
    p_cat.font.bold = True
    p_cat.font.color.rgb = SAFFRON_LIGHT
    p_cat.font.name = "Segoe UI"

    # Main Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.55))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = WHITE
    p_t.font.name = "Segoe UI"

    # Subtitle
    if subtitle_text:
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(0.4))
        tf_s = sub_box.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
        p_s = tf_s.paragraphs[0]
        p_s.text = subtitle_text
        p_s.font.size = Pt(11)
        p_s.font.color.rgb = TEXT_MUTED
        p_s.font.name = "Segoe UI"

def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.2)
    return shape

def add_image_with_border(slide, img_path, left, top, width, height):
    if os.path.exists(img_path):
        # Card border behind image
        add_card(slide, left - Inches(0.06), top - Inches(0.06), width + Inches(0.12), height + Inches(0.12), CARD_BG, SAFFRON)
        slide.shapes.add_picture(img_path, left, top, width, height)
        return True
    return False

# Initialize Presentation (16:9 Widescreen)
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

print("Building Slide 1: Title & Hackathon Overview...")
# =========================================================
# SLIDE 1: COVER / TITLE SLIDE
# =========================================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_bg(s1)

# Hackathon Header Pill
add_card(s1, Inches(0.8), Inches(0.65), Inches(8.8), Inches(0.42), RGBColor(14, 28, 54), SAFFRON)
badge_box = s1.shapes.add_textbox(Inches(0.95), Inches(0.7), Inches(8.5), Inches(0.35))
tf_b = badge_box.text_frame
tf_b.margin_top = tf_b.margin_left = tf_b.margin_bottom = tf_b.margin_right = 0
p = tf_b.paragraphs[0]
p.text = "★ DIGITAL SHRAM SANKALP IDEATION HACKATHON • PROBLEM STATEMENT 1"
p.font.size = Pt(9.5)
p.font.bold = True
p.font.color.rgb = SAFFRON_LIGHT

# Main Brand Title
t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.5), Inches(1.2))
tf = t_box.text_frame
tf.word_wrap = True
tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0
p = tf.paragraphs[0]
p.text = "PRAVASISHRAM AI"
p.font.size = Pt(44)
p.font.bold = True
p.font.color.rgb = WHITE
p.font.name = "Segoe UI"

# Tagline & Statement
sub_box = s1.shapes.add_textbox(Inches(0.8), Inches(2.4), Inches(11.5), Inches(0.8))
tf = sub_box.text_frame
tf.word_wrap = True
tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0
p = tf.paragraphs[0]
p.text = "“Track the migration event, not the person.”"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = SAFFRON
p2 = tf.add_paragraph()
p2.text = "Consent-Driven Migration Intelligence for Dignity, Welfare Delivery & Inter-State Coordination"
p2.font.size = Pt(13)
p2.font.color.rgb = TEXT_MUTED

# Left Card: Problem Statement Highlight
add_card(s1, Inches(0.8), Inches(3.45), Inches(5.6), Inches(3.4), CARD_BG, CARD_BORDER)
ps_box = s1.shapes.add_textbox(Inches(1.05), Inches(3.65), Inches(5.1), Inches(3.0))
tf = ps_box.text_frame
tf.word_wrap = True
tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0

p = tf.paragraphs[0]
p.text = "OFFICIAL CHALLENGE FOCUS"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = BLUE_LIGHT

p = tf.add_paragraph()
p.text = "Problem Statement 1: Migration Worker Tracking in eShram"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = WHITE
p.space_before = Pt(4)

p = tf.add_paragraph()
p.text = "“How might we build a consent-based, secure, and privacy preserving migrant tracking capability within eShram that enables location updates, migration heatmaps, predictive movement models, and simplified check-in mechanisms to better inform welfare delivery for migrant workers?”"
p.font.size = Pt(10)
p.font.color.rgb = TEXT_MUTED
p.space_before = Pt(6)

p = tf.add_paragraph()
p.text = "✔ 100% Aligned to all 8 Ministry Evaluation Criteria"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = EMERALD
p.space_before = Pt(10)

# Right Card: Team NavaSankalp Info
add_card(s1, Inches(6.7), Inches(3.45), Inches(5.8), Inches(3.4), CARD_BG, SAFFRON)
team_box = s1.shapes.add_textbox(Inches(6.95), Inches(3.65), Inches(5.3), Inches(3.0))
tf = team_box.text_frame
tf.word_wrap = True
tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0

p = tf.paragraphs[0]
p.text = "SUBMITTED BY: TEAM NAVASANKALP"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = SAFFRON

members_text = [
    ("BADGUJAR YASH RAMESHBHAI (Team Leader)", "ET25BTCO801 | SCET Surat | yashbadgujar.co24d3@scet.ac.in"),
    ("SONAR ANJALI SHIVDAS", "ET25BTCO821 | SCET Surat | anjalisonar.co24d3@scet.ac.in"),
    ("TANVI CHIB", "ET24BTCO206 | SCET Surat | tanvichib.co24d3@scet.ac.in"),
    ("JOGI PRANAV BHARAT", "250763107012 | SSASIT Surat | pranavjogi205@gmail.com")
]

for name, meta in members_text:
    p = tf.add_paragraph()
    p.text = f"• {name}"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_before = Pt(5)

    p_sub = tf.add_paragraph()
    p_sub.text = f"   {meta}"
    p_sub.font.size = Pt(8.5)
    p_sub.font.color.rgb = TEXT_MUTED

# Links footer inside card
p_links = tf.add_paragraph()
p_links.text = "🔗 Live Prototype: http://localhost:8888  |  GitHub: NavaSankalp/PravasiShram-AI"
p_links.font.size = Pt(9)
p_links.font.bold = True
p_links.font.color.rgb = BLUE_LIGHT
p_links.space_before = Pt(8)


print("Building Slide 2: Problem Context & Ground Realities...")
# =========================================================
# SLIDE 2: PROBLEM CONTEXT & GROUND REALITIES
# =========================================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_bg(s2)
add_header(s2, "Context & Pain Points", "The Unseen Crisis in India's Migrant Workforce Tracking", 
           "Over 450 Million domestic migrants drive India's economy, yet social protection remains bound to static domiciles.")

cards_data_s2 = [
    ("1. SURVEILLANCE PARADOX", 
     "Migrant workers actively resist continuous GPS apps due to severe battery drain, fear of employer surveillance, and data misuse. Any tracking framework requiring background monitoring experiences immediate user abandonment.", 
     SAFFRON),
    ("2. DIGITAL LITERACY BARRIER", 
     "Over 68% of informal construction and textile workers struggle with multi-page bureaucratic portal forms. English/complex Hindi portals lead to clerical fraud, middleman exploitation, and outdated worker registries.", 
     BLUE_LIGHT),
    ("3. WELFARE PORTABILITY LAG", 
     "When workers move from Bihar/UP to Gujarat/Maharashtra, destination state departments have zero advance warning. One Nation One Ration Card (ONORC), ESIC healthcare, and housing suffer chronic misallocation.", 
     INDIGO_ACCENT),
    ("4. REACTIVE VS PROACTIVE CRISIS", 
     "Current governance relies on post-calamity census updates. During seasonal floods, festival surges, or economic shocks, governments react weeks after bottlenecks occur rather than preparing ahead of time.", 
     EMERALD)
]

for idx, (title, desc, color) in enumerate(cards_data_s2):
    row = idx // 2
    col = idx % 2
    left = Inches(0.8 + col * 5.95)
    top = Inches(1.85 + row * 2.5)
    add_card(s2, left, top, Inches(5.75), Inches(2.25), CARD_BG, color)
    
    tb = s2.shapes.add_textbox(left + Inches(0.3), top + Inches(0.25), Inches(5.15), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = color
    
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.size = Pt(10.2)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(8)


print("Building Slide 3: The Paradigm Shift (Comparison Matrix)...")
# =========================================================
# SLIDE 3: THE PARADIGM SHIFT: EVENT VS PERSON
# =========================================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_bg(s3)
add_header(s3, "Core Innovation", "Paradigm Shift: “Track the Migration Event, Not the Person”", 
           "How PravasiShram AI resolves the dilemma between worker privacy and state welfare intelligence.")

# Left Card: Traditional Approach (Flawed)
add_card(s3, Inches(0.8), Inches(1.85), Inches(5.6), Inches(4.9), CARD_BG, RGBColor(239, 68, 68))
tb_left = s3.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.0), Inches(4.4))
tf_l = tb_left.text_frame
tf_l.word_wrap = True
tf_l.margin_top = tf_l.margin_left = tf_l.margin_bottom = tf_l.margin_right = 0

p = tf_l.paragraphs[0]
p.text = "❌ TRADITIONAL CONTINUOUS TRACKING"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = RGBColor(239, 68, 68)

flaws = [
    ("Constant Background GPS", "Drains battery, consumes high mobile data on low-cost budget devices."),
    ("Surveillance & Employer Coercion", "Workers fear location logs can be exploited by employers, police, or local middlemen."),
    ("DPDP Act 2023 Non-Compliance", "Violates Purpose Limitation & Data Minimisation principles of India's DPDP Act."),
    ("Permanent Identity Binding", "Every movement vector is tied directly to Aadhaar/identity forever, risking massive breaches."),
    ("High Churn & Uninstalls", "Over 90% uninstallation rate within 14 days of app installation.")
]
for h, b in flaws:
    p = tf_l.add_paragraph()
    p.text = f"• {h}: "
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_before = Pt(8)
    run = p.add_run()
    run.text = b
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

# Right Card: PravasiShram AI (Breakthrough)
add_card(s3, Inches(6.8), Inches(1.85), Inches(5.7), Inches(4.9), CARD_BG, EMERALD)
tb_right = s3.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.1), Inches(4.4))
tf_r = tb_right.text_frame
tf_r.word_wrap = True
tf_r.margin_top = tf_r.margin_left = tf_r.margin_bottom = tf_r.margin_right = 0

p = tf_r.paragraphs[0]
p.text = "✔ PRAVASISHRAM AI (OUR INNOVATION)"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = EMERALD

perks = [
    ("Voluntary Episodic Check-ins", "Zero continuous GPS. Worker triggers a single 30-sec check-in when migrating."),
    ("Speech-to-Intent AI in 5+ Languages", "Voice recognition in Hindi, Gujarati, Marathi, Bengali, and Hinglish."),
    ("Cryptographic Disassociation Vault", "Individual identity is instantly stripped before transit data enters the corridor engine."),
    ("Full Revocable Consent & 90-Day TTL", "Worker can withdraw consent at any time; transit events automatically purge after 90 days."),
    ("High Voluntary Compliance", "Workers trust the system because their privacy is guaranteed by technical design.")
]
for h, b in perks:
    p = tf_r.add_paragraph()
    p.text = f"• {h}: "
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_before = Pt(8)
    run = p.add_run()
    run.text = b
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED


print("Building Slide 4: System Architecture & Workflow...")
# =========================================================
# SLIDE 4: SYSTEM ARCHITECTURE & 5-TIER WORKFLOW
# =========================================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_bg(s4)
add_header(s4, "Engineering Architecture", "End-to-End Privacy-Preserving System Workflow", 
           "From multilingual worker speech to proactive state labour department welfare provisioning.")

workflow_steps = [
    ("TIER 1: MULTI-CHANNEL INGESTION", 
     "• Worker speaks 1 sentence or uses quick-check-in.\n• Web Speech API + Low-tech IVR/SMS fallback.\n• Zero GPS or app permissions required.", SAFFRON),
    ("TIER 2: SPEECH-TO-INTENT NLP", 
     "• Multilingual parser (Devanagari/Latin/Gujarati).\n• Entity Extraction: Origin, Destination, Sector.\n• Intent mapped without manual form fatigue.", BLUE_LIGHT),
    ("TIER 3: DISASSOCIATION VAULT", 
     "• Strips PII (Name, Aadhaar, Phone).\n• Generates ephemeral transit token.\n• Strict 90-day Time-To-Live (TTL) auto-purge.", EMERALD),
    ("TIER 4: CORRIDOR INTELLIGENCE", 
     "• Aggregates macro corridor flows (e.g. Bihar ➔ Surat).\n• Time-series predictive model (6-month horizon).\n• Detects emerging seasonal surges & drift.", INDIGO_ACCENT),
    ("TIER 5: PROACTIVE WELFARE ACTION", 
     "• Destination State Labour alerts 2-4 weeks early.\n• ONORC ration buffer stocks pre-positioned.\n• Mobile clinics & crèches deployed to hubs.", SAFFRON_LIGHT)
]

for idx, (title, points, color) in enumerate(workflow_steps):
    left = Inches(0.8 + idx * 2.38)
    top = Inches(2.0)
    add_card(s4, left, top, Inches(2.25), Inches(4.7), CARD_BG, color)
    
    tb = s4.shapes.add_textbox(left + Inches(0.18), top + Inches(0.25), Inches(1.9), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0
    
    # Step Number
    p_num = tf.paragraphs[0]
    p_num.text = f"STEP {idx+1}"
    p_num.font.size = Pt(11)
    p_num.font.bold = True
    p_num.font.color.rgb = color
    
    p_title = tf.add_paragraph()
    p_title.text = title.split(":")[1].strip()
    p_title.font.size = Pt(11)
    p_title.font.bold = True
    p_title.font.color.rgb = WHITE
    p_title.space_before = Pt(4)
    
    p_desc = tf.add_paragraph()
    p_desc.text = points
    p_desc.font.size = Pt(9.5)
    p_desc.font.color.rgb = TEXT_MUTED
    p_desc.space_before = Pt(10)


print("Building Slide 5: Worker Experience & Voice AI...")
# =========================================================
# SLIDE 5: WORKER EXPERIENCE & 30-SECOND VOICE CHECK-IN
# =========================================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_bg(s5)
add_header(s5, "User Experience & Accessibility", "Worker Check-in: 30-Second Voice-Driven Simplicity", 
           "Empowering low-literacy informal workers through speech-to-intent in regional vernaculars.")

# Left Content Card
add_card(s5, Inches(0.8), Inches(1.85), Inches(6.0), Inches(4.9), CARD_BG, SAFFRON)
tb = s5.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.4), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0

p = tf.paragraphs[0]
p.text = "ZERO-FRICTION DESIGN FOR INFORMAL WORKERS"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = SAFFRON

features = [
    ("One-Tap Vernacular Speech", "Worker taps the microphone and speaks naturally: 'Main Patna se Surat textile kaam ke liye aaya hoon' or Hindi Devanagari: 'मैं मुंबई से सूरत आया हूँ'."),
    ("4-Step Visual Progress Stepper", "Real-time state transitions: 1. Listening ➔ 2. Understanding ➔ 3. Protecting ➔ 4. Ready. Workers see their privacy being safeguarded in real time."),
    ("Multilingual NLP Entity Extraction", "Automatically extracts: Origin City, Destination Hub, Work Sector, and Migration Type without filling lengthy forms."),
    ("Worker Empowerment & Verification", "Extracted values remain 100% editable. The worker verifies their details before voluntary one-click confirmation."),
    ("Assisted & Low-Tech Fallbacks", "Integrated CSC (Common Service Centre) assisted desks, missed-call IVR, and SMS keywords for basic feature phones.")
]

for h, b in features:
    p = tf.add_paragraph()
    p.text = f"• {h}: "
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_before = Pt(6)
    run = p.add_run()
    run.text = b
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

# Right Side Image Crop
add_image_with_border(s5, "worker_checkin_crop.png", Inches(7.1), Inches(1.85), Inches(5.4), Inches(4.9))


print("Building Slide 6: Privacy by Design & DPDP Act 2023...")
# =========================================================
# SLIDE 6: PRIVACY BY DESIGN & DPDP ACT 2023 COMPLIANCE
# =========================================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_bg(s6)
add_header(s6, "Data Security & Governance", "Privacy by Design: Fully Aligned with DPDP Act 2023", 
           "Building trust through strict data minimisation, cryptographic disassociation, and revocable consent.")

# Left Side Image Crop
add_image_with_border(s6, "consent_crop.png", Inches(0.8), Inches(1.85), Inches(5.4), Inches(4.9))

# Right Content Card
add_card(s6, Inches(6.5), Inches(1.85), Inches(6.0), Inches(4.9), CARD_BG, EMERALD)
tb = s6.shapes.add_textbox(Inches(6.8), Inches(2.1), Inches(5.4), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0

p = tf.paragraphs[0]
p.text = "CORE DATA PROTECTION SAFEGUARDS"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = EMERALD

safeguards = [
    ("Purpose Limitation (Section 5)", "Transit event data is legally restricted to aggregate welfare planning and disaster response. Commercial, tracking, or punitive use is strictly forbidden."),
    ("Data Minimisation (Section 6)", "No continuous GPS coordinate capture. No background telemetry. The system captures only discrete episodic transit points."),
    ("Identity Disassociation Vault", "Direct worker identifiers (Aadhaar, mobile, full name) are severed from transit records. Macro corridors track movement vectors, not personal dossiers."),
    ("Unconditional Consent Revocation", "Workers possess a prominent 'Withdraw Consent' toggle. Withdrawing consent immediately deactivates events and purges future corridor factoring."),
    ("90-Day Time-To-Live (TTL) Lifecycle", "All episodic check-in records have an automatic 90-day expiry. No permanent historical tracking logs remain stored on servers.")
]

for h, b in safeguards:
    p = tf.add_paragraph()
    p.text = f"• {h}: "
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_before = Pt(6)
    run = p.add_run()
    run.text = b
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED


print("Building Slide 7: Migration Corridor Intelligence & Map...")
# =========================================================
# SLIDE 7: MIGRATION INTELLIGENCE & INTERACTIVE MAP
# =========================================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_bg(s7)
add_header(s7, "Spatial Intelligence & Analytics", "Interactive Migration Intelligence & Corridor Heatmaps", 
           "Visualizing macro worker movements across interstate economic corridors to guide resource allocation.")

# Left Content Card
add_card(s7, Inches(0.8), Inches(1.85), Inches(5.9), Inches(4.9), CARD_BG, BLUE_LIGHT)
tb = s7.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.3), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0

p = tf.paragraphs[0]
p.text = "AGGREGATE CORRIDOR FLOW ANALYTICS"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = BLUE_LIGHT

map_points = [
    ("Dynamic SVG India Spatial Map", "Custom vector India map rendering major transit nodes: Patna, Surat, Mumbai, Lucknow, Hyderabad, Bengaluru, etc."),
    ("Curved Corridor Particle Flow", "Animated Bezier curve flow lines illustrating directional transit intensity and seasonal migration corridors."),
    ("Multi-Dimensional Filtering", "Filter by Origin/Destination State (e.g. Bihar, UP, Gujarat), Industry Sector (Textiles, Construction, Agriculture), and Migration Type."),
    ("Corridor Detail Drawer", "Clicking any corridor instantly provides deep analytics: total transit volume, active sector breakdown, transit time, and risk signal."),
    ("Cluster Strain Detection", "Highlights emerging destination bottlenecks (e.g. Surat textile belt, MMR construction zones) for early intervention.")
]

for h, b in map_points:
    p = tf.add_paragraph()
    p.text = f"• {h}: "
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_before = Pt(6)
    run = p.add_run()
    run.text = b
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

# Right Side Image Crop
add_image_with_border(s7, "map_corridors_crop.png", Inches(7.0), Inches(1.85), Inches(5.5), Inches(4.9))


print("Building Slide 8: Predictive Corridor Forecasting...")
# =========================================================
# SLIDE 8: PREDICTIVE CORRIDOR FORECASTING
# =========================================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_bg(s8)
add_header(s8, "Predictive Modeling", "Corridor Forecasting: 6-Month Predictive Horizon", 
           "Transforming reactive crisis management into proactive welfare planning through time-series forecasting.")

# Left Side Image Crop
add_image_with_border(s8, "forecast_crop.png", Inches(0.8), Inches(1.85), Inches(5.4), Inches(4.9))

# Right Content Card
add_card(s8, Inches(6.5), Inches(1.85), Inches(6.0), Inches(4.9), CARD_BG, SAFFRON)
tb = s8.shapes.add_textbox(Inches(6.8), Inches(2.1), Inches(5.4), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0

p = tf.paragraphs[0]
p.text = "PROACTIVE WELFARE PROVISIONING"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = SAFFRON

forecast_points = [
    ("6-Month Time-Series Horizon", "Observed historical baseline combined with statistical predictive curves and upper/lower confidence bounds."),
    ("Seasonal Surge Anticipation", "Predicts massive seasonal return movements (Post-Diwali, Chhath Puja, agricultural harvesting) 2 to 4 weeks before arrival."),
    ("Selectable Corridor Projections", "Interactive models for key corridors: Bihar ➔ Gujarat, UP ➔ Maharashtra, Odisha ➔ Gujarat, and All Corridors aggregate."),
    ("ONORC Food Grain Pre-Positioning", "Notifies State Civil Supplies departments to position portable One Nation One Ration Card grain stocks at destination fair price shops."),
    ("Transit Healthcare & Shelter Hubs", "Enables municipal corporations to deploy mobile ESIC health vans and temporary night shelters before peak worker influx arrives.")
]

for h, b in forecast_points:
    p = tf.add_paragraph()
    p.text = f"• {h}: "
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_before = Pt(6)
    run = p.add_run()
    run.text = b
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED


print("Building Slide 9: MoLE Command Center & What-if Scenario...")
# =========================================================
# SLIDE 9: MOLE COMMAND CENTER & WHAT-IF SIMULATOR
# =========================================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_bg(s9)
add_header(s9, "Authority Command Center", "MoLE Command Center & “What-if Migration Scenario” Simulator", 
           "Executive dashboard empowering labour administrators with real-time signals and surge simulation.")

# Left Content Card
add_card(s9, Inches(0.8), Inches(1.85), Inches(6.1), Inches(4.9), CARD_BG, INDIGO_ACCENT)
tb = s9.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.5), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0

p = tf.paragraphs[0]
p.text = "ACTIONABLE LABOUR GOVERNANCE SUITE"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = INDIGO_ACCENT

command_points = [
    ("Executive KPI Monitoring", "Live tracking of Total Verified Events, Active Inter-State Corridors, Emerging Corridors, and High Activity Destination Regions."),
    ("Automated AI Planning Signals", "Intelligent system directives (e.g. 'Deploy mobile ESIC clinic near Surat Loom Hub; Buffer 500 MT grain at Pandesara')."),
    ("Top Corridors Density Table", "Ranked tabular overview showing origin, destination, estimated worker volume, and status signals."),
    ("NEW: What-if Migration Scenario Simulator", "Allows authorities to simulate sudden migrant surges from 5,000 to 50,000 workers dynamically in real time."),
    ("4 Deterministic Indicators", "Updates Corridor Activity, Planning Pressure, Service Capacity Response, and Emerging Corridor Signals with rule-based recommendations.")
]

for h, b in command_points:
    p = tf.add_paragraph()
    p.text = f"• {h}: "
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_before = Pt(6)
    run = p.add_run()
    run.text = b
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

# Right Side Image Crop
add_image_with_border(s9, "command_center_crop.png", Inches(7.2), Inches(1.85), Inches(5.3), Inches(4.9))


print("Building Slide 10: Official Hackathon Criteria Alignment Matrix...")
# =========================================================
# SLIDE 10: OFFICIAL HACKATHON CRITERIA ALIGNMENT MATRIX
# =========================================================
s10 = prs.slides.add_slide(blank_layout)
set_slide_bg(s10)
add_header(s10, "Hackathon Evaluation Mapping", "Direct Alignment with Official MyGov Selection Criteria (8/8)", 
           "Demonstrating rigorous, point-by-point adherence to the Ministry of Labour & Employment evaluation rubric.")

# Create Table for 8 Criteria
rows = 9
cols = 3
table_shape = s10.shapes.add_table(rows, cols, Inches(0.8), Inches(1.85), Inches(11.73), Inches(4.9))
table = table_shape.table
table.columns[0].width = Inches(2.4)
table.columns[1].width = Inches(3.6)
table.columns[2].width = Inches(5.73)

headers = ["EVALUATION CRITERIA", "OFFICIAL MYGOV BENCHMARK", "PRAVASISHRAM AI IMPLEMENTED SOLUTION"]
for c_idx, h in enumerate(headers):
    cell = table.cell(0, c_idx)
    cell.fill.solid()
    cell.fill.fore_color.rgb = RGBColor(14, 28, 54)
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = SAFFRON_LIGHT

criteria_rows = [
    ("1. Relevance to Problem Statement", "Alignment with challenge area (eShram); understanding of worker & system needs.", "Directly solves Problem Statement 1: 'Migration Worker Tracking in eShram' via episodic consent check-in."),
    ("2. Innovation & Originality", "Novelty, emerging AI/ML analytics, accessibility tools, multilingual systems.", "Pioneered 'Track the migration event, not person'; Speech-to-Intent NLP in 5+ vernaculars."),
    ("3. Feasibility & Implementability", "Practical execution within MoLE digital ecosystem; technical viability & scalability.", "Built on ultra-lightweight standard web tech; zero battery drain; zero GPS permission requirements."),
    ("4. Impact Potential", "Improve worker welfare, policy intelligence, service delivery enhancement.", "Enables proactive ONORC food grain buffering and transit clinic deployment weeks before arrival."),
    ("5. User Experience & Accessibility", "Ease of use for workers; multilingual, disability-friendly, low-tech options.", "30-sec voice check-in, high-contrast mode, low-data toggle, and assisted CSC/IVR fallbacks."),
    ("6. Data Security & Privacy", "Compliance with data protection; safeguards for sensitive worker data.", "Strict compliance with India's DPDP Act 2023; cryptographic disassociation vault; 90-day TTL lifecycle."),
    ("7. Sustainability & Long-Term Value", "Long-term operational sustainability, maintenance, and future readiness.", "Low cloud operational footprint; automatic data expiry reduces storage costs; modular architecture."),
    ("8. Clarity of Presentation", "Quality of documentation, solution articulation, end-to-end demonstration.", "Fully functional interactive prototype, 7-step guided demo wizard, comprehensive live walk-through.")
]

for r_idx, (crit, bench, soln) in enumerate(criteria_rows):
    cell_crit = table.cell(r_idx + 1, 0)
    cell_bench = table.cell(r_idx + 1, 1)
    cell_soln = table.cell(r_idx + 1, 2)
    
    bg = CARD_BG if r_idx % 2 == 0 else RGBColor(10, 16, 36)
    cell_crit.fill.solid(); cell_crit.fill.fore_color.rgb = bg
    cell_bench.fill.solid(); cell_bench.fill.fore_color.rgb = bg
    cell_soln.fill.solid(); cell_soln.fill.fore_color.rgb = bg
    
    p = cell_crit.text_frame.paragraphs[0]
    p.text = crit
    p.font.size = Pt(8.8)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    p = cell_bench.text_frame.paragraphs[0]
    p.text = bench
    p.font.size = Pt(8.2)
    p.font.color.rgb = TEXT_MUTED
    
    p = cell_soln.text_frame.paragraphs[0]
    p.text = soln
    p.font.size = Pt(8.2)
    p.font.color.rgb = EMERALD if "DPDP" in soln or "solves" in soln else WHITE


print("Building Slide 11: Implementation Roadmap & Scalability...")
# =========================================================
# SLIDE 11: IMPLEMENTATION ROADMAP & SCALABILITY
# =========================================================
s11 = prs.slides.add_slide(blank_layout)
set_slide_bg(s11)
add_header(s11, "MoLE Deployment Strategy", "Phased National Rollout & eShram Ecosystem Integration", 
           "A realistic, scalable pathway from pilot validation to pan-India welfare coordination.")

phases = [
    ("PHASE 1: PILOT CORRIDORS (0 - 3 MONTHS)", 
     "• Focus on high-density textile & construction corridors:\n  - Bihar ➔ Surat (Textile Hub)\n  - UP ➔ Mumbai/MMR (Construction)\n• Pilot in partnership with Surat & Mumbai District Labour Offices.\n• Deploy assisted check-in kiosks at major railway transit hubs.\n• Benchmark worker voice recognition accuracy across dialects.", SAFFRON),
    ("PHASE 2: eSHRAM INTEGRATION (3 - 6 MONTHS)", 
     "• API handshake with eShram universal database via OAuth2 tokens.\n• Direct benefit tagging: ONORC ration cards & Ayushman Bharat.\n• Enable State-to-State automated inter-labour alerts.\n• Launch missed-call IVR and SMS check-in on universal toll-free 14434.", BLUE_LIGHT),
    ("PHASE 3: PAN-INDIA EXPANSION (6 - 12 MONTHS)", 
     "• Full rollout across all 28 States & 8 Union Territories.\n• Institutionalization within Ministry of Labour & Employment (MoLE).\n• Integration with National Career Service (NCS) for job matching.\n• Continuous AI refinement for seasonal migration prediction.", EMERALD)
]

for idx, (p_title, p_desc, color) in enumerate(phases):
    left = Inches(0.8 + idx * 3.98)
    top = Inches(1.9)
    add_card(s11, left, top, Inches(3.8), Inches(4.85), CARD_BG, color)
    
    tb = s11.shapes.add_textbox(left + Inches(0.25), top + Inches(0.3), Inches(3.3), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0
    
    p = tf.paragraphs[0]
    p.text = p_title
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = color
    
    p2 = tf.add_paragraph()
    p2.text = p_desc
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(12)


print("Building Slide 12: Team NavaSankalp & Prototype Access...")
# =========================================================
# SLIDE 12: TEAM NAVASANKALP & PROTOTYPE ACCESS
# =========================================================
s12 = prs.slides.add_slide(blank_layout)
set_slide_bg(s12)
add_header(s12, "Submission & Contact", "Team NavaSankalp — Committed to Worker Dignity & Welfare", 
           "Prototype engineered for the Digital Shram Sankalp Ideation Hackathon 2026.")

# Left 4 Team Member Cards
for idx, (name, meta) in enumerate(members_text):
    row = idx // 2
    col = idx % 2
    left = Inches(0.8 + col * 3.8)
    top = Inches(1.85 + row * 2.1)
    
    is_leader = idx == 0
    add_card(s12, left, top, Inches(3.6), Inches(1.9), CARD_BG, SAFFRON if is_leader else CARD_BORDER)
    
    tb = s12.shapes.add_textbox(left + Inches(0.2), top + Inches(0.18), Inches(3.2), Inches(1.5))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0
    
    p = tf.paragraphs[0]
    p.text = "★ TEAM LEADER" if is_leader else "TEAM MEMBER"
    p.font.size = Pt(8.5)
    p.font.bold = True
    p.font.color.rgb = SAFFRON_LIGHT if is_leader else BLUE_LIGHT
    
    p2 = tf.add_paragraph()
    p2.text = name.replace(" (Team Leader)", "")
    p2.font.size = Pt(11)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(3)
    
    parts = meta.split(" | ")
    p3 = tf.add_paragraph()
    p3.text = f"Roll: {parts[0]}\nBranch: Computer Engineering\nCollege: {parts[1]}\nEmail: {parts[2]}"
    p3.font.size = Pt(8.2)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(3)

# Right Side Links & Call-To-Action Card
add_card(s12, Inches(8.6), Inches(1.85), Inches(3.93), Inches(4.3), CARD_BG, EMERALD)
tb = s12.shapes.add_textbox(Inches(8.85), Inches(2.1), Inches(3.43), Inches(3.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_top = tf.margin_left = tf.margin_bottom = tf.margin_right = 0

p = tf.paragraphs[0]
p.text = "PROTOTYPE DEMONSTRATION & REPO"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = EMERALD

p = tf.add_paragraph()
p.text = "🌐 LIVE WORKING PROTOTYPE"
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = WHITE
p.space_before = Pt(10)

p = tf.add_paragraph()
p.text = "http://localhost:8888\n(Features live voice recognition, interactive map, What-if scenario simulator & 7-stage walkthrough)"
p.font.size = Pt(8.5)
p.font.color.rgb = BLUE_LIGHT

p = tf.add_paragraph()
p.text = "💻 SOURCE CODE REPOSITORY"
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = WHITE
p.space_before = Pt(10)

p = tf.add_paragraph()
p.text = "https://github.com/YashBadgujar/PravasiShram-AI\n(Complete codebase, test suites & documentation)"
p.font.size = Pt(8.5)
p.font.color.rgb = SAFFRON_LIGHT

p = tf.add_paragraph()
p.text = "“Track the migration event, not the person.”\nThank you for your consideration."
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = WHITE
p.space_before = Pt(14)

# Save presentation
output_path = r"C:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi\PravasiShram_AI_NavaSankalp_Presentation.pptx"
prs.save(output_path)
print(f"\nPresentation successfully generated and saved to: {output_path}")
