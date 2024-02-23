# students = ["Hermilone", "Harry", "Ron"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# for student in students:
#     print(student)
    
# for i in range(len(students)):
#     print(i + 1, students[i])


# students = {
#     "Hermilone": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }

# print(students["Hermilone"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])


# for student in students:
#     print(f"My name is {student} i live in {students[student]}")
#     print(student, students[student], sep=", ")



students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None,
    },
]


for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

