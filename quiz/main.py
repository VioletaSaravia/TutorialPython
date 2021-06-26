from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    question_text = x['text']
    question_answer = x['answer']
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)
breakpoint()
# print(question_bank)
# print(question_bank[1].text)

quiz = QuizBrain(question_bank)
quiz.next_question()

print(f'Tu puntaje final es {quiz.victorias}/{quiz.partidas}\n')
