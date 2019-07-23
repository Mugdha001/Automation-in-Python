#  
#  Reference: Automate Boring Stuff with Python
#  Date: 07/23/2019
#  Author: Mugdha Wadikar
#  Purpose: Say you’re a geography teacher with 35 students in your class
#           and you want to give a pop quiz on US state capitals.
#           Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat.
#           You’d like to randomize the order of questions so that each quiz is unique,
#           making it impossible for anyone to crib answers from anyone else.
#           Of course, doing this by hand would be a lengthy and boring affair.
#           Fortunately, you know some Python.
#
######################################################################################################

# to randomize the process of picking questions and answer options
from random import choice
import random

# the capitals dictionary consists of key value pairs of States and their correct Capitals 
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
   'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
   'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
   'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
   'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
   'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
   'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany','North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
   'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
   'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
   'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# create a list of both capitals and states to be used in feeding the choice method for randomness
capitalList = list(capitals.values())
stateList = list(capitals.keys())

# iterate for 35 times
for i in range(35):
    stateSet = []
    #stateSet = set()
    # create a randomized set of States for each student
    while len(stateSet)<50:
        stateSelect = random.choice(stateList)
        if stateSelect not in stateSet:
            stateSet.append(stateSelect)

    # file names for each Quiz Set
    quizName = "quizSet"+str(i+1)
    fileObj = open(quizName, 'w')
    fileObj.write("\t\t\t\t\tGEOGRAPHY QUIZ SET : " + str(i+1) + "\n\n")
    fileObj.write("\t\t\tSelect capital of each state \n\n\n")
    n=1

    # generate unique Answer key for each Quiz Set (for teacher's reference)
    answerName = "answerSet"+str(i+1)
    ansObj = open(answerName, 'w')
    ansObj.write("\t\t\t\tGEOGRAPHY ANSWER SET : " + str(i+1) + "\n\n")

    # iterate for each state in the unique stateSet
    for state in stateSet:
        fileObj.write("\tQuestion number " + str(n) + " : ")
        fileObj.write(state+" \n")

        # add Question and Corresponding answers to the answer Set
        ansObj.write("\tQuestion number " + str(n) + " : ")
        ansObj.write(state+" \n")
        ansObj.write("\tAnswer:\t" + capitals[state] + "\n\n")       
        

        # create unique answer mcq options for quiz. First add the correct answer to the mcq options
        ansSet={capitals[state]}

        # add 3 other incorrect State Values
        while len(ansSet)<4:
            ansSet.add(choice(capitalList))

        # optionsAscii is used to print a), b), c), d) at the start of options
        optionsAscii = 97
        for val in ansSet:
            fileObj.write("\t\t" + chr(optionsAscii) + ") " + val + " \n")
            optionsAscii+=1
        fileObj.write("\n\n")
        n+=1

    
    fileObj.close()
    ansObj.close()
    
