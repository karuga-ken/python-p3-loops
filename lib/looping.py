#!/usr/bin/env python3

def happy_new_year():
    count = 11
    while count > 0:
        count -= 1
        print(count)
        print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
        return[x*x for x in int_list]
square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
fizzbuzz()
