l1 = [1,2,3,4,5]
#tuple
t1 = (1,2,3,4,5)
print(l1)
print(t1)
print(t1.count(2))
print(t1.index(2))

#커피숍 프로그램
menu = ("아메", "라떼", "유자차")
#아이스티 추가
menu1 = list(menu)
print(menu1)
menu1.append("아이스티")
print(menu1)
menu = tuple(menu1)
print(menu)

t2 = ()
print(t2)
t3 = 10,20,30,40,50
print(t3)

i4 = 10
print(type(i4))
t4 = 10,
print(type(t4))
print(t4)

lst = [10,20,30,44,5,6,1,1]
#lst.sort()
t3 = 1074,205,3,40,50
print("sorted(t3) : ", sorted(t3))
print("t3 : ", t3)

t10 = 1,2,3,4,5
for i in 1,2,3,4,5 :
    print(i)

#------------------------------------------------------------------------------------------------------

#dictionary
#d1 = { k1:v1, k2:v2, k3:k4, k4:v1 }    //키 중복 X
d1 = {}
d2 = dict() 

#사전에 값을 추가하자.
#1) 추가 방법 1
student = {}
student[101] = '홍'
student[102] = '김'
student[103] = '박'
print(student)
print("student[101] : ", student[101])
print("student[101] : ", student[102])
#print("student[0] : ", student['gkgk'])    //오류

lec = {}
lec['강좌명'] = '파이썬'
lec['개설년도'] = 2023
lec['수강생'] = ['홍', '김', '박', '고']
lec['인원'] = 35
print(lec)

#인원수를 변경하는 방법
lec['인원'] = 20
print(lec)

lec.update({'인원' : 10})
print(lec)

lec.update({'강의실' : 213, '교수' : '이희진'})
print(lec)

#------------------------------------------------------------------------------------------------------

#month
month = {1:'1월',2:'2월',3:'3월',4:'4월',5:'5월',6:'6월',7:'7월',8:'8월',8:'8월',9:'9월',10:'10월',11:'11월',12:'12월'}
#month[key] => value
print("#1")
for key in range(1,13) :
    print(month[key])

print("#2")
for key in 1,2,3,4,5,6,7,8,9,10,11,12 :
    print(month[key])

print("#3")
#print(month.keys())
for k in month.keys() : #[1,2,3,4,5,6....12]
    # month[key] -> value
    print(month[k])

print("#4")
#print(month.values())
for v in month.values() :   #[1월, 2월, 3월, 4월 ... ]
    print(v)

print("#5")
#month.items()
for item in month.items() : #[(k1, v1), (k2, v2), (k3, v3) ... ]
    print(item)

print("#6")
#month.items()
for item in month.items() : 
    # item  ->  (k1, v1)
    print("key : ", item[0])
    print("value : ", item[1])
    print("     ")
#key : xxx
#value : xxx

for hoho in month : #month.keys()
    print(hoho)

print(month.get('k1'))
print(month.get('key100'))
#print(month['k1'])         #오류
#print(month['key100'])     #오류

#------------------------------------------------------------------------------------------------------

#dictionary 삭제
print(month)
print("month.pop('k1') : ", month.pop(1)) # key값을 줘야함
print(month)    # 2월부터 //
print("month.popitem() : ", month.popitem()) # 맨 마지막 것을 삭제함
print(month)    #2월 ~ 11월

#------------------------------------------------------------------------------------------------------

#zip(), enumerate()

'''
l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']
l3 = [9,8,7,6,5]

zip()
조 = [1조, 2조, 3조...]
1반 = [홍,김,xx,xx,...]
2반 = [a, b, c, d]
3반 = [x, y, z, q]
zip(조, 1반, 2반, 3반)
[(1조, 홍, a, x),(2조, 김, b, y), ... ]
'''

l1 = ['한식', '중식', '일식', '양식', '분식']
l2 = ['전주식당', '전가복', '초밥집']
l3 = ['제육', '탕수육']

z = zip(l1, l2, l3)
print(type(z))
print(z)
print(list(z))

#dictionary
#list1 => dictionary x
#L2 - 키 , L3 - value

z1 = zip(l2, l3)
print(dict(z1))
#print(list(z1))

z2 = zip(l1, zip(l2, l3))
print(dict(z2))

#1개 리스트를 dictionary로 변경
#       0       1       2
l4 = ['제육', '탕수육', '연어덮밥']
print(enumerate(l4))
print(list(enumerate(l4)))
print(dict(enumerate(l4)))

#------------------------------------------------------------------------------------------------------

#문제
#과목을 주면 강의실을 알려주는 시스템

#1) dictionary로 변환해서 활용
#2) 무한루프로 강의실을 알려줘라
#3) quit 이라는 단어가 들어오면, 강의실 알려주는 시스템을 종료하라
#4) 다른 과목을 물어보면, "몰라요" 다시 과목명 물어보는 것으로 돌아간다.
#5) 해당과목에 대한 강의실을 알려준다.
#6) continue, break 활용할 것

subject = ['파이썬', '자바', 'c++', 'AI', '알고리즘']
classroom = [101, 102, 103, 104, 105]

d = dict(zip(subject, classroom))
# {파이썬 : 101, 자바 : 102, c++ : 103 ... }
while 1 :
    c = input("과목명을 입력하세요")
    if c == "quit" : #quit인 경우
        print("quit를 입력했으니, 종료")
        break # while을 종료

    if c in d.keys() :  # 해당과목인 경우   # 해당 과목명에 대해서 강의실을 넘겨준다.
        print("강의실은 ", d[c])    # 출력
    else :  # 아닌 경우     # 만약 해당과목명이 아닌경우엔, '몰라요'를 출력하고, 다시 루프
        print("몰라요")
        continue
    