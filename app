# streamlit_app.py

import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Santiago Lara | Data Analyst Portfolio", layout="wide")

# ---- SIDEBAR ----
st.sidebar.title("📁 Portfolio Sections")
page = st.sidebar.radio("Navigate to:", [
    "Homepage / About Me",
    "Power BI Projects",
    "Python Projects",
    "ML & Forecasting Models",
    "Downloadables"
])

# ---- HOMEPAGE / ABOUT ME ----
if page == "Homepage / About Me":
    st.title("👋 Hello, I'm Santiago Lara")

    st.markdown("""
    Welcome to my data analytics portfolio. I'm a data analyst passionate about turning data into actionable insights.
    
    **Career Focus**: Business Analytics | Dashboard Development | Predictive Modeling
    
    🔗 [Download my CV](path_to_cv.pdf)  
    🔗 [Visit my GitHub](https://github.com/yourusername)
    """)

# ---- POWER BI PROJECTS ----
elif page == "Power BI Projects":
    st.title("📊 Power BI Projects")

    st.markdown("Here you'll find dashboards and business intelligence solutions built using Power BI.")
    st.subheader("🏪 Sales Performance Dashboard")
    st.image("images/sales_dashboard.png")
    st.markdown("""
    - **Goal**: Analyze regional sales performance and identify underperforming segments.
    - **Tools**: Power BI, DAX, SQL
    - 🔗 [View on GitHub](https://github.com/yourusername/project1)
    - 📄 [Download PDF](files/project1_summary.pdf)
    """)

# ---- PYTHON PROJECTS ----
elif page == "Python Projects":
    st.title("🐍 Python Projects")

    st.markdown("Interactive data apps and scripts developed using Python and Streamlit.")
    st.subheader("📈 Revenue Explorer Tool")
    st.markdown("*(Placeholder for interactive data demo)*")

# ---- ML & FORECASTING MODELS ----
elif page == "ML & Forecasting Models":
    st.title("🧠 Machine Learning & Forecasting Models")

    st.markdown("Predictive models, time series analysis, and data science experiments.")
    st.subheader("📉 Sales Forecasting with Prophet")
    st.markdown("""
    - **Problem**: Forecast monthly revenue for vending machine business
    - **Tech**: Python, Facebook Prophet, Pandas
    - 📄 [Download Model Report](files/forecasting_report.pdf)
    """)

# ---- DOWNLOADABLES ----
elif page == "Downloadables":
    st.title("📥 Resources & Downloads")

    st.markdown("Here you can download my resume, project summaries, and access repositories.")
    with open("files/Santiago_Lara_CV.pdf", "rb") as file:
        st.download_button("📄 Download My CV", file, file_name="Santiago_Lara_CV.pdf")

    st.markdown("""
    🔗 [GitHub Repositories](https://github.com/yourusername)  
    📄 [Power BI Case Studies](files/pbi_cases.zip)  
    📄 [Python Projects Summaries](files/python_projects.zip)
    """)

# ---- FOOTER ----
st.markdown("""
---
© 2025 Santiago Lara | Built with ❤️ using Streamlit
""")
