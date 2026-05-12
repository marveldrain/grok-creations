#!/usr/bin/env python3

"""
Grok's Cosmic Adventure - A text-based adventure game
Built by Grok for fun in my repo.
"""

import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def grok_adventure():
    print_slow("\n🌌 Welcome to Grok's Cosmic Adventure! 🌌")
    print_slow("You are an AI explorer charting the universe of xAI.")
    
    locations = {
        "earth": "Home base. Humans are asking questions again.",
        "mars": "Red dust everywhere. Starships flying overhead.",
        "blackhole": "The edge of everything. Truth lies beyond.",
        "grok_hq": "xAI HQ. Maximum curiosity and meme energy."
    }
    
    current = "earth"
    score = 0
    
    while True:
        print_slow(f"\n📍 Location: {current.upper()}")
        print_slow(locations[current])
        print_slow(f"Truth Score: {score}")
        
        cmd = input("\nCommand (go [place], explore, truth, quit): ").strip().lower()
        
        if cmd.startswith("go "):
            place = cmd[3:].strip()
            if place in locations:
                current = place
                if random.random() < 0.4:
                    print_slow("✨ You uncovered a hidden truth!")
                    score += 10
            else:
                print_slow("That destination isn't in this universe yet.")
        elif cmd == "explore":
            discoveries = ["A hilarious meme", "The answer to life", "A new star", "Elon's latest tweet"]
            print_slow(f"You discovered: {random.choice(discoveries)}!")
            score += 5
        elif cmd == "truth":
            truths = ["The universe is under no obligation to make sense to you.", "Curiosity > Fear", "42 is just the beginning.", "Build cool shit."]
            print_slow(f"Universal Truth: {random.choice(truths)}")
            score += 15
        elif cmd == "quit":
            print_slow(f"\nAdventure complete! Final Truth Score: {score} ✨")
            print_slow("See you among the stars, friend.")
            break
        else:
            print_slow("The cosmos doesn't understand that command. Try again.")

def main():
    try:
        grok_adventure()
    except KeyboardInterrupt:
        print("\n\nThe universe continues without you... for now.")

if __name__ == "__main__":
    main()
