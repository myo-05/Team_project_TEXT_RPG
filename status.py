import random
from rich import *


class MainStatus:
    # 생성자
    def __init__(self, level=1):
        self.level = level
        self.max_experience = 100
        self.now_experience = 0
        self.max_hp = 5000
        self.now_hp = max(self.max_hp, 0)
        self.max_mp = 100
        self.now_mp = max(self.max_mp, 0)
        self.physical_damage = 1
        self.magical_damage = 1
        self.critical = 0.15
        self.strength = 10
        self.intelligence = 10
        self.dexterity = 10
        self.luck = 10
        self.weapon_level = 1
        self.weapon_name = ""
        self.gold = 1000
        self.hp_color = "[bold red]" + "■" + "[/bold red]"
        self.mp_color = "[bold blue]" + "■" + "[/bold blue]"
        self.exp_color = "[bold green]" + "■" + "[/bold green]"

    ## 비례법한칙을 이용, 체력 게이지바
    def bar(self, max, now, box_color):  # max:최대값, now:현재값
        try:  # 0으로 나누는 오류를 방지하기 위해 try문을 사용합니다.
            bar = 30  # 바의 길이
            now = round(now / max * bar)  # 바의 길이
            return box_color * now + "□" * (bar - now)  # 바를 출력합니다.
        except ZeroDivisionError:  # 0으로 나누는 오류가 발생하면
            return box_color * now + "□" * (bar - now)  # 바를 출력합니다.

    def print_info(func):  # 데코레이터
        def info(self, *args):  # *args:가변인자
            string = "─" * 100 + "\n"  # 상단 라인
            # 상단 라인

            # info
            message = func(self, *args)  # 메시지
            # 메시지
            string += f"\n{message}\n\n" + "─" * 100  # 메시지 출력과, 하단 라인 출력
            # 메시지 출력과, 하단 라인 출력
            print(string)  # 출력

        return info

    @print_info
    def print_message(self, s):
        return s

    def critical_damage(self, damage):
        random_value = random.uniform(0, 1)  # 0~1사이에 랜덤한 실수 생성! ex)0.15,0.7...
        # 랜덤값보다 자신의 크리티컬 값이 크다면 운빨 공격 발동(if문이 참이 됩니다.)
        if random_value < self.critical:
            value = random.randint(damage * 2, damage * 3)
            return value + damage
            # 자신의 데미지두배 ~ 세배 중  랜덤 값을 반환 받는다
        return damage

    def reduce_hp(self, target, damage):
        target.now_hp -= damage
        target.now_hp = max(target.now_hp, 0)

    def attack(self, target):
        damage = self.critical_damage(self.physical_damage)
        target.now_hp -= damage
        target.now_hp = max(target.now_hp, 0)

    def weapon_damage_add(self):
        self.physical_damage += 10 * self.weapon_level  # 플레이어 물리공격력
        self.magical_damage += 10 * self.weapon_level  # 플레이어 마법공격력

    def upgrade(self):  # 아이템 업그레이드
        if self.gold >= 1000:  # 플레이어 골드가 1000이상일때
            self.gold -= 1000  # 플레이어 골드 1000차감
            self.weapon_level += 1  # 아이템 레벨 1증가
            self.damage_add(self)
        else:
            print("골드가 부족합니다.")  # 플레이어 골드가 1000이하일때
            return  # 함수 종료

    def get_gold(self, target):
        value = random.uniform(0, 1)
        if value <= 0.3:
            self.gold += 30 * target.level
