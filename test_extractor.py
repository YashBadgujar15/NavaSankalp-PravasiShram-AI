import re

KNOWN = [
  {"city": "Patna", "state": "Bihar", "fullName": "Patna, Bihar", "patterns": [r"\bpatna\b", r"पटना", r"પટના", r"\bbihar\b", r"बिहार"]},
  {"city": "Surat", "state": "Gujarat", "fullName": "Surat, Gujarat", "patterns": [r"\bsurat\b", r"सूरत", r"સુરત"]},
  {"city": "Mumbai", "state": "Maharashtra", "fullName": "Mumbai, Maharashtra", "patterns": [r"\bmumbai\b", r"\bbombay\b", r"मुंबई", r"बॉम्बे", r"મુંબઈ"]},
  {"city": "Varanasi", "state": "Uttar Pradesh", "fullName": "Varanasi, Uttar Pradesh", "patterns": [r"\bvaranasi\b", r"\bbanaras\b", r"\bkashi\b", r"वाराणसी", r"बनारस", r"काशी", r"બનારસ"]},
  {"city": "Bhavnagar", "state": "Gujarat", "fullName": "Bhavnagar, Gujarat", "patterns": [r"\bbhavnagar\b", r"भावनगर", r"ભાવનગર"]},
  {"city": "Jaipur", "state": "Rajasthan", "fullName": "Jaipur, Rajasthan", "patterns": [r"\bjaipur\b", r"\brajasthan\b", r"जयपुर", r"राजस्थान"]},
  {"city": "Ahmedabad", "state": "Gujarat", "fullName": "Ahmedabad, Gujarat", "patterns": [r"\bahmedabad\b", r"\bamdavad\b", r"अहमदाबाद", r"અમદાવાદ"]},
  {"city": "Pune", "state": "Maharashtra", "fullName": "Pune, Maharashtra", "patterns": [r"\bpune\b", r"\bpoona\b", r"पुणे", r"પૂણે"]},
  {"city": "Delhi", "state": "Delhi", "fullName": "Delhi NCR, Delhi", "patterns": [r"\bdelhi\b", r"\bncr\b", r"दिल्ली", r"एनसीआर"]},
  {"city": "Bengaluru", "state": "Karnataka", "fullName": "Bengaluru, Karnataka", "patterns": [r"\bbengaluru\b", r"\bbangalore\b", r"बेंगलुरु", r"बैंगलोर"]},
  {"city": "Ganjam", "state": "Odisha", "fullName": "Ganjam, Odisha", "patterns": [r"\bganjam\b", r"\bodisha\b", r"गंजम", r"ओडिशा"]},
  {"city": "Murshidabad", "state": "West Bengal", "fullName": "Murshidabad, West Bengal", "patterns": [r"\bmurshidabad\b", r"\bmalda\b", r"मुर्शिदाबाद", r"মালদা"]},
  {"city": "Ranchi", "state": "Jharkhand", "fullName": "Ranchi, Jharkhand", "patterns": [r"\branchi\b", r"\bjharkhand\b", r"रांची", r"झारखंड"]},
  {"city": "Gorakhpur", "state": "Uttar Pradesh", "fullName": "Gorakhpur, Uttar Pradesh", "patterns": [r"\bgorakhpur\b", r"गोरखपुर"]},
  {"city": "Nagpur", "state": "Maharashtra", "fullName": "Nagpur, Maharashtra", "patterns": [r"\bnagpur\b", r"नागपुर"]}
]

def extract(text):
    found = []
    for loc in KNOWN:
        for pat in loc["patterns"]:
            m = re.search(pat, text, re.IGNORECASE)
            if m:
                found.append({"loc": loc, "start": m.start(), "end": m.end()})
                break
    found.sort(key=lambda x: x["start"])
    
    origin = "Not specified"
    dest = "Not specified"
    orig_state = ""
    dest_state = ""
    
    if len(found) >= 2:
        between = text[found[0]["end"]:found[1]["start"]]
        # In Hindi/Hinglish/Gujarati: [Origin] se [Destination] or [Origin]थी [Destination]
        if re.search(r"\b(?:se|thi|from)\b|से|थी|થી", between, re.I) or not re.search(r"\b(?:to|me|mein)\b|में|मे|को", between, re.I):
            origin = found[0]["loc"]["fullName"]
            orig_state = found[0]["loc"]["state"]
            dest = found[1]["loc"]["fullName"]
            dest_state = found[1]["loc"]["state"]
        else:
            dest = found[0]["loc"]["fullName"]
            dest_state = found[0]["loc"]["state"]
            origin = found[1]["loc"]["fullName"]
            orig_state = found[1]["loc"]["state"]
    elif len(found) == 1:
        after = text[found[0]["end"]:]
        if re.search(r"\b(?:se|thi)\b|से|थी|થી", after, re.I):
            origin = found[0]["loc"]["fullName"]
            orig_state = found[0]["loc"]["state"]
        else:
            dest = found[0]["loc"]["fullName"]
            dest_state = found[0]["loc"]["state"]
            
    # Sector
    sector = "Not specified"
    if re.search(r"\b(?:textiles?|cloth(?:ing)?|kapd[aaeo]|powerlooms?|weav(?:er|ing)|bunkar)\b|कपड़ा|कपड़े|कपड़ो|टेक्सटाइल|बुनकर|हथकरघा|કાપડ", text, re.I):
        sector = "Textile"
    elif re.search(r"\b(?:construction|nirman|buildings?|mason|mistr[iy]|mazdoo?r)\b|निर्माण|कंस्ट्रक्शन|मकान|मिस्त्री|मजदूर|બાંધકામ", text, re.I):
        sector = "Construction"
    elif re.search(r"\b(?:diamonds?|heera|hira|polishing|ghasai)\b|हीरा|डायमंड|घिसाई|હીરા", text, re.I):
        sector = "Diamond & Loom"
    elif re.search(r"\b(?:manufacturing|factory|karkhana|industr(?:y|ial)|plant)\b|विनिर्माण|कारखाना|फैक्ट्री|ઉદ્યોગ", text, re.I):
        sector = "Manufacturing"
    elif re.search(r"\b(?:garments?|apparel|silai|tailor|darji)\b|परिधान|सिलाई|टेलर|દરજી", text, re.I):
        sector = "Garments"
    elif re.search(r"\b(?:logistics?|transport|warehouses?|godown|driver)\b|लॉजिस्टिक्स|परिवहन|गोदाम|ड्राइवर", text, re.I):
        sector = "Logistics"
        
    # Purpose
    purpose = "Not specified"
    if re.search(r"\b(?:ka+m|naukri|jobs?|works?|employment|kamaa?ne|labou?r|kaary|rojga+r)\b|काम|नौकरी|जॉब|रोजगार|कार्य|मजदूरी|કામ|રોજગાર", text, re.I):
        purpose = "Employment"
    elif re.search(r"\b(?:skills?|training|placements?|prashikshan|hunar)\b|कौशल|प्रशिक्षण|हुनर|ट्रेनिंग", text, re.I):
        purpose = "Skill Placement"
    elif re.search(r"\b(?:famil(?:y|ies)|pariva+r|shifting|relocation|bachh?e|ghar)\b|परिवार|घर", text, re.I):
        purpose = "Family Relocation"
    elif sector != "Not specified":
        # If user explicitly specifies a work sector (e.g. construction, textile), infer Employment
        purpose = "Employment"
        
    m_type = "Inter-state"
    if orig_state and dest_state:
        m_type = "Intra-state" if orig_state.lower() == dest_state.lower() else "Inter-state"
        
    return {"origin": origin, "dest": dest, "sector": sector, "purpose": purpose, "type": m_type}

tests = [
    ("मैं मुंबई से सूरत आया हूँ", {
        "origin": "Mumbai, Maharashtra",
        "dest": "Surat, Gujarat",
        "sector": "Not specified",
        "purpose": "Not specified",
        "type": "Inter-state"
    }),
    ("Main Patna se Surat textile kaam ke liye aaya hoon.", {
        "origin": "Patna, Bihar",
        "dest": "Surat, Gujarat",
        "sector": "Textile",
        "purpose": "Employment",
        "type": "Inter-state"
    }),
    ("मैं पटना से सूरत कपड़ा काम के लिए आया हूँ", {
        "origin": "Patna, Bihar",
        "dest": "Surat, Gujarat",
        "sector": "Textile",
        "purpose": "Employment",
        "type": "Inter-state"
    }),
    ("Varanasi se Mumbai construction ke liye aaya hoon", {
        "origin": "Varanasi, Uttar Pradesh",
        "dest": "Mumbai, Maharashtra",
        "sector": "Construction",
        "purpose": "Employment",
        "type": "Inter-state"
    }),
    ("हम बनारस से मुंबई निर्माण कार्य के लिए आए हैं।", {
        "origin": "Varanasi, Uttar Pradesh",
        "dest": "Mumbai, Maharashtra",
        "sector": "Construction",
        "purpose": "Employment",
        "type": "Inter-state"
    }),
    ("હું ભાવનગરથી સુરત હીરા ઘસવાના કામ માટે આવ્યો છું.", {
        "origin": "Bhavnagar, Gujarat",
        "dest": "Surat, Gujarat",
        "sector": "Diamond & Loom",
        "purpose": "Employment",
        "type": "Intra-state"
    })
]

all_passed = True
for sentence, expected in tests:
    res = extract(sentence)
    matches = res == expected
    print(f"Sentence: {sentence}")
    print(f"  Got:      {res}")
    print(f"  Expected: {expected}")
    print(f"  Result:   {'PASS' if matches else 'FAIL'}\n")
    if not matches:
        all_passed = False

if all_passed:
    print("ALL TESTS PASSED PERFECTLY!")
else:
    print("SOME TESTS FAILED!")
