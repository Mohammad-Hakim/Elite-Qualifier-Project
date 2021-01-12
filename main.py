#Chatbot
import random


#Responses
def chatbox_responses(user_input):
  responses = ["Ok", "That's a tough one.", "Why don't you know?"]
  return random.choice(responses)
#Script
exit = "x"
name = input("What's your name?\n")
input("Hello " + name + ".\n")
feeling = input("How are you doing?\n")
if feeling == "Good" or feeling == "good":
  print("Superman does good, you're doing well.\n")
elif feeling == "Well" or feeling == "well":
  input("Nice grammer.\n")
else:
  print("No one cares.\n")
ranking = input("On a scale of 1 to 10, how would you rank me?\n")
if int(ranking) < 8:
  input("How can I improve?\n")
elif int(ranking) >= 8:
  print("Thanks, I think I'm pretty great too.\n")
else:
  print("I was looking for a numerical answer...\n")
input("Where would you like to go?\n")
print("I hear that's a nice place.\n")
answer = input("What would you like to ask me?\n")
while answer != exit:
  answer = input(chatbox_responses(answer) + "\n")