# Create virutal env with conda
* `conda create --name <your_env_name>
* `conda activate <your_env_name>

# now open folder on VS code
* `code .`

# Cteae file
* file name *task1.py*
```
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "id":[1,2,3],
    "name":['Ali',"hamza",'Junaid']
})

st.write("My First Streamlit project")
```

## now run above code
* go to **Terminal** on vs code tab
* `streamlit run <filename.py>