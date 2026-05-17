import streamlit as st
import os

st.set_page_config(
    page_title="CI/CD Agent Doctor", 
    page_icon="🚀",
    layout="wide"
)

# 🎯 Force find the absolute root directory of app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build precise absolute paths that work on both local and cloud environments
home_file = os.path.join(BASE_DIR, "views", "home.py")
dashboard_file = os.path.join(BASE_DIR, "views", "dashboard.py")
analytics_file = os.path.join(BASE_DIR, "views", "analytics.py")

# Double-check that files physically exist before initializing navigation
if not os.path.exists(home_file):
    st.error(f"❌ Absolute Path Error: File not found at `{home_file}`")
    st.info("Ensure that your 'views' folder and its python scripts are spelled correctly and placed right next to app.py.")
    st.stop()

try:
    # Initialize page structures with absolute paths
    home_page = st.Page(home_file, title="Home Page", icon="🏠", default=True)
    dashboard_page = st.Page(dashboard_file, title="Diagnostic Lab", icon="🛠️")
    analytics_page = st.Page(analytics_file, title="Cost Analytics", icon="📊")
    
    # Render the navigational sidebar panel
    pg = st.navigation([home_page, dashboard_page, analytics_page])
    pg.run()

except Exception as e:
    st.error(f"Navigation routing setup error: {e}")