import random
from rich import *
from status import MainStatus


def multiplier(x, y):
    return random.uniform(x, y)


class Monster(MainStatus):
    def give_message(self, s, target):
        # 상태 메시지 출력을 만들어서 인자값으로 보낸다!
        string = "========================================몬스터의 턴========================================\n\n"
        string += f"[{target.name}]\n"
        string += f" 체력: {target.bar(target.max_hp,target.now_hp,target.hp_color)} {target.now_hp}/{target.max_hp}\n"
        string += f" 마나: {target.bar(target.max_mp,target.now_mp,target.mp_color)} {target.now_mp}/{target.max_mp}\n"
        string += f" EXP : {target.bar(target.max_experience,target.now_experience,target.exp_color)} {target.now_experience}/{target.max_experience}\n"
        string += f" {target.weapon_name} lv.{target.weapon_level} \n{s}\n\n"
        string += f"                                        [{self.name}] lv.{self.level}\n"
        string += f"                                         체력: {self.bar(self.max_hp,self.now_hp,self.hp_color)} {self.now_hp}/{self.max_hp}\n"
        self.print_message(string)

    def __init__(self, **kwargs):  # 몬스터의 이름, 레벨, 골드를 받는다.
        super().__init__()
        self.name = kwargs.get('name')
        self.level = kwargs.get('level')
        self.max_hp = kwargs.get('hp') * kwargs.get('level')
        self.now_hp = kwargs.get('hp') * kwargs.get('level')
        self.physical_damage = kwargs.get('physical_damage') * kwargs.get('level')
        self.magical_damage = kwargs.get('magical_damage') * kwargs.get('level')
        self.experience = kwargs.get('exp') * kwargs.get('level')
        self.gold = kwargs.get('gold') * kwargs.get('level')
        self.token = True
        self.boss = False

    def skill(self, target):
        damage = round(self.magical_damage * multiplier(1.1, 1.3))  # 데미지 적용
        damage = self.critical_damage(damage)  # 크리티컬 데미지 적용
        # 스킬 메세지 적용
        skill_message = self.skill_message(damage)  # 스킬 메세지 적용
        # 인겜 데이터 수정
        self.reduce_hp(target, damage)  # 체력 감소
        self.give_message(skill_message, target)  # 메세지 출력

    def token_skill(self, target):  #
        if self.token:
            # 데미지 적용
            damage = round(self.magical_damage * multiplier(1.6, 2.0))  # 데미지 적용
            damage = self.critical_damage(damage)  # 크리티컬 데미지 적용
            # 스킬 메세지 적용
            skill_message = self.token_skill_message(damage)  # 스킬 메세지 적용
            # 인겜 데이터 수정
            self.reduce_hp(target, damage)
            self.give_message(skill_message, target)
            self.token = False
        else:
            self.skill(target)

    def battle_healing(self,target):
        if self.now_hp <= self.max_hp * 0.2:
            self.now_hp += round(self.max_hp * 0.2)
            if self.now_hp > self.max_hp:
                self.now_hp = self.max_hp
            self.give_message(f"{self.name}의 체력이 회복되었다!",target)

    def over_drive(self,target):
        if self.now_hp < self.max_hp * 0.3:
            if not self.overdrive:
                self.give_message(f"{self.name}의 오버 드라이브!" ,target)
                self.physical_damage *= 1.5
                self.magical_damage *= 1.5
                self.overdrive = True
            else:
                return False
        else:
            return False


class FireMonster(Monster):
    def skill_message(self, damage):
        text = ["화염방사", "화염자동차"]
        return f"{self.name}는 {random.choice(text)}를)사용했다! \n{damage}의 데미지를 입었다!"

    def token_skill_message(self, damage):
        text = ["불대문자", "플레어드라이브"]
        return f"{self.name}이 강력한 기술 {random.choice(text)}를 사용했다! \n{damage}의 데미지를 입었다!"


class GrassMonster(Monster):
    def skill_message(self, damage):
        text = ["잎날가르기", "덩굴채찍"]
        return f"{self.name}는 {random.choice(text)}을(를) 사용했다! \n{damage}의 데미지를 입었다!"

    def token_skill_message(self, damage):
        text = ["리프스톰", "리프블레이드"]
        return (
            f"{self.name}는 강력한 기술 {random.choice(text)}을(를) 사용했다! \n{damage}의 데미지를 입었다!"
        )


class WaterMonster(Monster):
    def skill_message(self, damage):
        text = ["물대포", "아쿠아 제트"]
        return f"{self.name}는 {random.choice(text)}를 사용했다! \n{damage}의 데미지를 입었다!"

    def token_skill_message(self, damage):
        text = ["하이드로펌프", "침뱉기"]
        return f"{self.name}는 강력한 기술 {random.choice(text)}를 사용했다! \n{damage}의 데미지를 입었다!"


class FireBossMonster(FireMonster):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.boss = True
        self.overdrive = False


class GrassBossMonster(GrassMonster):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.boss = True
        self.overdrive = False


class WaterBossMonster(WaterMonster):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.boss = True
        self.overdrive = False


monster_list = [
        #속성 / 이름 / 레벨 / 체력 / 기본 공격력 / 마법 공격력 / 경험치 / 골드
        FireMonster(
            name ="파이리",
            level= 1,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 10,
            gold= 100
        ),
        GrassMonster(
            name ="이상해씨",
            level= 1,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 10,
            gold= 100
        ),
        WaterMonster(
            name ="꼬부기",
            level= 1,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 10,
            gold= 100
        ),
        FireMonster(
            name ="브케인",
            level= 1,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 10,
            gold= 100
        ),
        FireMonster(
            name ="뚜꾸리",
            level= 1,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 10,
            gold= 100
        ),
        GrassMonster(
            name ="쥬리비안",
            level= 1,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 10,
            gold= 100
        ),
        WaterMonster(
            name ="팽도리",
            level= 1,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 10,
            gold= 100
        ),
        FireMonster(
            name ="가디",
            level= 1,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 10,
            gold= 100
        ),
        GrassMonster(
            name ="이상해꽃",
            level= 2,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 10,
            gold= 100
        ),
        WaterMonster(
            name ="어니부기",
            level= 2,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 10,
            gold= 100
        ),
        FireBossMonster(
            name ="공민영",
            level= 100,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 50,
            gold= 100
        ),
        WaterBossMonster(
            name ="나지쓰",
            level= 30,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 40,
            gold= 100
        ),
        GrassBossMonster(
            name="NO탁근",
            level= 40,
            hp= 200,
            physical_damage= 20,
            magical_damage= 20,
            exp= 50,
            gold= 100
        ),
    ]
