import streamlit as st
import pandas as pd
import numpy as np
import time
# 페이지 설정
st.set_page_config(page_title="캐싱 예제", page_icon="📊")

# 타이틀 설정
st.title("캐싱 예제 📊")

# 데이터프레임 생성 함수
@st.cache_data
def load_data():
    time.sleep(5)
    # 비용이 많이 드는 데이터 생성 작업 (예: 대규모 데이터 로드)
    df = pd.DataFrame(np.random.randn(1000, 3), columns=['a', 'b', 'c'])
    return df

# 데이터프레임 로드
df = load_data()

# 데이터프레임 표시
st.write("데이터프레임:")
st.dataframe(df)
