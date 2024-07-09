from data import Questions_bank
from Question import question
from Quiz import Quiz

ques_obj_list =[]
for i , ques in enumerate(Questions_bank):
    ques = question(ques["ques"], ques["ans"])
    ques_obj_list.append(ques)



quiz = Quiz(ques_obj_list)

while quiz.question_no < len(ques_obj_list):
    quiz.nxt_question()

print(f"Wow! You completed the quiz: \nyour Score is {quiz.score}")



