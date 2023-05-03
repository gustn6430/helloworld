#0503
#함수

'''
함수 이름 - addthree
기능 : 3을 더함
input : 숫자 1개
output : 숫자 1개, input 숫자에다가 3을 더한것을 내보냄

def function_name(input1, input2, input3) :
    #수행문 1,
    #수행문 2
'''

'''
def addthree(num) :
    return num + 3

result = addthree(100)  # result = 103
print(addthree(100))
print(result)

def printaddthree(num) :
    print( num + 3)

printaddthree(100)
'''

'''
def hello(name1="배진호", name2="주재석") :
    print("hello ", name1)
    print("hello ", name2)

hello("배","주")
'''

'''
def mysum(num1, num2) :
    return num1 + num2

result = mysum(100, 200)
'''

'''
def mysum2(*numbers) :
    result = 0
    for num in numbers:
        result = result + num
    return result

def cafe(**keyvalue) :
    for key in keyvalue :
        print(key, keyvalue[key])

cafe(아메=2000, 라떼=3000, 핫초코=5000 )
print("===================================")
cafe(아메=2000, 라떼=3000 )
print("===================================")
cafe(아메=2000 )
print("===================================")
menu = {"아메" : 2000, "라떼" : 3000, "핫초코" : 5000}
'''

'''
#lambda
def addthree(num) :
    return num + 3

print(addthree(100))

print((lambda num : num +3)(100))


def multiten(n) :
    return n*10

print(multiten(20))

print((lambda n : n*10)(20))


def multip(n1, n2) :
    return n1*n2

print(multip(3,5))
print((lambda n1, n2 : n1*n2)(3,5))
'''

'''
#map, filter
map(function, list)
map(function,[1,2,3,4,5])
[function(1), function(2), function(3), ..., function(5)]

def addthree(num) :
    return num + 3

print(list(map(addthree, [10,20,30,40,50])))

print(list(map(lambda x : x+3, [10,20,30,40,50])))
'''

'''
#5배를 하고, 10을 더해서 결과를 list로 출력하시오

#1) function
llist = [1,2,3,4,5,6]
def calculate(num) :
    return num * 5 + 10

print(list(map(calculate, llist)))

#2) lambda
print(list(map(lambda num : num*5+10, llist)))

#두개의 list를 하나씩 뽑아서, 두개를 더해서 하나의 리스트로 만들어라
#결과값 [11,22,33,44,55]

#1) function
# 두개의 값을 입력으로 받아서, 그 합을 구하는 function

lst10=[10,20,30,40,50]
lst11=[1,2,3,4,5]

def mysum(n1, n2) :
    return n1+n2

print(list(map(mysum, lst10, lst11)))
#[mysum(10, 1), mysum(20, 2)...]

#2) lambda
print(list(map(lambda n1, n2 : n1+n2, lst10, lst11)))
'''
# filter
# 조건을 만족하는가? 만족하면 결과물에 포함, 만족하지 않으면 포함 x
# map이랑 마찬가지로, 입력 리스트로 받아서, 그걸 결과로 나타냄

#map(function, list)
#filter(function, list)
def positive(x) :
    if x > 0 :
        return True
    else :
        return False

def positive2(x) :
    return x > 0

print(list(filter(positive, [10,-2,3,-5,9])))
print(list(filter(lambda x : x>0, [10,-2,3,-5,9])))