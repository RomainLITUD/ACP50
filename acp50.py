import streamlit as st
import pandas as pd 

st.set_page_config(page_title="ACP50 FAMILY", page_icon="vertical_traffic_light", layout="wide")
st.title("SEARCH YOUR NAME IN ACP50 FAMILY")

@st.cache_data
def read_data():
    df = pd.read_csv("author_cluster.csv")
    Names = df["Author"].values.tolist()
    return df, Names

df, Names = read_data()

yourname = st.selectbox("Type and search your name here", ['name']+Names)

newname = st.checkbox('My name is not in the list')


if not newname and yourname != "name":
    cluster = df[df["Author"] == yourname].Cluster.values[0]
    message = "You are mainly in cluster "+ str(cluster)
    st.title(message)
    show_keyword = st.checkbox('Show my reserch keywords:')
    if show_keyword:
        st.subheader(df[df["Author"] == yourname].typical_keywords.values[0])
        other_cluster = st.checkbox('Interested in all author clusters?')
        if other_cluster:
            st.image('Wordcloud.png')

if newname:
    st.write("Which word cloud better describes your main research interests?")
    st.image('Wordcloud.png')