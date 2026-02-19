numbers = [5, 8, -14, -7, -21, 9]
odd_numbers = list(filter(lambda x: x < 0 and x % 7 == 0, numbers))
print(odd_numbers)