import random
face = { "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" }
suit = { "♠", "♥", "♦", "♣" }
deck = [{'數字': fa, '花色': su} for fa in face for su in suit] 
'''def sum(hand): 
    a = 0
    for card in hand:
        if card['數字'] in ['K', 'Q', 'J']: #判斷有沒有JQK
            a += 10
        elif card['數字'] == 'A': #判斷有沒有A
            a += 1
        else:
            a += int(card['數字'])  #都沒有AJQK加數字總值
    return a'''
def toto(god):
    a = 0
    b = 5
    c = 0 
    for cod in god:
        if cod['數字'] in ['K', 'Q', 'J']: #判斷有沒有JQK
            b -= 1
        elif cod['數字'] == 'A': 
            a += 1 
        elif (b > 2):
            c += int(cod['數字'])
        elif (b == 2):
            a += int(cod['數字'])
   
    print(a)
    print(b)
    print(c)


player = []

for i in range(5):
    player.append(deck.pop(random.randint(0, len(deck) - 1)))

print(player)
player_sum = toto(player)
print(player_sum)
