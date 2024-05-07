#!/usr/bin/python3
import time

while(True):
    with open('example.txt', 'w') as file:
        file.write('Hello, world!')
    time.sleep(7)
    
