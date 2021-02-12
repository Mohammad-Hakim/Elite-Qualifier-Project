#Chatbot
import random

#Responses
def chatbox_responses(user_input):
  responses = ["Ok", "That's a tough one.", "Why don't you know?"]
  return random.choice(responses)
#Categories
categories = ["Travel", "Sports", "General"]
#Ranking
def ranking(user_input):
  if int(user_input) < 8:
    input("How can I improve?\n")
  elif int(user_input) >= 8:
    print("Thanks, I think I'm pretty great too.\n")
  return user_input
#Script
#def script():
  exit = "x"
  print("\n")
  print("\n")
  print("I am a chatbot. If I have not given a new prompt it is because you have to respond to my last prompt. Type 'x' when you want to stop the program.")
  answer = input("What's your name?\n")
  name = answer
  input("Hello " + name + ".\n")
  feeling = input("How are you doing?\n")
  if feeling == "Good" or feeling == "good":
    print("Superman does good, you're doing well.\n")
  elif feeling == "Well" or feeling == "well":
    input("Nice grammer.\n")
  else:
    print("No one cares.\n")
  rank = input("On a scale of 1 to 10, how would you rank me?\n")
  ranking(rank)
  travel = input("Where would you like to go?\n")
  print("I hear that's a nice place.\n")
  while answer != exit:
    print(*categories, sep = ", ")
    answer = input("What would you like to talk about?")
    if answer == "General" or answer == "general":
      while answer != exit:
        answer = input("What would you like to ask me?")
        input(chatbox_responses(answer) + "\n")
        if answer == exit:
          break
    if answer == "Sports" or answer == "sports":
      input("What is your favorite sport?\n")
      input("Why is it your favorite?\n")
      input("Who is your favorite player or team?\n")
      input("How well did they do in their last game?\n")
      input("How do you think they can improve?\n")
    if answer == "Travel" or answer == "travel":
      print("I hear you want to go to " + travel + ".")
      input("Have you been there before?\n")
      input("Do you know anyone there?\n")
      input("Why do you want to go there?\n")
      input("What would you do when you get there?\n")

#script()