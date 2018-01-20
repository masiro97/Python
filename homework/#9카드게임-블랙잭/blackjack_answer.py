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


#blackjack

def blackjack():
    print("Welcome to SMaSH Casino!")
    deck = fresh_deck()
    chips = 0
    while True:
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
                elif score_dealer == score_player:
                    print("We draw.")
                elif score_dealer < score_player:
                    print("You won.")
                    chips += 1
                else:
                    print("I won.")
                    chips -= 1
                print("chips =",chips)
                
        if  not more("Play more? (y/n)"):
            break
    print("Bye!")
