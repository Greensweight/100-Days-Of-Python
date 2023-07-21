from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for question in question_data:
    new_q = Question(question["text"], question["answer"])
    print(f"The text is {new_q.text} and the answer is {new_q.answer}")
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)
quiz.next_question()
