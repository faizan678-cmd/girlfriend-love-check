import random
import streamlit as st

st.set_page_config(page_title="She Loves Me?", page_icon="🌸", layout="centered")

st.markdown("""
<style>
    .main { background-color: #1a1a2e; }
    .stApp { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); }

    .title-text {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #ff6b9d, #ff8e53, #ff6b9d);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .subtitle-text {
        text-align: center;
        color: #a0a0c0;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .result-box {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        backdrop-filter: blur(10px);
        margin: 1.5rem 0;
    }
    .result-name {
        font-size: 1.6rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    .result-outcome {
        font-size: 1.3rem;
        font-weight: 500;
        margin-top: 0.5rem;
    }
    .loves { color: #ff6b9d; }
    .not-loves { color: #ff4444; }
    .likes { color: #56d4ff; }
    .hates { color: #ff4444; }
    .petals { font-size: 2.5rem; margin-bottom: 0.5rem; letter-spacing: 6px; }

    .history-item {
        background: rgba(255,255,255,0.04);
        border-radius: 10px;
        padding: 0.6rem 1rem;
        margin-bottom: 0.5rem;
        display: flex;
        justify-content: space-between;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #ff6b9d, #ff8e53);
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.7rem 1.5rem;
        transition: opacity 0.2s;
        cursor: pointer;
    }
    .stButton > button:hover { opacity: 0.85; }
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 10px !important;
        color: white !important;
        font-size: 1.1rem !important;
        padding: 0.6rem 1rem !important;
    }
</style>
""", unsafe_allow_html=True)

outcomes = [
    {"text": "loves you 💖",        "cls": "loves",     "petals": "🌸🌸🌸🌸🌸"},
    {"text": "does NOT love you 💔", "cls": "not-loves", "petals": "🥀🥀🥀🥀🥀"},
    {"text": "likes you 😊",         "cls": "likes",     "petals": "🌼🌼🌼🌼🌼"},
    {"text": "hates you 😤",         "cls": "hates",     "petals": "🥀😤🥀😤🥀"},
    {"text": "bhai teri kismat mai ye ladki nhi hn ,dusri dund 🥀",         "cls": "kismat",     "petals": "🥀😤😤🥀"},
    {"text": "skal dekhi  apni (ladki ke dimag mai yehi feelings hn tere liye) 😤",         "cls": "sakal",     "petals": "🥀😤🥀"},
]

if "history" not in st.session_state:
    st.session_state.history = []
if "result" not in st.session_state:
    st.session_state.result = None

st.markdown('<p class="title-text">check She Loves u…?by faizu 🌸</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Enter a name and let fate decide</p>', unsafe_allow_html=True)

name = st.text_input("", placeholder="Girlfriend ka naam to dal chutiye .", label_visibility="collapsed")

if st.button("🌸 Ask the flower"):
    if name.strip():
        pick = random.choice(outcomes)
        st.session_state.result = {"name": name.strip(), **pick}
        st.session_state.history.insert(0, {"name": name.strip(), **pick})
        if len(st.session_state.history) > 5:
            st.session_state.history.pop()
    else:
        st.warning("Pehle naam toh dalo! 😅")

if st.session_state.result:
    r = st.session_state.result
    st.markdown(f"""
    <div class="result-box">
        <div class="petals">{r['petals']}</div>
        <div class="result-name">{r['name']}</div>
        <div class="result-outcome {r['cls']}">{r['text']}</div>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.history:
    st.markdown("---")
    st.markdown("#### 📜 Recent readings")
    for h in st.session_state.history:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write(f"**{h['name']}**")
        with col2:
            st.write(h['text'])

    if st.button("🗑️chal chutiye Clear history kr ,warna faizan dekh lega"):
        st.session_state.history = []
        st.session_state.result = None
        st.rerun()
