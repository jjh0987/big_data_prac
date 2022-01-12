customer = {'홍길동': [1234, 0], '길동홍': [2345, 1000]}

class CAccount:
    global customer
    def __init__(self,name):
        self.cust_name = name # 클래스 안에서 다른 함수에서 cust_name으로 활동가능
        print(f'{name} 통장')
        print('-' * 20)
        print('1.잔액확인\n2.입금\n3.출금\n4.종료\n' + '-' * 20)
        choice = int(input('메뉴를 선택해 주세요.'))
        if choice == 4:
            print('계좌 거래가 종료되었습니다.')
        else:
            customer_pass = int(input('계좌 비밀번호를 입력해 주세요'))
            if customer_pass == customer[name][0]:
                if choice == 1:
                    print(f'잔액은 {customer[name][1]}원 입니다.')
                elif choice == 2:
                    temp = int(input('입금할 금액을 알려주세요.'))
                    customer[name][1] = CAccount.deposit('',customer[name][1], temp)
                    print(f'{temp}원 입금되었습니다. 잔액은 {customer[name][1]}원 입니다.')
                else:
                    temp = int(input('출금할 금액을 알려주세요'))
                    if temp < 0:
                        print('정확한 금액을 입력하세요.')
                    elif customer[name][1] - temp < 0:
                        print('잔액부족, 거래가 거절 되었습니다.')
                    else:
                        customer[name][1] = CAccount.withdraw('',customer[name][1],temp)
                        print(f'{temp}원 출금되었습니다. 잔액은 {customer[name][1]}원 입니다.')
            else:
                print('비밀번호가 틀렸습니다.')
    def deposit(self, x,temp):
        return x + temp

    def withdraw(self, x,temp):
        return x - temp
    #def check(self):
    #   print(self.cust_name)

x =  CAccount('홍길동')