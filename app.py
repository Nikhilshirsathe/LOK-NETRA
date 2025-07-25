# app.py  
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load your data
df = pd.read_excel("Politicians.xlsx")

st.set_page_config(page_title="LokNetra", layout="wide")

# Sidebar
st.sidebar.image("https://img.icons8.com/color/48/000000/eye.png", width=48)
st.sidebar.title("LokNetra")
search_name = st.sidebar.text_input("Search MP by name or constituency")

# Filter data
if search_name:
    filtered = df[df['Name'].str.contains(search_name, case=False) | df['Constituency'].str.contains(search_name, case=False)]
else:
    filtered = df

# Main UI
st.title("MP Dashboard")

if not filtered.empty:
    mp = filtered.iloc[0]  # Show first match for demo
    card_css = """
<style>
.card-3d {
    background: #f4f6fb;
    border-radius: 16px;
    box-shadow: 0 8px 24px 0 rgba(30, 42, 73, 0.15), 0 1.5px 4px 0 rgba(30, 42, 73, 0.10);
    padding: 24px;
    margin-bottom: 24px;
    transition: transform 0.15s cubic-bezier(.17,.67,.83,.67), box-shadow 0.15s;
    cursor: pointer;
    border: 1.5px solid #e3e8f0;
    color: #1e2a49;
}
.card-3d:hover {
    transform: translateY(-6px) scale(1.03);
    box-shadow: 0 16px 32px 0 rgba(30, 42, 73, 0.22), 0 3px 8px 0 rgba(30, 42, 73, 0.13);
    border: 1.5px solid #1976d2;
}
.card-title {
    color: #1976d2;
    font-weight: 700;
    margin-bottom: 12px;
}
</style>
"""
    st.markdown(card_css, unsafe_allow_html=True)

    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown(
            "<div style='width:150px; height:180px; display:flex; align-items:center; justify-content:center; border:2px solid #1976d2; border-radius:12px; background:#e3e8f0; font-size:60px; box-shadow: 0 8px 24px 0 rgba(30, 42, 73, 0.15);'>👤</div>",
            unsafe_allow_html=True
        )
        st.subheader(mp['Name'])
        st.write(mp['Party'])
        st.write(mp['State'])
        st.write(mp['Constituency'])
        st.write(mp['Education'])
        st.write(mp['Past Experience'])

    with col2:
        st.markdown(
            f"""
            <div class="card-3d" onclick="window.location.href='#';">
                <div class="card-title">Projects (Last 10 Years)</div>
                <div>{mp['Projects (Last 10 Years)']}</div>
            </div>
            <div class="card-3d" onclick="window.location.href='#';">
                <div class="card-title">Criminal Cases</div>
                <div>{mp['Criminal Cases']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("""
            <div style='background: #f4f6fb; border-radius: 10px; box-shadow: 0 2px 8px #eee; padding: 20px; margin-bottom: 20px;'>
                <h3 style='margin-top:0;'>Bills Introduced</h3>
                <p>{}</p>
            </div>
        """.format(mp['Bills Introduced']), unsafe_allow_html=True)

        st.markdown("""
            <div style='background: #f4f6fb; border-radius: 10px; box-shadow: 0 2px 8px #eee; padding: 20px; margin-bottom: 20px;'>
                <h3 style='margin-top:0;'>Political Career Timeline</h3>
                <p>{}</p>
            </div>
        """.format(mp['Political Career Timeline']), unsafe_allow_html=True)

        st.markdown("""
            <div style='background: #f4f6fb; border-radius: 10px; box-shadow: 0 2px 8px #eee; padding: 20px; margin-bottom: 20px;'>
                <h3 style='margin-top:0;'>Public Reviews</h3>
                <p>**{} ⭐**</p>
                <p>{}</p>
            </div>
        """.format(mp['Rating'], mp['Latest_Review']), unsafe_allow_html=True)

        st.markdown("""
            <div style='background: #f4f6fb; border-radius: 10px; box-shadow: 0 2px 8px #eee; padding: 20px; margin-bottom: 20px;'>
                <h3 style='margin-top:0;'>Assembly Performance</h3>
                <p>Attendance: {}%</p>
                <p>Debates Participated: {}</p>
                <p>Questions Raised: {}</p>
                <p>Private Bills Introduced: {}</p>
            </div>
        """.format(mp['Attendance (%)'], mp['Debates Participated'], mp['Questions Raised'], mp['Private Bills Introduced']), unsafe_allow_html=True)

    st.markdown("### Public Reviews")
    st.write(f"**{mp['Rating']} ⭐**")
    st.write(mp['Latest_Review'])
else:
    st.info("No MP found. Please search by name or constituency.")

# Add more features: Compare, Region Dashboard, etc.