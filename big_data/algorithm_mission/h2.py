s = input()
len_s = len(s)
dp_count_odd = [0]*len_s
for i in range(len_s):
    dp_count_odd[i] += 1
    for j in range(1,len_s):
        if i-j >= 0 and i+j <= len_s:
            try:
                if s[i+j] == s[i-j]:
                    dp_count_odd[i] += 2
                else:
                    break
            except:
                break
        else:
            break

dp_count_even = [0]*len_s
for i in range(len_s):
    dp_count_even[i] += 1
    try:
        if s[i] == s[i-j]:
            case = 0
            dp_count_even[i] += 1
        elif s[i] == s[i+j]:
            case = 1
            dp_count_even[i] += 1
    except:
        pass
    for j in range(1,len_s):
        if i-j >= 0 and i+j <= len_s:
            try:
                if case == 0 and s[i+j] == s[i-j-1]:
                    if i-j == 0:
                        break
                    dp_count_even[i] += 2
                elif case == 1 and s[i+j+1] == s[i-j]:
                    dp_count_even[i] += 2
                else:
                    break
            except:
                break
        else:
            break

M_even = max(dp_count_even)
M_odd = max(dp_count_odd)
if M_even == len_s or M_odd == len_s:
    print(s)
elif M_odd > M_even:
    if M_odd > 1:
        r = int((M_odd-1)/2)
        print(s[dp_count_odd.index(M_odd)-r:dp_count_odd.index(M_odd)+r+1])
    else:
        print(s[dp_count_odd.index(M_odd)])
else:
    if M_even > 1:
        r = int((M_even-1)/2)
        can1 = s[dp_count_even.index(M_even) - r - 1:dp_count_even.index(M_even) + r + 1]
        can2 = s[dp_count_even.index(M_even) - r:dp_count_even.index(M_even) + r + 2]
        if can1[0] == can1[-1]:
            print(can1)
        else:
            print(can2)
    else:
        print(s[dp_count_even.index(M_even)])