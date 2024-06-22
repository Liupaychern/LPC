def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Unsupported character or syntax"
    except:
        return "Error: Invalid expression"

def check_balanced_parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def main():
    while True:
        expression = input("Enter an arithmetic expression (or 'q' to quit): ").strip()
        
        if expression.lower() == 'q':
            print("Exiting program.")
            break
        
        if not expression:
            print("Please enter a non-empty expression.")
            continue
        
        if not all(char.isdigit() or char in '+-*/()' for char in expression):
            print("Error: Unsupported character")
            continue
        
        if not check_balanced_parentheses(expression):
            print("Error: Unbalanced parentheses")
            continue
        
        try:
            result = evaluate_expression(expression)
            print("Result:", result)
        except:
            print("Error: Invalid expression")

if __name__ == "__main__":
    main()
