# binary index tree
import sys
input = sys.stdin.readline
# n:데이터 수, m:변경 횟수, k:구간합 계산 횟수
n,m,k = map(int,input().split())

# (3&-3) # 3에 대한 0 이아닌 마지막 비트 값
arr = [0]*(n+1)
tree = [0]*(n+1)

# i번쨰 까지 누적합 계산 함수
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        # 0이 아닌 마지막 비트만큼 빼가면서 이동
        i -= (i&-i)
    return result

# i번째 수를 dif 만큼 더하는 함수
def update(i,dif):
    while i <= n:
        tree[i] += dif
        i += (i&-i)

# start to end 구간 합 계산하는 함수
def interval_sum(start,end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1,n+1):
    x = int(input())
    arr[i] = x
    update(i,x)

for i in range(m+k):
    a,b,c, = map(int,input().split())
    # case of update
    if a == 1:
        update(b,c-arr[b])
        arr[b] = c
    else:
        print(interval_sum(b,c))