class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return len(self.question_list) > self.question_number
        
    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_q.text} (True/false): ").lower()
        self.check_answer(user_ans, current_q.answer)

    def check_answer(self, u_ans, c_ans):
        if u_ans == c_ans.lower():
            self.score += 1
            print(f"You got it right! Your score is {self.score}/{self.question_number}") 
        else:
            print(f"You got it wrong. Your score is {self.score}/{self.question_number}")

        print(f"The right answer was {c_ans} \n")