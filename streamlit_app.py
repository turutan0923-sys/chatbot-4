import streamlit as st

# 年齢・性別ごとのがん検診推奨ロジック
def recommend_cancer_screenings(age, gender):
    recommendations = []
    # 男女共通
    if age >= 50:
        recommendations.append("胃がん検診（2年に1回）")
    if age >= 40:
        recommendations.append("肺がん検診（年1回）")
        recommendations.append("大腸がん検診（年1回）")
    # 女性のみ
    if gender == "女性":
        if age >= 40:
            recommendations.append("乳がん検診（2年に1回）")
        if age >= 20:
            recommendations.append("子宮頸がん検診（2年に1回）")
    return recommendations

st.title("あなたに合ったがん検診案内")

age = st.number_input("年齢を入力してください", min_value=0, max_value=120, value=40)
gender = st.selectbox("性別を選択してください", ["男性", "女性"])

if st.button("おすすめのがん検診を表示"):
    recs = recommend_cancer_screenings(age, gender)
    if recs:
        st.write(f"**{age}歳・{gender}に推奨されるがん検診**")
        for r in recs:
            st.write(f"- {r}")
    else:
        st.write("該当する推奨がん検診はありません。")
