#BlackJack
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

def blackjack():
    #환영인사를 프린트한다.
    print("Welcome to SMash Casino!")
    print()
    #잘 섞은 카드 1벌을 준비한다.
    deck = fresh_deck()
    #점수를 초기화한다.
    chips = 0
    #손님이 원하는 한 다음을 반복한다.
    while(True):
        #카드를 한장씩 손님, 딜러, 손님, 딜러 순으로 배분한다.
        dealer = []
        player = []
        card, deck = hit(deck) # 1장 뽑아서
        player.append(card) #손님에게 주고
        card, deck = hit(deck) #1장 뽑아서
        dealer.append(card) # 딜러에게 주고
        card, deck = hit(deck) #1장 뽑아서
        player.append(card) #손님에게 주고
        card, deck = hit(deck) #1장 뽑아서
        dealer.append(card) #딜러에게 준다
        #딜러의 카드를 보여준다. (첫 카드는 가림)
        print("My cards are:")
        print(" ","****","**")
        print(" ",dealer[1]["suit"],dealer[1]['rank'])
        print()

        #손님의 카드를 보여준다.
        show_cards(player,"Your cards are: ")
        print()

        #손님과 딜러의 카드 두 장의 합을 각각 계산한다.
        score_player = count_score(player)
        score_dealer = count_score(dealer)

        if score_player == 21:
            print("BlackJack! You won.")
            chips += 2
        else:
            while score_player < 21 and more("Hit?(y/n)"):
                card, deck = hit(deck)
                player.append(card)
                score_player = count_score(player)
                print(card['suit'],card['rank'])
            
            if score_player > 21:
                print("You bust! I won.")
                chips -=1
                
            else:
                if score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)
                
            
                if score_dealer > 21:
                    print("I bust. You won.")
                    chips +=1
                
                else:
                    if score_player == score_dealer:
                        print("We draw")
                
                    elif score_player > score_dealer:
                        print("You won.")
                        chips += 1
                    else:
                        print("I won")
                        chips -= 1
        print()                        
        show_cards(dealer,"My cards are: ")
        print("Chips =",chips)
        print()
        if more("Play more?(y/n)") == False:
            print("Bye!")
            break
        else:
            print("--------------")
    
            
                            
                                
                
                
        
