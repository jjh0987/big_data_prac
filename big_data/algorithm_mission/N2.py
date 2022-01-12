# O(nlogn + n^2)
nums = sorted(list(map(int,input().split())))
ans = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        try:
            target_idx = nums[i] + nums[j]
            target = nums[nums.index(-(target_idx))]
            if target == -(target_idx):
                temp = [nums[i], nums[j]]
                temp.append(target)
                #temp.sort()
                if temp.count(-(target_idx)) > nums.count(nums[i]) or temp.count(-(target_idx)) > nums.count(nums[j]):
                    continue
                if temp in ans:
                    pass
                else:
                    ans.append(temp)
        except:pass
for i in ans:
    i.sort()
ans_li = []
for i in ans:
    if i in ans_li:
        pass
    else:
        ans_li.append(i)
print(ans_li)