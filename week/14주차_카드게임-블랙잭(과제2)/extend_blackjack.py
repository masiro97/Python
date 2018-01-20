#Card Game API
import random

def fresh_deck():
    suits = {"Spade","Heart","Diamond","Club"}
    ranks = {2,3,4,5,6,7,8,9,10,"J","Q","K","A"}
    deck = []
    #카드 52장을 만들어 리스트 deck에 모은다.
    for s in suits:
        for r in ranks:
            card = {"suit" : s, "rank" : r}
            deck.append(card)
    #카드 52장을 만들어 리스트 deck을 무작위로 섞는다.
    random.shuffle(deck)
    return deck

def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return (deck[0],deck[1:])

def count_score(cards):
    score = 0
    number_of_ace = 0 
    for card in cards:
        #card의 값을 평가하여 score에 더함
        rank = card['rank']
        if rank == 'A':
            score += 11
            number_of_ace += 1
        elif rank in {'J','Q','K'}:
            score += 10
        else:
            score += rank
    #score가 21이 넘고 A가 있으면 score를 재조정함
    #A가 2장 이상 있을 수 있음에 유의
    while score > 21 and number_of_ace > 0 :
        score -= 10
        number_of_ace -= 1
    return score

def show_cards(cards,message):
    print(message)
    for card in cards:
        #card를 보기 좋게 한줄에 프린트
        print(' ',card['suit'],card['rank'])

def more(message):
    answer = input(message)
    while not (answer =='y'or answer =='n'):
        answer =  input(message)
    return answer == 'y'


def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name,passwd,tries,wins,chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd,tries,wins,chips = members[name]
        line = name + ','+passwd+','+\
               str(tries)+','+str(wins)+','+\
               str(chips)+'\n'
        file.write(line)
    file.close()


#login(members)
#회원 사전 members를 가지고 회원 로그인과 출력을 처리하는 함수
def login(members):
    username = input("Enter your name : (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name : (4 letters max) ")
    trypasswd = input("Enter your password : ")
    if username in members:
        if trypasswd == members[username][0]:
            tries = members[username][1]
            wins = members[username][2]
            chips = members[username][3]
            win_rate = divide(wins,tries) 
            print("You played",tries,"games and won",wins,"of them")
            print("You all-time winning percentage is",float(win_rate)*100,"%")
            if chips < 0:
                print("You owe",-chips,"chips.")
            else:
                print("You have",chips,"chips.")
            
            return username,trypasswd,tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd)
        return username,trypasswd,0,0,0,members #<- tuple
    
#0으로 나누기 오류 방지
def divide(x,y):
    return "{0:.2f}".format(x/y) if y!= 0 else 0


def show_top5(members):
    print("---")
    sorted_members =sorted(members.items(),key = lambda x:x[1][3],reverse = True) #칩 개수의 역순으로 정렬
    print("All-time Top 5 based on the number of chips earned")
    z = 0
    for x in range(len(sorted_members)):
        if sorted_members[x][1][3] > 0:
            z +=1
            print(z,".",sorted_members[x][0], ":",sorted_members[x][1][3]) 
  

def extend_blackjack():
    print("Welcome to SMaSH Casino!")
    members = load_members()
    username, passwd,tries, wins, chips, members = login(members)
    members[username] = (passwd,tries,wins,chips)
    store_members(members)
    #members.txt파일에서 회원자료를 읽고 로그인 절차를 통해서 사용자이름,
    #게임시도 횟수, 이긴횟수, 칩보유 개수, 전체회원 정보를 사전에 담는다.
    deck = fresh_deck()
    chips_today = 0
    tries_today = 0
    wins_today =0
    
    while True:
        tries_today += 1
        dealer = []
        player = []
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        print("My cards are:")
        print(" ","****","**")
        print(" ",dealer[1]["suit"],dealer[1]["rank"])
        show_cards(player,"Your cards are: ")
        score_player = count_score(player)
        score_dealer = count_score(dealer)
        if score_player == 21:
            print("Blackjack! You won.")
            wins_today +=1
            chips_today += 2
            print("chips = ",today_chips)
        else:
            while score_player < 21 and more("Hit? (y/n) "):
                card, deck = hit(deck)
                player.append(card)
                score_player = count_score(player)
                print(" ",card["suit"],card["rank"])
            if score_player > 21:
                print("You bust! I won.")
                chips_today -= 1
                print("chips =",chips_today)
            else:
                while score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)

                show_cards(dealer,"My cards are:")
                if score_dealer > 21:
                    print("I bust! You won.")
                    wins_today +=1
                    chips_today += 1
                elif score_dealer == score_player:
                    print("We draw.")
                    wins_today += 0.5
                elif score_dealer < score_player:
                    print("You won.")
                    wins_today +=1
                    chips_today += 1
                else:
                    print("I won.")
                    chips_today -= 1
                print("chips =",chips_today)
                
        if  not more("Play more? (y/n)"):
            break
    print("You played",tries_today,"games and won",wins_today,"of them")
    print("Your winning Percentage today is",float(divide(wins_today,tries_today))*100,"%")
    chips += chips_today
    wins += wins_today
    tries += tries_today
    members[username] = (passwd,tries,wins,chips)
    store_members(members)
    show_top5(members)
 

    #게임이 진행되는 동안 승패횟수와 칩의 획득 개수를 추적하여, 게임이 끝난 뒤
    #결과를 회원사전에 적용하여 수정하고, members.txt 파이에 저장한다.
   
