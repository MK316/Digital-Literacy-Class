import streamlit as st
import os
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(page_title="PDF 뷰어", layout="wide")

st.title("📄 PDF 자료 보기")

# -----------------------------
# 1) 항목 목록 설정
# -----------------------------
# 각 항목은 "type"이 "pdf" 또는 "link" 중 하나입니다.
# pdf: 화면에 PDF를 표시
# link: 버튼을 눌러야만 새 탭으로 이동 (예: Google Form)
ITEMS = {
    "1. HTML 가이드": {"type": "pdf", "path": "pages/data/week02/files/01-HTML-guide.pdf"},
    "2. 과업 안내문": {"type": "pdf", "path": "pages/data/week02/files/02-task-guide.pdf"},
    "3. Task 01": {"type": "pdf", "path": "pages/pages/data/week02/files/Task_01.pdf"},
    "4. Task 02": {"type": "pdf", "path": "pages/data/week02/files/Task_02.pdf"},
    "5. Task 03": {"type": "pdf", "path": "pages/data/week02/files/Task_03.pdf"},
    "6. 사후 설문지 (Google Form)": {
        "type": "link",
        "url": "https://forms.gle/urACShNuqUFxJP73A",
    },
    "7. 확인하기 (Google sheet)": {
        "type": "link",
        "url": "https://docs.google.com/spreadsheets/d/1knnx8Om_gb21AjS6Aa6lGv_dyU-sNAGOMHCcX6vupiQ/edit?usp=sharing",
    },
}

# -----------------------------
# 2) 드롭다운 메뉴
# -----------------------------
selected_label = st.selectbox(
    "확인할 항목을 선택하세요",
    options=list(ITEMS.keys()),
)

selected_item = ITEMS[selected_label]

# -----------------------------
# 3) PDF 표시 함수
# -----------------------------
def display_pdf(file_path: str):
    if not os.path.exists(file_path):
        st.error(f"파일을 찾을 수 없습니다: {file_path}")
        st.info("data/week02/files 폴더 안에 해당 파일이 있는지 확인해 주세요.")
        return

    # streamlit-pdf-viewer 컴포넌트는 pdf.js 기반이라
    # base64+iframe 방식보다 훨씬 안정적으로 렌더링됩니다.
    pdf_viewer(input=file_path, width=900, height=1000)

    # 다운로드 버튼도 함께 제공
    with open(file_path, "rb") as f:
        pdf_bytes = f.read()

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

if selected_item["type"] == "link":
    st.write(f"**{selected_label}**")
    st.write("아래 버튼을 누르면 새 탭에서 이동합니다.")
    st.link_button("🔗 새 탭에서 열기", selected_item["url"])

elif selected_item["type"] == "pdf":
    display_pdf(selected_item["path"])
