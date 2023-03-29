import player
from player import *

# 사용자 이름 입력!
name = input()

job_list = [ 
    [Boss(name)], # 0번
    [Math_Teacher(name)],# 1번
    [Muggle(name)], # 2번
    [Smoker(name)], # 3번
    [Flaming(name)] # 4번
]
#직업 선택 !
job = int(input())-1  #리스트 0번 = 1번 직업이니까 1을 뺀다 이거죠?? ㅇㅇ

print(job_list[job][0].name)

job_list[job][0].magic_attack()












# # - 규칙
# #     - 협업을 위해 코드 컨벤션을 정해야 합니다.
# #     - 기능별로 파일을 나눠 작업해야 합니다.
# #     - 함수, 클래스를 사용해 중복된 코드 사용을 최소화해야 합니다.

# # - 기능
# #     - 플레이어의 직업이 있고 직업별 특수 능력이 있어야 합니다.
# #     - 몬스터와 1:N or N:M 전투가 가능해야 합니다.
# #     - 몬스터 사냥 성공시 보상에 따른 게임 진행이 되어야 합니다.

# # 기본에 충실하자 !
# # 가장 중요한것, 자신의 코드를 직관적이고 소개할 수 있게끔 만든다!

# # 필수 기능
# 스토리main.py(1/1명) 스토리 + 어디에 어떤 액션이 들어갈지 - K ... time, for, os rich

# # 클래스 제작 -
# 아이템 클래스 (1/1명) + 상점 05쨩 + 인벤토리연구 강화!
# #  >>>>>>>>인벤토리<<<<<<<<<<<이게 은근 어려울듯 < 장비 저장하는 인벤토리 ㅎㅎㅎㅎㅎ
# #부모 클래스(status)
#     cheack status 이건 무조건 부모
    
#     # 상속(2인1조)
#         Monster() 몬스터(1/1명)<승호쟝 예약 드루와 - ! - exp gold
#             #몬스터 스킬 
#     몬스터가 스킬을 사용했다 ! 제네시스! 플레이어 전체 사망
#         Player() 플레이어(1/1명) 폰캡틴 쏜 N이쨩 힘들면 help 나쓰쨩 쏜나! help n 쏜나씅! 집합!
#             직업
#             스킬
#             # attack(m1,m2)
#             #     m1.hp-= damage
#             #     m2.hp-= damage

# ★★★★★★★★★★★★★★★★★★★
# 아이템 1) 캐릭터 생성시 직업선택, 무기 지급 이후부터는 강화식.(골드소비) exp gold self.str_ += enchant_level(강화도)*10 
# ★★★★★★★★★★★★★★★★★★★

# # 배틀 시스템 같이!
# # 스펙이 낮으면 도망치기 ~
# # 플레이어 > 몬스터1 > 몬스터2 > 몬스터3
#  3고정
# 발열 - 하루종일 핸드폰 게임 @@@@@
# 플레이어 몬스터n?

# monster_dict = {
#         "1": Monster("악플러", 100, 20),
#         "2": Monster("수학쌤", 200, 30),
#         "3": Monster("문순실", 300, 40),
#     }

# m1=mosnter()
# m2=monster()
# monstercol = [m1,m2]
# player.attack(monstercol[int(input())-1])
# 1


# class Allclass:
#     def __init__(self, ):
#         self
# # 디테일
# # 저장 기능
# # 스토리와,오프닝
# # 장비창
# # 획득 - 경험치
# # 맵 이동 

# 스토리 1명, 아이템 클래스 1명, 플레이어 1명, 몬스터 1명 
# # 상점 입장 !!

# # 1 파괴자의 장갑 100원에 살 수 있다.
# # 2 쏜의 비밀 수첩을 99999원에 살 수 있다.


# # player team choice 1m, 2m, 3m
# # monster team choice 1m,2m, 3m






