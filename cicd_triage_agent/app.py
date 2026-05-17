import streamlit as st

st.set_page_config(
    page_title="CI/CD Agent Doctor", 
    page_icon="??",
    layout="wide"
)

home_page = st.Page("views/home.py", title="Home Page", icon="??", default=True)
dashboard_page = st.Page("views/dashboard.py", title="Diagnostic Lab", icon="???")
analytics_page = st.Page("views/analytics.py", title="Cost Analytics", icon="??")

pg = st.navigation([home_page, dashboard_page, analytics_page])
pg.run()
