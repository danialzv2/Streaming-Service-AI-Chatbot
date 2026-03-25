import streamlit as st
from src.rag.e_explanation_service import ask_tonton

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Tonton AI",
    layout="wide"
)

# =========================
# CUSTOM CSS (from your CSS)
# =========================
st.markdown("""
<style>
body {
    background-color: #0a0a0a;
    color: #F0F0F0;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    padding-top: 2rem;
}

/* Chat bubbles */
.user-bubble {
    background-color: #222;
    padding: 10px;
    border-radius: 10px;
    text-align: right;
    margin-bottom: 10px;
}

.bot-bubble {
    background-color: #181818;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}

/* Suggestions */
.sug-btn {
    background-color: #181818;
    color: #F0F0F0;
    padding: 6px 12px;
    border-radius: 8px;
    margin: 4px;
    border: none;
}

/* Sidebar */
.sidebar-title {
    font-size: 20px;
    color: #E50914;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE (your JS memory replacement)
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "is_loading" not in st.session_state:
    st.session_state.is_loading = False

# =========================
# SIDEBAR (your sidebar)
# =========================
with st.sidebar:
    st.markdown('<div class="sidebar-title">TONTON AI</div>', unsafe_allow_html=True)

    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("### Suggestions")

    suggestions = [
        "🔥 Iklan Untuk Langganan Premium",
        "🎬 Cerita Mengenai Pembelajaran",
        "❓ Masalah Tidak Boleh Tonton Selepas Pembayaran"
    ]

    for sug in suggestions:
        if st.button(sug):
            st.session_state.messages.append({
                "role": "user",
                "content": sug
            })
            st.rerun()

# =========================
# MAIN HEADER (your welcome)
# =========================
if len(st.session_state.messages) == 0:
    st.markdown("""
    <h1 style="text-align:center;">TONTON <span style="color:#E50914;">AI</span></h1>
    <p style="text-align:center; color:#888;">
    I'm your AI Agent ready to help regarding Tonton.
    </p>
    """, unsafe_allow_html=True)

# =========================
# DISPLAY MESSAGES (your appendMessage)
# =========================
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

# =========================
# INPUT (your sendMessage)
# =========================
user_input = st.chat_input("Ask something...")

if user_input and not st.session_state.is_loading:

    st.session_state.is_loading = True

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message immediately
    st.markdown(f'<div class="user-bubble">{user_input}</div>', unsafe_allow_html=True)

    # Bot response (typing simulation)
    with st.spinner("Thinking..."):
        try:
            response = ask_tonton(user_input)
        except Exception:
            response = "⚠️ Error connecting to backend"

    # Add bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.markdown(f'<div class="bot-bubble">{response}</div>', unsafe_allow_html=True)

    st.session_state.is_loading = False

# =========================
# AUTO SCROLL (Streamlit limitation workaround)
# =========================
st.write("")