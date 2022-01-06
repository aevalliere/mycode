#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print("My", challenge[2][1] + "! These", challenge[2][0], "do", challenge[3] + "!!!" )  

a=trial[2]["goggles"]
b=trial[2]["eyes"]
c= trial[3]

print(f"My {a}! The {b} do {c}!")

