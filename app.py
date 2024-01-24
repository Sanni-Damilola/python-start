from classes_and_objects import student
from question import Question

student1 = student("Sanni", "Backend Developer", 4.5, False)
student2 = student("Bola", "Software Developer", 2.3, True)
# print(student2.on_honor_rol())


question_prompts = [
    "What Color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Green",
    "What Color are Bananas?\n(a) Magenta\n(b) Teal\n(c) Yellow",
    "What Color are strawberries?\n(a) Red\n(b) Yellow\n(c) Blue"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    total_questions = len(questions)

    for question in questions:
        answer = input(question.prompt + "\nYour answer: ")
        if answer.lower() == question.answer.lower():
            score += 1

    print(f"You got {score}/{total_questions} correct.")

# run_test(questions)