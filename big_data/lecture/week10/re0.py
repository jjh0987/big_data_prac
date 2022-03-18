import re
filtering = re.compile('[a-z]+')
ls = filtering.findall('life 33 is too a3short')
print(ls)

for i in filtering.finditer('life is too short'):
    print(i)
    print(i[0])

filtering.search('1 life life') # 첫 서치 반환
filtering.search('too')

mat = filtering.match('python') # 첫 매치
mat.start()
mat.end()
mat.span()

re.match('[a-z]+','python')
print(re.match('a.b','a\nb'))

p = re.compile('a.b',re.DOTALL)
m = p.match('a\nb')
print(m)

p = re.compile('[a-z]+',re.I) # 대문자 허용
m = p.match('Python1')
print(m)
p = re.compile('python\s\w+')
print(p.findall('python one life python two a'))


