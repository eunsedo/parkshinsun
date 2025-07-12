import random

def math_quiz():
    # 두 숫자와 연산자 랜덤 생성
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*', '/'])

    # 문제와 정답 계산
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    else:
        # 나누기는 소수점 둘째 자리까지 제한
        correct_answer = round(num1 / num2, 2)

    # 사용자에게 문제 출력
    user_answer = input(f"문제: {num1} {operator} {num2} = ? (소수점 둘째 자리까지 입력) ")

    try:
        # 사용자 답을 숫자로 변환 (float 처리)
        user_answer = float(user_answer)

        if abs(user_answer - correct_answer) < 0.01:  # 오차 범위 0.01
            print("정답입니다! 🎉")
        else:
            print(f"틀렸어요. 정답은 {correct_answer} 입니다.")
    except:
        print("숫자를 입력해주세요.")

if __name__ == "__main__":
    math_quiz()

