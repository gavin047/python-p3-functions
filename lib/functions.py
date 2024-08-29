#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

 
def greet(name):
    print(f"Hello, {name}!")
greet("Naureen")



def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default("Sunny")

def add(num1, num2):
    function_name = num1 + num2
    return function_name    

print(add(1, 2))


def halve(number):
    return number / 2
print(halve(100))
