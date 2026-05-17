import streamlit as st
import os

st.set_page_config(
    page_title="CI/CD Agent Doctor", 
    page_icon="🚀",
    layout="wide"
)

# Define standard relative layout paths
home_rel = "views/home.py"
dashboard_rel = "views/dashboard.py"
analytics_rel = "views/analytics.py"

# Cloud Fallback check: If Streamlit loses its place, look inside the current working directory explicitly
if not os.path.exists(home_rel):
    home_rel = os.path.join(os.getcwd(), "views", "home.py")
    dashboard_rel = os.path.join(os.getcwd(), "views", "dashboard.py")
    analytics_rel = os.path.join(os.getcwd(), "views", "analytics.py")

try:
    # Initialize the page instances cleanly
    home_page = st.Page(home_rel, title="Home Page", icon="🏠", default=True)
    dashboard_page = st.Page(dashboard_rel, title="Diagnostic Lab", icon="🛠️")
    analytics_page = st.Page(analytics_rel, title="Cost Analytics", icon="📊")
    
    # Run navigation panel routing stream
    pg = st.navigation([home_page, dashboard_page, analytics_page])
    pg.run()

except Exception as e:
    st.error(f"Navigation routing setup error: {e}")
    st.info("Ensure your files match the following structure: cicd_triage_agent/views/home.py")