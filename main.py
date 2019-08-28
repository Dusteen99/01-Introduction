#!/usr/bin/env python3

import utils
import time

utils.check_version((3,7))
utils.clear()

#Answering the questions, making the program wait
print('My name is Dustin Adkins.')
print('My favorite game is Dark Souls, but I really enjoy Runescape and League of Legends as well.')
print('The only concern that I have about this class is that it may not be as in-depth as I would like.')
print('I am excited to work with others on bigger projects and actually creating games.')
print('My user number is 11991236.')
print('My Github profile is located at https://github.com/Dusteen99')
print('')
time.sleep(10)

#Creating an elipsis and making the program wait in order to add something fun.
print('.')
time.sleep(1)
print('..')
time.sleep(1)
print('...')
time.sleep(1)
print('')
print('What are you still doing here?')
print('')
time.sleep(3)

#Taking input from user, making it a string that I can check
color = input("Now I would like to ask you questions. What is your favorite color? ")
color = color.lower().strip()

#Asking the user about their favorite color and job, giving different responses based on answer using if-else
job = ""
if (color == "blue"):
    print('Wow, that is also my favorite!')
    job = input("Do you have a job? If so, just tell me what you do as a job. ")
    job = job.lower().strip()
else:
    job = input("What a strange color! Do you have a job? If so, just tell me what you do as a job. ")
    job = job.lower().strip()

#Same as the previous section
if (job == "no" or job == "no."):
    print('Hmmm... I wonder how you make money.')

#Adding a little joke for people who don't like this
age = input("How old are you? ")
fun = input("Are you having fun answering my questions? ")
fun = fun.lower().strip()

#Terminating program, for loop counts to 100 as a joke to entertain user
if (fun == "no" or fun == "no."):
    print('I am sorry to hear that. Instead of more questions, I will count to 100 for you.')
    time.sleep(3)
    for i  in range(100):
        print('{}'.format(i + 1))
    time.sleep(2)
    print('Now I am the one that is bored. Goodbye.')
else:
    print('Too bad. This is the end of me. I am terminating. Goodbye.')




