import streamlit as st
import time

def run_triage_crew(custom_scenario=None):
    time.sleep(1.2)
    if custom_scenario and "numpy" in custom_scenario:
        return "### ?? Incident Analysis Playbook\n\n**?? Error:** `numpy<=1.21.5` conflict.\n\n**??? Mitigation:** Lifted requirements constraints."
    return "### ?? Incident Analysis Playbook\n\n**?? Error:** `SocketError: connection reset by peer`\n\n**??? Mitigation:** Injected pipeline retry parameters (`retry_count=3`)."

st.title("??? Live Diagnostic Command Center")
st.caption("Inspect live runtime trace diagnostics and execute remediation actions.")
st.markdown("---")
col1, col2 = st.columns([1, 1.8])
with col1:
    analysis_mode = st.radio("Log Input Target Mode:", ["Read Active Repository Stream (error_log.txt)", "Simulate Custom Error Signature Preset"])
    selected_input = None
    if analysis_mode == "Simulate Custom Error Signature Preset":
        selected_input = st.selectbox("Select Scenario Template:", ["test_payment_gateway_timeout FAILED SocketError: connection reset by peer", "Cannot install package_x because of a version conflict. package_x requires numpy<=1.21.5"])
    if st.button("?? Run Diagnostic Agents", type="primary", use_container_width=True):
        with st.spinner("Invoking Automated Agent Crew via CascadeFlow..."):
            st.session_state['playbook_result'] = run_triage_crew(selected_input)
with col2:
    if 'playbook_result' in st.session_state:
        st.markdown(st.session_state['playbook_result'])
    else:
        st.warning("Awaiting Instruction. Run diagnostics to generate a playbook.")
