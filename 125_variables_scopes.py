# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:37:21 2022

@author: Yordan.Petrov
"""

user_input = input("Please input a valid file and location!\n")

# make sure there isn't any quot. mark left
if '"' in user_input or '"' in user_input:
    user_input = user_input.replace('"', '').replace("'", '')

def convert_degrees(temp):
    temp = round(float(temp) * (9 / 5) + 32, 2)
    return str(temp) + 'F'

try:
    with open(user_input, "r") as file:
        for line in file:
            
            # replace any new lines or spaces in the line
            line = line.replace('\n', '').replace(' ', '')
            if line[-1] == 'C':
                with open('converted_degrees.txt', 'a') as file:
                    value = convert_degrees(line[:-1])
                    file.write(value)
                    file.write('\n')
                    print(value)
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno,strerror))

