import streamlit as st

st.set_page_config(
    page_title="Real-Time ALFIE Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Real-Time ALFIE Dashboard")

# column1 [timeline, Issue, Tracker]
dash_set_1_1, dash_set_1_2 = st.columns([0.5, 0.5])

# column2 [Traffic, Activity Map]
dash_set_2_1, dash_set_2_2 = st.columns([0.5, 0.5])

# column3 [Live Feeds,Top Profiles]
dash_set_3_1, dash_set_3_2 = st.columns([0.5, 0.5])


with dash_set_1_1:
    st.markdown("### Timeline")
    

with dash_set_1_2:
    st.markdown("### Issue Status")


with dash_set_2_1:
    st.markdown("### Traffic")


with dash_set_2_2:
    st.markdown("### Activity Map")


with dash_set_3_1:
    st.markdown("### Live Feeds")

with dash_set_3_2:
    st.markdown("### Top Profiles")