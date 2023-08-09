# With List Comprehension
greetings = ['hello', 'hi', 'hey', 'hola']
letter_list = [greeting[1] for greeting in greetings]
print(letter_list)

# Without List Comprehension
greetings = ['hello', 'hi', 'hey', 'hola']
letter_list = []
for greeting in greetings:
    letter_list.append(greeting[1])
print(letter_list)

# With List Comprehension
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [digit for digit in digits if digit % 2 == 1]
print(odd_numbers)

# Without List Comprehension
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = []
for digit in digits:
    if digit % 2 == 1:
        odd_numbers.append(digit)
print(odd_numbers)
