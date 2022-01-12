arr = list(map(int,input().split()))
sub_arr = arr[arr[arr.index(min(arr))]:]
print(max(sub_arr)-sub_arr[0])