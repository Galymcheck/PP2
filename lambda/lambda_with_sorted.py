students = [("Windows", 25), ("MacOs", 22), ("Linux", 28)]
sorted_students = sorted(students, key=lambda x: x[1]) #sorted by increasing order
print(sorted_students)
sorted_students = sorted(students, key=lambda x: x[0]) #sorted by alphabet
print(sorted_students)