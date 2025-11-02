import streamlit as st

st.title("あなたに合ったがん検診案内")

st.markdown("### 元気でにこにこしている、さまざまな年代の男女")
# イラスト画像のリスト（パスまたはURL）
images = [
    "images/kids.png",
    "images/young_adult.png",
    "images/middle_age.png",
    "images/senior.png"
]
captions = [
    "元気な子ども",
    "若い男性と女性",
    "中年の男女",
    "高齢の男女"
]

# 横並びで画像を表示
cols = st.columns(len(images))
for i, (img, cap) in enumerate(zip(images, captions)):
    with cols[i]:
        st.image(img, caption=cap, use_column_width=True)

st.write("---")
# ↓がん検診の案内・入力フォーム（前回例の流用）
def recommend_cancer_screenings(age, gender):
    recommendations = []
    if age >= 50:
        recommendations.append("胃がん検診（2年に1回）")
    if age >= 40:
        recommendations.append("肺がん検診（年1回）")
        recommendations.append("大腸がん検診（年1回）")
    if gender == "女性":
        if age >= 40:
            recommendations.append("乳がん検診（2年に1回）")
        if age >= 20:
            recommendations.append("子宮頸がん検診（2年に1回）")
    return recommendations

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
