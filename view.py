from datetime import datetime
from rich import *
import keyboard, time, os, random, system, player


# 맵 그리기
def location(x, y, rows, cols, xarr, yarr, hunting_ground):
    # 테두리와, 배열 초기값
    arr = [" " * rows] * cols
    string = "□ = you   ■ : monster\n"
    if hunting_ground == 0:
        string += "               다음사냥터>>>\n"
    elif hunting_ground == 3:
        string += "<<< 돌아가기\n"
    else:
        string += "<<< 돌아가기     다음사냥터>>>\n"
    string += "─" * 30 + "\n"
    # 반복문을 돌며, 플레이어의 위치, 몬스터의 위치를 탐색한다.
    for i in range(cols):
        for j in range(rows):
            if i == y and j == x:
                string += "ㅁ"
            elif xarr[0] == j and yarr[0] == i:
                string += "■"
            elif xarr[1] == j and yarr[1] == i:
                string += "■"
            elif xarr[2] == j and yarr[2] == i:
                string += "■"
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


def move(player: player.Adventurer):
    cols = 6
    rows = 30
    x = 5
    y = 0
    # xarr,yarr : 랜덤으로 생성될 몬스터위 좌표
    xarr = [0, 0, 0]
    yarr = [0, 0, 0]
    set_monster_location(xarr, yarr, rows, cols)
    hunting_ground = 0

    # 탐험 시작
    while True:
        time.sleep(0.15)
        os.system("cls")
        # 맵 출력!
        print(location(x, y, rows, cols, xarr, yarr, hunting_ground))

        for i in range(len(xarr)):
            if x == xarr[i] and y == yarr[i]:
                # 결투 매칭
                x, y = 5, 0
                continue

        if x == rows - 1 and hunting_ground != 3:
            hunting_ground += 1
            x = 5
            set_monster_location(xarr, yarr, rows, cols)

        if x == 0 and hunting_ground != 0:
            hunting_ground -= 1
            x = 25
            set_monster_location(xarr, yarr, rows, cols)

        if keyboard.is_pressed("w") and keyboard.is_pressed("W"):
            y -= 1
            time.sleep(0.01)
        elif keyboard.is_pressed("s") and keyboard.is_pressed("S"):
            y += 1
            time.sleep(0.01)
        elif keyboard.is_pressed("s") and keyboard.is_pressed("A"):
            x -= 1
            time.sleep(0.01)
        elif keyboard.is_pressed("d") and keyboard.is_pressed("D"):
            x += 1
            time.sleep(0.01)
        else:
            continue
        if x >= rows:
            x = rows - 1
        elif x < 0:
            x = 0
        if y >= cols:
            y = cols - 1
        elif y < 0:
            y = 0
