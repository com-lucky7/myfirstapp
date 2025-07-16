import streamlit as st
import pandas as pd
import altair as alt
import os

# 데이터 불러오기 함수
@st.cache_data
def load_data():
    local_file = "countriesMBTI_16types.csv"
    
    if os.path.exists(local_file):
        df = pd.read_csv(local_file)
        return df
    else:
        st.error("❌ 데이터 파일(countriesMBTI_16types.csv)이 앱 폴더에 없습니다.")
        return pd.DataFrame()

# 데이터 로딩
df = load_data()

# 데이터가 존재할 때만 실행
if not df.empty:
    st.set_page_config(page_title="국가별 MBTI Top3", page_icon="🌍", layout="centered")

    st.title("🌍 나라별 MBTI 유형 Top 3")
    st.write("원하는 나라를 선택하면 해당 국가에서 비율이 높은 **MBTI 유형 Top 3**를 시각화해서 보여드려요!")

    # 나라 선택
    countries = df['Country'].sort_values().unique().tolist()
    selected_country = st.selectbox("나라를 선택하세요", countries)

    # 선택한 나라의 데이터
    country_row = df[df["Country"] == selected_country].iloc[0]
    mbti_data = country_row.drop("Country")

    # Top 3 추출
    top3 = mbti_data.sort_values(ascending=False).head(3)
    top3_df = pd.DataFrame({
        "MBTI": top3.index,
        "비율": top3.values
    })

    # 시각화 (Altair)
    chart = alt.Chart(top3_df).mark_bar(cornerRadiusTop=5).encode(
        x=alt.X("MBTI", sort="-y"),
        y=alt.Y("비율", title="비율"),
        color=alt.Color("MBTI", legend=None)
    ).properties(
        width=500,
        height=400,
        title=f"{selected_country}의 MBTI 유형 Top 3"
    )

    st.altair_chart(chart, use_container_width=True)

    # 수치 데이터 보기
    with st.expander("📊 수치로 보기"):
        st.dataframe(top3_df.set_index("MBTI").style.format({"비율": "{:.2%}"}))
