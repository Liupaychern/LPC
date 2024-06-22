import re

expression = "X^5+3*X+2"
expression = "-X^3-12*X^2+100"
expression = "X^X+X*X+X"
expression = "X^4+23*X^3+17*X^2+9453"
x_value = -11

expression = expression.replace("+", " + ")
expression = expression.replace("-", " - ")

while "^" in expression:
    index = expression.find("^")
    print(f"index: {index}")

    coefficient = ""
    coefficient_index = index - 1
    # Find the number before the "^"
    for i in range(index - 1, -1, -1):
        if expression[i] == " " or expression[i] == "*":
            break
        coefficient = expression[i] + coefficient
    print(f"coefficient: {coefficient}")

    # Find the number after the "^"
    exponent = ""
    for i in range(index + 1, len(expression)):
        if expression[i] == " ":
            break
        exponent += expression[i]
    print(f"exponent: {exponent}")
    # break

    # Replace the expression with the result
    print(f"coeff: {coefficient}, operator: ^, exp: {exponent}")
    term = coefficient + "^" + exponent

    if coefficient == "X" and exponent == "X":
        term_value = x_value**x_value
    elif coefficient == "X":
        term_value = x_value ** int(exponent)
    elif exponent == "X":
        term_value = int(coefficient) ** x_value
    else:
        term_value = int(coefficient) ** int(exponent)
    print(f"term: {term}")
    print(f"term_value: {term_value}")

    # replace the term with the value
    expression = expression.replace(term, str(term_value))
    print(f"expression: {expression}")

while "*" in expression:
    index = expression.find("*")
    print(f"index: {index}")

    front = ""
    # Find the number before the "*"
    for i in range(index - 1, -1, -1):
        if expression[i] == " ":
            break
        front = expression[i] + front
    print(f"front: {front}")

    # Find the number after the "*"
    tail = ""
    for i in range(index + 1, len(expression)):
        if expression[i] == " ":
            break
        tail += expression[i]
    print(f"tail: {tail}")

    # Replace the expression with the result
    print(f"front: {front}, operator: *, tail: {tail}")
    term = front + "*" + tail

    if front == "X" and tail == "X":
        term_value = x_value * x_value
    elif front == "X":
        term_value = x_value * int(tail)
    elif tail == "X":
        term_value = int(front) * x_value
    else:
        term_value = int(front) * int(tail)
    print(f"term: {term}")
    print(f"term_value: {term_value}")

    # replace the term with the value
    expression = expression.replace(term, str(term_value))
    print(f"expression: {expression}")

# replace the "X" with the value
expression = expression.replace("X", str(x_value))

# replace the spaces
expression = expression.replace(" ", "")
print(f"expression: {expression}")

# find if there exists two consecutive operators "--"
while "--" in expression:
    expression = expression.replace("--", "+")
print(f"expression: {expression}")

# replace the "-" with "+-"
expression = expression.replace("-", "+-")
print(f"expression: {expression}")

# split the expression by "+"
terms = expression.split("+")
print(f"terms: {terms}")

result = 0
for term in terms:
    # print(term.strip())
    if term.strip() == "":
        continue
    result += int(term.strip())
print(f"result: {result}")
