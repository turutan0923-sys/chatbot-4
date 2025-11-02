import streamlit as st

st.title("あなたに合ったがん検診案内チャットボット")

st.write("年齢と性別を入力してください。あなたに推奨されるがん検診をチャット形式でご案内します。")

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

if st.button("チャットボットに質問"):
    recs = recommend_cancer_screenings(age, gender)
    with st.chat_message("user"):
        st.write(f"私は{age}歳・{gender}です。どんながん検診を受ければいいですか？")
    with st.chat_message("assistant"):
        if recs:
            st.write("厚生労働省の推奨に基づき、あなたには以下のがん検診をおすすめします：")
            for r in recs:
                st.write(f"- {r}")
        else:
            st.write("現時点で推奨されるがん検診はありません。")

    # チェックボックスの状態をsession_stateで管理
    if recs:
        st.write("---")
        st.write(f"**{age}歳・{gender}に推奨されるがん検診受診チェック**")
        checked = []
        for i, r in enumerate(recs):
            key = f"chk_{age}_{gender}_{i}"
            # チェックボックスの値をsession_stateで管理（初期値はFalse）
            if key not in st.session_state:
                st.session_state[key] = False
            checked.append(st.checkbox(f"{r} を受けましたか？", key=key))
        count = sum(checked)
        st.write(f"🏅 × {count}（{count}個の健診を受けました！）" if count > 0 else "まだ受けた健診がありません。")
