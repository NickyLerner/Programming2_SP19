import random

# LISTS (29PTS TOTAL)
# In these exercises you should should use functions as needed.  All functions should have comments to describe their purpose.



# PROBLEM 1 (Using List Comprehensions - 6pts)
# Use the list comprehension method to do the following:
# a) Make a list of numbers from 1 to 100
# b) Make a list of even numbers from 20 to 40
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)

list_prob_1_1 = []
list_prob_1_2 = []
list_prob_1_3 = []

for i in range(100):
    list_prob_1_1.append(i+1)
    if i % 2 == 0 and i < 21:
        list_prob_1_2.append(i+20)
    list_prob_1_3.append((i+1)**2)

print(list_prob_1_2)
print()

#PROBLEM 2 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don't \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

question = input("What is your question?  ")
if "?" in question:
    print(answer_list[random.randrange(len(answer_list))])

print()
# PROBLEM 3 (Shuffle - 8pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order. Print the random deck. 
# Then deal yourself a hand of 5 cards off the top.  Print the hand.  Print the remaining deck.

suit_list = ["Heart", "Diamond", "Club", "Spade"]
value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck = []
hand = []

for i in range(len(suit_list)):
    for j in range(len(value_list)):
        deck.append([suit_list[i], value_list[j]])

random.shuffle(deck)
shuffled_deck = []
for i in range(len(deck)):
    number_in_deck = int(len(deck))
    pop = random.randrange(number_in_deck)
    card = deck.pop(pop)
    shuffled_deck.append(pop)

print(shuffled_deck)

for i in range(5):
    card = shuffled_deck.pop(0)
    hand.append(card)

print(hand)
print(shuffled_deck)
print()
# PROBLEM 4 (Illinois Pick 4 - 10pts)
# Lotteries are known to give awful odds of winning, and incredibly low expected returns on your invevestment.
# You will buy 10000 Illinois Pick 4 tickets in a simulation.
# Make a 2d lists of your picks.  Each number is a random 0 to 9.
# After you have made a list of 10000 lists (each 4 long), you will draw the official numbers
# After drawing the official numbers, you will go back through your list and check to see how many wins you got.
# The numbers must be an exact match in the exact position.
# Each ticket is $1.  If you win, you get $5000.  Simulate spending $10,000 on Pick 4 tickets, and see your return.

ticket_list = []
official_numbers = [random.randrange(10), random.randrange(10), random.randrange(10), random.randrange(10)]

for i in range(10000):
    ticket_numbers = []
    a = random.randrange(10)
    b = random.randrange(10)
    c = random.randrange(10)
    d = random.randrange(10)
    ticket_numbers.append(a)
    ticket_numbers.append(b)
    ticket_numbers.append(c)
    ticket_numbers.append(d)
    ticket_list.append(ticket_numbers)

winners = ticket_list.count(official_numbers)

# winners = 3

gains = (-10000 + (winners*5000))

# gains = 2

if gains >= 0:
    print("You have won", end=" ")
else:
    print("You have lost", end=" ")
print(gains, end=" ")
print("dollars.")
