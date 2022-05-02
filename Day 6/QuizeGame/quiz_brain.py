class QuizBrain:

    def __init__(self, qList):
        self.questionNum = 0
        self.questionList = qList
        self.score = 0


    def stillHasQuestion(self):
        return self.questionNum < len(self.questionList)


    def nextQuestion(self):
        currentQestion = self.questionList[self.questionNum]
        self.questionNum += 1
        input(f"Q. {self.questionNum}: {currentQestion.text} (True/False): ")

    
    def checkAnswer(self, userAnswer, corretAnswer):
        if userAnswer.lower() == corretAnswer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"the correct answer was: {corretAnswer}.")
        print(f"Your current score is: {self.score}/{self.questionNum}")
        print("\n")
