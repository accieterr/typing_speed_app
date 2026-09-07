import time
import json
import random
import curses
from curses import wrapper

def run_test(stdscr):
    #text colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()

    #generates prompt and prints
    prompt = generate_prompt()
    stdscr.addstr(f"Type the following sentence and press ENTER afterwards:\n\n{prompt}\n")
    user_input = []
    start_time = time.time()
    while True:
        user_key = stdscr.getkey()
        stdscr.addstr(user_key)
        if ord(user_key) == ord("\n"):
            break 
        user_input.append(user_key)
    
    end_time = time.time()


    user_input = "".join(user_input)
    stdscr.addstr(f"\nTime it took: {end_time-start_time:.2f} seconds\n")
    correct = 0
    for letter_a, letter_b in zip(prompt, user_input):
        if letter_a == letter_b:
            correct += 1
    
    accuracy = correct/len(prompt)
    stdscr.addstr(f"Accuracy: {accuracy*100:.2f}%")
    

def generate_prompt():
    #loads 300 most common english words from JSON file
    with open("en_300.json", "r") as file:
        en_300 = json.load(file)

    #appends 30 randomly selected words to words
    words = []
    for i in range(30):
        words.append(en_300["words"][random.randint(0,299)]["englishWord"]) 

    #returns prompt string
    return ' '.join(words) 

def main(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr("Press ESC to exit the program and any other key to run the typing test.\n")
        user_key = stdscr.getkey()
        if ord(user_key) == 27:
            break
        run_test(stdscr)

wrapper(main)