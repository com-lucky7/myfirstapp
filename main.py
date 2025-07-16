import streamlit as st

# 디즈니 공주 추천 사전
mbti_to_princess = {
    "ISTJ": ("엘사", "책임감이 강하고 신중한 당신에게는 아이스 퀸 '엘사'가 잘 어울려요!"),
    "ISFJ": ("신데렐라", "다정하고 배려심 넘치는 당신에게는 '신데렐라'가 찰떡이에요!"),
    "INFJ": ("벨", "이상주의적이면서도 지적인 당신은 '벨' 그 자체에요."),
    "INTJ": ("에사메랄다", "논리적이면서도 독립적인 당신에게 '에사메랄다'가 어울려요."),
    "ISTP": ("뮬란", "과감하고 실용적인 당신은 '뮬란'과 같은 전사 타입!"),
    "ISFP": ("포카혼타스", "자연을 사랑하고 감성적인 당신에게는 '포카혼타스'가 딱이에요."),
    "INFP": ("오로라", "순수하고 몽환적인 당신은 '오로라' 공주와 닮았어요."),
    "INTP": ("메리다", "호기심 많고 독립적인 당신에게는 '메리다'가 잘 어울려요."),
    "ESTP": ("재스민", "모험을 즐기고 자유로운 영혼인 당신은 '재스민' 그 자체!"),
    "ESFP": ("안나", "명랑하고 따뜻한 에너지로 가득한 당신은 '안나'와 찰떡이에요!"),
    "ENFP": ("라푼젤", "상상력이 풍부하고 활발한 당신은 '라푼젤' 스타일이에요."),
    "ENTP": ("바네로피", "엉뚱하고 톡톡 튀는 당신은 '바네로피'와 잘 어울려요."),
    "ESTJ": ("티아나", "실용적이고 야무진 당신은 '티아나'와 닮았어요."),
    "ESFJ": ("아리엘", "사교적이고 따뜻한 마음의 소유자인 당신은 '아리엘' 그 자체!"),
    "ENFJ": ("벨", "타인을 이끄는 리더십 있는 당신에게는 '벨'이 어울려요."),
    "ENTJ": ("엘사", "냉철한 판단력과 카리스마를 지닌 당신은 '엘사'와 찰떡이에요."),
}

# 페이지 설정
st.set_page_config(page_title="MBTI 디즈니 공주 추천기", page_icon="👑", layout="centered")

# 타이틀
st.title("👑 MBTI로 알아보는 나와 닮은 디즈니 공주")
st.write("당신의 MBTI를 선택하면, 어울리는 디즈니 공주를 알려드릴게요 ✨")

# MBTI 선택
mbti_list = list(mbti_to_princess.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", [""] + mbti_list)

# 결과 출력
if selected_mbti:
    princess_name, description = mbti_to_princess[selected_mbti]
    st.subheader(f"💖 당신에게 어울리는 디즈니 공주는: **{princess_name}**!")
    st.write(description)
    st.markdown("---")
    st.markdown("👸 공주처럼 오늘도 빛나는 하루 되세요!")

# 푸터
st.markdown("<small style='color: gray;'>디즈니 공주 MBTI 추천은 재미로 보세요 😊</small>", unsafe_allow_html=True)
