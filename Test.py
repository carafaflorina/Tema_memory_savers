students = [
    {
        'nume': 'Lenny',
        'nota': 10
    },
    {
        'nume': 'Simona Halep',
        'nota': 4
    },
    {
        'nume': 'NoName',
        'nota': 3
    }
]

students_admisi = list(filter(lambda s: s.get('nota') < 5, students))
print(students_admisi)