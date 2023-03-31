from player import *
from monster import *
from rich import *
import time, random, os, time,keyboard,opening



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
                monster.battle_healing(player_character)  # 보스 몬스터가 힐링
                monster.over_drive(player_character)  # 보스 몬스터가 오버드라이브
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
            print("이김^^\n계속 하려면 아무키나 입력해주세요.")
            break  # 몬스터가 모두 죽었을때~

        elif player_character.now_hp <= 0:
            print("끔살 당해뽀림??")
            break  # 플레이어가 억까 당햇을때~
                # break

# 맵 그리기
def location(x, y, rows, cols, xarr, yarr, hunting_ground):
    # box color
    player_box = "[bold red]" + "■" + "[/bold red]"
    monster_box = "[bold blue]" + "■" + "[/bold blue]"
    hunting_ground_message = ""
    # 테두리와, 배열 초기값
    arr = [" " * rows] * cols
    string = f"{player_box} = you   {monster_box} : monster\n"
    #삼항 안에, 삼항
    string += f"{ '다음 사냥터>>>' if hunting_ground == 0 else ('<<< 이전 사냥터' if hunting_ground == 3 else '<<< 돌아가기     다음 사냥터>>>')}\n"
    string += "─" * 30 + "\n"

    # 반복문을 돌며, 플레이어의 위치, 몬스터의 위치를 탐색한다.
    for i in range(cols):
        for j in range(rows):
            if i == y and j == x:
                string += player_box
            elif (j, i) in zip(xarr, yarr):
                string += monster_box
            else:
                string += arr[i][j]
        string += "\n"
    
    string += "─" * 30 + "\n"
    string += "w,a,s,d 키를 이용해 움직이세요.\n"
    string += "k = 운빨 테스트 하러가기\n"
    string += "현재 사냥터 레벨 " + str(hunting_ground)
    return string


# 몬스터의 랜덤 위치값 조정, list는 주소를 담고있어 반환할 필요 없다.
def set_monster_location(xarr, yarr, rows, cols):
    for i in range(3):
        xarr[i] = random.randint(5, rows - 5)
        yarr[i] = random.randint(1, cols - 1)

def move():
    cols = 6
    rows = 30
    x = 5
    y = 0
    # xarr,yarr : 랜덤으로 생성될 몬스터위 좌표
    xarr = [0, 0, 0]
    yarr = [0, 0, 0]
    # 몬스터의 좌표 랜덤하게 수정
    set_monster_location(xarr, yarr, rows, cols)
    hunting_ground = 0

    key_map = {"w":-1,"s":1,"a":-1,"d":1,"k":1}
    # 탐험 시작
    while True:
        
        time.sleep(0.15)
        os.system("cls")
        # 맵 출력!
        print(location(x, y, rows, cols, xarr, yarr, hunting_ground))
        print(x,y)

        #3마리의 몬스터의 좌표들중, 일치하는 값이 있는지 탐색
        for i in range(len(xarr)):
            if x == xarr[i] and y == yarr[i]:
                #몬스터 매칭!
                battle()
                x, y = 5, 0
                continue
            #죽은걸로 판정
        if player_character.now_hp <= 0 : 
            player_character.now_hp = int(player_character.max_hp/2)
            player_character.life -= 1
            if(player_character.life > 0) : 
                print(f"특별히 부활시켜드림 ㅋㅋ 남은 라이프 {player_character.life}/3")
                time.sleep(2)
                continue
            else : 
                print("더는 부활할 수 없으셈 ㅋㅋ")
                time.sleep(2)
                break
            

        key = keyboard.read_key().lower()
        #입력 받은 값이, 딕셔너리에 있다면 key값에 맞는 value 를 반환한다.
        # key_map = {"w":1,"s":-1,"a":-1,"d":1}
        if key in key_map:
            if key == "k" :
                player_character.weapon_upgrade()
            elif key == "w" or key == "s":
                y += key_map[key]
            else:
                x += key_map[key]
        else:
            continue
        print(x,y)
        
        # 좌표 x,y의 값들이 최대,최소값의 범위를 벗어난다면 조정
        x = max(0, min(x, rows-1))
        y = max(0, min(y, cols-1))
        # max는 0보다 큰 값을 결정
        # min은 최대값보다 작은 값을 결정

         # 다음 사냥터 이동
        if x == rows - 1 and hunting_ground != 3:
            hunting_ground += 1
            x = 5
            set_monster_location(xarr, yarr, rows, cols)
        # 이전 사냥터 이동
        elif x == 0 and hunting_ground != 0:
            hunting_ground -= 1
            x = 25
            set_monster_location(xarr, yarr, rows, cols)

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
start_time=time.time() #게임시작시간측정
move()
end_time=time.time() #게임종료시간측정
print("\n즐거운 운빨게임! 좋은 플레이! 좋은 하루! 가지다 너는!")
playtime = f"{end_time-start_time:.3f} 초"
print(f"\n총 플레이 시간 [{playtime}]")


# 1. monster.py 64번줄, battle_healing의 출력 메소드 호출 코드가 give_message가 아닌 print_message
#   > give_message로 변경.
# 2. systme.py의 몬스터 기본공격시 출력 없음
#   > 랜덤값이 2 이상이면 공격 메시지 출력 추가.
# 3. over_drive스킬 메시지 출력 없음
#   > monster class의 overdrive 스킬 메시지 추가
