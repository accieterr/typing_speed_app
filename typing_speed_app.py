import time
import json
import random

def run_test():
    print("\n"*20)
    prompt = generate_prompt()
    print(f"Type the following sentence and press ENTER afterwards:\n\n{prompt}\n")
    start_time = time.time()
    user_input = input()
    end_time = time.time()

    print(f"\nTime it took: {end_time-start_time:.2f} seconds")
    correct = 0
    for letter_a, letter_b in zip(prompt, user_input):
        if letter_a == letter_b:
            correct += 1
    
    accuracy = correct/len(prompt)
    print(f"Accuracy: {accuracy*100:.2f}%")
    

def generate_prompt():
    #loads 300 most common english words from JSON file
    with open("en_300.json", "r") as file:
        en_300 = json.load(file)
    
    words = []

    for i in range(30):
        words.append(en_300["words"][random.randint(0,299)]["englishWord"]) 

    return ' '.join(words) 

run_test()