#QuizMaker

#A program to make mini quizzes for onennote, or pdf printout.

#input of questions and production of simple numerical question types, aimed at AQA GCSE Specification 8525

#imports
import csv
import random

#subroutines

#import questions
#[ "Section number", "Question", "Answer"]

def import_questions():
    
    data = [
        ["3.1","What is the binary for 123?", "1111011"],
        ["3.1","What is the hexadecimal for 16?","10"], 
        ["3.3", "What is the impact on file size of increasing resolution?","increases file size"],
        ["3.4","Q4","A4"],
        ["3.5","Q5","A5"],
        ["3.6","Q6","A6"],
        ["3.7","Q7","A7"]
    ]
    
    return data

#output_pdf

def create_number_question():
    randombase = random.randint(1,6)
    question = []
    #dec to bin // done
    if randombase == 1:
        start = "What is the binary for the decimal number "
        randomq = random.randint(1,255)
        answer = str(bin(randomq))[2:]
        question = ["3.1", start + str(randomq), answer]
        return question
    #bin to dec 
    if randombase == 2:
        start = "What is the decimal for the binary number "
        randomnum = random.randint(1,255)
        randomq = bin(randomnum)[2:]
        answer = randomnum
        question = ["3.1", start + str(randomq), answer]
        return question
    #hex to bin //done
    if randombase == 3:
        start = "What is the binary for the hexadecimal number "
        randomq = hex(random.randint(16,255))[2:]
        answer = bin(int(randomq,16))[2:]
        question = ["3.1", start + str(randomq).upper(), answer]
        return question
    #bin to hex
    if randombase == 4:
        start = "What is the decimal for the binary number "
        randomnum = random.randint(1,255)
        randomq = bin(randomnum)[2:]
        answer = randomnum
        question = ["3.1", start + str(randomq), answer]
        return question
    #hex to dec
    if randombase == 5:
        start = "What is the decimal for the hexadecimal number "
        randomnum = random.randint(1,255)
        randomq = hex(randomnum)[2:]
        answer = randomnum
        question = ["3.1", start + str(randomq), answer]
        return question
    #dec to hex
    if randombase == 6:
        start = "What is the hexadecimal for the decimal number "
        randomnum = random.randint(1,255)
        randomq = randomnum
        answer = hex(randomnum)[2:]
        question = ["3.1", start + str(randomq), answer]
        return question


#output simple txt
def create_quiz(length, data):
    quiz = []
    for i in range(1,length+1):
        #q = random.choice(data)

        q = create_number_question()
        quiz.append(q)
    
    return quiz


#user input
#asks user for question sections to be included

#main
def main():
    data = import_questions()
    quiz = create_quiz(10, data)
    qnum = 1
    for question in quiz:
        print()
        print("Q" + str(qnum))
        print(question[1])
        print(question[2])
        qnum += 1
    
main()