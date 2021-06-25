from data import question_data
from question_model import Question

question_bank = []

for x in question_data:
    question_text = x['text']
    question_answer = x['answer']
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

print(question_bank)
print(new_q)
