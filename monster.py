import random,time
from status import MainStatus

def multiplier(x,y):
    return random.uniform(x,y)


class Monster(MainStatus):
    def give_message(self,s,target):
        #상태 메시지 출력을 만들어서 인자값으로 보낸다!
        string = f"{self.bar(target.max_hp,target.now_hp)}\n{target.name} 체력 : {target.now_hp}/{target.max_hp}\n{s}"
        self.print_message(string)

    def __init__(self,name,level,gold):
        super().__init__(self)
        self.name=name
        self.level = level
        self.gold= gold
        self.token=True

    def skill(self,target):
        damage = round(self.magical_damage * multiplier(1.1,1.3))
        damage=self.critical_damage(damage)
        #스킬 메세지 적용
        skill_message = self.skill_message(damage)
        #인겜 데이터 수정
        self.reduce_hp(target,damage)
        self.give_message(skill_message,target)

    def token_skill(self,target):
        if self.token == True:
            #데미지 적용
            damage = round(self.magical_damage * multiplier(1.6,2.0))
            damage = self.critical_damage(damage)
            #스킬 메세지 적용
            skill_message = self.token_skill_message(damage)
            #인겜 데이터 수정
            self.reduce_hp(target,damage)
            self.give_message(skill_message,target)
            self.token=False
        else:
            self.skill(target)

class FireMonster(Monster):
    def skill_message(self,damage):
        text=['화염방사','화염자동차']
        return f"{self.name}이 {random.choice(text)}를 사용했다! \n{damage}의 데미지를 입었다!"
    
    def token_skill_message(self,damage):
        text=['불대문자','플레어드라이브']
        return f"{self.name}이 강력한 기술 {random.choice(text)}를 사용했다! \n{damage}의 데미지를 입었다!"
        
class GrassMonster(Monster):
    def skill_message(self,damage):
        text=['잎날가르기','덩굴채찍']
        return f"{self.name}이 {random.choice(text)}를 사용했다! \n{damage}의 데미지를 입었다!"
    
    def token_skill_message(self,damage):
        text=['리프스톰','리프블레이드']
        return f"{self.name}이 강력한 기술 {random.choice(text)}를 사용했다! \n{damage}의 데미지를 입었다!"


class WaterMonster(Monster):
    def skill_message(self,damage):
        text=['물대포','아쿠아 제트']
        return f"{self.name}이 {random.choice(text)}를 사용했다! \n{damage}의 데미지를 입었다!"
    
    def token_skill_message(self,damage):
        text=['하이드로펌프','침뱉기']
        return f"{self.name}이 강력한 기술 {random.choice(text)}를 사용했다! \n{damage}의 데미지를 입었다!"

class FireBossMonster(FireMonster):
    pass

class GrassBossMonster(GrassMonster):
    pass

class WaterBossMonster(WaterMonster):
    pass

# monster1 = FireMonster('리자몽',1,1)
# monster1 = WaterMonster('리자몽',1,1)
monster1 = GrassMonster('리자몽',1,1)
monster2 = FireMonster('파이리',1,1)
monster1.token_skill(monster2)
time.sleep(2)
