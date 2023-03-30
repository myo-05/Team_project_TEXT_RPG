from player import *
from monster import *
from rich import *
import time, random, os, time


def battle():  # 선택한 수학쌤가져오기 !
    # 랜덤(1~3마리)생성하고
    monster_list = [
        FireMonster("파이리", 1, 200, 20, 20, 10, 100),
        GrassMonster("이상해씨", 1, 200, 20, 20, 10, 100),
        WaterMonster("꼬부기", 1, 200, 20, 20, 10, 100),
        FireMonster("브케인", 1, 200, 20, 20, 10, 100),
        FireMonster("뚜꾸리", 1, 200, 20, 20, 10, 100),
        GrassMonster("쥬리비안", 1, 200, 20, 20, 10, 100),
        WaterMonster("팽도리", 1, 200, 20, 20, 10, 100),
        FireMonster("가디", 1, 200, 20, 20, 10, 100),
        GrassMonster("이상해꽃", 2, 200, 20, 20, 10, 100),
        WaterMonster("어니부기", 2, 200, 20, 20, 10, 100),
        FireBossMonster("공민영", 100, 200, 20, 20, 50, 100),
        GrassBossMonster("NO탁근", 4, 200, 20, 20, 50, 100),
        WaterBossMonster("나지쓰", 3, 200, 20, 20, 40, 100),
    ]

    while True:

        os.system("cls" if os.name == "nt" else "clear")
        
        player_turn = int(input("당신의 행동을 선택해주세요 ! \n 1.일반 공격 2. 마법 공격 3.회복 4.필살기 : "))
        mob = random.choices(monster_list, k=random.randint(1, 3))
        random_value = random.randrange(len(mob))
        # player_turn = 2  # 1 일반 공격
        if player_turn > 4 or player_turn < 1:
            print("1~4번 숫자를 입력해 주세요.")
            continue

        if player_turn == 1:  # 1 일반 공격
            m1.attack(mob[random_value])  # 플레이어가 몬스터를 공격
            m1.give_message(f"{m1.name}의 공격!!!", mob[random_value])

        elif player_turn == 2:  # 2 공격 스킬
            if m1.now_mp < 10:
                print("마나가 부족합니다.")
                continue
            m1.magic_attack(mob[random_value])

        elif player_turn == 3:  # 3 힐 스킬
            if m1.now_mp < 20:
                print("마나가 부족합니다.")
                continue
            m1.cure(mob[random_value])

        elif player_turn == 4:  # 4 궁극기 발싸!!!!!!!!!!
            if m1.now_mp < 30:
                print("마나가 부족합니다.")
                continue
            m1.counter(mob[random_value])

        for monster in mob:
            skill = [
                lambda: monster.attack(m1),
                lambda: monster.attack(m1),
                lambda: monster.skill(m1),
                lambda: monster.token_skill(m1),
            ]
            if monster.boss:
                monster.battle_healing()  # 보스 몬스터가 힐링
                monster.over_drive()  # 보스 몬스터가 오버드라이브
            skill[random.randrange(len(skill))]()  # 몬스터가 플레이어를 공격
            time.sleep(0.8)

        #########결과판별#########
        if mob[random_value].now_hp <= 0:  # 몬스터가 죽었을때
            m1.get_exp(mob[random_value])  #    경험치 획득
            m1.get_gold(mob[random_value])  #    골드 획득
            del mob[random_value]  # 몬스터 삭제
            # 경험치 획득

        if not mob:
            print("이김^^")
            break  # 몬스터가 모두 죽었을때~

        elif m1.now_hp <= 0:
            print("끔살 당해뽀림??")
            break  # 플레이어가 억까 당햇을때~

        # break


# 사용자 이름 입력!
print("이름을 입력해주세요.")
name = str(input())


job_list = [
    Boss(name),  # 0번
    Math_Teacher(name),  # 1번
    Muggle(name),  # 2번so
    Smoker(name),  # 3번
    Flaming(name),  # 4번
]

# 직업 선택 !
# print("직업을 선택해주세요.\n1.부장님 2.수학쌤 3. 머글 4.애연가. 5.악플러")
while True:
    try:
        job = (
            int(input("직업을 선택해주세요.\n1.부장님 2.수학쌤 3. 머글 4.애연가. 5.악플러 : ")) - 1
        )  # 수학쌤을 선택했다!
        break
    except ValueError:
        print("숫자를 입력해 주세용^ㅁ^")
        continue
m1 = job_list[job]
battle()
print("\n테스트성공!")
# 정리 쵝오맨#
######################################################################
# 1. 플레이어 선택
#       > 플레이어의 공격 , 스킬 발동 => 타겟을 누구로 지정할지 정하기 (체력이 제일 높은 몬스터부터? 랜덤으로?)
# 2. 몬스터 선택 (1 , 2 , 3)
#       > 몬스터1 의 공격
#       > 몬스터2 의 공격
#       > 몬스터3 의 공격
# 3. 죽은 사람 , 몬스터가 있는지?
#   3-1)없다면 다시 위로
#          continue
#   3-2)사람이 죽었다면
#          게임끝메시지
#          break
#   3-3)몬스터가 죽었다면
#          경험치 획득
#          골드 획득
#       3-3-1) 죽은 몬스터 수 == 소환된 몬스터 수
#             break
#       3-3-2) 죽은 몬스터 수 랑 소환된 몬스터 수 같지 않으면
#            continue
#############################################################################
