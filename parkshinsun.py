import pygame
import random
import sys
import time

# 초기화
pygame.init()
pygame.font.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("수학 생존 게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (0, 200, 0)

# 글꼴
FONT = pygame.font.SysFont("arial", 32)

# 문제 생성 함수
def generate_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(['+', '-', '*'])
    question = f"{a} {op} {b}"
    answer = str(eval(question))
    return question, answer

# 게임 상태 초기화
question, answer = generate_problem()
user_input = ""
score = 0
time_limit = 10
start_time = time.time()

# 메인 게임 루프
running = True
while running:
    screen.fill(WHITE)

    # 시간 계산
    elapsed_time = time.time() - start_time
    remaining_time = max(0, time_limit - elapsed_time)

    if remaining_time == 0:
        running = False

    # 출력
    screen.blit(FONT.render(f"문제: {question}", True, BLACK), (50, 100))
    screen.blit(FONT.render(f"답 입력: {user_input}", True, BLACK), (50,_
