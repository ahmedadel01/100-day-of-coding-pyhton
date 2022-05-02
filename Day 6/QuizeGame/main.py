from question_model import Question
from data import questionData
from quiz_brain import QuizBrain


questionBank = []
for question in questionData:
    questionText = question["text"]
    questionAnswer = question["answer"]
    newQestion = Question(questionText, questionAnswer)
    questionBank.append(newQestion)

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestion():
    quiz.nextQuestion()

print("You've completed the quiz")
print(f"Your final scour was: {quiz.score}/{quiz.questionNum}")
