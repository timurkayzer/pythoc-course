#!/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a", type=int)
parser.add_argument("action" , choices=["+","-","/","*"])
parser.add_argument("b", type=int)


args = parser.parse_args()

a = args.a
b = args.b
action = args.action


if action == '+':
    print(a + b)
elif action == '-':
    print(a - b)
elif action == '*':
    print(a * b)
elif action == '/':
    print(a/b)
else:
    print("Unknown value")