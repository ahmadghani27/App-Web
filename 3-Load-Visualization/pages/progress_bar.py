import streamlit as st
import time

'Downloading...'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    if i > 79 and i < 100:
        bar.progress(i+1)
        time.sleep(1)
    else:
        bar.progress(i+10)
        time.sleep(0.1) 
    
'Success!'