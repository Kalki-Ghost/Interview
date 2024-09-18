"""The program is to find the percentage of the student and print it."""

student_data = {
    'jay': {'details': {'roll': 101, 'marks': [92, 89, 90, 95, 78]}},
    'viru': {'details': {'roll': 102, 'marks': [61, 81, 91, 98, 79]}},
    'basanti': {'details': {'roll': 101, 'marks': [83, 89, 80, 95, 78]}},
    'thakur': {'details': {'roll': 101, 'marks': [52, 69, 90, 95, 78]}},
}
length = len(student_data['jay']['details']['marks'])
for name in student_data:
    percentage = sum(student_data[name]['details']['marks']) / length
    student_data[name]['details']['percentage'] = percentage
    print(f"{name} has got {round(percentage, 2)}%")

print(student_data)
