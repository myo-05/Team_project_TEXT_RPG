import random, time
from rich import *
from status import MainStatus


def multiplier(x, y):
    return random.uniform(x, y)


class Monster(MainStatus):
    def give_message(self, s, target):
        # 상태 메시지 출력을 만들어서 인자값으로 보낸다!
        string = "========================================플레이어의 턴!========================================\n\n"
        string += f"[{target.name}]\n"
        string += f" 체력: {target.bar(target.max_hp,target.now_hp,target.hp_color)} {target.now_hp}/{target.max_hp}\n"
        string += f" 마나: {target.bar(target.max_mp,target.now_mp,target.mp_color)} {target.now_mp}/{target.max_mp}\n"
        string += f" EXP : {target.bar(target.max_experience,target.now_experience,target.exp_color)} {target.now_experience}/{target.max_experience}\n"
        string += f" {target.weapon_name} lv.{target.weapon_level} \n{s}\n\n"
        string += f"[{self.name}] lv.{self.level}\n 체력: {self.bar(self.max_hp,self.now_hp,self.hp_color)} {self.now_hp}/{self.max_hp}\n"
        self.print_message(string)

    def __init__(
        self, name, level, hp, physical_damage, magical_damage, exp, gold
    ):  # 몬스터의 이름, 레벨, 골드를 받는다.
        super().__init__(name, level)  # 상속받은 클래스의 생성자를 호출한다.
        self.max_hp = hp * level
        self.now_hp = hp * level
        self.physical_damage = physical_damage * level
        self.magical_damage = magical_damage * level
        self.experience = exp * level
        self.gold = gold * level
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
        time.sleep(2)
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

    def battle_healing(self):
        if self.now_hp <= self.max_hp * 0.2:
            self.now_hp += round(self.max_hp * 0.2)
            if self.now_hp > self.max_hp:
                self.now_hp = self.max_hp
            self.give_message(f"{self.name}의 체력이 회복되었다!")

    def over_drive(self):
        self.give_message(f"{self.name}의 오버 드라이브!")
        if not self.overdrive:
            if self.now_hp < self.max_hp * 0.3:
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
    def __init__(self, name, level, hp, physical_damage, magical_damage, exp, gold):
        super().__init__(name, level, gold, hp, physical_damage, magical_damage, exp)
        self.boss = True
        self.overdrive = False


class GrassBossMonster(GrassMonster):
    def __init__(self, name, level, hp, physical_damage, magical_damage, exp, gold):
        super().__init__(name, level, gold, hp, physical_damage, magical_damage, exp)
        self.boss = True
        self.overdrive = False


class WaterBossMonster(WaterMonster):
    def __init__(self, name, level, hp, physical_damage, magical_damage, exp, gold):
        super().__init__(name, level, gold, hp, physical_damage, magical_damage, exp)
        self.boss = True
        self.overdrive = False


# # monster1 = FireMonster('리자몽',1,1)
# # monster1 = WaterMonster('리자몽',1,1)
# monster1 = GrassMonster("리자몽", 1, 1)
# monster2 = FireMonster("파이리", 1, 1)
# monster1.token_skill(monster2)
# time.sleep(2)
