# Lambda test

num = (lambda x: x * -1)
print(num(4))

num2 = lambda y: y * 2
print(num2(3))

def Double(num):
    return num * 2

numbers = [1, 2, 3]
print(list(map(Double, numbers)))

# Equivalent in Lambda
print(list(map(lambda x: x * 3, numbers)))

squared = lambda num: num * num
print(f"5 square is {squared(5)}")

# Filter
print(f"Numbers greater than 10: {list(filter(lambda x: x > 10, [1, 20, 40, 25, 16, 9, 8]))}")