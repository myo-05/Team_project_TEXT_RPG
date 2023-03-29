# 여기다가 스토리 짤거라고 아 ㅋㅋ
# 투명드래곤이 울부짖었다 크아앙
# 세상이 멸망해따

print("""
      아재 드래곤 : 크아아아아앙! 나는 아재드래곤이다! 부엉이가 바다에 가면?
      (Enter를 누르시면 다음 문장이 실행됩니다)
""")
input()
print("아재 드래곤 : 씨부엉 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ, 그러면 부엉이가 바다에서 헤엄을 치면??")
input()
print("아재 드래곤 : 첨부엉 첨부엉 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ .... ㅈㅅ 다 죽여 버리겠다! ")
input()
print("나 : ....뭐지?? . 여긴 어디지 ?")
input()
print("세상에 멸망 했습니다.. ")
input()
# 플레이어 이름 설정
while True:
    name = input("\n사용할 닉네임을 입력해주세요: ")
    if name.strip():
        break
    else:
        continue

# 공격타입 선택
print("\n 직업을 선택하세요. ")
while True:
    attack_type = input("""1.애연가 2. 마법사 3. 잼민이 4. 부장님 5.수학선생님
""")
    if attack_type != "1" and attack_type != "2" and attack_type != "3" and attack_type != "4" and attack_type != "5":
        print("잘못된 입력입니다. 1~5 사이 숫자를 입력하세요.")
    else:
        break
    
# attack_type 딕셔너리
attack_type_dict = {
    "1": "애연가",
    "2": "마법사",
    "3": "잼민이",
    "4": "부장님",
    "5": "수학선생님",
}


# 타이틀