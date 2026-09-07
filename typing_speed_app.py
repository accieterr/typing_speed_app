import time
import json
import random
import curses
from curses import wrapper

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

def run_test(stdscr):
    #text colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.nodelay(True)

    prompt = generate_prompt()
    start_time = time.time()
    user_input = []
    
    while True:
        stdscr.clear()
        stdscr.addstr(f"Type the following sentence and press ENTER afterwards:\n\n{prompt}")
        correct = 0

        for i in range(len(user_input)):
            if i >= len(prompt) or prompt[i] != user_input[i]:
                stdscr.addstr(2, i, user_input[i], curses.color_pair(2))
            else:
                correct += 1
                stdscr.addstr(2, i, user_input[i], curses.color_pair(1))

        end_time = time.time()
        elapsed_time_min = ((max((end_time-start_time), 1))/60)
        raw_wpm = (len(user_input)/5) / elapsed_time_min
        accuracy = correct/max(1 , min(len(user_input), len(prompt)))
        wpm = max(0 , raw_wpm - ((len(user_input)-correct) / elapsed_time_min))
        stdscr.addstr(4, 0, f"NET WPM: {wpm:.0f} wpm")
        stdscr.addstr(5, 0, f"RAW WPM: {raw_wpm:.0f} wpm")
        stdscr.addstr(6, 0, f"ACCURACY: {accuracy*100:.2f}%")

        try:
            user_key = stdscr.getkey()
        except:
            continue
        
        if ord(user_key) == ord("\n"):
            break 
        if user_key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(user_input) > 0:
                user_input.pop()
        else:
            user_input.append(user_key)

    stdscr.nodelay(False)

    stdscr.addstr(8, 0, "Press any key to continue...")
    stdscr.getkey()
    
    
def main(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr("Press ESC to exit the program and any other key to run the typing test.\n")
        user_key = stdscr.getkey()
        if ord(user_key) == 27:
            break
        run_test(stdscr)

wrapper(main)