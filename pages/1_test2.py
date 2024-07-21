import streamlit as st
if st.button("불러오기"):
    if "var" in st.session_state:
        st.write(st.session_state.var)
    else :
        st.write("error: NOT FOUND")