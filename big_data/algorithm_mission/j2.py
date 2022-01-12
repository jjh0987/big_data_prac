nums = sorted(list(map(int,input().split())))
target = int(input())
ans = []
tar_list = []
for i in nums:
    if target > i:
        tar_list.append(i)
    elif target == i:
        ans.append(i)
    else:break
for j in range(len(tar_list)):
    factor = tar_list.pop(-1)
    ans = []
    ans.append(factor)
    for i in tar_list:
        if factor <= target:
            factor += i
            ans.append(i)
        else:
            break
    if sum(ans) == target:
        break
for i in ans:
    print(nums.index(i))

# 중복숫자 존재시 fail 추가적인 조작 필요함
# 1 1 7 11 15 -> 2 0 0