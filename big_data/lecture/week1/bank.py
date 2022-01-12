class CAccount:
    class Error:
        def accerr(self):
            print('정확한 금액을 입력하세요.')
        def lackerr(self):
            print('잔액부족, 거래가 거절되었습니다.')
        def passerr(self):
            print('비밀번호가 틀렸습니다.')

    def __init__(self,owner,passward = '1234'):
        self.owner = owner
        self.balance = 0
        self.passward = passward
        self.display_title_Message()
        self.transaction()
    def transaction(self):
        choice = int(input('메뉴를 선택해 주세요.'))
        if choice == 4:
            self.choiceEnd()
        else:
            passward_inp = int(input('계좌 비밀번호를 입력해 주세요.'))
            if passward_inp == self.passward:
                if choice == 1:
                    self.dispBalance()
                elif choice == 2:
                    self.deposit()
                else:
                    self.withdraw()
            else:
                Error().passerr()
    def deposit(self):
        temp = int(input('입금할 금액을 알려주세요.'))
        print(f'{temp}원 입금되었습니다. 잔액은 {self.balance + temp}원 입니다.')
    def withdraw(self):
        temp = int(input('출금할 금액을 알려주세요.'))
        if temp < 0:
            Error().accerr()
        elif self.balance - temp < 0:
            Error().lackerr()
        else:
            print(f'{temp}원 출금되었습니다. 잔액은{self.balance - temp}원 입니다.')
    def display_title_Message(self):
        print(f'{self.owner} 통장')
        print('-' * 20)
        print('1.잔액확인\n2.입금\n3.출금\n4.종료\n' + '-' * 20)
    def dispBalance(self):
        print(f'잔액은 {self.balance}원 입니다.')
    def choiceEnd(self):
        print('계좌 거래가 종료되었습니다.')

check = CAccount('홍길동',1111)