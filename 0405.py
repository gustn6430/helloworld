'''
str = "파이썬수업 씨수업 자바수업 파이썬수업 파이썬수업"
str2 = "파이썬수업,씨수업,자바수업,이썬수업,파이썬수업"

print(3, "+" ,4, "=" ,7)
f1 = "{} + {} = {}".format(3,4,3+4)
f2 = "{0} + {1} = {2}, {2}, {2}, {2}".format(3,4,3+4)
f3 = "{0:d} + {1:f} = {2:f}, {2}, {2}, {2}".format(3,4.0,3+4.0)
f4 = "{0:10d} + {1:10f} = {2:10.3f}, {2}, {2}, {2}".format(3,4.0,3+4.0)
print(f4)



#print("**".join(str))


print(str2.split(","))
print(str2.split("업"))



print("find : ", str.find("씨") , "index : ", str.index("씨수업"))
print(str.find("에이아이"))
print(str.index("에이아이"))


print(str.replace("파이썬","자바",3))

print(str.count("파이썬"))
'''
#-------------------------------------------------------
'''
print(type(True), type(False))
a = "hello"
print(bool("hello"), bool("hi"), bool(3), bool(1.2), bool(-2))
print(bool(""), bool(0))
print(int(True), int(False), str(True))
'''
#-------------------------------------------------------
'''
h = 9
if h < 12 :
    print("오전 ", h, " 가 12보다 작다 ")
elif h < 18 :
    print("오후 ", h, " 가 12보다 크고 18보다 작아요 ")
else :
    print("오후 ", h , "는 12보다 크다.")
'''

'''
lunch = input("밥 먹을래?")
if lunch == "yes" :
    print("밥을 먹고 싶군요.")
    cafe = input("학식?")
    if cafe == "yes" :
        print("8호관 1층으로 ")
    else :
        print("학식을 싫어하는군요.")
        subway = input("subway? ")
        if subway == "yes" :
            print("8호관 1층으로 ㄱㄱ")
        else :
            print("subway를 싫어하는군요.")
else:
    print("굶어 그럼")
'''

'''
for i in 10,25,32,4354,635,216 :
    print("i : ", i)

for i in range (1,21,2):
    print("i : ", i)
'''

'''
sum = 0
for i in 1,2,3,4,5,6,7,8,9,10 :
    sum = sum + i
    print(i ," 번째 loop입니다. sum은 ", sum , "입니다.")

sum = 0
for i in range(1,11,1) :
    sum = sum + i
    print(i ," 번째 loop입니다. sum은 ", sum ," 입니다.")
'''

'''
sum=0
n=0
while n<11:
    #print("n : ", n)
    sum += n
    print(n, " 번째 sum : ", sum )
    n=n+1

print("while 밖에서 sum의 값 : ",sum)

while True : 
    word = input("단어를 입력하세요.")
    if word == "exit":
        print("넌 exit를 입력했다. break를 만난다.")
        break
    elif word == "apple":
        print("넌 apple을 입력했다. continue를 만난다.")
        continue
    else:
        for i in range(3):
            print(word, end=' ')
        print("해당 단어 끝")

    print("apple을 넣으면 이걸 절대 볼 수 없음")
'''

num=0

while num < 4 :
    key = 0
    print("너 키가 몇이니? : ",key)
    if key >= 150 :
        num+=1
        print("입장 가능")
    else :
        print("입장 불가")
    
    
print("출발합니다.")    