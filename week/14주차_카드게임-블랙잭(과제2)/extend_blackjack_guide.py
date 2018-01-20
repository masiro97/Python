#실습 1
#login(members)
#회원 사전 members를 가지고 회원 로그인과 출력을 처리하는 함수
def login(members):
    username = input("Enter your name : (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name : (4 letters max) ")
    trypasswd = input("Enter your password : ")
    #...
    #...
    if <members의 키 중에서 username이 있는가?>:
        if <trypasswd가 username의 비밀번호와 일치하는가?>:
            #username의 게임시도 횟수와 이긴횟수를
            #members에서 가져와 보여준다.
            #예시: You played 101 games and won 54 of them
            ##
            #승률 계산하여 %로 보여준다
            #(분모가 0인 오류는 방지해야 함)
            #예시: Your all-time winning percentage is 53.5%
            ##
            #칩 보유개수를 보여준다
            #예시: 개수가 양수이면, You have 5 chips.
            #예시: 개수가 음수이면, You owe 5 chips.
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        #username을 members 사전에 추가한다.
        return username,0,0,0,members #<- tuple
    
#0으로 나누기 오류 방지
def divide(x,y):
    return x/y if y!= 0 else 0
#소수점 이하 지정자리수에서 반올림하기
#"{0:.2f}".format(0.246)

#실습2
#show_top5(members)
#회원사전 members를 인수로 받아 칩의 보유개수가 가장 많은 순으로 화면에 출력해주는 프로시저
#(칩의 개수가 0이하의 겨우는 보여주지 않음)
#---
#All-time Top5 based on the number of chips earned
#1. doh : 35
#2. didi : 10
#3. hy : 2

def show_top5(members):
    print("---")
    sorted_members = #칩 개수의 역순으로 정렬
    print("All-time Top 5 based on the number of chips earned")
    #sorted_members[:5]의 원소를 참고하여 차례로 프린트하되
    #0이하는 무시하고 프린트 하지 않는다.


#사전 정렬하기
#didi,edd844,130,55.0,10
#hy,er878re,35,18.0,2
#doh,sid73,998,552.0,34
dict = {}
dict["didi"] = ("edd844",130,55.0,10)
dict["hy"] = ("er878re",35,18.0,2)
dict["doh"] = ("sid73",998,552.0,34)
sorted(dict)# ->사전의 키를 정렬
sorted(dict.items())#-> item과 함께 정렬
sorted(dict.items(),key = lambda x:x[1][1]) #x는 전체 x[1]인덱스 의 [1]인덱스 만들때는 [3]으로 해야겟지..



sorted(dict.items(),key = lambda x:x[1][3],reverse = True) #칩 보유개수의 역순으로 정

    
