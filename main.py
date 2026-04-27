import streamlit as st

# PAGE CONFIG
st.set_page_config(layout="wide", page_title="FitSync", page_icon="💪")

# ── GLOBAL CSS ─────────────────────────────────────────────────────────────────
st.markdown(
    '''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400&family=Poppins:wght@600&display=swap');
    body { background-color: #0d1117; color: #e6edf3; font-family: 'Inter', sans-serif; }
    h1, h2, h3 { font-family: 'Poppins', sans-serif; color: #00bfa5; }
    .stSidebar { background-color: #161b22; border-right: 1px solid #30363d; }
    footer { display: none; }
    .stButton > button { background-color: #00bfa5; color: white; border-radius: 12px; padding: 10px 28px; font-size: 1em; border: none; cursor: pointer; transition: transform 0.2s; }
    .stButton > button:hover { transform: scale(1.05); background-color: #007c91; }
    .card { background-color: #161b22; border: 1px solid #00bfa5; border-radius: 16px; padding: 24px; text-align: center; }
    .section-title { font-size: 1.8em; font-weight: 700; color: #00bfa5; border-bottom: 2px solid #00bfa5; padding-bottom: 8px; margin-bottom: 24px; }
    html { scroll-behavior: smooth; }
    </style>
    ''', unsafe_allow_html=True
)

# ── Sidebar Content ────────────────────────────────────────────────────────────
st.sidebar.markdown(
    '''
    <div>
        <h1>💪 FitSync</h1>
        <p>Health Analytics</p>
    </div>
    ''', unsafe_allow_html=True
)

# ── HERO SECTION - Align message to the left ───────────────────────────────────

# To adjust the spacing of the "Get Started" button

# HERO SECTION
left_col, right_col = st.columns([2, 1])

left_col.markdown(
    '''<div style="text-align: left;">
        <h1>🌿 Welcome to FitSync</h1>
        <p>Your AI-powered Personal Health Analytics Dashboard</p>
        <i>"Track. Analyze. Thrive."</i>
        <!-- Removed the button here -->
    </div>''', unsafe_allow_html=True
)

right_col.markdown(
    '''
    <!-- Insert animated SVG heart here -->
    ''', unsafe_allow_html=True
)

# ── Divider ────────────────────────────────────────────────────────────────────
st.markdown("""<hr style='background-color: #30363d; border: none; height: 1px;'/>""", unsafe_allow_html=True)

# ── 3 Metric Cards ─────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.markdown(
    '''
    <div class="card">
        <h1>📊 Dashboard</h1>
        <p>Your health metrics at a glance</p>
    </div>
    ''', unsafe_allow_html=True
)
col2.markdown(
    '''
    <div class="card">
        <h1>🔍 Trends & Insights</h1>
        <p>Dive deep into your data over time</p>
    </div>
    ''', unsafe_allow_html=True
)
col3.markdown(
    '''
    <div class="card">
        <h1>⚙️ Settings</h1>
        <p>Personalize your FitSync experience</p>
    </div>
    ''', unsafe_allow_html=True
)

# ── Getting Started Section ────────────────────────────────────────────────────
st.markdown('<div class="section-title">🚀 Getting Started</div>', unsafe_allow_html=True)
st.markdown('''<!-- Insert HTML stepper here -->''', unsafe_allow_html=True)

# ── Motivational Quote Banner ──────────────────────────────────────────────────
st.markdown('''
<blockquote>
    "Take care of your body. It's the only place you have to live."<br>
    &mdash; Jim Rohn
</blockquote>
''', unsafe_allow_html=True)

# ── Why FitSync Section ────────────────────────────────────────────────────────
st.markdown('<div class="section-title">✨ Why FitSync?</div>', unsafe_allow_html=True)
feat_col1, feat_col2 = st.columns(2)
feat_col1.markdown(
    '''
    <div class="card">
        <h1>🎯 Goal Tracking</h1>
        <p>Set and track your personal health goals with ease.</p>
    </div>
    <div class="card">
        <h1>📈 Smart Analytics</h1>
        <p>AI-powered insights that adapt to your unique data.</p>
    </div>
    ''', unsafe_allow_html=True
)

feat_col2.markdown(
    '''
    <div class="card">
        <h1>🔔 Daily Reminders</h1>
        <p>Stay on track with personalized health nudges.</p>
    </div>
    <div class="card">
        <h1>🔒 Private & Secure</h1>
        <p>Your health data stays yours — always encrypted.</p>
    </div>
    ''', unsafe_allow_html=True
)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown(
    '''
    <footer>
        <p>Made with ❤️ by the FitSync Team  ·  © 2025 FitSync  ·  All rights reserved</p>
    </footer>
    ''', unsafe_allow_html=True
)

