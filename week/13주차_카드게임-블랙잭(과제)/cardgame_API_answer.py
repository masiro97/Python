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
