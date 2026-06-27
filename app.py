import streamlit as st
from crew import blog
import time

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI YouTube Blog Generator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.main-title{
    font-size:50px;
    font-weight:800;
    text-align:center;
    color:#4F8BF9;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:grey;
    margin-bottom:30px;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    background:#4F8BF9;
    color:white;
    font-size:20px;
    font-weight:bold;
}

.stDownloadButton>button{
    width:100%;
    border-radius:12px;
}

.agent-card{
    padding:15px;
    border-radius:12px;
    background:#262730;
    color:white;
    margin-bottom:15px;
}

.metric{
    font-size:18px;
    font-weight:bold;
    color:#4F8BF9;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🤖 CrewAI Dashboard")

    st.markdown("---")

    st.markdown("### 👨‍💻 Active Agents")

    st.success("🔍 Research Agent")
    st.success("✍ Blog Writer")

    st.markdown("---")

    st.markdown("### ⚙ Configuration")

    st.info("LLM : Groq GPT OSS 20B")

    st.info("Execution : Sequential")

    st.info("Memory : Disabled")

    st.info("Cache : Disabled")

    st.markdown("---")

    st.markdown("### 📈 Features")

    st.write("✅ Dynamic YouTube Channel")

    st.write("✅ AI Research")

    st.write("✅ Blog Generation")

    st.write("✅ Markdown Export")

# -----------------------------
# Header
# -----------------------------

st.markdown(
    """
<div class="main-title">
🤖 AI YouTube Blog Generator
</div>

<div class="subtitle">
Generate high-quality blogs from ANY YouTube channel using CrewAI Agents
</div>
""",
unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Input Section
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    channel = st.text_input(
        "📺 YouTube Channel URL",
        placeholder="https://www.youtube.com/@DarshilParmar"
    )

with col2:

    topic = st.text_input(
        "📝 Blog Topic",
        placeholder="LangGraph"
    )

st.divider()

# -----------------------------
# Generate Button
# -----------------------------

if st.button("🚀 Generate Blog"):

    if channel == "" or topic == "":

        st.warning("Please fill all the fields.")

    else:

        progress = st.progress(0)

        status = st.empty()

        status.info("🔍 Research Agent is searching YouTube...")

        progress.progress(20)

        time.sleep(0.5)

        status.info("📺 Extracting video insights...")

        progress.progress(45)

        time.sleep(0.5)

        status.info("🧠 AI is understanding the content...")

        progress.progress(70)

        result = blog(channel, topic)

        progress.progress(100)

        status.success("✅ Blog Generated Successfully!")

        st.balloons()

        st.divider()

        st.subheader("📄 Generated Blog")

        st.markdown(result)

        st.download_button(
            "📥 Download Markdown",
            result,
            file_name=f"{topic}.md",
            mime="text/markdown"
        )