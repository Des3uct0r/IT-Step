def сс(a):
    def wrapper(expression):
        try:
            return a(expression)
        except ZeroDivisionError:
            return "Error: Division by zero."
        except SyntaxError:
            return "Error: Invalid syntax."
        except Exception as e:
            return f"Error: {str(e)}"
    return wrapper
@сс
def calculate(expression):
    return eval(expression)
print(calculate("1 + 2"))
print(calculate("10 / 0"))
print(calculate("10 +"))
print(calculate("10 + a"))
