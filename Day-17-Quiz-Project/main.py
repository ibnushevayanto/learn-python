from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item['text'], item['answer']))

quiz_brain = QuizBrain(question_bank)

while True:
    quiz_brain.next_question()
    if quiz_brain.getIsNotHaveQuestionAgain() == True:
        break
