class QuizBrain():
    def __init__(self, question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.victorias = 0
        self.partidas = 0

        
    def chequear(self, respuesta, correcta):
        if respuesta.lower() == correcta.lower(): # Hacer ambos minúscula
            print("Correct.")
            self.victorias += 1
        else:
            print(f"Incorrect. The right answer was {correcta}.")
        self.partidas += 1
        print(f'Tu puntaje actual es {self.victorias}/{self.partidas}\n')

      
    def next_question(self):
        # if self.question_number == len(self.questions_list):
        #     return
        siguiente = self.questions_list[self.question_number]
        self.question_number += 1
        respuesta = input(f'Q.{self.question_number}: {siguiente.text} (True/False)?: ')
        self.chequear(respuesta, siguiente.answer)
        return self.next_question() if self.question_number != len(self.questions_list) else 0
        
