name_score_dict = {}
name_score_dict['홍길동'] = [90,88,55]
name_score_dict['김기영'] = [77,66,100]
name_score_dict['곽진수'] = [88,99,98]

subject_score_dict = {}
subject_score_dict['국어'] = [90,77,88]
subject_score_dict['영어'] = [88,66,99]
subject_score_dict['수학'] = [55,100,98]

f = open('../hw/mission.txt', 'w')
data = '이름   '
for i in list(subject_score_dict.keys()):
    data += i + ' '
f.write(data)
f.write('총점 평균\n')
line = '='*25 + '\n'
f.write(line)

for i in list(name_score_dict.keys()):
    data = ''
    temp = ''
    for j in range(len(subject_score_dict)):
        temp += ' ' + str(name_score_dict[i][j])
        if len(str(name_score_dict[i][j])) == 2:
            temp += '  '
        elif len(str(name_score_dict[i][j])) == 3:
            temp += ' '
        else: temp += '   '
    summation = sum(name_score_dict[i])
    data = i + temp + ': ' + str(summation) + '  ' + str(round(summation/len(subject_score_dict),1)) + '\n'
    f.write(data)
line = '='*25 + '\n'
f.write(line)

data = '총점   '
temp = 0
for i in list(subject_score_dict.keys()):
    summation = sum(subject_score_dict[i])
    temp += summation
    data += str(summation) + '  '
data += str(temp) + '\n'
f.write(data)

data = '평균   '
temp = 0
for i in list(subject_score_dict.keys()):
    avg = sum(subject_score_dict[i])/len(name_score_dict)
    temp += avg
    data += str(round(avg,1)) + '  '
data += '    ' + str(round(temp/len(subject_score_dict),1))
f.write(data)

f.close()
