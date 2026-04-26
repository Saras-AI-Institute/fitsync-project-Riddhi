import streamlit as st

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(layout="wide", page_title="FitSync", page_icon="💪")

# ── Dark Mode Toggle ───────────────────────────────────────────────────────────
if "theme" not in st.session_state:
    st.session_state.theme = "light"

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

is_dark = st.session_state.theme == "dark"

# ── Theme Variables ────────────────────────────────────────────────────────────
bg_main      = "#0d1117" if is_dark else "#f5f7fa"
bg_surface   = "#161b22" if is_dark else "#ffffff"
bg_card      = "#1e2a38" if is_dark else "#e8f4f1"
border_color = "#30363d" if is_dark else "#b2dfdb"
text_primary = "#e6edf3" if is_dark else "#1a1a2e"
text_muted   = "#8b949e" if is_dark else "#546e7a"
teal_main    = "#00bfa5"
teal_dark    = "#007c91"
accent_border= "#00bfa5"
nav_hover_bg = "#1e2a38" if is_dark else "#e0f7f4"
active_bg    = "#1e2a38" if is_dark else "#e0f7f4"

# ── Global CSS — overrides ALL Streamlit elements ──────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@600;700&display=swap');

/* ── Root app background ── */
html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > section,
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
.main .block-container,
.stMainBlockContainer {{
    background-color: {bg_main} !important;
    color: {text_primary} !important;
    font-family: 'Inter', sans-serif;
    transition: background-color 0.3s ease, color 0.3s ease;
}}

/* ── Default text color for everything ── */
[data-testid="stApp"] p,
[data-testid="stApp"] span,
[data-testid="stApp"] label,
[data-testid="stApp"] li,
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] span {{
    color: {text_primary} !important;
}}

/* ── Headings ── */
[data-testid="stApp"] h1,
[data-testid="stApp"] h2,
[data-testid="stApp"] h3,
[data-testid="stApp"] h4 {{
    font-family: 'Poppins', sans-serif !important;
    color: {teal_main} !important;
}}

/* ══════════════════════════════════════════
   SIDEBAR — every layer overridden
══════════════════════════════════════════ */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div,
[data-testid="stSidebar"] > div > div,
[data-testid="stSidebarContent"],
[data-testid="stSidebarUserContent"],
section[data-testid="stSidebar"] {{
    background-color: {bg_surface} !important;
    border-right: 1px solid {border_color} !important;
}}

/* All sidebar text */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] a,
[data-testid="stSidebar"] li,
[data-testid="stSidebar"] label,
[data-testid="stSidebarContent"] * {{
    color: {text_primary} !important;
    background-color: transparent !important;
}}

/* ── Sidebar nav links (pages) ── */
[data-testid="stSidebarNav"],
[data-testid="stSidebarNav"] ul,
[data-testid="stSidebarNav"] li,
[data-testid="stSidebarNavItems"],
[data-testid="stSidebarNavItems"] ul,
[data-testid="stSidebarNavItems"] li {{
    background-color: {bg_surface} !important;
}}

[data-testid="stSidebarNavLink"],
[data-testid="stSidebarNavItems"] a,
[data-testid="stSidebarNavItems"] li a {{
    background-color: transparent !important;
    color: {text_primary} !important;
    border-radius: 8px;
    transition: background-color 0.2s;
}}

[data-testid="stSidebarNavLink"] span,
[data-testid="stSidebarNavItems"] a span,
[data-testid="stSidebarNavItems"] li a span {{
    color: {text_primary} !important;
    font-weight: 500;
    font-size: 0.95em;
}}

/* Active page nav link */
[data-testid="stSidebarNavLink"][aria-current="page"],
[data-testid="stSidebarNavLink"][aria-selected="true"] {{
    background-color: {active_bg} !important;
}}
[data-testid="stSidebarNavLink"][aria-current="page"] span,
[data-testid="stSidebarNavLink"][aria-selected="true"] span {{
    color: {teal_main} !important;
    font-weight: 700;
}}

/* Hover on nav links */
[data-testid="stSidebarNavLink"]:hover {{
    background-color: {nav_hover_bg} !important;
}}
[data-testid="stSidebarNavLink"]:hover span {{
    color: {teal_main} !important;
}}

/* ── Page header / toolbar ── */
[data-testid="stHeader"],
[data-testid="stDecoration"],
[data-testid="stToolbar"],
.stToolbar {{
    background-color: {bg_main} !important;
}}
[data-testid="stHeader"] *,
[data-testid="stToolbar"] * {{
    color: {text_primary} !important;
}}

/* ── Buttons ── */
.stButton > button {{
    background-color: {teal_main} !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 10px 28px !important;
    font-size: 1em !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: transform 0.2s, background-color 0.2s !important;
}}
.stButton > button:hover {{
    transform: scale(1.05) !important;
    background-color: {teal_dark} !important;
    color: white !important;
}}

/* ── Section title class ── */
.section-title {{
    font-size: 1.8em;
    font-weight: 700;
    color: {teal_main} !important;
    border-bottom: 2px solid {teal_main};
    padding-bottom: 8px;
    margin-bottom: 24px;
    font-family: 'Poppins', sans-serif;
}}

/* ── Hide Streamlit branding ── */
#MainMenu, footer, header {{ visibility: hidden; }}

/* ── Block container top padding ── */
.block-container {{
    padding-top: 2rem !important;
}}

/* ── Scrollbar ── */
::-webkit-scrollbar {{ width: 6px; }}
::-webkit-scrollbar-track {{ background: {bg_main}; }}
::-webkit-scrollbar-thumb {{ background: {border_color}; border-radius: 3px; }}
</style>
""", unsafe_allow_html=True)

# ── Sidebar Content ────────────────────────────────────────────────────────────
st.sidebar.markdown(f"""
<div style="text-align:center;padding:20px 0 28px;">
  <div style="font-size:3em;">💪</div>
  <h2 style="color:#00bfa5 !important;margin:10px 0 4px;font-family:'Poppins',sans-serif;">FitSync</h2>
  <p style="color:{text_muted} !important;font-size:0.85em;margin:0;">Health Analytics</p>
</div>
<hr style="border:1px solid {border_color};margin-bottom:16px;">
""", unsafe_allow_html=True)

# ── Top Bar: Theme Toggle ──────────────────────────────────────────────────────
col_spacer, col_btn = st.columns([10, 1])
with col_btn:
    label = "🌙 Dark" if not is_dark else "☀️ Light"
    st.button(label, on_click=toggle_theme)

# ── Hero Section ───────────────────────────────────────────────────────────────
col_left, col_right = st.columns([1, 2])

with col_left:
    st.markdown("""
    <div style="display:flex;justify-content:center;align-items:center;height:260px;">
      <svg width="150" height="150" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <path d="M50 85 C20 65 5 45 5 30 C5 15 17 5 30 5 C38 5 46 10 50 17 C54 10 62 5 70 5 C83 5 95 15 95 30 C95 45 80 65 50 85Z" fill="#00bfa5">
          <animateTransform attributeName="transform" type="scale" values="1;1.1;1" dur="1.2s" repeatCount="indefinite" additive="sum" origin="50 50"/>
        </path>
        <circle cx="50" cy="50" r="48" fill="none" stroke="#00bfa5" stroke-width="1.5" opacity="0.3">
          <animate attributeName="r" values="48;60;48" dur="1.2s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="0.3;0;0.3" dur="1.2s" repeatCount="indefinite"/>
        </circle>
      </svg>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown(f"""
    <div style="padding:40px 0 24px;text-align:left;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <span style="font-size:2em;">🌿</span>
        <h1 style="font-family:'Poppins',sans-serif;font-size:2.6em;color:#00bfa5 !important;
                   margin:0;border-bottom:3px solid #00bfa5;padding-bottom:8px;">
          Welcome to FitSync
        </h1>
      </div>
      <p style="font-size:1.25em;font-weight:600;color:{text_primary} !important;
                margin:20px 0 10px;font-family:'Poppins',sans-serif;">
        Your AI-powered Personal Health Analytics Dashboard
      </p>
      <p style="font-size:1.05em;color:#00bfa5 !important;font-style:italic;margin-bottom:28px;">
        "Track. Analyze. Thrive."
      </p>
    </div>
    """, unsafe_allow_html=True)
    st.button("🚀 Get Started →")

# ── Divider ────────────────────────────────────────────────────────────────────
st.markdown(f"<hr style='border:1px solid {border_color};margin:32px 0;'>", unsafe_allow_html=True)

# ── 3 Metric Cards ─────────────────────────────────────────────────────────────
c1, c2, c3 = st.columns(3)
cards = [
    ("📊", "Dashboard", "Your health metrics at a glance"),
    ("🔍", "Trends & Insights", "Dive deep into your data over time"),
    ("⚙️", "Settings", "Personalize your FitSync experience"),
]
for col, (icon, title, desc) in zip([c1, c2, c3], cards):
    with col:
        st.markdown(f"""
        <div style="background:{bg_card};border:1.5px solid {accent_border};border-radius:18px;
                    padding:28px;text-align:center;transition:transform 0.2s;">
          <div style="font-size:3em;margin-bottom:14px;">{icon}</div>
          <h3 style="color:#00bfa5 !important;margin:0 0 8px;font-family:'Poppins',sans-serif;">{title}</h3>
          <p style="color:{text_muted} !important;font-size:0.95em;margin:0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ── Getting Started Section ────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f'<p class="section-title">🚀 Getting Started</p>', unsafe_allow_html=True)

steps = [
    ("1", "Open Dashboard", "Navigate to the Dashboard from the sidebar to see your daily health summary."),
    ("2", "Explore Trends", "Visit Trends & Insights to identify patterns and track your progress over time."),
    ("3", "Tune Settings", "Go to Settings to customize preferences and make FitSync truly yours."),
]
steps_html = f'<div style="display:flex;gap:20px;margin:16px 0 40px;flex-wrap:wrap;">'
for num, title, desc in steps:
    steps_html += f"""
    <div style="flex:1;min-width:180px;background:{bg_surface};border-radius:16px;padding:24px;
                border:1px solid {border_color};text-align:center;">
      <div style="width:52px;height:52px;border-radius:50%;background:#00bfa5;color:white;
                  font-size:1.5em;font-weight:700;display:flex;align-items:center;
                  justify-content:center;margin:0 auto 16px;">{num}</div>
      <h4 style="color:{text_primary} !important;margin:0 0 8px;font-family:'Poppins',sans-serif;">{title}</h4>
      <p style="color:{text_muted} !important;font-size:0.9em;margin:0;">{desc}</p>
    </div>"""
steps_html += "</div>"
st.markdown(steps_html, unsafe_allow_html=True)

# ── Motivational Quote Banner ──────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#00bfa5,#007c91);border-radius:16px;
            padding:28px 40px;margin:16px 0 40px;text-align:center;">
  <p style="font-size:1.3em;color:white !important;font-style:italic;margin:0 0 8px;">
    "Take care of your body. It's the only place you have to live."
  </p>
  <p style="color:rgba(255,255,255,0.8) !important;font-size:0.95em;margin:0;">— Jim Rohn</p>
</div>
""", unsafe_allow_html=True)

# ── Why FitSync Section ────────────────────────────────────────────────────────
st.markdown(f'<p class="section-title">✨ Why FitSync?</p>', unsafe_allow_html=True)

features = [
    ("🎯 Goal Tracking", "Set and monitor your personal health goals with clarity and ease."),
    ("📈 Smart Analytics", "AI-powered insights that adapt to your unique health data."),
    ("🔔 Daily Reminders", "Stay consistent with personalized health nudges every day."),
    ("🔒 Private & Secure", "Your health data stays yours — always encrypted and safe."),
]
feat_html = f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:40px;">'
for title, desc in features:
    feat_html += f"""
    <div style="background:{bg_surface};border-radius:14px;padding:22px;
                border-left:4px solid #00bfa5;border-top:1px solid {border_color};
                border-right:1px solid {border_color};border-bottom:1px solid {border_color};">
      <h4 style="color:#00bfa5 !important;margin:0 0 8px;font-family:'Poppins',sans-serif;">{title}</h4>
      <p style="color:{text_muted} !important;font-size:0.9em;margin:0;">{desc}</p>
    </div>"""
feat_html += "</div>"
st.markdown(feat_html, unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="text-align:center;padding:40px 0 16px;color:{text_muted} !important;
            font-size:0.85em;border-top:1px solid {border_color};margin-top:48px;">
  Made with ❤️ by the FitSync Team &nbsp;·&nbsp; © 2025 FitSync &nbsp;·&nbsp; All rights reserved
</div>
""", unsafe_allow_html=True)