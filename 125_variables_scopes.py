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


def read_file(input_file, target_file, error_log_file, converter_func):
    try:
        start = datetime.datetime.now()
        with open(user_input, "r") as file:
            with open(target_file, 'a') as src_file:
                with open(error_log_file, 'a') as errors_file:
                    counter = 0
                    errors_counter = 0
                    for line in file:          
                        counter += 1
                        # replace any new lines or spaces in the line
                        line = line.replace('\n', '').replace(' ', '')
                        try:
                            if line[-1] == 'C':
                                value = converter_func(line[:-1])
                                src_file.write(value)
                                src_file.write('\n')
                        except IndexError:
                            errors_counter += 1
                            errors_file.write(f"IndexError at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} on line: {counter}\n")
                            pass
                        except ValueError:
                            errors_counter += 1
                            errors_file.write(f"ValueError at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} on line: {counter}\n")
                            pass
                        except:   
                            errors_counter += 1
                            errors_file.write(f"OtherError at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} on line: {counter}\n")
                            pass
    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno,strerror))
        pass

    end = datetime.datetime.now()
    time_required = end-start
    return counter, errors_counter, time_required

result = read_file(user_input, 'converted_degrees.txt', 'error_log.txt', convert_degrees)
print(f"Number of source records: {result[0]}")
print(f"Number of errors: {result[1]}")
print(f"Processing time: {result[2]}")
