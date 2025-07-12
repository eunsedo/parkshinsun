import streamlit as st
import random

st.title("수학 퀴즈 게임")

score = st.session_state.get("score", 0)
question, answer = st.session_state.get("question"), st.session_state.get("answer")

if question is None or answer is None:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(['+', '-', '*'])
    question = f"{a} {op} {b}"
    answer = str(eval(question))
    st.session_state["question"] = question
    st.session_state["answer"] = answer

st.write(f"문제: {question}")

user_answer = st.text_input("정답을 입력하세요", key="user_answer")

if st.button("제출"):
    if user_answer == answer:
        score += 1
        st.session_state["score"] = score
        st.success(f"정답입니다! 현재 점수: {score}")
        # 새로운 문제 생성
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(['+', '-', '*'])
        question = f"{a} {op} {b}"
        answer = str(eval(question))
        st.session_state["question"] = question
        st.session_state["answer"] = answer
        st.session_state["user_answer"] = ""
    else:
        st.error(f"틀렸습니다! 최종 점수: {score}")
        st.session_state["score"] = 0
        st.session_state["question"] = None
        st.session_state["answer"] = None
        st.session_state["user_answer"] = ""

st.write(f"현재 점수: {score}")
