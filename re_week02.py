#1~100 사이의 랜덤한 숫자를 맞추는 게임, O(log n) 의 시간복잡도를 가지게 제작.
import random
answer = random.randrange(1,101)
guess = 0
inochi = 7
win = False
i = 0
while i < inochi:
    print(f"{inochi - i}번 남았습니다.")
    guess = int(input("정수를 입력하시오 : "))
    if guess == answer:
        print("정답입니다.")
        win = True
        break
    elif guess > answer:
        print("LOW")
    else:
        print("HIGH")
    i += 1

if win:
    print("네가최고야")
else:
    print("YOU LOSE")

