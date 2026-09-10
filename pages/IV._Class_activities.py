import streamlit as st
import base64
import os

st.set_page_config(page_title="PDF 뷰어", layout="wide")

st.title("📄 PDF 자료 보기")

# -----------------------------
# 1) PDF 파일 목록 설정
# -----------------------------
# 표시할 이름(드롭다운에 보이는 라벨) : 실제 파일 경로
# 파일 위치: pages/data/week02/files/ (이 스크립트는 pages/ 폴더 기준)
PDF_FILES = {
    "1. HTML 가이드": "pages/data/week02/files/01-HTML-guide.pdf",
    "2. 과업 안내문": "pages/data/week02/files/02-task-guide.pdf",
    "3. Task 01": "pages/pages/data/week02/files/Task_01.pdf",
    "4. Task 02": "data/week02/files/Task_02.pdf",
    "5. Task 03": "data/week02/files/Task_03.pdf",
}

# -----------------------------
# 2) 드롭다운 메뉴
# -----------------------------
selected_label = st.selectbox(
    "확인할 PDF 파일을 선택하세요",
    options=list(PDF_FILES.keys()),
)

selected_path = PDF_FILES[selected_label]

# -----------------------------
# 3) PDF 표시 함수
# -----------------------------
def display_pdf(file_path: str):
    if not os.path.exists(file_path):
        st.error(f"파일을 찾을 수 없습니다: {file_path}")
        st.info("pdfs 폴더 안에 해당 파일이 있는지 확인해 주세요.")
        return

    with open(file_path, "rb") as f:
        pdf_bytes = f.read()

    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    pdf_display = f"""
        <iframe
            src="data:application/pdf;base64,{base64_pdf}"
            width="100%"
            height="900px"
            type="application/pdf">
        </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

    # 다운로드 버튼도 함께 제공
    st.download_button(
        label="⬇️ PDF 다운로드",
        data=pdf_bytes,
        file_name=os.path.basename(file_path),
        mime="application/pdf",
    )


# -----------------------------
# 4) 실행
# -----------------------------
st.divider()
display_pdf(selected_path)
