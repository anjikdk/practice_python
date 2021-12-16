from num2words import num2words
from tkinter import *

def num_to_words():
    given_num = float(input("Enter value: "))
    num_in_word = num2words(given_num)
    print(num_in_word)

num_to_words()