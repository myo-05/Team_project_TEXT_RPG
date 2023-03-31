import random, status,keyboard
from rich import *

# 상속받을 페이지 status 연결


# player
class Player(status.MainStatus):
    def __init__(self, name, level=1):
        super().__init__(level)
        self.name = name
        # 무기 공격력 기본값 증가.
        self.weapon_damage_add()

    def give_message(self, s, target):
        string = "========================================플레이어 턴========================================\n\n"
        string += f"[{self.name}]\n"
        string += f" 체력 : {self.bar(self.max_hp,self.now_hp,self.hp_color)} {self.now_hp}/{self.max_hp}\n"  # 체력바
        string += f" 마나 : {self.bar(self.max_mp,self.now_mp,self.mp_color)} {self.now_mp}/{self.max_mp}\n"  # 마나바
        string += f" EXP : {self.bar(self.max_experience,self.now_experience,self.exp_color)} {self.now_experience}/{self.max_experience}\n"  # 경험치바
        string += f" 무기 :{self.weapon_name}lv.{self.weapon_level} \n{s}\n\n"  # 무기 이름 , 무기레벨, 코멘트 추가
        string += f"[{target.name}] lv.{target.level}\n체력 : {target.bar(target.max_hp,target.now_hp,target.hp_color)} {target.now_hp}/{target.max_hp}"
        self.print_message(string)


    def level_up(self):
        # 레벨업하면 스탯이 조정된다
        self.max_experience += 10
        self.max_hp += 10
        self.now_hp = self.max_hp
        self.max_mp += 10
        self.now_mp = self.max_mp
        self.physical_damage += 10
        self.magical_damage += 10
        self.critical

    def get_exp(self, target):
        # 상대방의 경험치를 받아와서 내 현재 경험치를 증가 시킨다
        self.now_experience += target.experience
        while self.now_experience >= self.max_experience:
            # 현재 경험치가, 최대 경험치보다 작을때까지
            self.now_experience -= self.max_experience  # 현재 경험치에서 최대 경험치를 뺀다.
            self.level_up()  # 레벨업을 한다.
            self.give_message("레벨업!!", target)  # 레벨업 메시지를 출력한다.
            self.level += 1

    # 스킬
    ##################################################################################################################################################################
    # 마법공격
    def magic_attack(self, target):
        # 크리티컬이 포함된 데미지 또는, 포함 안된 데미지 반환받는다.
        damage = self.critical_damage(self.magical_damage * self.intelligence)
        # 마법 공격 텍스트를 추가하고
        string = self.magic_attack_massage()
        # 마나 소모
        self.now_mp -= 10
        # 상대 방의 체력을 조정한다.
        self.reduce_hp(target, damage)
        # 마법 공격 텍스트를 출력하고
        self.give_message(string, target)

    # 회복
    def cure(self, target):
        # 자신의 행운값 + 마법공격력 / 3 만큼 체력을 회복하고, 최대 체력을 넘지 않게 조정한다.
        self.now_hp = min(
            self.now_hp + int(self.magical_damage / 3) * self.luck, self.max_hp
        )
        # 회복 스킬 메시지를 선택하고.
        s = self.cure_massage()  # 텍스트를 출력하고
        self.now_mp -= 20  # 마나를 소모하고
        # 텍스트를 출력한다.
        self.give_message(s, target)  # 텍스트를 출력한다.

    # 카운터 스킬
    def counter(self, target):
        # 데미지 값을 조정하고.
        damage = int(target.max_hp / 3) + self.magical_damage
        # 상대방의 체력을 조정한다.
        self.reduce_hp(target, damage)
        self.now_mp -= 30
        # 카운터 스킬 텍스트를 출력하고.
        self.give_message(self.counter_massage(), target)


# 상속, 수학 선생님
########################################################################################################################################################
class Math_Teacher(Player):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.critical = 0.30
        self.job = "수학 선생님"
        self.weapon_name = "삼각함수의 칼날"

    def magic_attack_massage(self):  # self 넣어야함
        text = ["숙제 2배~", "숙제가 적지??", "보강 하자"]
        return "수학 선생님이, 갑작스레 말씀하셨다. [ 공격 스킬 ] : " + str(random.choice(text))

    def cure_massage(self):
        text = ["오늘 휴강 ~ ^^", "루미 큐브 할까?", "숙제 줄여 줄까?"]
        return " 학생들이 환호합니다!! [ 회복 스킬 ] 수학 선생님 : " + str(random.choice(text))

    def counter_massage(self):
        text = ["숙제 50배!! ", "부모님께 말씀 드린다?", "대학가면 애인 생길거야"]
        return " 수학 선생님이 비장한 표정을 짓고, 분위기가 고조되었다. [ 필살기! ]: " + str(random.choice(text))


############################################################################################################################################################
class Muggle(Math_Teacher):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.physical_damage = 60
        self.job = "머글"
        self.weapon_name = "떡갈나무지팡이"
        # 스킬별 메시지 출력 - 수학 선생님

    ########################################################################################################################################################
    def magic_attack_massage(self):  # self 넣어야함
        text = ["지팡이로 때리겠쓰", "스탯을 실수로 힘으로 찍어버렸다.", "마법책으로 때리겠쓰"]
        return "머글이, 근육을 꿈틀거리며 노려본다. [ 공격 스킬 ] : " + str(random.choice(text))

    def cure_massage(self):
        text = ["도망가겠쓰", "회복하겠쓰", "피 채우겠쓰"]
        return " 근육들이 회복 중에 있습니다. [ 회복 스킬 ] 머글쓰 : " + str(random.choice(text))

    def counter_massage(self):
        text = ["샷건 쏘겠쓰", "형은 말하지 않아도, 다~ 아는 방법이 있다?", "전변호사 처리해! 지지지직"]
        return " 진실의 방으로 입장하셨습니다 !! [ 필살기! ]: " + str(random.choice(text))


#############################################################################################################################################################
class Flaming(Math_Teacher):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.max_hp = 250
        self.now_hp = self.max_hp
        self.job = "악플러"
        self.weapon_name = "침뱉는 무선키보드"
        # 스킬별 메시지 출력 - 악플러

    ########################################################################################################################################################
    def magic_attack_massage(self):  # self 넣어야함
        text = ["어쩔티비", "쿠쿠루 삥뽕~", "안물 안궁"]
        return "피시방에 잼민이의 목소리가 우렁차게 울립니다! [ 공격 스킬 ] : " + str(random.choice(text))

    def cure_massage(self):
        text = ["맘스터콜", "구몬 읽기", "후원하고 환불해달라 때쓰기"]  # 대규모 맘카페 엄마들의 댓글테러를 말함
        return "조카들이 당신의 방에 쳐들어왔습니다! [ 회복 스킬 ] : " + str(random.choice(text))

    def counter_massage(self):
        text = ["저격하기", "샷건치기", "악플달기"]
        return "내가 한거 아니라고 !!! 빼애애액 ! [ 필살기! ]: " + str(random.choice(text))


#############################################################################################################################################################
class Boss(Math_Teacher):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.magical_damage = 90
        self.job = "부장님"
        self.weapon_name = "담배를 부르는 으아메리카노"

        # 스킬별 메시지 출력 - 부장님

    ########################################################################################################################################################
    def magic_attack_massage(self):  # self 넣어야함
        text = [
            "부엉이가 물에 빠지면? 첨부엉 읔ㅋㅋㅋㅋㅋㅋㅋㅋ",
            "부엉이가 바다에 빠지면? 씨부엉ㅋㅋㅋㅋㅋㅋㅋㅋ",
            "차가 죽으면??  부르릉ㅋㅋㅋㅋㅋㅋㅋㅋ",
        ]

        return "부장님의 개그에, 어쩔 수 없이 웃으셔야 합니다! [ 공격 스킬 ] : " + random.choice(text)

    def cure_massage(self):
        text = [
            "커피 한 잔 씩 해야지?",  # 대규모 맘카페 엄마들의 댓글테러를 말함
            "라떼는 말이야?",
            "손대리 오늘 회식있는거 알지?",
        ]
        return "부장님이 집에 들어가기 싫어합니다!! [ 회복 스킬 ] : " + str(random.choice(text))

    def counter_massage(self):
        text = ["먼저 퇴근들해~(단호,하지만 눈치가 보인다..)", "이걸 보고서라고 써온거야?", "요즘 MZ은 말이야?!"]
        return "5년차가 이것도 못해?! (부장님이 화나셔서 두피도 빨개졌습니다.)[ 필살기! ]: " + str(
            random.choice(text)
        )


#############################################################################################################################################################
class Smoker(Math_Teacher):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.max_mp = 250
        self.now_mp = self.max_mp
        self.job = "애연가"
        self.weapon_name = "스모커의 전자담배"

        # 스킬별 메시지 출력 - 애연가

    ########################################################################################################################################################
    def magic_attack_massage(self):  # self 넣어야함
        text = ["도넛 발싸!!!!!!!", "가스 가스 가스!! 화생방 경보!", "술 자리에, 당신만 남겨두고 담배피러 갑니다!"]
        return "스모커가 연기를 당신에게 뿜습니다. [공격 스킬] : " + str(random.choice(text))

    def cure_massage(self):
        text = [
            "무호흡 흡연",  # 대규모 맘카페 엄마들의 댓글테러를 말함
            "전자 담배를 충전합니도",
            "스모커가 당신의 돛대를 뺏어갑니다!",
        ]
        return "새해에는 금연 할려 했는데...[ 회복 스킬 ] : " + str(random.choice(text))

    def counter_massage(self):
        text = ["너는 이런거 배우지 마라...", "뭉게 뭉게 구름 만들기~", "폴폴~~ 냄새 풍기기"]
        return "난 담배는 피워도 바람은 안피워[ 필살기! ]: " + str(random.choice(text))


#############################################################################################################################################################
