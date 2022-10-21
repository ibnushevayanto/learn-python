class QuizBrain:

    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_number = 0

    def next_question(self):
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {self.questions[self.question_number - 1].text}. (True/False)?: ").lower()
        self.check_answer(self.question_number, answer)

    def check_answer(self, question_number, answer):
        question_answer = self.questions[question_number - 1].answer.lower()
        is_correct_answer = question_answer == answer

        if is_correct_answer == True:
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")

        print(f"The correct answer was: {question_answer}")
        print(f"Your current score is: {self.score}/{question_number}\n")
        return is_correct_answer

    def getIsNotHaveQuestionAgain(self):
        return self.question_number == len(self.questions)
