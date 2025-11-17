import random
deck=['AceD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JackD', 'QueenD', 'KingD', 'AceH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JackH', 'QueenH', 'KingH', 'AceS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JackS', 'QueenS', 'KingS', 'AceC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JackC', 'QueenC', 'KingC' 'AceD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JackD', 'QueenD', 'KingD', 'AceH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JackH', 'QueenH', 'KingH', 'AceS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JackS', 'QueenS', 'KingS', 'AceC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JackC', 'QueenC', 'KingC']
player1 = []
bot=[]
discard=[]
def take(Y,i):
   for i in range(i):
        pick = random.choice(deck)
        deck.remove(pick)
        Y.append(pick)

take(player1,10)
print(player1)
def take(Y,i):
   for i in range(i):
        pick = random.choice(deck)
        deck.remove(pick)
        Y.append([pick])

take(bot,10)
print(bot)
take(player1,1)
print(player1)
def sort():
    for i in player1:

        print('hi')
