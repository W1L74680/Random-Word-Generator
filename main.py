import random
import os
import time

words = ["Hello", "World", "Python Is Cool", "Follow Me On YouTube!", "Follow Me On SoundCloud!", "Use repl.it", "Join My Discord Server"]

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def randomWord():
    while True:
        # you can change the time
        print(random.choice(words))
        time.sleep(1)
        clear()
        time.sleep(1)

randomWord()