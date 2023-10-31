"""
tuples.py
Jennifer Larsen
10/10/2023
This module contains functions to read and write from a file using tuples
"""
import os as os


def get_student_info(student_name):
    my_tuple = (student_name, [])
    scores = input("Please enter a list of test scores separated by a comma: ")
    score_list = scores.split(",")
    for score in score_list:
        my_tuple[1].append(score)
    write_to_file(my_tuple)


def write_to_file(my_tuple):
    f = open('student_info.txt', 'a')
    f.write(str(my_tuple) + '\n')
    f.close()


def read_from_file():
    file_dir = os.path.dirname(__file__)
    file_name = 'student_info.txt'
    f = open(os.path.join(file_dir, file_name), "r")
    for line in f:
        print(line)
    f.close()


if __name__ == "__main__":
    get_student_info('Jennifer')
    get_student_info('John')
    get_student_info('Justin')
    get_student_info('Julie')

    read_from_file()
