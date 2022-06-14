from question_model import Question
from quiz_brain import QuizBrain
import requests, html
from ui import QuizInterface
# Get question data from API----------------------
# set parameters
parameters= {
    "amount" : 10,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php",params=parameters)
#check if any errors
response.raise_for_status()
data = response.json()
# store data to question_data
question_data = data["results"]


question_bank = []
for question in question_data:
    #split the question data to question and answer, then store in question object
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(html.unescape(question_text), question_answer)
    #put the question in th the question bank
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
#
ui =QuizInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()
#
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")

