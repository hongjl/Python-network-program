#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order,along with the answer key.

import random

# the quiz data,keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate 35 quiz files.

for quizNum in range(35):
    # create the quiz(小测验) and answer key files.
    quizFile = open('capitalsquiz%s.txt' %(quizNum+1),'w')  # 测验文件
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum+1),'w')  # 问题答案文件

    # write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')  
    quizFile.write((' '*20)+'State capitals quiz (form %s)' % (quizNum+1))
    quizFile.write('\n\n')

    # shuffle the order of the states.
    states = list(capitals.keys())  # 将全部州的名字生成一个列表
    random.shuffle(states)  # 原地打乱

    # loop through all 50 states,making a question for each
    for questionNum in range(50):  # 做出50道题

        # get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]  # 正确答案
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]  # 在错误答案的列表中，删去正确答案
        wrongAnswers = random.sample(wrongAnswers,3)  # 从错误答案中选出3个，返回一个列表
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # write the question and the answer options to the quiz file.
        quizFile.write('%s.what is the capital of %s?\n' % (questionNum+1,states[questionNum]))

        for i in range(4):
            quizFile.write( '%s.%s\n' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')
        

        # write the answer key to a file
        answerKeyFile.write('%s.%s\n' % (questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))  # 找到正确答案的下标
    quizFile.close()
    answerKeyFile.close()


















        
