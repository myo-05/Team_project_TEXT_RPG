from rich import *
from main import *
import keyboard, time, os, random


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

    key_map = {"w":-1,"s":1,"a":-1,"d":1}
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
                battle()
                x, y = 5, 0
                continue

        key = keyboard.read_key().lower()
        #입력 받은 값이, 딕셔너리에 있다면 key값에 맞는 value 를 반환한다.
        # key_map = {"w":1,"s":-1,"a":-1,"d":1}
        if key in key_map:
            if key == "w" or key == "s":
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