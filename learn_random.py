import random

deck = list(range(1,53))
random.shuffle(deck)
# print(deck) 

hand = random.sample(deck,k=5)

print(hand)
# greetings = ['hello','hi','hey','hola']
# colors = ['red','green','blue']

# rnd_float = random.uniform(0,99)
# rnd_int = random.randint(0,10)

# rg= random.choice(greetings)
# colors= random.choices(colors,weights=[9,9,2],k=10)



# print(rnd_int)
# print(rnd_float)
# print(f"{rg} , Corey")
# print(colors)