from player import *
from monster import *
from rich import *
import time

# 사용자 이름 입력!
print("이름을 입력해주세요.")
name = input()


job_list = [
    [Boss(name)],  # 0번
    [Math_Teacher(name)],  # 1번
    [Muggle(name)],  # 2번
    [Smoker(name)],  # 3번
    [Flaming(name)],  # 4번
]
# 직업 선택 !
print("직업을 선택해주세요.\n1.부장님 2.수학쌤 3. 머글 4.애연가. 5.악플러")
job = int(input()) - 1  # 리스트 0번 = 1번 직업이니까 1을 뺀다 이거죠?? ㅇㅇ


# 직업 선택 후, 직업에 따른 스탯 출력!
# help meeeeeeeeeee

player_ = job_list[job][0]
monster1 = GrassMonster("리자몽", 1, 1)

player_.magic_attack(monster1)
time.sleep(1)
monster1.token_skill(player_)
