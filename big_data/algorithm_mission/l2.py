def summation(s):
    l = s.split() # list map (int,input().split)
    l_in = []
    for i in l:
        l_in.append(eval(i))
    M_idx = l_in.index(max(l_in))
    l_temp = l_in[M_idx:]
    l_temp.reverse()
    ML = [l_in[0]]
    MR = [l_temp[0]]
    for i in range(M_idx):
        try:
            if ML[i] >= l_in[i+1]:
                ML.append(ML[i])
            else:
                ML.append(l_in[i+1])
        except:break
    for i in range(len(l_temp)):
        try:
            if MR[i] >= l_temp[i+1]:
                MR.append(MR[i])
            else:
                MR.append(l_temp[i+1])
        except:break
    return sum(MR)+sum(ML)-max(l_in)-sum(l_in)

print(summation('0 1 0 2 1 0 1 3 2 1 2 1'))