import streamlit as st 
from functions.engine import Engine


workspace = "D:\\ptyped\\Stable\\Auto-GPT\\autogpt\\auto_gpt_workspace"
system = Engine(workspace)

# set the page config
st.set_page_config(
    page_title="ALFIE | Artificail Lifeform Intelligent Entity.",
    layout="wide",
)

# page title.
st.title("A.L.F.I.E")
st.markdown("``` Artificial Lifeform Intelligent Entity ```")


# function to create the project Overview.
def project_overview(project):
    st.subheader(project["project_name"])
    st.markdown(project["location"])



# main page made up of 2 columns (0.30% and 0.70%).
projects, project_overview = st.columns([0.3, 0.7])

with projects:
    pass

with project_overview:
    pass