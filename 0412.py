'''
#리스트
["김밥", "떡볶이", "돈까스"]
#튜플
("김밥", "떡볶이", "돈까스")


#딕셔너리 - 사전    apple -  동그란 빨간 과일
{k1:v1 , k2:v2}
adress = {"홍길동" : "구로구", "김현수" : "마포구"}
'''

'''
#1. 빈 리스트를 만들어서, 하나씩 원소를 추가하는 방식
lst = []
print(type(lst))
lst.append("김밥")
lst.append("햄버거")
lst.append("감자튀김")
lst.append("탕수육")
#print(lst)
lst.append("파스타")
#print(lst)
lst.insert(0,"학식")
#print(lst)
lst.insert(0,"서브웨이")
#print(lst)

print("list에서 3번째에 있는 값입니다 : ",lst[2])

#점심메뉴 출력하기 1
for i in range(len(lst)):
    print(lst[i])

#점심메뉴 출력하기 2
for item in lst :
    print(item)

print(lst)
print('lst.count("탕수육")', lst.count("탕수육"), lst.index("탕수육"))
'''
'''
#slicing
['써브웨이', '학식', '김밥', '햄', '감자튀김', '탕수육', '파스타', "볶음밥", "짜장면"]
#lst[start : end : step]
print(lst[::])
print(lst[0:len(lst):1])
print(lst[0:8:2])
print(lst[3:7:1])
print(lst[::-1])
print(lst[0:6:3])
'''

'''
lst=[]
lst.append("김밥")
lst.append("햄버거")
lst.append("감자튀김")
lst.append("탕수육")
lst.append("파스타")
lst.append("커피")  

lst.append("김밥")
print(lst)
lst.remove("김밥")
print(lst)

item1="커피"
if item1 in lst :
    lst.remove(item1)
    print("커피존재함", lst)
else:
    print("커피 존재 안함", lst)

#pop
print(lst)
print("lst.pop() : ",lst.pop())
print(lst)

print("lst.pop(0) : ",lst.pop(0))
print(lst)
'''

'''
lst=[]
lst.append("김밥")
lst.append("햄버거")
lst.append("감자튀김")
lst.append("탕수육")
lst.append("파스타")
lst.append("커피")
print(lst)
dessert = ["케익", "커피", "우유", "와플"]
print(dessert)
lst.extend(dessert)
print(lst.extend(dessert))

l1 = ["orange", "apple", "mango", "kiwi", "banana"]

print(l1)
print(sorted(l1))
print(l1)

print("====l1.sort()실행====")
l1.sort()
print(l1)   

l1.reverse()
print(l1)

l1.clear()
print(l1)

del l1
print(l1)
'''

#리스트를 짧게 , 간결하게

#1) 그냥 선언
l1 = [0,1,2,3,4,5,6,7,8,9]

#2 for 문으로 append
l2 = []
for i in range(10) :
    l2.append(i)

#3 리스트 컴프리핸션
l3 = [ i for i in range(11) ]


l4 = [ i*3 for i in range(11) ]


l5 = []
for i in range(11):
    if i % 2 == 0:
        l5.append(1**2)

i6 = [ i**2     for i in range(11)     if i % 2 == 0 ]

#list 를 복사
a = [0, 4, 16, 36, 64, 100]
b = a
a.pop()
print("a : ", a)
print("b : ", b)

b.append("333")
print("a : ", a)
print("b : ", b)

c = a[:]    #a[:]
#c = a.copy()
#c = list(a)
print("a is c : ", a is c)

print("deep copy")
print("a : ", a)
print("c : ", c)

a.pop()
print("====after a.pop()====")
print("a : ", a)
print("b : ", b)
print("c : ", c)

c.append(555)
print("==== after c.append(555)====")
print("a : ", a)
print("b : ", b)
print("c : ", c)

