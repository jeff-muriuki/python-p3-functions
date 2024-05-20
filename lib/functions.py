#!/usr/bin/env python3

def greet_programmer():
    print('Hello, programmer!')

greet_programmer()


def greet(jeff):
    print(f'Hello, {jeff}!')

greet('jeff')


def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')
    
greet_with_default('muriuki')    

def add(num1, num2):
    return num1 + num2

add(1,2)


def halve(number):
    if not isinstance(number, (int, float)):
        return None
    
    return number / 2

halve(10)