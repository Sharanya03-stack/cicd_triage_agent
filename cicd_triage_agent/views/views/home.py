import streamlit as st

st.title("CI/CD Pipeline Triage Agent")
st.caption("AI-Powered Pipeline Failure Intelligence & Automated Remediation Engine")
st.markdown("---")

with st.container(border=True):
    st.markdown("""
    ### Project Architecture Context
    When software deployments execute across production pipelines, automated jobs often crash with dense, unorganized terminal log streams. Locating structural errors manually can strain operational workflows.
    
    This platform integrates specialized agent models designed to intercept, extract, parse, and handle raw system error data automatically.
    """)

st.subheader("Core Architectural Components")

c1, c2 = st.columns(2)
with c1:
    with st.container(border=True):
        st.markdown("#### CascadeFlow Runtime")
        st.markdown(
            "Isolates relevant trace logs directly inside the workspace before routing parameters "
            "touch external models. This safeguards performance overhead and drops computing cost footprints."
        )

with c2:
    with st.container(border=True):
        st.markdown("#### Hindsight Vector Memory")
        st.markdown(
            "Caches historical errors and resolution tracking parameters. If an engineering incident repeats, "
            "the platform automatically matches historical signatures to yield stable remediation strategies."
        )

st.info("To begin an evaluation, use the left sidebar navigation panels to open the Live Diagnostic Lab.")