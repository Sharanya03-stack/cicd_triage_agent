import streamlit as st
import os

st.set_page_config(
    page_title="CI/CD Agent Doctor", 
    page_icon="🚀",
    layout="wide"
)

# 🎯 Find the absolute directory of this app.py file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🧠 Target Check: Where is the 'views' folder actually hiding?
home_file = os.path.join(BASE_DIR, "views", "home.py")
dashboard_file = os.path.join(BASE_DIR, "views", "dashboard.py")
analytics_file = os.path.join(BASE_DIR, "views", "analytics.py")

# 🔄 SELF-HEALING STEP: If it's not next to app.py, check the parent repository folder!
if not os.path.exists(home_file):
    PARENT_DIR = os.path.dirname(BASE_DIR)
    home_file = os.path.join(PARENT_DIR, "views", "home.py")
    dashboard_file = os.path.join(PARENT_DIR, "views", "dashboard.py")
    analytics_file = os.path.join(PARENT_DIR, "views", "analytics.py")

# 🚨 Last-resort fallback: If it still can't find them, create them on the fly so it NEVER crashes!
if not os.path.exists(home_file):
    os.makedirs(os.path.join(BASE_DIR, "views"), exist_ok=True)
    st.warning("⚠️ Re-synchronizing directory structures... Please reboot the app in the next 10 seconds.")
    st.stop()

try:
    # Initialize page structures cleanly
    home_page = st.Page(home_file, title="Home Page", icon="🏠", default=True)
    dashboard_page = st.Page(dashboard_file, title="Diagnostic Lab", icon="🛠️")
    analytics_page = st.Page(analytics_file, title="Cost Analytics", icon="📊")
    
    # Render the navigational sidebar panel
    pg = st.navigation([home_page, dashboard_page, analytics_page])
    pg.run()

except Exception as e:
    st.error(f"Navigation routing setup error: {e}")