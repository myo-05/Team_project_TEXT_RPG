from player import *
from monster import *
from rich import *
import time, random, os, time,keyboard,opening,view

monster_list = [
        #속성 / 이름 / 레벨 / 체력 / 기본 공격력 / 마법 공격력 / 경험치 / 골드
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

def player_choice():
    q_message = "[bold red]" + "Q - 일반 공격 " + "[/bold red]"
    w_message = "[bold blue]" + "W - 마법 공격 " + "[/bold blue]"
    e_message = "[bold yellow]" + "E - 힐  스킬 " + "[/bold yellow]"
    r_message = "[bold magenta]" + "R - 궁 극 기" + "[/bold magenta]"

    print("사용할 스킬을 입력해주세요.")
    print(q_message+w_message+e_message+r_message)
    # dictionary형태로, q,w,e,r의 value값을 설정한다.
    key_map = {"q":1,"w":2,"e":3,"r":4}
    while True :
        #입력 받은 값을, 소문자건 대문자건, lower함수를 통해 소문자로 변경한다.
        key = keyboard.read_key().lower()
        #입력 받은 값이, 딕셔너리에 있다면 key값에 맞는 value 를 반환한다.
        if key in key_map:
            return key_map[key]

def battle():  # 전투가 진행되는 함수
    #생성될 몬스터 종류

    #랜덤 몬스터 생성(최대 3마리)
    mob = random.choices(monster_list, k=random.randint(1, 3))

    while True:
        # 콘솔창 클리어
        os.system("cls" if os.name == "nt" else "clear")

        #플레이어 행동 선택
        player_turn =  player_choice()
        time.sleep(0.1) # 입력 종료후 잠시 기다림

        #플레이어가 공격할 타겟 랜덤 설정
        player_target = random.randrange(len(mob))
        os.system("cls" if os.name == "nt" else "clear")
        if player_turn == 1:  # 1 일반 공격
            player_character.attack(mob[player_target])  # 플레이어가 몬스터를 공격
            player_character.give_message(f"{player_character.name}의 공격!!!", mob[player_target])
        #  마나가 소모되는 스킬을 사용할때, 마나 잔량 확인
        elif player_character.now_mp < (player_turn-1) * 10 :
            # player_turn 2 = 공격스킬  1 * 10 = 10 , 요구 마나 = 10
            # player_turn 3 = 힐  스킬  2 * 10 = 20 , 요구 마나 = 20
            # player_turn 4 = 궁 극 기  3 * 10 = 30 , 요구 마나 = 30
            print("마나가 부족합니다!")
            time.sleep(2) # 마나 없는점을 확인시켜주고, 잠시뒤 반복문으로 재귀함
            continue

        elif player_turn == 2:  # 2 마법 스킬
            player_character.magic_attack(mob[player_target])
        
        else: # 3 = 힐 스킬 , 4 = 궁극기 스킬
            player_character.cure(mob[player_target]) if player_turn == 3 else player_character.counter(mob[player_target])

        # elif player_turn == 3:  # 3 힐 스킬
        #     player_character.cure(mob[player_target])

        # elif player_turn == 4:  # 4 궁극기 발싸!!!!!!!!!!
        #     player_character.counter(mob[player_target])

        # 몬스터 차례
        
        
        time.sleep(3)# 플레이어 턴, 3초간 메시지 출력하고 콘솔 클리어
        os.system("cls" if os.name == "nt" else "clear")
        for monster in mob:
            skill = [
                lambda: monster.attack(player_character),
                lambda: monster.attack(player_character),
                lambda: monster.skill(player_character),
                lambda: monster.token_skill(player_character),
            ]
            if monster.boss:
                monster.battle_healing()  # 보스 몬스터가 힐링
                monster.over_drive()  # 보스 몬스터가 오버드라이브
            value = random.randrange(len(skill))
            skill[value]()  # 몬스터가 플레이어를 공격
            if value < 2 :
                monster.give_message(f"{monster.name}의 공격!!!",player_character)
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")

        #########결과판별#########
        if mob[player_target].now_hp <= 0:  # 몬스터가 죽었을때
            player_character.get_exp(mob[player_target])  #    경험치 획득
            player_character.get_gold(mob[player_target])  #    골드 획득
            del mob[player_target]  # 몬스터 삭제
            # 경험치 획득

        if not mob:
            print("이김^^")
            break  # 몬스터가 모두 죽었을때~

        elif player_character.now_hp <= 0:
            print("끔살 당해뽀림??")
            break  # 플레이어가 억까 당햇을때~

        # break

os.system('cls')
# 사용자 이름 입력!
name = str(input("이름을 입력해주세요 : "))
# 플레이어가 사용할 직업을 담은 리스트
job_list = [
    Boss(name),  # 0번
    Math_Teacher(name),  # 1번
    Muggle(name),  # 2번
    Smoker(name),  # 3번
    Flaming(name),  # 4번
]

# 직업 선택 !
while True:
    try:
        # job = (
        #     int(input("직업을 선택해주세요.\n1.부장님 2.수학쌤 3. 머글 4.애연가. 5.악플러 : ")) - 1
        # ) 
        job = int(input("직업을 선택해주세요.\n1.부장님 2.수학쌤 3. 머글 4.애연가. 5.악플러 : ")) - 1
        # job의 기대값은 0~4 , 올바른 입력값이 아닐경우 판별
        if job > 4 or job < 0:
            print("1~5번의 숫자를 입력해 주셔야 합니다.")
            continue
        break
    #숫자가 아닌, 문자를 입력했을때 판별
    except ValueError:
        print("숫자를 입력해 주세용^ㅁ^")
        continue

player_character = job_list[job]
opening.oppening()

print("\n테스트성공!")

# 1. monster.py 64번줄, battle_healing의 출력 메소드 호출 코드가 give_message가 아닌 print_message
#   > give_message로 변경.
# 2. systme.py의 몬스터 기본공격시 출력 없음
#   > 랜덤값이 2 이상이면 공격 메시지 출력 추가.
# 3. over_drive스킬 메시지 출력 없음
#   > monster class의 overdrive 스킬 메시지 추가