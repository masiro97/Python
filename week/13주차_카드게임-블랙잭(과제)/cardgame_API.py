def fresh_deck():
    suits = {"Spade","Heart","Diamond","Club"}
    ranks = {2,3,4,5,6,7,8,9,10,"J","Q","K","A"}
    deck = []
    #카드 52장을 만들어 리스트 deck에 모은다.
    for in :
        for  in :


    #카드 52장을 만들어 리스트 deck을 무작위로 섞는 다.

def hit(deck):
    if   :


    return ,

def count_score(cards):
    score = 0
    number_of_ace = 0 
    for card in cards:
        #card의 값을 평가하여 score에 더함


    #score가 21이 넘고 A가 있으면 score를 재조정함
    #A가 2장 이상 있을 수 있음에 유의


    return score

def show_cards(cards,message):
    print(message)
    for card in cards:
        #card를 보기 좋게 한줄에 프린트

def more(message):
    answer = input(message)
    while not:
        answer =  input(message)
    return
