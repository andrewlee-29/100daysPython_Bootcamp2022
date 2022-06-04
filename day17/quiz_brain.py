class QuizBrain:

    def __init__(self, data_list):
        self.question_number = 0
        self.question_list = data_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q. {self.question_number}{current_question.text} (True/False) ")
        self.checkanswer(current_question,ans)

    def still_has_questions(self):
        return (len(self.question_list)) > self.question_number

    def checkanswer(self,current_question,ans):
        if ans.lower() == current_question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You are wrong!!")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print("\n")