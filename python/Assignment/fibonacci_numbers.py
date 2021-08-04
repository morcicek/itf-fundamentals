fibonacci_numbers = []
a, b = 0, 1
while a < 55:
    a, b = b, a+b
    fibonacci_numbers.append(a)

print(fibonacci_numbers)
