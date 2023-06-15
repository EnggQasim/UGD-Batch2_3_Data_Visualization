import pandas as pd
import streamlit as st


df = pd.DataFrame({
    "lat":[24.82150302902485,24.80833695109378],
    "lon":[67.04695880349462, 67.03704535930605]
})

st.table(df)
st.write(df)

st.map(df)