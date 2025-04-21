# streamlit_app.py

import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Santiago Lara | Data Analyst Portfolio", layout="wide")

def set_background_color(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

background_color = "black"  # You can change this to any valid CSS color
set_background_color(background_color)

# ---- SIDEBAR ----
st.sidebar.title("📁 Portfolio Sections")
page = st.sidebar.radio("Navigate to:", [
    "Homepage / About Me",
    "Power BI Projects",
    "Python Projects",
    "ML & Forecasting Models",
    "Courses and Certifications",
    "Research Projects"
])

# ---- HOMEPAGE / ABOUT ME ----
if page == "Homepage / About Me":
    st.title("👋 Hello, I'm Santiago Lara")
    
    st.subheader("Industrial and Systems Engineering (IISE) | Data Analytics & BI | UI/UX Design")
    
    st.divider()

    st.markdown("""
    Welcome to my data analytics portfolio! I'm a data analyst passionate about turning 
    data into actionable insights.  \n  \nData is more than numbers—it's a story waiting to be told. 
    I enjoy turning raw information into clear, visual insights that help people 
    and businesses make smarter decisions. Whether it's building dashboards, 
    exploring data with Python, or designing user-friendly reports in Power BI, 
    I focus on practical solutions that make a real impact.""")
    
    
    st.markdown("""
    **Career Focus: Business Analytics | Dashboard Development | Looking to expand on Machine Learning**  
    🔗 [Download my CV](path_to_cv.pdf)  
    🔗 [Visit my LinkedIn profile](https://www.linkedin.com/in/santiagolara35234)
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

# ---- Courses and Certifications ----
elif page == "Courses and Certifications":
    st.title("🏅 Courses and Certifications")

    st.markdown("Below are some of the independent courses and certifications I've completed to enhance my analytics skills.")
    st.subheader("📉 Sales Forecasting with Prophet")
    st.markdown("""
    - **Problem**: Forecast monthly revenue for vending machine business
    - **Tech**: Python, Facebook Prophet, Pandas
    - 📄 [Download Model Report](files/forecasting_report.pdf)
    """)

# ---- DOWNLOADABLES ----
elif page == "Research Projects":
    st.title("📥 Research Projects")

    st.markdown("Here you'll find details on my research projects, highlighting the methodologies I employed "
    "and the key learnings gained through independent investigation.")

# ---- FOOTER ----
st.markdown("""
---
© 2025 Santiago Lara | Built using Streamlit
""")
