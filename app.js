/**
 * PRAVASISHRAM AI - MASTER JAVASCRIPT CONTROLLER
 * "Track the migration event, not the person."
 * Digital Shram Sankalp Ideation Hackathon • Problem Statement 1
 */

// =========================================================
// 1. LOCAL SYNTHETIC DEMONSTRATION DATASET
// =========================================================

const syntheticDataset = {
  kpis: {
    totalEvents: 4820,
    activeCorridors: 27,
    emergingCorridors: 8,
    highActivityRegions: 6
  },
  
  corridors: [
    {
      id: "bihar-gujarat",
      originState: "Bihar",
      originCity: "Patna",
      destState: "Gujarat",
      destCity: "Surat",
      events: 1284,
      trend: "increasing",
      trendText: "↑ Increasing (+18% MoM)",
      sector: "Textile",
      migrationType: "Inter-state",
      signal: "Higher migration activity detected in this synthetic demonstration dataset. Review destination-area migrant service capacity."
    },
    {
      id: "up-maharashtra",
      originState: "Uttar Pradesh",
      originCity: "Varanasi",
      destState: "Maharashtra",
      destCity: "Mumbai",
      events: 1042,
      trend: "increasing",
      trendText: "↑ Increasing (+12% MoM)",
      sector: "Construction",
      migrationType: "Inter-state",
      signal: "Sustained urban infrastructure labor influx detected in western industrial corridor."
    },
    {
      id: "odisha-gujarat",
      originState: "Odisha",
      originCity: "Ganjam",
      destState: "Gujarat",
      destCity: "Surat",
      events: 876,
      trend: "stable",
      trendText: "→ Stable (±2% MoM)",
      sector: "Diamond & Loom",
      migrationType: "Inter-state",
      signal: "Established artisanal textile & diamond cluster movement pattern remains consistent."
    },
    {
      id: "rajasthan-gujarat",
      originState: "Rajasthan",
      originCity: "Jaipur",
      destState: "Gujarat",
      destCity: "Ahmedabad",
      events: 654,
      trend: "increasing",
      trendText: "↑ Increasing (+9% MoM)",
      sector: "Manufacturing",
      migrationType: "Inter-state",
      signal: "Emerging short-haul inter-state manufacturing cluster corridor."
    },
    {
      id: "wb-maharashtra",
      originState: "West Bengal",
      originCity: "Murshidabad",
      destState: "Maharashtra",
      destCity: "Pune",
      events: 580,
      trend: "increasing",
      trendText: "↑ Increasing (+14% MoM)",
      sector: "Garments",
      migrationType: "Inter-state",
      signal: "Apparel & light engineering skill migration cluster expanding in synthetic model."
    },
    {
      id: "jharkhand-delhi",
      originState: "Jharkhand",
      originCity: "Ranchi",
      destState: "Delhi NCR",
      destCity: "Delhi",
      events: 384,
      trend: "stable",
      trendText: "→ Stable (±1% MoM)",
      sector: "Logistics",
      migrationType: "Inter-state",
      signal: "National capital logistics warehousing transit corridor stable."
    }
  ],

  timeline: [
    {
      id: "evt-01",
      date: "12 Aug 2026",
      origin: "Patna, Bihar",
      dest: "Surat, Gujarat",
      purpose: "Employment",
      sector: "Textile",
      type: "Inter-state",
      consent: "active"
    },
    {
      id: "evt-02",
      date: "28 Aug 2026",
      origin: "Surat, Gujarat",
      dest: "Ahmedabad, Gujarat",
      purpose: "Employment",
      sector: "Industrial",
      type: "Intra-state",
      consent: "active"
    },
    {
      id: "evt-03",
      date: "15 Sep 2026",
      origin: "Ahmedabad, Gujarat",
      dest: "Surat, Gujarat",
      purpose: "Skill Placement",
      sector: "Textile",
      type: "Intra-state",
      consent: "active"
    }
  ],

  forecastCorridors: {
    all: {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul (Proj)", "Aug (Proj)", "Sep (Proj)"],
      observed: [3100, 3350, 3720, 4100, 4480, 4820, null, null, null],
      projected: [null, null, null, null, null, 4820, 5190, 5580, 6040],
      minVal: 2500,
      maxVal: 6500
    },
    "corridor-1": {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul (Proj)", "Aug (Proj)", "Sep (Proj)"],
      observed: [980, 1050, 1180, 1340, 1420, 1530, null, null, null],
      projected: [null, null, null, null, null, 1530, 1680, 1850, 1940],
      minVal: 800,
      maxVal: 2200
    },
    "corridor-2": {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul (Proj)", "Aug (Proj)", "Sep (Proj)"],
      observed: [820, 890, 1010, 1140, 1220, 1290, null, null, null],
      projected: [null, null, null, null, null, 1290, 1410, 1530, 1610],
      minVal: 600,
      maxVal: 1800
    },
    "corridor-3": {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul (Proj)", "Aug (Proj)", "Sep (Proj)"],
      observed: [480, 530, 600, 680, 740, 790, null, null, null],
      projected: [null, null, null, null, null, 790, 860, 940, 990],
      minVal: 350,
      maxVal: 1100
    },
    "corridor-4": {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul (Proj)", "Aug (Proj)", "Sep (Proj)"],
      observed: [410, 450, 510, 570, 620, 660, null, null, null],
      projected: [null, null, null, null, null, 660, 720, 780, 830],
      minVal: 300,
      maxVal: 950
    },
    "corridor-5": {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul (Proj)", "Aug (Proj)", "Sep (Proj)"],
      observed: [340, 380, 420, 480, 520, 550, null, null, null],
      projected: [null, null, null, null, null, 550, 610, 670, 710],
      minVal: 250,
      maxVal: 800
    }
  },

  forecast: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul (Proj)", "Aug (Proj)", "Sep (Proj)"],
    observed: [3100, 3350, 3720, 4100, 4480, 4820, null, null, null],
    projected: [null, null, null, null, null, 4820, 5190, 5580, 6040]
  }
};

// =========================================================
// 2. MULTILINGUAL DICTIONARY (I18N)
// =========================================================

const I18N = {
  en: {
    brandTag: "Track the migration event, not the person.",
    heroTitle: "Understand where migration is moving. Without constantly tracking people.",
    heroSub: "PravasiShram AI transforms voluntary migration check-ins into privacy-preserving, aggregated intelligence that can help inform welfare planning.",
    btnJourney: "Experience the Worker Journey",
    btnIntel: "Explore Migration Intelligence",
    workerTitle: "Update your migration",
    voicePrompt: 'Press the mic and say: "Main Patna se Surat textile kaam ke liye aaya hoon."',
    consentTitle: "Your movement. Your consent.",
    activeConsent: "Consent Status: ACTIVE",
    withdrawnConsent: "Consent Status: WITHDRAWN",
    demoBadge: "CONCEPT PROTOTYPE • DEMONSTRATION MODE"
  },
  hi: {
    brandTag: "प्रवासन घटना को ट्रैक करें, व्यक्ति को नहीं।",
    heroTitle: "प्रवासन कहाँ जा रहा है, समझें। बिना लोगों की निरंतर निगरानी किए।",
    heroSub: "प्रवासीश्रम AI स्वैच्छिक चेक-इन को गोपनीयता-संरक्षित, समेकित डेटा में बदलता है ताकि कल्याणकारी योजनाओं को बेहतर बनाया जा सके।",
    btnJourney: "श्रमिक यात्रा का अनुभव करें",
    btnIntel: "प्रवासन इंटेलिजेंस देखें",
    workerTitle: "अपना प्रवासन अपडेट करें",
    voicePrompt: 'माइक दबाएं और कहें: "Main Patna se Surat textile kaam ke liye aaya hoon."',
    consentTitle: "आपकी आवाजाही। आपकी सहमति।",
    activeConsent: "सहमति स्थिति: सक्रिय (ACTIVE)",
    withdrawnConsent: "सहमति स्थिति: वापस ली गई (WITHDRAWN)",
    demoBadge: "अवधारणा प्रोटोटाइप • प्रदर्शन मोड"
  },
  gu: {
    brandTag: "સ્થળાંતર ઘટનાને ટ્રેક કરો, વ્યક્તિને નહીં.",
    heroTitle: "સમજો સ્થળાંતર ક્યાં જઈ રહ્યું છે. લોકો પર સતત દેખરેખ રાખ્યા વિના.",
    heroSub: "પ્રવાસીશ્રમ AI સ્વૈચ્છિક ચેક-ઇનને ગોપનીયતા-સુરક્ષિત, એકત્રિત ઇન્ટેલિજન્સમાં ફેરવે છે જેથી કલ્યાણ આયોજન વધુ સારું થઈ શકે.",
    btnJourney: "શ્રમિક પ્રવાસનો અનુભવ કરો",
    btnIntel: "સ્થળાંતર ઇન્ટેલિજન્સ જુઓ",
    workerTitle: "તમારું સ્થળાંતર અપડેટ કરો",
    voicePrompt: "માઇક દબાવો અને કહો: 'હું ભાવનગરથી સુરત હીરા ઘસવાના કામ માટે આવ્યો છું.'",
    consentTitle: "તમારું સ્થળાંતર. તમારી સંમતિ.",
    activeConsent: "સંમતિ સ્થિતિ: સક્રિય (ACTIVE)",
    withdrawnConsent: "સંમતિ સ્થિતિ: પાછી ખેંચી (WITHDRAWN)",
    demoBadge: "કન્સેપ્ટ પ્રોટોટાઇપ • ડેમો મોડ"
  },
  mr: {
    brandTag: "स्थળાંતर घटना ट्रॅक करा, व्यक्तीला नाही.",
    heroTitle: "स्थળાंतर कुठे होत आहे ते समजून घ्या. लोकांवर सतत नजर न ठेवता.",
    heroSub: "प्रवासीश्रम AI ऐच्छिक चेक-इनचे गोपनीयता-संरक्षित विश्लेषणात रूपांतर करते ज्यामुळे कल्याणकारी योजनांचे नियोजन सुलभ होते.",
    btnJourney: "कामगार प्रवासाचा अनुभव घ्या",
    btnIntel: "स्थળાंतर इंटेलिजन्स एक्सप्लोर करा",
    workerTitle: "आपले स्थળાंतर अद्यतनित करा",
    voicePrompt: "माईक दाबा आणि सांगा: 'मी नागपूरहून पुण्यात बांधकाम कामासाठी आलो आहे.'",
    consentTitle: "तुमची हालचाल. तुमची संमती.",
    activeConsent: "संमती स्थिती: सक्रिय (ACTIVE)",
    withdrawnConsent: "संमती स्थिती: मागे घेतली (WITHDRAWN)",
    demoBadge: "संकल्पना प्रोटोटाइप • डेमो मोड"
  },
  bn: {
    brandTag: "অভিবাসন ঘটনা ট্র্যাক করুন, ব্যক্তিকে নয়।",
    heroTitle: "অভিবাসন কোথায় হচ্ছে তা বুঝুন। মানুষের উপর ক্রমাগত নজরদারি না করে।",
    heroSub: "প্রবাসীশ্রম AI স্বেচ্ছাসেবী চেক-ইনকে গোপনীয়তা-সুরক্ষিত সংগৃহীত তথ্যে রূপান্তরিত করে যা কল্যাণ পরিকল্পনায় সাহায্য করতে পারে।",
    btnJourney: "শ্রমিক যাত্রা অনুভব করুন",
    btnIntel: "মাইগ্রেশন ইন্টেলিজেন্স দেখুন",
    workerTitle: "আপনার অভিবাসন আপডেট করুন",
    voicePrompt: "মাইক টিপুন এবং বলুন: 'আমি মালদা থেকে মুম্বাই পোশাক কারখানায় কাজের জন্য এসেছি।'",
    consentTitle: "আপনার গতিবিধি। আপনার সম্মতি।",
    activeConsent: "সম্মতি স্থিতি: সক্রিয় (ACTIVE)",
    withdrawnConsent: "সম্মতি স্থिति: প্রত্যাহার করা হয়েছে (WITHDRAWN)",
    demoBadge: "ধারণা প্রোটোটাইপ • প্রদর্শনী মোড"
  }
};

// =========================================================
// 3. APPLICATION STATE
// =========================================================

const state = {
  currentLang: "en",
  consentStatus: "active",
  isListening: false,
  activeCorridor: syntheticDataset.corridors[0],
  filters: {
    state: "all",
    sector: "all",
    type: "all"
  },
  demoStep: 1,
  demoAutoPlayTimer: null,
  speechRecognitionAvailable: false,
  highContrast: false,
  lowDataMode: false,
  currentTranscript: "",
  workerDraft: {
    origin: "Patna, Bihar",
    dest: "Surat, Gujarat",
    purpose: "Employment",
    sector: "Textile",
    type: "Inter-state"
  }
};

// =========================================================
// 4. SOUND ENGINE (PROCEDURAL WEB AUDIO API)
// =========================================================

class ProceduralSoundEngine {
  constructor() {
    this.ctx = null;
    this.enabled = true;
  }

  init() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) this.ctx = new AudioCtx();
    }
  }

  playBeep(freq = 600, duration = 0.08, type = "sine") {
    if (!this.enabled || state.lowDataMode) return;
    try {
      this.init();
      if (!this.ctx) return;
      if (this.ctx.state === "suspended") this.ctx.resume();

      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
      gain.gain.setValueAtTime(0.06, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + duration);

      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + duration);
    } catch (e) {}
  }

  playChime() {
    if (!this.enabled || state.lowDataMode) return;
    this.playBeep(880, 0.12, "sine");
    setTimeout(() => this.playBeep(1320, 0.18, "sine"), 80);
  }

  playClick() {
    this.playBeep(420, 0.04, "triangle");
  }

  playWarning() {
    this.playBeep(320, 0.15, "square");
  }
}

const sound = new ProceduralSoundEngine();

// =========================================================
// 5. TOAST NOTIFICATION SYSTEM
// =========================================================

function showToast(title, message, type = "info") {
  const container = document.getElementById("toastContainer");
  if (!container) return;

  const toast = document.createElement("div");
  toast.className = `toast-item ${type}`;
  toast.innerHTML = `
    <div>
      <strong style="display:block; font-size:0.86rem; color:#fff;">${title}</strong>
      <span style="font-size:0.78rem; color:#cbd5e1;">${message}</span>
    </div>
  `;

  container.appendChild(toast);
  sound.playChime();

  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateX(50px)";
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

// =========================================================
// 6. INITIALIZATION & DOM READY
// =========================================================

document.addEventListener("DOMContentLoaded", () => {
  // 1. Language selector setup
  initLanguageSwitcher();

  // 2. Accessibility & Low-Data controls
  initAccessibilityControls();

  // 3. Worker Check-in Experience (Voice & Manual)
  initWorkerExperience();

  // 4. Consent Center functionality
  initConsentCenter();

  // 5. Timeline renderer
  renderTimeline();

  // 6. SVG Map & Corridor Controller
  initSvgMapAndCorridors();

  // 7. Authority Command Center & KPIs
  renderAuthorityDashboard();

  // 8. Corridor Forecast Chart
  renderForecastChart();

  // 9. Guided 2-Minute Demo Engine
  initDemoJourney();

  // 10. Universal Modal Click-outside & Escape
  initModalListeners();

  // 11. Responsive Mobile Navigation Menu
  initMobileNavigation();

  // Initial welcome toast
  setTimeout(() => {
    showToast("PravasiShram AI Active", "Consent-driven migration intelligence demonstration ready.", "info");
  }, 1000);
});

// =========================================================
// 7. LANGUAGE SWITCHER
// =========================================================

function initLanguageSwitcher() {
  const select = document.getElementById("langSelector");
  if (!select) return;

  select.addEventListener("change", (e) => {
    sound.playClick();
    setLanguage(e.target.value);
  });
}

function setLanguage(lang) {
  state.currentLang = lang;
  const dict = I18N[lang] || I18N.en;

  // Update prominent elements
  const elBrandTag = document.getElementById("i18n-brand-tag");
  if (elBrandTag) elBrandTag.textContent = dict.brandTag;

  const elHeroTitle = document.getElementById("i18n-hero-title");
  if (elHeroTitle) elHeroTitle.textContent = dict.heroTitle;

  const elHeroSub = document.getElementById("i18n-hero-sub");
  if (elHeroSub) elHeroSub.textContent = dict.heroSub;

  const elBtnJourney = document.getElementById("i18n-btn-journey");
  if (elBtnJourney) elBtnJourney.textContent = dict.btnJourney;

  const elBtnIntel = document.getElementById("i18n-btn-intel");
  if (elBtnIntel) elBtnIntel.textContent = dict.btnIntel;

  const elWorkerTitle = document.getElementById("i18n-worker-title");
  if (elWorkerTitle) elWorkerTitle.textContent = dict.workerTitle;

  const elVoicePrompt = document.getElementById("i18n-voice-prompt");
  if (elVoicePrompt) elVoicePrompt.textContent = dict.voicePrompt;

  const elConsentTitle = document.getElementById("i18n-consent-title");
  if (elConsentTitle) elConsentTitle.textContent = dict.consentTitle;

  updateConsentBannerUI();
  showToast("Language Updated", `Switched interface to ${lang.toUpperCase()}`, "info");
}

// =========================================================
// 8. ACCESSIBILITY & LOW DATA MODE
// =========================================================

function initAccessibilityControls() {
  const btnContrast = document.getElementById("btnToggleContrast");
  const btnLowData = document.getElementById("btnToggleLowData");

  if (btnContrast) {
    btnContrast.addEventListener("click", () => {
      sound.playClick();
      state.highContrast = !state.highContrast;
      document.body.classList.toggle("high-contrast", state.highContrast);
      btnContrast.classList.toggle("active", state.highContrast);
      showToast("Display Mode", state.highContrast ? "High Contrast Enabled" : "Standard Display", "info");
    });
  }

  if (btnLowData) {
    btnLowData.addEventListener("click", () => {
      sound.playClick();
      state.lowDataMode = !state.lowDataMode;
      document.body.classList.toggle("low-data", state.lowDataMode);
      btnLowData.classList.toggle("active", state.lowDataMode);
      showToast("Data Mode", state.lowDataMode ? "Low-Data Mode Active (Animations Disabled)" : "Full Experience Enabled", "info");
    });
  }
}

// =========================================================
// 9. WORKER EXPERIENCE: VOICE & MANUAL CHECK-IN
// =========================================================

function initWorkerExperience() {
  // Tab switcher (Voice vs Manual)
  const tabVoice = document.getElementById("tabCheckinVoice");
  const tabManual = document.getElementById("tabCheckinManual");
  const paneVoice = document.getElementById("paneVoice");
  const paneManual = document.getElementById("paneManual");

  if (tabVoice && tabManual) {
    tabVoice.addEventListener("click", () => {
      sound.playClick();
      tabVoice.classList.add("active");
      tabManual.classList.remove("active");
      if (paneVoice) paneVoice.style.display = "block";
      if (paneManual) paneManual.style.display = "none";
    });

    tabManual.addEventListener("click", () => {
      sound.playClick();
      tabManual.classList.add("active");
      tabVoice.classList.remove("active");
      if (paneVoice) paneVoice.style.display = "none";
      if (paneManual) paneManual.style.display = "block";
    });
  }

  // Helper for displaying actual or demo transcript inside phone screen
  function displayTranscript(labelHtml, badgeText, textContent, isLive = false) {
    const container = document.getElementById("voiceTranscriptContainer");
    const elLabel = document.getElementById("transcriptLabel");
    const elBadge = document.getElementById("transcriptStatusBadge");
    const elText = document.getElementById("voiceTranscriptText");

    if (container) container.style.display = "block";
    if (elLabel) elLabel.innerHTML = labelHtml;
    if (elBadge) {
      elBadge.textContent = badgeText;
      if (isLive) {
        elBadge.style.color = "#f43f5e";
        elBadge.style.background = "rgba(244,63,94,0.12)";
      } else {
        elBadge.style.color = "var(--emerald-light)";
        elBadge.style.background = "rgba(16,185,129,0.12)";
      }
    }
    if (elText) elText.textContent = textContent;
  }

  // Helper to clear old/stale extraction state when a new session starts
  function resetExtractedFieldsToProcessing(statusText = "Listening...") {
    const elOrigin = document.getElementById("entityOrigin");
    const elDest = document.getElementById("entityDest");
    const elSector = document.getElementById("entitySector");
    const elPurpose = document.getElementById("entityPurpose");
    const elType = document.getElementById("entityType");

    if (elOrigin) elOrigin.value = statusText;
    if (elDest) elDest.value = statusText;
    if (elSector) elSector.value = statusText;
    if (elPurpose) elPurpose.value = statusText;
    if (elType) elType.value = statusText;

    state.workerDraft = {
      origin: statusText,
      dest: statusText,
      sector: statusText,
      purpose: statusText,
      type: statusText
    };

    const steps = [
      document.getElementById("stepListening"),
      document.getElementById("stepUnderstanding"),
      document.getElementById("stepProtecting"),
      document.getElementById("stepReady")
    ];
    steps.forEach((s, idx) => {
      if (s) s.classList.toggle("active", idx === 0);
    });
  }

  // Voice Recognition & Simulator Fallback
  const micBtn = document.getElementById("btnBigMic");
  const micStatus = document.getElementById("micStatusText");

  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  let recognition = null;

  function stopListeningUI() {
    state.isListening = false;
    if (micBtn) micBtn.classList.remove("recording");
  }

  if (SpeechRecognition) {
    state.speechRecognitionAvailable = true;
    recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = true;

    recognition.onstart = () => {
      state.isListening = true;
      if (micBtn) micBtn.classList.add("recording");
      if (micStatus) micStatus.innerHTML = '<span style="color:#f43f5e;">🎙️ Listening... Speak now</span>';
      displayTranscript('<i class="fa-solid fa-microphone-lines" style="color:#f43f5e;"></i> Listening...', 'Live', 'Listening to microphone input...', true);
      resetExtractedFieldsToProcessing("Listening...");
    };

    recognition.onresult = (e) => {
      let interimTranscript = '';
      let finalTranscript = '';

      for (let i = e.resultIndex; i < e.results.length; ++i) {
        if (e.results[i].isFinal) {
          finalTranscript += e.results[i][0].transcript;
        } else {
          interimTranscript += e.results[i][0].transcript;
        }
      }

      if (interimTranscript && !finalTranscript) {
        displayTranscript('<i class="fa-solid fa-microphone-lines" style="color:#f97316;"></i> Listening (Live):', 'Speaking...', `"${interimTranscript}"`, true);
      }

      if (finalTranscript) {
        const spokenText = finalTranscript.trim();
        state.currentTranscript = spokenText;
        displayTranscript('<i class="fa-solid fa-quote-left" style="color:#34d399;"></i> You said:', 'Speech Recognized', `"${spokenText}"`, false);
        if (micStatus) micStatus.innerHTML = '<span style="color:#34d399;">Speech recognized! Processing event...</span>';
        stopListeningUI();
        extractMigrationIntent(spokenText);
      }
    };

    recognition.onerror = (err) => {
      stopListeningUI();
      const reason = err && err.error === 'not-allowed' 
        ? 'Mic Permission Denied' 
        : err && err.error === 'no-speech' 
          ? 'No Speech Detected' 
          : 'Recognition Fallback';
      
      const fallbackText = "Main Patna se Surat textile kaam ke liye aaya hoon.";
      state.currentTranscript = fallbackText;
      displayTranscript('<i class="fa-solid fa-circle-info" style="color:#fb923c;"></i> Demo input:', reason, `"${fallbackText}"`, false);
      if (micStatus) micStatus.innerHTML = `<span style="color:#fb923c;">Demo input (${reason}): "${fallbackText}"</span>`;
      extractMigrationIntent(fallbackText);
    };

    recognition.onend = () => {
      stopListeningUI();
    };
  }

  if (micBtn) {
    micBtn.addEventListener("click", () => {
      sound.playClick();
      if (!state.isListening) {
        resetExtractedFieldsToProcessing("Listening...");
        if (recognition) {
          try {
            recognition.lang = state.currentLang === "hi" ? "hi-IN" : "en-IN";
            recognition.start();
          } catch (err) {
            const fallbackText = "Main Patna se Surat textile kaam ke liye aaya hoon.";
            state.currentTranscript = fallbackText;
            displayTranscript('<i class="fa-solid fa-circle-info" style="color:#fb923c;"></i> Demo input:', 'Demo Fallback', `"${fallbackText}"`, false);
            simulateVoiceProcessing(fallbackText);
          }
        } else {
          // Graceful fallback simulation
          const fallbackText = "Main Patna se Surat textile kaam ke liye aaya hoon.";
          state.currentTranscript = fallbackText;
          displayTranscript('<i class="fa-solid fa-circle-info" style="color:#fb923c;"></i> Demo input (Browser speech API unavailable):', 'Demo Fallback', `"${fallbackText}"`, false);
          simulateVoiceProcessing(fallbackText);
        }
      } else {
        if (recognition) recognition.stop();
        stopListeningUI();
      }
    });
  }

  // Quick Preset Sample Chips
  const presetChips = document.querySelectorAll(".qvc-btn");
  presetChips.forEach(chip => {
    chip.addEventListener("click", () => {
      sound.playClick();
      const text = chip.getAttribute("data-sample") || chip.textContent.trim();
      state.currentTranscript = text;
      resetExtractedFieldsToProcessing("Extracting scenario...");
      displayTranscript('<i class="fa-solid fa-circle-play" style="color:#60a5fa;"></i> Demo input:', 'Preset Scenario', `"${text}"`, false);
      simulateVoiceProcessing(text);
    });
  });

  // Manual Form Submission
  const manualForm = document.getElementById("manualCheckinForm");
  if (manualForm) {
    manualForm.addEventListener("submit", (e) => {
      e.preventDefault();
      sound.playClick();
      const origin = document.getElementById("manualOrigin").value;
      const dest = document.getElementById("manualDest").value;
      const sector = document.getElementById("manualSector").value;
      const purpose = document.getElementById("manualPurpose").value;

      state.workerDraft = {
        origin,
        dest,
        purpose,
        sector,
        type: origin.split(",")[1]?.trim() !== dest.split(",")[1]?.trim() ? "Inter-state" : "Intra-state"
      };

      triggerAiPipelineSteps(() => {
        updateExtractedFields();
        showToast("Extracted Successfully", "Review and confirm your voluntary migration event.", "success");
      });
    });
  }

  // Confirm Check-in Button with duplicate listener prevention
  const btnConfirm = document.getElementById("btnConfirmCheckin");
  if (btnConfirm && !btnConfirm.dataset.bound) {
    btnConfirm.dataset.bound = "true";
    btnConfirm.addEventListener("click", () => {
      sound.playChime();
      recordWorkerCheckin();
    });
  }
}

function simulateVoiceProcessing(transcript) {
  const micStatus = document.getElementById("micStatusText");
  const micBtn = document.getElementById("btnBigMic");

  if (micBtn) micBtn.classList.add("recording");
  if (micStatus) micStatus.innerHTML = `<span style="color:#f97316;">Processing: "${transcript}"</span>`;

  setTimeout(() => {
    if (micBtn) micBtn.classList.remove("recording");
    extractMigrationIntent(transcript);
  }, 700);
}

// Location knowledge base supporting English, Hindi (Devanagari), and Gujarati
const KNOWN_LOCATIONS = [
  { city: "Patna", state: "Bihar", fullName: "Patna, Bihar", patterns: [/\bpatna\b/i, /पटना/i, /પટના/i, /\bbihar\b/i, /बिहार/i] },
  { city: "Surat", state: "Gujarat", fullName: "Surat, Gujarat", patterns: [/\bsurat\b/i, /सूरत/i, /સુરત/i] },
  { city: "Mumbai", state: "Maharashtra", fullName: "Mumbai, Maharashtra", patterns: [/\bmumbai\b/i, /\bbombay\b/i, /मुंबई/i, /बॉम्बे/i, /મુંબઈ/i] },
  { city: "Varanasi", state: "Uttar Pradesh", fullName: "Varanasi, Uttar Pradesh", patterns: [/\bvaranasi\b/i, /\bbanaras\b/i, /\bkashi\b/i, /वाराणसी/i, /बनारस/i, /काशी/i, /બનારસ/i] },
  { city: "Ahmedabad", state: "Gujarat", fullName: "Ahmedabad, Gujarat", patterns: [/\bahmedabad\b/i, /\bamdavad\b/i, /अहमदाबाद/i, /અમદાવાદ/i] },
  { city: "Pune", state: "Maharashtra", fullName: "Pune, Maharashtra", patterns: [/\bpune\b/i, /\bpoona\b/i, /पुणे/i, /પૂણે/i] },
  { city: "Delhi", state: "Delhi", fullName: "Delhi NCR, Delhi", patterns: [/\bdelhi\b/i, /\bnew delhi\b/i, /\bncr\b/i, /दिल्ली/i, /एनसीआर/i, /દિલ્હી/i] },
  { city: "Bengaluru", state: "Karnataka", fullName: "Bengaluru, Karnataka", patterns: [/\bbengaluru\b/i, /\bbangalore\b/i, /बेंगलुरु/i, /बैंगलोर/i, /બેંગલુરુ/i] },
  { city: "Ganjam", state: "Odisha", fullName: "Ganjam, Odisha", patterns: [/\bganjam\b/i, /\bodisha\b/i, /\borissa\b/i, /गंजम/i, /ओडिशा/i, /ઓડિશા/i] },
  { city: "Jaipur", state: "Rajasthan", fullName: "Jaipur, Rajasthan", patterns: [/\bjaipur\b/i, /\brajasthan\b/i, /जयपुर/i, /राजस्थान/i, /જયપુર/i] },
  { city: "Murshidabad", state: "West Bengal", fullName: "Murshidabad, West Bengal", patterns: [/\bmurshidabad\b/i, /\bmalda\b/i, /मुर्शिदाबाद/i, /মালদা/i, /મુર્શિદાબાદ/i] },
  { city: "Ranchi", state: "Jharkhand", fullName: "Ranchi, Jharkhand", patterns: [/\branchi\b/i, /\bjharkhand\b/i, /रांची/i, /झारखंड/i, /રાંચી/i] },
  { city: "Gorakhpur", state: "Uttar Pradesh", fullName: "Gorakhpur, Uttar Pradesh", patterns: [/\bgorakhpur\b/i, /गोरखपुर/i, /ગોરખપુર/i] },
  { city: "Nagpur", state: "Maharashtra", fullName: "Nagpur, Maharashtra", patterns: [/\bnagpur\b/i, /नागपुर/i, /નાગપુર/i] },
  { city: "Bhavnagar", state: "Gujarat", fullName: "Bhavnagar, Gujarat", patterns: [/\bbhavnagar\b/i, /भावनगर/i, /ભાવનગર/i] },
  { city: "Kolkata", state: "West Bengal", fullName: "Kolkata, West Bengal", patterns: [/\bkolkata\b/i, /\bcalcutta\b/i, /कोलकाता/i, /कलकत्ता/i, /কলকাতা/i] },
  { city: "Lucknow", state: "Uttar Pradesh", fullName: "Lucknow, Uttar Pradesh", patterns: [/\blucknow\b/i, /लखनऊ/i] },
  { city: "Kanpur", state: "Uttar Pradesh", fullName: "Kanpur, Uttar Pradesh", patterns: [/\bkanpur\b/i, /कानपुर/i] }
];

const SECTOR_RULES = [
  {
    sector: "Textile",
    patterns: [/\btextiles?\b/i, /\bcloth(?:ing)?\b/i, /\bkapd[aaeo]\b/i, /\bpowerlooms?\b/i, /\blooms?\b/i, /\bweav(?:er|ing)\b/i, /\bbunkar\b/i, /कपड़ा/i, /कपड़े/i, /कपड़ो/i, /टेक्सटाइल/i, /बुनकर/i, /हथकरघा/i, /કાપડ/i]
  },
  {
    sector: "Construction",
    patterns: [/\bconstruction\b/i, /\bnirman\b/i, /\bbuildings?\b/i, /\bmason\b/i, /\bmistr[iy]\b/i, /\bmazdoo?r\b/i, /\bmajoo?r\b/i, /\bbeldaar\b/i, /\bcement\b/i, /निर्माण/i, /कंस्ट्रक्शन/i, /मकान/i, /मिस्त्री/i, /मजदूर/i, /બાંધકામ/i]
  },
  {
    sector: "Diamond & Loom",
    patterns: [/\bdiamonds?\b/i, /\bheera\b/i, /\bhira\b/i, /\bratan\b/i, /\brathna\b/i, /\bpolishing\b/i, /\bghasai\b/i, /हीरा/i, /डायमंड/i, /घिसाई/i, /હીરા/i]
  },
  {
    sector: "Manufacturing",
    patterns: [/\bmanufacturing\b/i, /\bfactor(?:y|ies)\b/i, /\bkarkhana\b/i, /\bindustr(?:y|ial)\b/i, /\bplant\b/i, /\bfabrication\b/i, /विनिर्माण/i, /कारखाना/i, /फैक्ट्री/i, /ઉદ્યોગ/i]
  },
  {
    sector: "Garments",
    patterns: [/\bgarments?\b/i, /\bapparel\b/i, /\bsilai\b/i, /\btailor\b/i, /\bdarji\b/i, /परिधान/i, /सिलाई/i, /टेलर/i, /દરજી/i]
  },
  {
    sector: "Logistics",
    patterns: [/\blogistics?\b/i, /\btransport\b/i, /\bwarehouses?\b/i, /\bgodown\b/i, /\bdrivers?\b/i, /\bdelivery\b/i, /लॉजिस्टिक्स/i, /परिवहन/i, /गोदाम/i, /ड्राइवर/i]
  },
  {
    sector: "Hospitality",
    patterns: [/\bhotels?\b/i, /\brestaurants?\b/i, /\bcook\b/i, /\bchef\b/i, /\bwaiter\b/i, /\bdhaba\b/i, /होटल/i, /रसोई/i, /ढाबा/i]
  }
];

const PURPOSE_RULES = [
  {
    purpose: "Employment",
    patterns: [/\bka+m\b/i, /\bnaukri\b/i, /\bjobs?\b/i, /\bworks?\b/i, /\bemployment\b/i, /\bkamaa?ne\b/i, /\blabou?r\b/i, /\bkaary\b/i, /\brojga+r\b/i, /काम/i, /नौकरी/i, /जॉब/i, /रोजगार/i, /कार्य/i, /मजदूरी/i, /કામ/i, /રોજગાર/i]
  },
  {
    purpose: "Skill Placement",
    patterns: [/\bskills?\b/i, /\btraining\b/i, /\bplacements?\b/i, /\bprashikshan\b/i, /\bhunar\b/i, /कौशल/i, /प्रशिक्षण/i, /हुनर/i, /ट्रेनिंग/i, /પ્લેસમેન્ટ/i]
  },
  {
    purpose: "Family Relocation",
    patterns: [/\bfamil(?:y|ies)\b/i, /\bpariva+r\b/i, /\bshifting\b/i, /\brelocation\b/i, /\bbachh?e\b/i, /\bghar\b/i, /परिवार/i, /घर/i]
  }
];

function extractMigrationIntent(transcript) {
  state.currentTranscript = transcript;

  const foundLocations = [];
  KNOWN_LOCATIONS.forEach(loc => {
    for (const pat of loc.patterns) {
      const match = pat.exec(transcript);
      if (match) {
        foundLocations.push({
          city: loc.city,
          state: loc.state,
          fullName: loc.fullName,
          index: match.index,
          length: match[0].length
        });
        break;
      }
    }
  });

  foundLocations.sort((a, b) => a.index - b.index);

  let origin = "Not specified";
  let dest = "Not specified";
  let originState = "";
  let destState = "";

  if (foundLocations.length >= 2) {
    const between = transcript.substring(foundLocations[0].index + foundLocations[0].length, foundLocations[1].index);
    // In Hindi/Hinglish/Gujarati: [Origin] se [Destination] or [Origin]थी [Destination]
    if (/\b(?:se|thi|from)\b|से|थी|થી/i.test(between) || !/\b(?:to|me|mein)\b|में|मे|को/i.test(between)) {
      origin = foundLocations[0].fullName;
      originState = foundLocations[0].state;
      dest = foundLocations[1].fullName;
      destState = foundLocations[1].state;
    } else {
      dest = foundLocations[0].fullName;
      destState = foundLocations[0].state;
      origin = foundLocations[1].fullName;
      originState = foundLocations[1].state;
    }
  } else if (foundLocations.length === 1) {
    const after = transcript.substring(foundLocations[0].index + foundLocations[0].length);
    if (/\b(?:se|thi)\b|से|थी|થી/i.test(after)) {
      origin = foundLocations[0].fullName;
      originState = foundLocations[0].state;
    } else {
      dest = foundLocations[0].fullName;
      destState = foundLocations[0].state;
    }
  }

  // Sector extraction
  let sector = "Not specified";
  for (const rule of SECTOR_RULES) {
    if (rule.patterns.some(p => p.test(transcript))) {
      sector = rule.sector;
      break;
    }
  }

  // Purpose extraction
  let purpose = "Not specified";
  for (const rule of PURPOSE_RULES) {
    if (rule.patterns.some(p => p.test(transcript))) {
      purpose = rule.purpose;
      break;
    }
  }
  if (purpose === "Not specified" && sector !== "Not specified") {
    // If user specifies a work sector, infer Employment
    purpose = "Employment";
  }

  // Migration type calculation
  let type = "Inter-state";
  if (originState && destState) {
    type = (originState.toLowerCase() === destState.toLowerCase()) ? "Intra-state" : "Inter-state";
  }

  state.workerDraft = { origin, dest, purpose, sector, type };

  triggerAiPipelineSteps(() => {
    updateExtractedFields();
    showToast("Parameters Extracted", `${origin} → ${dest}`, "success");
  });
}

function processVoiceTranscript(transcript) {
  extractMigrationIntent(transcript);
}

function triggerAiPipelineSteps(onComplete) {
  const steps = [
    document.getElementById("stepListening"),
    document.getElementById("stepUnderstanding"),
    document.getElementById("stepProtecting"),
    document.getElementById("stepReady")
  ];

  let current = 0;
  function nextStep() {
    steps.forEach((s, idx) => {
      if (s) {
        s.classList.toggle("active", idx <= current);
      }
    });

    sound.playBeep(450 + current * 120, 0.08);
    current++;
    if (current < steps.length) {
      setTimeout(nextStep, 300);
    } else {
      if (onComplete) onComplete();
    }
  }

  nextStep();
}

function updateExtractedFields() {
  const elOrigin = document.getElementById("entityOrigin");
  const elDest = document.getElementById("entityDest");
  const elSector = document.getElementById("entitySector");
  const elPurpose = document.getElementById("entityPurpose");
  const elType = document.getElementById("entityType");

  if (elOrigin) elOrigin.value = state.workerDraft.origin;
  if (elDest) elDest.value = state.workerDraft.dest;
  if (elSector) elSector.value = state.workerDraft.sector;
  if (elPurpose) elPurpose.value = state.workerDraft.purpose;
  if (elType) elType.value = state.workerDraft.type;
}

// Submission state lock to prevent duplicate timeline insertions
let isSubmittingCheckin = false;
let lastSubmittedEventSig = null;

function recordWorkerCheckin() {
  if (isSubmittingCheckin) return; // Prevent concurrent rapid submissions

  if (state.consentStatus === "withdrawn") {
    showToast("Consent Required", "Please re-enable consent to submit voluntary migration event.", "warn");
    return;
  }

  // Read manual or extracted values from editable inputs
  const origin = document.getElementById("entityOrigin")?.value.trim() || state.workerDraft.origin;
  const dest = document.getElementById("entityDest")?.value.trim() || state.workerDraft.dest;
  const sector = document.getElementById("entitySector")?.value.trim() || state.workerDraft.sector;
  const purpose = document.getElementById("entityPurpose")?.value.trim() || state.workerDraft.purpose;
  const type = document.getElementById("entityType")?.value.trim() || state.workerDraft.type;

  // Guard against recording before speech processing completes
  if (origin.startsWith("Listening") || origin.startsWith("Processing") || origin.startsWith("Extracting")) {
    showToast("Processing Speech", "Please wait until speech parameter extraction completes.", "warn");
    return;
  }

  const currentEventSig = `${origin}::${dest}::${sector}::${purpose}::${type}`;

  // Prevent accidental duplicate insertion in the same submission cycle
  if (lastSubmittedEventSig === currentEventSig) {
    showToast("Already Recorded", "This voluntary migration event is already on your timeline.", "info");
    const tlSec = document.getElementById("timeline");
    if (tlSec) tlSec.scrollIntoView({ behavior: "smooth" });
    return;
  }

  isSubmittingCheckin = true;
  const btnConfirm = document.getElementById("btnConfirmCheckin");
  if (btnConfirm) {
    btnConfirm.disabled = true;
    btnConfirm.style.opacity = "0.7";
    btnConfirm.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Recording Event...';
  }

  const newEvent = {
    id: `evt-${Date.now().toString().slice(-4)}`,
    date: new Date().toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" }),
    origin,
    dest,
    purpose,
    sector,
    type,
    consent: "active"
  };

  // Prepend exactly ONE new event to timeline
  syntheticDataset.timeline.unshift(newEvent);
  syntheticDataset.kpis.totalEvents += 1;
  lastSubmittedEventSig = currentEventSig;

  // Re-render timeline and authority counters
  renderTimeline();
  renderAuthorityDashboard();

  showToast("Check-in Recorded", "Migration check-in recorded for this demonstration.", "success");
  setTimeout(() => {
    showToast("Prototype Demonstration", "Demonstration only — no government database was altered.", "info");
  }, 1200);

  // Cooldown before allowing next distinct submission
  setTimeout(() => {
    isSubmittingCheckin = false;
    if (btnConfirm) {
      btnConfirm.disabled = false;
      btnConfirm.style.opacity = "1";
      btnConfirm.innerHTML = '<i class="fa-solid fa-circle-check"></i> Event Recorded (Consent Active)';
    }
  }, 900);

  // Smooth jump to timeline
  const tlSec = document.getElementById("timeline");
  if (tlSec) tlSec.scrollIntoView({ behavior: "smooth" });
}

// =========================================================
// 10. CONSENT CENTER
// =========================================================

function initConsentCenter() {
  const btnGive = document.getElementById("btnGiveConsent");
  const btnReview = document.getElementById("btnReviewDataUse");
  const btnWithdraw = document.getElementById("btnWithdrawConsent");

  if (btnGive) {
    btnGive.addEventListener("click", () => {
      sound.playChime();
      state.consentStatus = "active";
      updateConsentBannerUI();
      showToast("Consent Active", "Voluntary migration event sharing is enabled for this session.", "success");
    });
  }

  if (btnReview) {
    btnReview.addEventListener("click", () => {
      sound.playClick();
      openModal("dataUseModal");
    });
  }

  if (btnWithdraw) {
    btnWithdraw.addEventListener("click", () => {
      sound.playWarning();
      openModal("withdrawConfirmModal");
    });
  }

  const btnConfirmWithdraw = document.getElementById("btnConfirmWithdrawAction");
  if (btnConfirmWithdraw) {
    btnConfirmWithdraw.addEventListener("click", () => {
      state.consentStatus = "withdrawn";
      updateConsentBannerUI();
      closeModal("withdrawConfirmModal");

      // Mark timeline events as withdrawn
      syntheticDataset.timeline.forEach(t => t.consent = "withdrawn");
      renderTimeline();

      showToast("Consent Withdrawn", "No migration event was shared. All voluntary tracking disabled.", "warn");
    });
  }
}

function updateConsentBannerUI() {
  const banner = document.getElementById("consentStatusBanner");
  const title = document.getElementById("csbTitle");
  const sub = document.getElementById("csbSub");
  const icon = document.getElementById("csbIcon");
  const dict = I18N[state.currentLang] || I18N.en;

  if (!banner) return;

  if (state.consentStatus === "active") {
    banner.classList.remove("withdrawn");
    if (title) title.textContent = dict.activeConsent;
    if (sub) sub.textContent = "Your migration event information is shared strictly for aggregated welfare intelligence.";
    if (icon) icon.className = "csb-icon fa-solid fa-circle-check";
  } else {
    banner.classList.add("withdrawn");
    if (title) title.textContent = dict.withdrawnConsent;
    if (sub) sub.textContent = "Consent is inactive. No migration events will be shared or stored in this demonstration.";
    if (icon) icon.className = "csb-icon fa-solid fa-circle-xmark";
  }
}

// =========================================================
// 11. TIMELINE RENDERER
// =========================================================

function renderTimeline() {
  const container = document.getElementById("timelineEventsList");
  if (!container) return;

  container.innerHTML = "";

  syntheticDataset.timeline.forEach(evt => {
    const card = document.createElement("div");
    card.className = "timeline-event-card";

    const isWithdrawn = evt.consent === "withdrawn" || state.consentStatus === "withdrawn";

    card.innerHTML = `
      <div class="timeline-node-dot ${isWithdrawn ? '' : 'verified'}"></div>
      <div class="tec-header">
        <div class="tec-route">
          <i class="fa-solid fa-route" style="color:var(--saffron);"></i>
          ${evt.origin} <i class="fa-solid fa-arrow-right-long" style="font-size:0.85rem; color:var(--text-muted);"></i> ${evt.dest}
        </div>
        <span class="tec-date"><i class="fa-regular fa-calendar"></i> ${evt.date}</span>
      </div>
      <div class="tec-meta-row">
        <span><i class="fa-solid fa-briefcase" style="color:var(--blue-light);"></i> Purpose: <strong>${evt.purpose}</strong></span>
        <span><i class="fa-solid fa-industry" style="color:var(--emerald-light);"></i> Sector: <strong>${evt.sector}</strong></span>
        <span><i class="fa-solid fa-shield-halved" style="color:${isWithdrawn ? 'var(--rose)' : 'var(--emerald)'};"></i> Status: <strong>${isWithdrawn ? 'Consent Withdrawn' : 'Consent Active'}</strong></span>
      </div>
    `;

    container.appendChild(card);
  });
}

// =========================================================
// 12. SVG MAP & CORRIDORS CONTROLLER
// =========================================================

function initSvgMapAndCorridors() {
  renderCorridorFilters();
  renderCorridorPills();
  renderCorridorDetailPanel(state.activeCorridor);
  drawSvgCorridors();
}

function renderCorridorFilters() {
  const filterState = document.getElementById("filterState");
  const filterSector = document.getElementById("filterSector");
  const filterType = document.getElementById("filterType");

  if (filterState) {
    filterState.addEventListener("change", (e) => {
      sound.playClick();
      state.filters.state = e.target.value;
      applyCorridorFilters();
    });
  }

  if (filterSector) {
    filterSector.addEventListener("change", (e) => {
      sound.playClick();
      state.filters.sector = e.target.value;
      applyCorridorFilters();
    });
  }

  if (filterType) {
    filterType.addEventListener("change", (e) => {
      sound.playClick();
      state.filters.type = e.target.value;
      applyCorridorFilters();
    });
  }
}

function applyCorridorFilters() {
  const filtered = syntheticDataset.corridors.filter(c => {
    const matchState = state.filters.state === "all" || c.originState.toLowerCase() === state.filters.state.toLowerCase() || c.destState.toLowerCase() === state.filters.state.toLowerCase();
    const matchSector = state.filters.sector === "all" || c.sector.toLowerCase().includes(state.filters.sector.toLowerCase());
    const matchType = state.filters.type === "all" || c.migrationType.toLowerCase() === state.filters.type.toLowerCase();
    return matchState && matchSector && matchType;
  });

  drawSvgCorridors(filtered);
  if (filtered.length > 0) {
    selectCorridor(filtered[0]);
  }
}

function renderCorridorPills() {
  const container = document.getElementById("heroCorridorPills");
  if (!container) return;

  container.innerHTML = "";
  syntheticDataset.corridors.slice(0, 5).forEach(c => {
    const pill = document.createElement("button");
    pill.className = `corridor-pill ${c.id === state.activeCorridor.id ? 'active' : ''}`;
    pill.innerHTML = `<i class="fa-solid fa-arrow-trend-up"></i> ${c.originState} → ${c.destState}`;
    pill.addEventListener("click", () => {
      sound.playClick();
      selectCorridor(c);
      // Smooth jump to map
      const mapEl = document.getElementById("intelligence");
      if (mapEl) mapEl.scrollIntoView({ behavior: "smooth" });
    });
    container.appendChild(pill);
  });
}

function selectCorridor(corridor) {
  state.activeCorridor = corridor;
  renderCorridorDetailPanel(corridor);
  highlightSvgCorridor(corridor.id);

  // Update pill active classes
  document.querySelectorAll(".corridor-pill").forEach(p => {
    if (p.textContent.includes(corridor.originState) && p.textContent.includes(corridor.destState)) {
      p.classList.add("active");
    } else {
      p.classList.remove("active");
    }
  });
}

function renderCorridorDetailPanel(corridor) {
  const panel = document.getElementById("corridorDetailPanel");
  if (!panel || !corridor) return;

  panel.innerHTML = `
    <div class="cdc-header">
      <span class="section-category"><i class="fa-solid fa-route"></i> SYNTHETIC DEMONSTRATION CORRIDOR</span>
      <h3 class="cdc-title">${corridor.originState.toUpperCase()} → ${corridor.destState.toUpperCase()}</h3>
      <span style="font-size:0.82rem; color:var(--text-secondary);">${corridor.originCity} to ${corridor.destCity} • ${corridor.migrationType}</span>
    </div>

    <div class="cdc-stats-grid">
      <div class="cdc-stat-box">
        <span class="csb-tag">MIGRATION EVENTS (DEMO)</span>
        <div class="csb-num">${corridor.events.toLocaleString()}</div>
      </div>
      <div class="cdc-stat-box">
        <span class="csb-tag">MOVEMENT TREND</span>
        <div class="csb-num" style="font-size:1.2rem; color:var(--emerald-light);">${corridor.trendText}</div>
      </div>
      <div class="cdc-stat-box">
        <span class="csb-tag">PRIMARY DESTINATION</span>
        <div class="csb-num" style="font-size:1.15rem; color:#fff;">${corridor.destCity}</div>
      </div>
      <div class="cdc-stat-box">
        <span class="csb-tag">COMMON SECTOR</span>
        <div class="csb-num" style="font-size:1.15rem; color:var(--blue-light);">${corridor.sector}</div>
      </div>
    </div>

    <div class="cdc-signal-box">
      <strong><i class="fa-solid fa-brain"></i> Planning Signal:</strong>
      <p style="margin-top:0.35rem;">${corridor.signal}</p>
    </div>

    <div style="font-size:0.75rem; color:var(--text-muted); text-align:center;">
      <i class="fa-solid fa-circle-info"></i> Generated from simulated, privacy-preserved voluntary check-ins.
    </div>
  `;
}

// Draw Curved Corridors on SVG
function drawSvgCorridors(corridorsList = syntheticDataset.corridors) {
  const svg = document.getElementById("indiaMapSvg");
  if (!svg) return;

  // City coordinate anchors relative to SVG viewBox (0 0 600 680)
  const coords = {
    "Patna": { x: 410, y: 310 },
    "Surat": { x: 200, y: 400 },
    "Varanasi": { x: 370, y: 320 },
    "Mumbai": { x: 210, y: 450 },
    "Ganjam": { x: 390, y: 440 },
    "Jaipur": { x: 230, y: 280 },
    "Ahmedabad": { x: 190, y: 360 },
    "Murshidabad": { x: 460, y: 350 },
    "Pune": { x: 230, y: 470 },
    "Ranchi": { x: 420, y: 360 },
    "Delhi": { x: 260, y: 240 }
  };

  const group = svg.getElementById("svgCorridorArcs");
  if (!group) return;

  group.innerHTML = "";

  corridorsList.forEach((c, i) => {
    const p1 = coords[c.originCity] || { x: 300, y: 300 };
    const p2 = coords[c.destCity] || { x: 250, y: 400 };

    // Quadratic curve control point
    const cx = (p1.x + p2.x) / 2 - 40;
    const cy = (p1.y + p2.y) / 2 - 50;

    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path.setAttribute("id", `arc-${c.id}`);
    path.setAttribute("d", `M ${p1.x} ${p1.y} Q ${cx} ${cy} ${p2.x} ${p2.y}`);
    path.setAttribute("fill", "none");
    path.setAttribute("stroke", c.id === state.activeCorridor.id ? "#f97316" : "rgba(96, 165, 250, 0.5)");
    path.setAttribute("stroke-width", c.id === state.activeCorridor.id ? "3.5" : "2");
    path.setAttribute("stroke-dasharray", "6 4");
    path.style.cursor = "pointer";

    path.addEventListener("click", () => {
      sound.playClick();
      selectCorridor(c);
    });

    group.appendChild(path);

    // End node pulse
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", p2.x);
    circle.setAttribute("cy", p2.y);
    circle.setAttribute("r", "5");
    circle.setAttribute("fill", "#10b981");
    group.appendChild(circle);
  });
}

function highlightSvgCorridor(corridorId) {
  const svg = document.getElementById("indiaMapSvg");
  if (!svg) return;

  syntheticDataset.corridors.forEach(c => {
    const el = svg.getElementById(`arc-${c.id}`);
    if (el) {
      if (c.id === corridorId) {
        el.setAttribute("stroke", "#f97316");
        el.setAttribute("stroke-width", "4");
      } else {
        el.setAttribute("stroke", "rgba(96, 165, 250, 0.4)");
        el.setAttribute("stroke-width", "2");
      }
    }
  });
}

// =========================================================
// 13. AUTHORITY COMMAND CENTER
// =========================================================

function renderAuthorityDashboard() {
  // Update KPI counters
  const elTotal = document.getElementById("kpiTotalEvents");
  const elActive = document.getElementById("kpiActiveCorridors");
  const elEmerging = document.getElementById("kpiEmergingCorridors");
  const elRegions = document.getElementById("kpiHighRegions");

  if (elTotal) elTotal.textContent = syntheticDataset.kpis.totalEvents.toLocaleString();
  if (elActive) elActive.textContent = syntheticDataset.kpis.activeCorridors;
  if (elEmerging) elEmerging.textContent = syntheticDataset.kpis.emergingCorridors;
  if (elRegions) elRegions.textContent = syntheticDataset.kpis.highActivityRegions;

  // Render Table of Corridors
  const tableBody = document.getElementById("commandCorridorsTableBody");
  if (tableBody) {
    tableBody.innerHTML = "";
    syntheticDataset.corridors.forEach(c => {
      const tr = document.createElement("tr");
      tr.style.cursor = "pointer";
      tr.innerHTML = `
        <td><strong>${c.originState} → ${c.destState}</strong></td>
        <td>${c.destCity}</td>
        <td><span style="background:rgba(255,255,255,0.06); padding:0.18rem 0.5rem; border-radius:4px;">${c.sector}</span></td>
        <td><strong>${c.events.toLocaleString()}</strong></td>
        <td><span style="color:var(--emerald-light); font-weight:700;">${c.trendText}</span></td>
      `;

      tr.addEventListener("click", () => {
        sound.playClick();
        selectCorridor(c);
        const mapEl = document.getElementById("intelligence");
        if (mapEl) mapEl.scrollIntoView({ behavior: "smooth" });
      });

      tableBody.appendChild(tr);
    });
  }

  // Render AI Planning Signals
  const signalsContainer = document.getElementById("aiSignalsList");
  if (signalsContainer) {
    signalsContainer.innerHTML = "";
    syntheticDataset.corridors.slice(0, 3).forEach(c => {
      const card = document.createElement("div");
      card.className = "ai-signal-card";
      card.innerHTML = `
        <div class="ais-tag"><i class="fa-solid fa-satellite-dish"></i> PROTOTYPE AI SIGNAL • SYNTHETIC DEMONSTRATION DATA</div>
        <div class="ais-text">${c.signal}</div>
        <div class="ais-action"><i class="fa-solid fa-list-check"></i> Potential Planning Action: Review destination-area welfare infrastructure capacity</div>
      `;
      signalsContainer.appendChild(card);
    });
  }

  // Initialize What-if Migration Scenario simulator
  initWhatIfScenario();
}

// =========================================================
// 13B. WHAT-IF MIGRATION SCENARIO SIMULATOR
// =========================================================

function initWhatIfScenario() {
  const slider = document.getElementById("whatIfVolumeSlider");
  if (!slider || slider.dataset.bound) return;
  slider.dataset.bound = "true";

  function updateScenario(val) {
    const volume = parseInt(val, 10);
    const elBadge = document.getElementById("whatIfVolumeBadge");
    const elPercent = document.getElementById("whatIfSurgePercent");
    const elActivity = document.getElementById("whatIfCorridorActivity");
    const elActBadge = document.getElementById("whatIfCorridorBadge");
    const elPressure = document.getElementById("whatIfPlanningPressure");
    const elPressBadge = document.getElementById("whatIfPressureBadge");
    const elCapacity = document.getElementById("whatIfServiceCapacity");
    const elCapBadge = document.getElementById("whatIfCapacityBadge");
    const elSignal = document.getElementById("whatIfEmergingSignal");
    const elSigBadge = document.getElementById("whatIfSignalBadge");
    const elRec = document.getElementById("whatIfRecommendationText");

    if (elBadge) elBadge.textContent = `${volume.toLocaleString()} workers`;

    const baseline = 4820;
    const surgeMultiplier = Math.round(((volume - baseline) / baseline) * 100);
    if (elPercent) elPercent.textContent = `+${Math.max(0, surgeMultiplier)}% Simulated Inflow`;

    if (volume < 18000) {
      // Lower volume: Low / Moderate
      if (elActivity) elActivity.textContent = "+15% to +30% Volume Drift";
      if (elActBadge) {
        elActBadge.textContent = "Low / Moderate";
        elActBadge.style.color = "var(--blue-light)";
        elActBadge.style.background = "rgba(96,165,250,0.12)";
      }
      if (elPressure) elPressure.textContent = "Normal Buffer Capacity";
      if (elPressBadge) {
        elPressBadge.textContent = "Low / Manageable";
        elPressBadge.style.color = "var(--emerald-light)";
        elPressBadge.style.background = "rgba(16,185,129,0.12)";
      }
      if (elCapacity) elCapacity.textContent = "Standard Transit Desks Sufficient";
      if (elCapBadge) {
        elCapBadge.textContent = "Standard Operations";
        elCapBadge.style.color = "var(--emerald-light)";
        elCapBadge.style.background = "rgba(16,185,129,0.12)";
      }
      if (elSignal) elSignal.textContent = "Bihar → Gujarat (Textile Cluster)";
      if (elSigBadge) {
        elSigBadge.textContent = "Steady Drift";
        elSigBadge.style.color = "#a78bfa";
        elSigBadge.style.background = "rgba(167,139,250,0.12)";
      }
      if (elRec) elRec.textContent = "Standard baseline monitoring is active. Consider reviewing service capacity along high-volume corridors if seasonal patterns align.";
    } else if (volume < 35000) {
      // Medium volume: Moderate / High
      if (elActivity) elActivity.textContent = "+45% to +65% High Inflow";
      if (elActBadge) {
        elActBadge.textContent = "Moderate / High";
        elActBadge.style.color = "var(--saffron)";
        elActBadge.style.background = "rgba(249,115,22,0.12)";
      }
      if (elPressure) elPressure.textContent = "Heightened Transit Hub Demand";
      if (elPressBadge) {
        elPressBadge.textContent = "Moderate / Escalating";
        elPressBadge.style.color = "var(--saffron)";
        elPressBadge.style.background = "rgba(249,115,22,0.12)";
      }
      if (elCapacity) elCapacity.textContent = "Prepare Buffer Desks & ONORC Counters";
      if (elCapBadge) {
        elCapBadge.textContent = "Advance Buffering";
        elCapBadge.style.color = "var(--saffron)";
        elCapBadge.style.background = "rgba(249,115,22,0.12)";
      }
      if (elSignal) elSignal.textContent = "UP → Maharashtra & Odisha → Gujarat";
      if (elSigBadge) {
        elSigBadge.textContent = "Emerging Surge";
        elSigBadge.style.color = "var(--saffron)";
        elSigBadge.style.background = "rgba(249,115,22,0.12)";
      }
      if (elRec) elRec.textContent = "Consider reviewing service capacity along high-volume corridors. Early inter-state notification memo recommended 2 weeks prior to projected arrival.";
    } else {
      // High volume: High / Critical
      if (elActivity) elActivity.textContent = "+85% to +130% Peak Surge";
      if (elActBadge) {
        elActBadge.textContent = "High / Critical";
        elActBadge.style.color = "var(--rose)";
        elActBadge.style.background = "rgba(244,63,94,0.12)";
      }
      if (elPressure) elPressure.textContent = "Critical Cluster Strain Expected";
      if (elPressBadge) {
        elPressBadge.textContent = "High / Critical";
        elPressBadge.style.color = "var(--rose)";
        elPressBadge.style.background = "rgba(244,63,94,0.12)";
      }
      if (elCapacity) elCapacity.textContent = "Activate Inter-State Coordination Protocol";
      if (elCapBadge) {
        elCapBadge.textContent = "Urgent Coordination";
        elCapBadge.style.color = "var(--rose)";
        elCapBadge.style.background = "rgba(244,63,94,0.12)";
      }
      if (elSignal) elSignal.textContent = "Multi-Corridor High Influx Across 4 States";
      if (elSigBadge) {
        elSigBadge.textContent = "Multi-Cluster Alert";
        elSigBadge.style.color = "var(--rose)";
        elSigBadge.style.background = "rgba(244,63,94,0.12)";
      }
      if (elRec) elRec.textContent = "High surge simulated. Advise coordinating between origin and destination labour commissioners to provision proactive transit welfare resources.";
    }
  }

  slider.addEventListener("input", (e) => {
    updateScenario(e.target.value);
  });

  slider.addEventListener("change", () => {
    sound.playClick();
  });

  updateScenario(slider.value);
}

// =========================================================
// 14. CORRIDOR FORECAST (TIME-SERIES CHART)
// =========================================================

function renderForecastChart() {
  const canvas = document.getElementById("forecastChartCanvas");
  if (!canvas) return;

  const selector = document.getElementById("forecastCorridorSelect");
  const ctx = canvas.getContext("2d");

  // Simple clean canvas renderer for zero external dependencies
  function drawChart() {
    canvas.width = canvas.parentElement.clientWidth || 600;
    canvas.height = 320;

    const w = canvas.width;
    const h = canvas.height;
    const pad = 45;

    ctx.clearRect(0, 0, w, h);

    const activeKey = selector ? selector.value : "all";
    const data = (syntheticDataset.forecastCorridors && syntheticDataset.forecastCorridors[activeKey]) || syntheticDataset.forecast;
    const maxVal = data.maxVal || 7000;
    const minVal = data.minVal || 2500;

    // Draw Grid
    ctx.strokeStyle = "rgba(255,255,255,0.08)";
    ctx.lineWidth = 1;
    for (let i = 0; i <= 4; i++) {
      const y = pad + (h - pad * 2) * (i / 4);
      ctx.beginPath();
      ctx.moveTo(pad, y);
      ctx.lineTo(w - pad, y);
      ctx.stroke();

      const labelVal = Math.round(maxVal - i * ((maxVal - minVal) / 4));
      ctx.fillStyle = "#64748b";
      ctx.font = "10px JetBrains Mono";
      ctx.fillText(labelVal, 10, y + 4);
    }

    const stepX = (w - pad * 2) / (data.labels.length - 1);

    // Labels
    data.labels.forEach((lbl, idx) => {
      const x = pad + idx * stepX;
      ctx.fillStyle = "#94a3b8";
      ctx.font = "10px Plus Jakarta Sans";
      ctx.textAlign = "center";
      ctx.fillText(lbl, x, h - 15);
    });

    // Draw Observed Line (Solid Blue)
    ctx.beginPath();
    ctx.strokeStyle = "#60a5fa";
    ctx.lineWidth = 3;
    let started = false;

    data.observed.forEach((val, idx) => {
      if (val !== null) {
        const x = pad + idx * stepX;
        const y = h - pad - ((val - minVal) / (maxVal - minVal)) * (h - pad * 2);
        if (!started) {
          ctx.moveTo(x, y);
          started = true;
        } else {
          ctx.lineTo(x, y);
        }
      }
    });
    ctx.stroke();

    // Draw Projected Line (Dashed Saffron)
    ctx.beginPath();
    ctx.strokeStyle = "#f97316";
    ctx.lineWidth = 3;
    ctx.setLineDash([6, 5]);
    let startedProj = false;

    data.projected.forEach((val, idx) => {
      if (val !== null) {
        const x = pad + idx * stepX;
        const y = h - pad - ((val - minVal) / (maxVal - minVal)) * (h - pad * 2);
        if (!startedProj) {
          ctx.moveTo(x, y);
          startedProj = true;
        } else {
          ctx.lineTo(x, y);
        }
      }
    });
    ctx.stroke();
    ctx.setLineDash([]); // Reset line dash
  }

  if (selector && !selector.dataset.bound) {
    selector.dataset.bound = "true";
    selector.addEventListener("change", () => {
      sound.playClick();
      drawChart();
      const selectedName = selector.options[selector.selectedIndex]?.text || "Corridor";
      showToast("Forecast Model Updated", `Projections loaded for: ${selectedName}`, "info");
    });
  }

  drawChart();
  window.addEventListener("resize", drawChart);
}

// =========================================================
// 15. GUIDED 2-MINUTE DEMO JOURNEY
// =========================================================

const demoSteps = [
  {
    step: 1,
    title: "1. Voluntary Worker Check-in",
    desc: "Ramesh, a textile worker moving from Patna (Bihar) to Surat (Gujarat), triggers a voluntary 30-second check-in via speech or simple form.",
    sectionTarget: "worker"
  },
  {
    step: 2,
    title: "2. Consent Verification & Privacy Notice",
    desc: "The system requests purpose-limited consent: 'Share this migration event strictly to improve destination welfare planning.' No continuous GPS is requested.",
    sectionTarget: "consent"
  },
  {
    step: 3,
    title: "3. AI Extracts Migration Event",
    desc: "Speech-to-Intent AI extracts minimum necessary parameters: Origin (Patna), Destination (Surat), Purpose (Employment), Sector (Textile).",
    sectionTarget: "worker"
  },
  {
    step: 4,
    title: "4. Privacy Layer Minimises & Disassociates Identity",
    desc: "Personal identities are separated. Only the sanitized migration event (Patna ➔ Surat, Textile) enters the cryptographic aggregation pipeline.",
    sectionTarget: "privacy"
  },
  {
    step: 5,
    title: "5. Migration Corridor Analytics Update",
    desc: "The synthetic Bihar ➔ Gujarat corridor increments by +1 event. Real-time corridor intensity reflects aggregate seasonal shifts.",
    sectionTarget: "intelligence"
  },
  {
    step: 6,
    title: "6. Authority Command Center Receives Planning Signal",
    desc: "State and central welfare planners see macro movement signals, enabling proactive allocation for grain, medical camps, and transit desks.",
    sectionTarget: "authority"
  },
  {
    step: 7,
    title: "7. Proactive Welfare Portability Decision",
    desc: "Authorities review capacity in Surat GIDC. 'From one consented migration event to better planning intelligence.'",
    sectionTarget: "forecast"
  }
];

function initDemoJourney() {
  const btnPrev = document.getElementById("btnDemoPrev");
  const btnNext = document.getElementById("btnDemoNext");
  const btnAuto = document.getElementById("btnDemoAutoPlay");

  renderDemoStep(1);

  if (btnPrev) {
    btnPrev.addEventListener("click", () => {
      sound.playClick();
      if (state.demoStep > 1) {
        state.demoStep--;
        renderDemoStep(state.demoStep);
      }
    });
  }

  if (btnNext) {
    btnNext.addEventListener("click", () => {
      sound.playClick();
      if (state.demoStep < demoSteps.length) {
        state.demoStep++;
        renderDemoStep(state.demoStep);
      }
    });
  }

  if (btnAuto) {
    btnAuto.addEventListener("click", () => {
      sound.playClick();
      if (state.demoAutoPlayTimer) {
        clearInterval(state.demoAutoPlayTimer);
        state.demoAutoPlayTimer = null;
        btnAuto.innerHTML = `<i class="fa-solid fa-play"></i> Auto-Play Demo`;
        showToast("Demo Paused", "Manual navigation restored.", "info");
      } else {
        btnAuto.innerHTML = `<i class="fa-solid fa-pause"></i> Pause Demo`;
        showToast("Auto-Play Demo Active", "Advancing through 7-step journey every 5 seconds...", "info");
        state.demoAutoPlayTimer = setInterval(() => {
          if (state.demoStep < demoSteps.length) {
            state.demoStep++;
          } else {
            state.demoStep = 1;
          }
          renderDemoStep(state.demoStep);
        }, 5000);
      }
    });
  }
}

function renderDemoStep(stepNum) {
  const stepData = demoSteps[stepNum - 1];
  if (!stepData) return;

  const elProgress = document.getElementById("demoProgressText");
  const elLabel = document.getElementById("demoStageLabel");
  const elTitle = document.getElementById("demoStageTitle");
  const elDesc = document.getElementById("demoStageDesc");

  if (elProgress) elProgress.textContent = `${stepNum} / ${demoSteps.length}`;
  if (elLabel) elLabel.textContent = `STEP ${stepNum} OF ${demoSteps.length} • GUIDED JUDGE JOURNEY`;
  if (elTitle) elTitle.textContent = stepData.title;
  if (elDesc) elDesc.textContent = stepData.desc;

  // Update step nodes
  for (let i = 1; i <= demoSteps.length; i++) {
    const node = document.getElementById(`demoNode${i}`);
    if (node) {
      node.classList.toggle("active", i === stepNum);
      node.classList.toggle("completed", i < stepNum);
    }
  }

  // Smoothly highlight corresponding section if wanted
  const targetSection = document.getElementById(stepData.sectionTarget);
  if (targetSection && stepNum > 1) {
    targetSection.classList.add("section-focus-glow");
    setTimeout(() => targetSection.classList.remove("section-focus-glow"), 1800);
  }
}

// =========================================================
// 16. MODAL & EVENT LISTENERS
// =========================================================

function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add("active");
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove("active");
  }
}

function initModalListeners() {
  document.addEventListener("click", (e) => {
    if (e.target.classList && e.target.classList.contains("modal-backdrop") && e.target.classList.contains("active")) {
      e.target.classList.remove("active");
    }
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      document.querySelectorAll(".modal-backdrop.active").forEach(m => m.classList.remove("active"));
    }
  });
}

// =========================================================
// 17. RESPONSIVE MOBILE NAVIGATION
// =========================================================

function initMobileNavigation() {
  const btnMobile = document.getElementById("btnMobileMenu");
  const navMenu = document.getElementById("navMenu");
  if (!btnMobile || !navMenu) return;

  btnMobile.addEventListener("click", (e) => {
    e.stopPropagation();
    const isOpen = navMenu.classList.toggle("open");
    btnMobile.innerHTML = isOpen ? '<i class="fa-solid fa-xmark"></i>' : '<i class="fa-solid fa-bars"></i>';
    btnMobile.setAttribute("aria-expanded", isOpen ? "true" : "false");
    btnMobile.setAttribute("aria-label", isOpen ? "Close navigation menu" : "Open navigation menu");
  });

  navMenu.querySelectorAll(".nav-item").forEach(link => {
    link.addEventListener("click", () => {
      navMenu.classList.remove("open");
      btnMobile.innerHTML = '<i class="fa-solid fa-bars"></i>';
      btnMobile.setAttribute("aria-expanded", "false");
      btnMobile.setAttribute("aria-label", "Open navigation menu");
    });
  });

  document.addEventListener("click", (e) => {
    if (!navMenu.contains(e.target) && !btnMobile.contains(e.target) && navMenu.classList.contains("open")) {
      navMenu.classList.remove("open");
      btnMobile.innerHTML = '<i class="fa-solid fa-bars"></i>';
      btnMobile.setAttribute("aria-expanded", "false");
      btnMobile.setAttribute("aria-label", "Open navigation menu");
    }
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && navMenu.classList.contains("open")) {
      navMenu.classList.remove("open");
      btnMobile.innerHTML = '<i class="fa-solid fa-bars"></i>';
      btnMobile.setAttribute("aria-expanded", "false");
      btnMobile.setAttribute("aria-label", "Open navigation menu");
    }
  });
}

