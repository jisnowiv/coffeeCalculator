#!/usr/bin/env python
"""
This script returns the amount of water to bloom and then brew coffee based on the grounds measured.
It requests input for the grounds measurement then returns the water measurements.

User can optionally add a ratio other than 16 to 1 in the cmd line.

usage: python main.py <ratio>
"""
import sys

RATIO = 16  # Change this for stronger or weaker coffee

if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) > 1:
        try:
            RATIO = int(sys.argv[1])
            print(f"Ratio changed from 16:1 to {RATIO}:1.")
        except ValueError:
            print("Please enter an integer value for ratio.")

    while True:
        try:
            grounds = int(input("How many grams of coffee did you measure?\n"))

            water = grounds * RATIO
            bloom = int(water / 9.1)

            print(f"Bloom with {bloom} ml of water.")
            print(f"Wait 60 seconds, then add water until {water} ml.")
            break

        except ValueError:
            print("Please enter an integer value.")
