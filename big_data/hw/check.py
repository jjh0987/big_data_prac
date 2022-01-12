class CAccount:
    def __init__(self, amount=0):
        self.amount = amount

    def deposit(self, dmoney):  # 입금 업무를 위한 함수
        while dmoney < 0:
            dmoney = int(input("정확한 금액을 입력하세요."))
            continue
        while dmoney >= 0:
            self.amount += dmoney
            print("%d 원 입금되었습니다. 잔액은 %s 원입니다." % (dmoney, self.amount))
            return 'success'

    def withdraw(self, wmoney):  # 출금 업무를 위한 함수
        while wmoney < 0 or wmoney > self.amount:
            if wmoney < 0:
                wmoney = int(input("정확한 금액을 입력하세요."))
                break
            else:
                print("잔액부족으로 거래가 거절되었습니다.")
                break
        while wmoney >= 0 and wmoney <= self.amount:
            self.amount -= wmoney
            print("%d 원 출금되었습니다. 잔액은 %d 원입니다." % (wmoney, self.amount))
            return 'success'


owner = "홍길동"
rpw = '0603'

print("%s 통장\n" % owner + "-" * 15)
print("""
1. 잔액확인
2. 입금
3. 출금
4. 종료
""" + "-" * 15)

men = int(input("메뉴를 선택해 주세요 : "))

while True:
    if men in [1, 2, 3, 4]:
        pw = input("계좌 비밀번호를 입력해 주세요 : ")
        break

    else:
        print("잘못된 메뉴입니다.")
        men = int(input("메뉴를 다시 선택해 주세요 : "))
        continue

while pw != rpw:
    print("비밀번호가 잘못되었습니다.")
    pw = input("계좌 비밀번호를 입력해 주세요: ")

cac = CAccount(10000)

while pw == rpw:
    if men == 1:
        amount = cac.amount
        print("1번 선택: 잔액은 %d 원입니다." % amount)
        men = int(input("다른 메뉴를 선택하시겠습니까? (1. 잔액확인 2. 입금 3. 출금 4. 종료)  "))

    elif men == 2:
        amount = cac.amount
        dmoney = int(input("2번 선택: 입금할 금액을 알려주세요. "))
        result = cac.deposit(dmoney)
        if result == "success":
            men = int(input("다른 메뉴를 선택하시겠습니까? (1. 잔액확인 2. 입금 3. 출금 4. 종료)"))
            continue

    elif men == 3:
        amount = cac.amount
        wmoney = int(input("3번 선택: 출금할 금액을 알려주세요. "))
        result = cac.withdraw(wmoney)
        if result == "success":
            men = int(input("다른 메뉴를 선택하시겠습니까? (1. 잔액확인 2. 입금 3. 출금 4. 종료)"))
        else:
            break

    elif men == 4:
        print("\n계좌 거래가 종료되었습니다.\n")
        print("=" * 30)
        pw = '0214'  # 맨 위 while문 탈출을 위해 pw 값 변경
        break





