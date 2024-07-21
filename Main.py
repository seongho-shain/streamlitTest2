import streamlit as st
import cv2
import numpy as np
from datetime import datetime
import os
from streamlit_image_comparison import image_comparison

# 갤러리 디렉터리 설정
GALLERY_DIR = "gallery"
if not os.path.exists(GALLERY_DIR):
    os.makedirs(GALLERY_DIR)

# Streamlit 앱 제목
st.title("셀카 찍고 이미지 비교하기")

# 카메라 입력 위젯
img_file_buffer = st.camera_input("사진을 찍으세요")

# 사진이 찍혔을 때
if img_file_buffer is not None:
    # 파일을 BytesIO 객체로 변환
    bytes_data = img_file_buffer.getvalue()

    # OpenCV를 사용하여 이미지 읽기
    img_array = np.frombuffer(bytes_data, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # 현재 시간을 사용하여 파일 이름 생성
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(GALLERY_DIR, f"selfie_{timestamp}.png")

    # 이미지 저장
    cv2.imwrite(file_path, img)

    # 그레이스케일 이미지 생성
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)  # 3채널로 변환

    # 이미지 비교
    st.write("이미지 비교")
    image_comparison(
        img1=img,
        img2=gray_img,
        label1="트루컬러",
        label2="그레이스케일"
    )

    st.success(f"사진이 {file_path}에 저장되었습니다.")
