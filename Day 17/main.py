from question_model import Question
from data import question_data

question_Bank = [
    Question(question["text"], question["answer"]) for question in question_data
]

print(question_Bank[0].text)
