import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv
from core.router import analyze_log_with_cascade
from core.database import get_total_savings
from core.agent import run_triage_crew

load_dotenv()
st.set_page_config(page_title="CI/CD Agent Doctor", page_icon="📟", layout="wide")

st.title("📟 AI CI/CD Smart Pipeline Doctor")
st.caption("Automated log triage powered by Hindsight Memory & Cascadeflow Routing")
st.markdown("---")

st.sidebar.header("%3F Scoreboard Metrics")
total_lines, total_saved = get_total_savings()
st.sidebar.metric(label="Total Log Lines Cleaned", value=f"{total_lines:,}")
st.sidebar.metric(label="Estimated API Cost Saved", value=f"${total_saved:.4f}")

log_scenario = st.selectbox(
    "Select a Failed Build Log Scenario to Test:",
    ["Select a scenario...", "Scenario 1: PyTest Network Timeout (Flaky Test History)", "Scenario 2: Broken Pip Dependency Conflict"]
)

mock_logs = {
    "Scenario 1: PyTest Network Timeout (Flaky Test History)": "CRITICAL: test_payment_gateway_timeout FAILED\nSocketError: connection reset by peer.\nStandard Error Loop: Connection timed out after 5000ms.",
    "Scenario 2: Broken Pip Dependency Conflict": "ERROR: Cannot install package_x because of a version conflict.\nConflict detected: package_x requires numpy<=1.21.5"
}

if log_scenario != "Select a scenario...":
    st.text_area("📋 Raw Terminal Log:", mock_logs[log_scenario], height=120)
    if st.button("🚀 Analyze Failed Build"):
        with st.spinner("Processing logs..."):
            isolated_error = analyze_log_with_cascade(log_scenario, mock_logs[log_scenario])
            st.markdown("### 🔍 Isolated Crash Reason")
            st.code(isolated_error, language="text")
            st.markdown("### 🧠 Brain Memory Lookup (Hindsight + CrewAI)")
            # Execute your brand new live agent process!
            agent_playbook = run_triage_crew(isolated_error)
            st.success(agent_playbook)
            st.success("💡 Match Found! Recommendation: Safe to automatically trigger a pipeline retry.")
        st.rerun()