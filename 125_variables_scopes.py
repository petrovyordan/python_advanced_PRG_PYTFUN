# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:37:21 2022

@author: Yordan.Petrov
"""

import datetime

user_input = input("Please input a valid file and location!\n")

# make sure there isn't any quot. mark left
user_input = user_input.replace('"', '').replace("'", '')

def convert_degrees(temp):
    temp = round(float(temp) * (9 / 5) + 32, 2)
    return str(temp) + 'F'

try:
    start = datetime.datetime.now()
    with open(user_input, "r") as file:
        with open('converted_degrees.txt', 'a') as src_file:
            with open('error_log.txt', 'a') as errors_file:
                counter = 0
                for line in file:          
                    counter += 1
                    # replace any new lines or spaces in the line
                    line = line.replace('\n', '').replace(' ', '')
                    try:
                        if line[-1] == 'C':
                            value = convert_degrees(line[:-1])
                            src_file.write(value)
                            src_file.write('\n')
                    except IndexError:
                        errors_file.write(f"IndexError at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} on line: {counter}\n")
                        pass
                    except ValueError:
                        errors_file.write(f"ValueError at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} on line: {counter}\n")
                        pass
                    except:   
                        errors_file.write(f"OtherError at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} on line: {counter}\n")
                        pass
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno,strerror))
    pass

end = datetime.datetime.now()

print(end-start)
