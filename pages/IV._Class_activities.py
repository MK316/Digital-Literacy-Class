import streamlit as st
import os
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(page_title="PDF 뷰어", layout="wide")

st.title("📄 PDF 자료 보기")

# -----------------------------
# 탭 구성 (3개 - 나머지 2개는 추후 사용)
# -----------------------------
tab1, tab2, tab3 = st.tabs(["자료 보기", "탭 2 (준비 중)", "탭 3 (준비 중)"])

# =========================================
# TAB 1: 기존 PDF / 링크 뷰어
# =========================================
with tab1:
    # -----------------------------
    # 1) 항목 목록 설정
    # -----------------------------
    # 각 항목은 "type"이 "pdf" 또는 "link" 중 하나입니다.
    # pdf: 화면에 PDF를 표시
    # link: 버튼을 눌러야만 새 탭으로 이동 (예: Google Form)
    ITEMS = {
        "1. HTML 가이드": {"type": "pdf", "path": "pages/data/week02/files/01-HTML-guide.pdf"},
        "2. 과업 안내문": {"type": "pdf", "path": "pages/data/week02/files/02-task-guide.pdf"},
        "3. Task 01": {"type": "pdf", "path": "pages/data/week02/files/Task_01.pdf"},
        "4. Task 02": {"type": "pdf", "path": "pages/data/week02/files/Task_02.pdf"},
        "5. Task 03": {"type": "pdf", "path": "pages/data/week02/files/Task_03.pdf"},
        "6. 사후 설문지 (Google Form)": {
            "type": "link",
            "url": "https://forms.gle/urACShNuqUFxJP73A",
        },
        "7. 확인하기 (Google Sheet)": {
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
        key="tab1_selectbox",
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
            key=f"download_{os.path.basename(file_path)}",
        )

    # -----------------------------
    # 4) 실행
    # -----------------------------
    st.divider()

    if selected_item["type"] == "link":
        st.write(f"**{selected_label}**")
        st.write("아래 버튼을 누르면 새 탭에서 이동합니다.")
        st.link_button("🔗 새 탭에서 열기", selected_item["url"], key="tab1_link_button")

    elif selected_item["type"] == "pdf":
        display_pdf(selected_item["path"])

# =========================================
# TAB 2: 조별 발표 자료 (AI 키워드 학습용 기사)
# =========================================
with tab2:
    st.header("🗞️ 조별 발표 자료")
    st.markdown(
        """
        아래는 **디지털리터러시와 영어교육** 3주차 활동을 위해 선정한 최신 AI 관련 영어 기사입니다.  
        **조별로 기사 1개를 배정받아** 함께 읽고, 기사 속에 등장하는 AI 키워드를 스스로 찾아본 뒤 발표를 준비하세요.
        """
    )
    st.divider()

    # -----------------------------
    # 조별 기사 목록
    # -----------------------------
    ARTICLES = [
        {
            "group": "1조",
            "title": "Nvidia confirms it will buy Hugging Face for $12.9 billion",
            "source": "TechCrunch (2026.09.03)",
            "url": "https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/",
            "keywords": "Hugging Face, GPT, Claude, 반도체 기업, 오픈소스 LLM",
            "desc": "반도체 기업 엔비디아가 오픈소스 AI 플랫폼 허깅페이스를 인수한다는 소식을 다룬 기사입니다.",
        },
        {
            "group": "2조",
            "title": "OpenAI launches GPT-6 Astra, its most powerful model yet",
            "source": "Fortune (2026.09.03)",
            "url": "https://fortune.com/2026/09/03/openai-debuts-gpt-6-astra-computer-use-greg-brockman-says-start-of-agi/",
            "keywords": "GPT, LLM, AGI, 성능측정(벤치마크), Claude, Agent AI",
            "desc": "오픈AI의 새 모델 GPT-6 Astra 출시 소식과 함께, AGI·벤치마크·컴퓨터를 조작하는 AI 에이전트 개념을 다룹니다.",
        },
        {
            "group": "3조",
            "title": "KOSPI leads Asia lower as AI slowdown debate hits memory stocks",
            "source": "Aju Press (2026.09.14)",
            "url": "https://www.ajupress.com/view/20260914093527319",
            "keywords": "AGI, Anthropic, 삼성전자, SK하이닉스, 반도체",
            "desc": "AI 기업 앤스로픽의 'AGI 개발 속도조절' 발언이 삼성전자·SK하이닉스 주가에 미친 영향을 다룬 기사입니다.",
        },
        {
            "group": "4조",
            "title": "Samsung and TSMC hope ASML's new machines will help address the chip shortage",
            "source": "Engadget (2026.09.08)",
            "url": "https://www.engadget.com/2252462/samsung-tsmc-commit-asml-fab/",
            "keywords": "반도체 공장, TSMC, 파운드리, 반도체 장비",
            "desc": "삼성전자와 TSMC가 반도체 공장(팹)에 ASML의 최신 장비를 도입해 칩 부족 문제를 해결하려는 시도를 다룹니다.",
        },
        {
            "group": "5조",
            "title": "AI News for September 15, 2026 — Daily Edition",
            "source": "AI Weekly (2026.09.15)",
            "url": "https://aiweekly.co/ai-news-today/edition/2026-09-15",
            "keywords": "코딩, Claude, GPT/Codex, 교육 영역",
            "desc": "AI가 코드 작성 대부분을 담당하게 된 개발 현장의 변화(코딩 에이전트)를 포함한 최신 AI 뉴스 모음입니다.",
        },
        {
            "group": "6조",
            "title": "Computer-Use AI Agents: The Best Open-Source & Closed-Source Tools in 2026",
            "source": "Turing Post (2026.09.13)",
            "url": "https://www.turingpost.com/p/computer-use-ai-agents",
            "keywords": "Agent AI, Claude, 코딩 에이전트",
            "desc": "화면을 직접 조작하며 작업을 수행하는 'Agent AI' 도구들을 비교 정리한 기사입니다.",
        },
    ]

    # -----------------------------
    # 카드 형태로 출력
    # -----------------------------
    for article in ARTICLES:
        with st.container(border=True):
            st.subheader(f"{article['group']} · {article['title']}")
            st.caption(f"출처: {article['source']}")
            st.write(article["desc"])
            st.markdown(f"**🔑 관련 키워드:** {article['keywords']}")
            st.link_button(
                "📖 기사 읽으러 가기 (새 탭)",
                article["url"],
                key=f"article_link_{article['group']}",
            )
        st.write("")  # 카드 사이 여백

# =========================================
# TAB 3: 추후 사용 예정
# =========================================
with tab3:
    st.info("이 탭은 추후 사용 예정입니다.")
