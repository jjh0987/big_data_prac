movie = ['Dark Knight','Harry Porter','Parasite','Matrix','La La Land']
print('='*20,'영화목록','='*20)
for i in movie:
    print(i)
print('='*49)
choice = input('영화를 선택해 주세요 : ')
while 1:
    if choice not in movie:
        choice = input('예매할 수 없는 영화입니다. 영화 예매를 선택해 주세요')
    else:
        print(choice,'를 선택 하셨습니다')
        break

people = input('인원 수를 입력하세요.')
while 1:
    if type(eval(people)) is not int or eval(people) < 0:
        people = input('인원 수 를 양의 정수로 입력해 주세요.')
    else:
        print(people,'명 입니다.')
        break

coupon_dic = {}
coupon_dic['n'] = 0
coupon_dic['ORANGE'] = 2000
coupon_dic['VALENTINE'] = 3000
coupon_dic['CHRISTMAS'] = 4000
coupon_dic['INDEPENDENCE'] = 5000
choice_discount = input('할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해 주세요 :')
choice_dis = ['y','n']
while 1:
    if choice_discount not in choice_dis:
        choice_discount = input('잘못된 입력입니다. 다시 입력해 주세요 :')
    elif choice_discount == 'y':
        coupon = input('쿠폰 번호를 입력해 주세요.:')
        if coupon not in list(coupon_dic.keys()):
            print('존재하지 않는 할인권입니다')
            choice_discount = input('할인권을 다시 입려하려면 y, 아니면 n을 입력해 주세요.:')
        else:
            print(coupon_dic[coupon],'원 할인됩니다')
            break
    else:
        print('할인권을 사용하지 않았습니다.')
        coupon = 'n'
        break
original_price = 12000
print('영화 제목:',choice)
print('결제 내역')
print('-'*20)
print('인원:',people)
print('영화 제목:',choice)
print('합산 금액:',int(people)*original_price)
print('할인 금액:',coupon_dic[coupon])
print('-'*20)
price = int(people)*original_price - coupon_dic[coupon]
print('총 결제 금액:',price)

x = input().split(',')
temp = 1
for i in range(int(x[1])):
    temp = temp*int(x[0])
