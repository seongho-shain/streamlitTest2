import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="데이터프레임 편집기", page_icon="📊")

# 타이틀 설정
st.title("데이터프레임 편집기 📊")

# 샘플 데이터프레임 생성
data = {
    '이름': ['홍길동', '이순신', '유관순'],
    '나이': [25, 32, 19],
    '직업': ['학생', '군인', '활동가']
}
df = pd.DataFrame(data)

# 데이터프레임 편집기
edited_df = st.data_editor(df)

# 수정된 데이터프레임 표시
st.write("수정된 데이터프레임:")
st.dataframe(edited_df)
