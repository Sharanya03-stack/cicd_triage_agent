import streamlit as st
import os

# Configure global layout settings
st.set_page_config(
    page_title="CI/CD Agent Doctor", 
    page_icon="🚀",
    layout="wide"
)

# 🧠 ABSOLUTE PATH RESOLUTION: Dynamically pinpoint the exact directory of app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build bulletproof absolute paths to your sub-views
home_path = os.path.join(BASE_DIR, "views", "home.py")
dashboard_path = os.path.join(BASE_DIR, "views", "dashboard.py")
analytics_path = os.path.join(BASE_DIR, "views", "analytics.py")

try:
    # Pass the verified absolute paths directly into the page initializer
    home_page = st.Page(home_path, title="Home Page", icon="🏠", default=True)
    dashboard_page = st.Page(dashboard_path, title="Diagnostic Lab", icon="🛠️")
    analytics_page = st.Page(analytics_path, title="Cost Analytics", icon="📊")
    
    # Render the navigational sidebar menu
    pg = st.navigation([home_page, dashboard_page, analytics_page])
    pg.run()

except Exception as e:
    st.error(f"Navigation routing setup error: {e}")
    st.info("System is attempting to locate page submodules via absolute directory paths.")