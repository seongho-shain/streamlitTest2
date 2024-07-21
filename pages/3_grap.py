import streamlit as st
text = st.text_input("값 입력")
if st.button("저장") :
    st.write("저장 되었습니다.")
    st.session_state.var = text