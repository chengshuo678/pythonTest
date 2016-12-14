# 生成随机的测试试卷的文件

import random
testData = {'AA': 1, 'BB': 2, 'CC': 3, 'DD': 4}

# create the quiz
for quizNum in range(5):
    # create the quiz and answer key files
    quizFile = open('capitalsquiz%s.txt' %(quizNum + 1),'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '* 20) + 'State Capitals Quiz (Form %s)' % (quizNum +1))
    quizFile.write('\n\n')

    # Shuffle the order of the states
    states = list(testData.keys())
    random.shuffle(states)

    # create  the answer options
    for questionNum in range(4):
        correctAnswer = testData[states[questionNum]]
        # print(type(testData.values()))
        wrongAnswers = list(testData.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions) # 打乱顺序

        # write the question and answer options to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum+1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        # write the answer to the answer file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
answerKeyFile.close()









