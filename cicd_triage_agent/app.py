import streamlit as st
import time

# Configure the page layout
st.set_page_config(page_title="CI/CD Agent Doctor", layout="wide")

st.title("🚀 AI CI/CD Smart Pipeline Doctor")
st.markdown("---")

# Layout Columns
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🛠️ Run Pipeline Analysis")
    scenario = st.selectbox(
        "Choose a Broken Pipeline Scenario:",
        ["Payment Gateway Timeout Error", "Package Dependency Version Conflict"]
    )
    
    if st.button("Run Diagnostic Agent", type="primary"):
        with st.spinner("Analyzing log errors via CascadeFlow..."):
            time.sleep(1.5)
            st.success("Analysis Complete!")

with col2:
    st.subheader("📊 Agent Diagnostics Scoreboard")
    # Quick metric display mockup
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Logs Analyzed", "12", "+2")
    m2.metric("Traditional Token Cost", "$0.18", "-85%")
    m3.metric("Cascade Flow Cost", "$0.01", "Optimal")
    
    st.info("Select a scenario on the left and trigger the agent to view isolated playbooks.")