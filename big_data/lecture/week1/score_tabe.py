class Cstudent:
    def __init__(self,*args):
        self.cnt = len(args)
        self.total = 0
        self.sublist = []
        for i in range(self.cnt):
            self.sublist.append(args[i])
    def getName(self):
        return str(self.sublist[0])
    def getKor(self):
        return str(self.sublist[1])
    def getEng(self):
        return str(self.sublist[2])
    def getMath(self):
        return str(self.sublist[3])
    def getTotal(self):
        for i in range(1,self.cnt):
            self.total += self.sublist[i]
        return str(self.total)
    def getAvg(self):
        return str(round(self.total/(self.cnt-1),1))

student_list = []
student_list.append(Cstudent('홍길동',90,88,55))
student_list.append(Cstudent('박주형',77,66,100))
student_list.append(Cstudent('송채원',88,99,98))

f = open('hw/mission_class.txt', 'w')
data = '이름   '
for i in list(['국어','영어','수학']):
    data += i + ' '
f.write(data)
f.write('총점 평균\n')
line = '=' * 25 + '\n'
f.write(line)
for i in student_list:
    f = open('hw/mission_class.txt', 'a')
    data = i.getName()+' '+i.getKor()+\
           '  '+i.getEng()+'  '+i.getMath()+\
           ' : '+i.getTotal()+'  '+i.getAvg()+'\n'
    f.write(data)
line = '=' * 25 + '\n'
f.write(line)

data = '총점   '
listK = [int(i.getKor()) for i in student_list]
listE = [int(i.getEng()) for i in student_list]
listM = [int(i.getMath()) for i in student_list]
listSum = [sum(listK),sum(listE),sum(listM)]
for i in listSum:
    data += str(i) + ' '
data += ' ' + str(sum(listSum)) + '\n'
f.write(data)

data = '평균   '
for i in listSum:
    data += str(round(i/len(listSum),1)) + ' '
data += '    ' + str(round(sum(listSum)/len(listSum),1))
f.write(data)
f.close()

#파이썬_클래스 _ 전준호.py 로 파이썬 클래스에 업로드
class Cstudent:
    def __init__(self,*args):
        self.cnt = len(args)
        self.total = 0
        self.sublist = []
        for i in range(self.cnt):
            self.sublist.append(args[i])
    def getName(self):
        return self.sublist[0]
    def getKor(self):
        return self.sublist[1]
    def getEng(self):
        return self.sublist[2]
    def getMath(self):
        return self.sublist[3]
    def getTotal(self):
        for i in range(1,self.cnt):
            self.total += self.sublist[i]
        return self.total
    def getAvg(self):
        return round(self.total/(self.cnt-1),1)

student_list = []
student_list.append(Cstudent('홍길동',90,88,55))
student_list.append(Cstudent('박주형',77,66,100))
student_list.append(Cstudent('송채원',88,99,98))

totAVG = [0,0,0,0,0]
for i in student_list:
    totAVG[0] += i.getKor()
    totAVG[1] += i.getEng()
    totAVG[2] += i.getMath()
    totAVG[3] += i.getTotal()
    totAVG[4] += i.getAvg()

subject = ['국어','영어','수학']
f = open('hw/mission_class.txt', 'w')
data = '이름   '
for i in subject:
    data += i + ' '
f.write(data)
f.write('총점 평균\n')
line = '=' * 25 + '\n'
f.write(line)
student_list[0].getTotal()

for i in student_list:
    f = open('hw/mission_class.txt', 'a')
    data = str(i.getName())+' '+str(i.getKor())+\
           '  '+str(i.getEng())+'  '+str(i.getMath())+\
           ' : '+str(i.getTotal())+'  '+str(i.getAvg())+'\n'
    f.write(data)
line = '=' * 25 + '\n'
f.write(line)
data = '총점   '
for i in totAVG[:len(subject)+1]:
    data += str(i) + ' '
f.write(data)
f.close()