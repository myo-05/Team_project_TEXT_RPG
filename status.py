import os,random
class MainStatus:
    #생성자
    def __init__(self,name,job,level=1):
        self.job = job
        self.name = name
        self.level = level
        self.max_experience = 100
        self.now_experience = 0
        self.max_hp = 100
        self.now_hp = self.max_hp 
        self.max_mp = 100
        self.now_mp = self.max_mp
        self.physical_damage = 20
        self.magical_damage = 30
        self.critical = 0.15
        self.strength = 10
        self.intelligence = 10
        self.dexterity = 10
        self.luck = 10

    
    ## 비례법한칙을 이용, 체력 게이지바
    def bar(self,max,now):
        try :
            bar = 30
            now = round(now/max*bar)
            return "■" * now + "□"*(bar-now)
        except ZeroDivisionError:
            return "■" * now + "□"*(bar-now)
    
    def print_info(func):
        def info(self,*args):
            os. system('cls')
            string = "─" * 100+"\n"
            # 상단 라인
            
            # info
            message = func(self,*args)
            # 메시지
            string += f"\n{message}\n\n"+"─" * 100
            #메시지 출력과, 하단 라인 출력
            print(string)
        return info
    
    @print_info
    def print_message(self, s):
        return s
    
    def critical_damage(self,damage):
        random_value = random.uniform(0,1) # 0~1사이에 랜덤한 실수 생성! ex)0.15,0.7...
        # 랜덤값보다 자신의 크리티컬 값이 크다면 운빨 공격 발동(if문이 참이 됩니다.)
        if(random_value < self.critical):
            value = random.randint(damage*2,damage*3)
            return value + damage
            # 자신의 데미지두배 ~ 세배 중  랜덤 값을 반환 받는다
        return damage

    def reduce_hp(self,target,damage):
        target.now_hp -= damage
        target.now_hp = max(target.now_hp,0)

    def attack(self,target):
        damage = self.critical_damage(self.physical_damage)
        target.now_hp -= damage
        target.now_hp = max(target.now_hp,0)

 
