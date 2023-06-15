import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "id":[1,2,3],
    "name":['Ali',"hamza",'Junaid']
})

st.write("My First Streamlit project")
st.write(df)