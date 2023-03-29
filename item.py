#             공격              회복                 방어               소환(보류)             카운터
# 수학쌤 : 숙제 2배~        / 오늘 휴강 ^^(회복)   / 안 통해(방어)    / 간식 먹을 사람?          / 숙제 50배
# 악플러 : 어쩔티비         /맘스터콜                /악플달기           /샷건치기                /저격하기
# 머글쓰 : 지팡이로 때리겠쓰 / 도망가게쓰             / 마법책으로 막겠쓰     / DM보내겠쓰            / 샷건쏘겠쓰
# 부장님 : 아재드립(공격)   / 커피한잔씩해야지?(회복)   / 라떼는말이야(방어)   / 회식해야지?(소환)       / 먼저 퇴근들 해(카운터)
# 애연가:   도넛 발사!      /무호흡 흡연              /냄새 풍기기        /뭉게 뭉게 구름 만들기     /너는 이런거 배우지 마라...


# 아이템 종류 | 무기(physical_damage,magical_damage) 모자(max_hp,max_mp,intelligence) 갑옷(max_hp,max_mp,strength) 장갑(max_hp,max_mp,dexterity) 신발(max_hp,max_mp,luck) 
# 직업별 아이템 만들기
    #                    무기            모자            갑옷            장갑            신발
    #1 수학쌤 : 삼각함수의 칼날     / 피타고라스의 모자  /  수식의 방어막     /  미적분의 손목보호대    /   실내슬리퍼 
    #2 악플러 : 무선키보드 / 험한 말 하는 삿갓 / 극악무도한 비판 갑옷 / 비난 날리는 손목 / 도주용 오리발
    #3 머글쓰 : 떡갈나무지팡이 /  
    #4 부장님 : 결제판 / 빛나는머리 / 빛바랜체크무늬셔츠 /  / 삼선슬리퍼
    #5 담배맨 : 전자담배 / 

class Item:
     def __init__(self,name,job,level=1):
        self.job = job
        self.name = name
        self.level = level 

class Weapon(Item):
    def __init__(self,name,level,job):
        super().__init__()
        self.job=1

        self.physical_damage += 10*self.level
        self.magical_damage += 10
        # self.critical
        print("분필이 장착되었습니다.")


# class Cap

# class Armor

# class Gloves

# class Shoes