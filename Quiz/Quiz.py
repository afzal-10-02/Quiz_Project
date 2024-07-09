class Quiz:
    def __init__(self, ques_obj_list):
        self.question_no =0
        self.score =0
        self.ques_obj_list =ques_obj_list
    
    def nxt_question(self):
        current_question = self.ques_obj_list[self.question_no].question
        current_answer = self.ques_obj_list[self.question_no].answer
        
        self.question_no+=1
        user_answer = input(f'Qno.{self.question_no}: {current_question} True/false? ')

        self.check_answer(current_answer , user_answer)
    
    def check_answer(self, current_answer , user_answer):
        if user_answer.lower()==current_answer.lower():
            self.score+=1
            print(f"That's Correct Answer \nScore: {self.score}")
            
        else:
            print(f'Incorrect Answer \nScore: {self.score}')
            
