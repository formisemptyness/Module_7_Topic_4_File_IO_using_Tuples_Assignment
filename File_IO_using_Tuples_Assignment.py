'''
Program: File_IO_using_Tuples_Assignment.py
Author: Joshua M McGinley
Last Date Modified: 10/12/2022

What you're creating
In this assignment you will tie together the seemingly unrelated tuple and arbitrary argument list to perform file
input and output.  Your program will take a student's name and an unknown number of test scores, store them in a
tuple, save that tuple into a file, and then finally print the data from the file back to the screen.
How you're doing it

    Write a function write_to_file() that accepts a tuple to be added to the end of a file
        Open the file for appending (name your file 'student_info.txt')
        Write the tuple on one line (include any newline characters necessary)
        Close the file
    Write a function get_student_info() that
        Accepts an argument for a student name
        Prompts the user to input as many test scores as they wish
        Stores the information (name and scores) in a tuple
        Calls the function write_to_file() sending the tuple to be written to the end of the file
    Write a function read_from_file() that
        Reads a file line by line
        Prints each line to the console
    In main
        Call the get_student_info() for at least 4 different students.
        Call read_from_file()

Notes/Hints

    Because tuples are immutable, you'll want to store your data in a tuple that has a list nested inside of it.
        ('name',[score1,score2,score3,etc.])
        You'll be able to edit the list inside the tuple.  In the example above, you could append to the list by
        doing something like this:  score_list[1].append(student_score)
    There are more elegent ways to do things but for this assignment, you can just write the tuples to the file as
    strings and then read the strings back at the end of the program
    Remember that you'll also need to include a "\n" to each line you write to the file so you don't just end up
    with one long string on a single line
    Because you are going to be appending to the file each time, it might be good for you to include this as the
    first thing you do in your main:
        open("student_info.txt","w").close()
        It basically overwrites the file with a blank file.
        This prevents you from appending more and more each time you rerun your program.

Submit your working .py file.  This is worth 10 points.
'''

def write_to_file(data_to_write):
    f = open('student_info.txt', 'w')
    f.writelines(data_to_write)
    f.close()


def get_student_info(name):
    scores = []
    while (sentinel != "exit"):
        try:
            next_score = int(input('Enter score or exit to quit: '))
        except:
            print('You are wrong.')
        if next_score == 'exit':
            sentinel = 'exit'
            break
    scores.append(next_score)
    if next_score == 'exit':
        break
    sentinel = input('Enter exit to quit: ')
    student_and_score = (name, [scores])
    write_to_file(student_and_score)



def read_from_file():
    readlines()
    file_name = 'student_info.txt'
    f = open(os.path.join(file_dir, file_name), 'r')
    line = f1.readline()
    print(line)
    f.close()



if __name__=='__main__':
    get_student_info(Josh)
    get_student_info(Jerad)
    get_student_info(Greg)
    get_student_info(Dave)
    get_student_info(Mick)
    read_from_file()
##
##This is an ongoing project... A bit of help would be greatly appreciated. ;/
