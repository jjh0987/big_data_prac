'''
# Q1

'''
#ans : shirt
'''
# Q2

'''
i = 0
ans = 0
while i < 1001:
    if i%3 == 0:
        ans += i
    i += 1
print(ans)
'''
# Q3

'''
i = 1
while i < 6:
    print('*'*i)
    i += 1
'''
# Q4

'''
for i in range(1,101):
    print(i)
'''
# Q5

'''
score = [70,60,55,75,95,90,80,85,100]
summation = 0
for i in score:
    summation += i
print(summation/len(score))

'''
# Q6

'''
numbers = [1,2,3,4,5]
result = [x*2 for x in numbers if x%2 == 1]
