from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

questions = []
for data in question_data:
    questions.append(Question(data["question"],data["correct_answer"]))
quiz_bank = QuizBrain(questions)

while (quiz_bank.still_has_questions()):
    quiz_bank.next_question()

print(f"Your final Score is :{quiz_bank.score}")