import streamlit as st

# 페이지 설정
st.set_page_config(page_title="간단한 챗봇", page_icon="🤖")

# 타이틀 설정
st.title("간단한 챗봇 🤖")

# 챗봇 대화 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 유저 입력 처리
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("메시지를 입력하세요:", key="input")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input:
    # 유저 메시지를 대화에 추가
    st.session_state.messages.append({"role": "user", "content": user_input})
    # 챗봇 응답을 대화에 추가
    st.session_state.messages.append({"role": "bot", "content": "ok"})

# 대화 출력
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"**유저**: {message['content']}")
    else:
        st.write(f"**챗봇**: {message['content']}")
