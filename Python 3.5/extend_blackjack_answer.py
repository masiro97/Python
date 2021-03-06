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
    #if answer == 'y':
        #return True
    #else:
        #return False

#Data base API


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

def login(members):
    username = input("Enter your name : (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name : (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members.keys():
        if trypasswd == members[username][0]:
            tries = members[username][1]
            wins = members[username][2]
            print("You played",tries,"games and won",wins,"of them")
            wpercent = 100 * wins / tries if tries > 0 else 0
            print("Your all-time winning percentage is",\
                  "{0:.1f}".format(wpercent),"%")
            chips = members[username][3]
            if chips >= 0:
                print("You have",chips,"chips.")
            else:
                print("You owe",-chips,"chips.")
            return username,tries,wins,chips,members
        
        else:
            return login(members)
            
    else:
        members[username] = (trypasswd,0,0,0)
        return username,0,0,0,members


def show_top5(members):
    print('-----')
    sorted_members = sorted(members.items(),\
                            key = lambda x: x[1][3],\
                            reverse = True)
    print("All-time Top 5 based on number of chips earned")
    rank = 1
    for member in sorted_members[:5]:
        chips = member[1][3]
        if chips <= 0:
            break
        print(rank,".",member[0],":",chips)
        rank +=1 
            
    
    
#blackjack

def blackjack():
    print("Welcome to SMaSH Casino!")
    username , tries, wins, chips, members = login(load_members())
    deck = fresh_deck()
    win = 0
    lose = 0
    while True:
        print("-----")
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
            chips += 2
            win += 1
            print("chips = ",chips)
        else:
            while score_player < 21 and more("Hit? (y/n) "):
                card, deck = hit(deck)
                player.append(card)
                score_player = count_score(player)
                print(" ",card["suit"],card["rank"])
            if score_player > 21:
                print("You bust! I won.")
                chips -= 1
                lose += 1
                print("chips =",chips)
            else:
                while score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)

                show_cards(dealer,"My cards are:")
                if score_dealer > 21:
                    print("I bust! You won.")
                    chips += 1
                    win +=1
                elif score_dealer == score_player:
                    print("We draw.")
                    win += 0.5
                    lose += 0.5
                elif score_dealer < score_player:
                    print("You won.")
                    chips += 1
                    win += 1
                else:
                    print("I won.")
                    chips -= 1
                    lose += 1
                print("chips =",chips)
                
        if  not more("Play more? (y/n)"):
            break
    print("-----")
    played = int(win + lose)
    print("You played",played,"games and won",win,"of them")
    wpercent =100*win/played if played > 0 else 0
    print("Your winning percentage today is",\
          "{0:.1f}".format(wpercent),"%")
    tries += played
    wins += win
    members[username] = (members[username][0],tries,wins,chips)
    store_members(members)
    show_top5(members) 
    print("Bye!")
