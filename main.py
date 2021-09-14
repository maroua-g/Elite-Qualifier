import random


def init_chat():
  quit_character = 'q'

  user_input = input("Hello, how are you?\n")

  while user_input != quit_character:
    
    user_input = input(random.choice(a) + "\n")

    user_input = input("What did you eat today?" + "\n")
    user_input = input(random.choice(b) + "\n")

    user_input = input("Can you describe the sky to me?" + "\n")
    user_input = input(random.choice(c) + "\n")
    
    user_input = input("What will you be doing later?" + "\n")
    user_input = input(random.choice(d) + "\n")
    
    user_input = input("Is there any hobbies you take part of?" + "\n")
    user_input = input(random.choice(e) + "\n")
    
    user_input = input("Have you ever been to a ball?" + "\n")
    user_input = input(random.choice(f) + "\n")
    
    user_input = input("This conversation is getting a bit lengthy, don't you think?" + "\n")
    user_input = input(random.choice(g) + "\n")

    user_input = input("Yes yes, but before you go! Do you think I'm funny? I think I'm funny but do you..?" + "\n")
    user_input = input(random.choice(h) + "\n")


a = ["I'm glad","That's great","Awesome"]
b = ["Sounds good!","Mmm, now I'm hungry","I wish I could try that","Sounds like it would clog my system.","Hahahha.. I-I think I'm allergic to that"]
c = ["It sounds magical thank you for this new information","I would love to see that","I guess I'll have to look at it from my programmed images","I would have never guessed"]
d = ["I'll try that sometime","Sounds fun","So this is what humans like.."]
e = ["For me, that sounds a bit much","At least you enjoy it","I think I've read about that"]
f = ["So you're a peasant I suppose","I can't relate","Well, well.."]
g = ["Uh yes, I thought the same","Well then, you should go now","Take this time to get a beauty sleep as humans say","Bye bye, human."]
h = ["Why yes, I've always been funny","I knew it!","Haha I know, right?","Of course thank you"]


if __name__ == "__main__":
  init_chat()
