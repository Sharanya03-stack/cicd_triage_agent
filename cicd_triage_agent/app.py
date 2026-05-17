import streamlit as st
import os

st.set_page_config(
    page_title="CI/CD Agent Doctor", 
    page_icon="🚀",
    layout="wide"
)

# 🗺️ DYNAMIC PATH RADAR: Automatically detect where the views folder is hiding
possible_paths = [
    "views",                                         # Local path setup
    "cicd_triage_agent/views",                      # Cloud nested directory path setup
    os.path.join(os.getcwd(), "views"),             # Fallback active runtime directory
    os.path.join(os.getcwd(), "cicd_triage_agent", "views") 
]

views_dir = None
for path in possible_paths:
    if os.path.exists(path) and os.path.isdir(path):
        views_dir = path
        break

if views_dir is None:
    st.error("❌ Critical Structure Error: Could not locate the 'views' folder directory.")
    st.info(f"Current working scanning directory: {os.getcwd()}")
    st.stop()

# Match the detected views directory folder back to relative strings for st.Page
home_file = os.path.join(views_dir, "home.py").replace("\\", "/")
dashboard_file = os.path.join(views_dir, "dashboard.py").replace("\\", "/")
analytics_file = os.path.join(views_dir, "analytics.py").replace("\\", "/")

try:
    # Initialize the page instances cleanly with verified strings
    home_page = st.Page(home_file, title="Home Page", icon="🏠", default=True)
    dashboard_page = st.Page(dashboard_file, title="Diagnostic Lab", icon="🛠️")
    analytics_page = st.Page(analytics_file, title="Cost Analytics", icon="📊")
    
    # Run the navigation panel routing stream
    pg = st.navigation([home_page, dashboard_page, analytics_page])
    pg.run()

except Exception as e:
    st.error(f"Navigation routing setup error: {e}")
    st.info(f"Attempted paths:\n- Home: {home_file}\n- Dashboard: {dashboard_file}\n- Analytics: {analytics_file}")