#A program for counting/ calculating the words per minute typed"""
import time


def calculate_wpm(text, time_taken):
    words = len(text.split())
    minutes = time_taken / 60
    wpm = words / minutes
    return wpm


def main():
    print("This program calculates words per minute you type :)")
    input('Press "Enter" when ready')

    start = time.time()
    sample = "This program calculates words per minute you type :)"
    print(f"Type the this text: {sample}")
    user = input("Start typing here::  ")
    end = time.time()
    time_elapsed = end - start
    wpm = calculate_wpm(user, time_elapsed)
    print(f"Time taken is: {time_elapsed:.2f} seconds")
    print(f"Words per minute: {wpm:.2f} words")


main()
