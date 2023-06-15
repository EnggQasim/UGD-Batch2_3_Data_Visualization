import streamlit as st

# st.title("Pakistan")
# st.header("Pakistan header")
# st.subheader("Pakistan subheader")
# st.markdown("# Pakistan with markdown syntax")
# st.markdown("`Hello world code style`")

import pandas as pd

df = pd.DataFrame({
    "id":[1,2,3],
    "name":['Ali',"hamza",'Junaid']
})

st.write(df)
st.dataframe(df)
st.table(df)

