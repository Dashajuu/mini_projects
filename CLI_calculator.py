#cli
history = []

def addition(*args):
    return sum([*args])


def subtraction(*args):
    l = [*args]
    x = l[0]

    for i in range(1, len(l)):
        x -= l[i]

    return x


def multiplication(*args):
    l = [*args]
    x = l[0]

    for i in range(1, len(l)):
        x *= l[i]

    return x


def division(*args):
    l = [*args]
    x = l[0]

    for i in range(1, len(l)):
        x /= l[i]

    return x


def calculate(expression):
    expression = expression.replace(" ", "")

    tokens = []
    num = ""

    for char in expression:
        if char.isdigit() or char == '.':
            num += char
        else:
            tokens.append(float(num))
            tokens.append(char)
            num = ""

    tokens.append(float(num))

    actions = {
        '+': addition,
        '-': subtraction,
        '*': multiplication,
        '/': division
    }

    i = 0

    while i < len(tokens):
        if tokens[i] in ('*', '/'):
            func = actions[tokens[i]]
            result = func(tokens[i - 1], tokens[i + 1])

            tokens[i - 1:i + 2] = [result]
            i -= 1

        else:
            i += 1

    i = 0

    while i < len(tokens):
        if tokens[i] in ('+', '-'):
            func = actions[tokens[i]]
            result = func(tokens[i - 1], tokens[i + 1])

            tokens[i - 1:i + 2] = [result]
            i -= 1
        else:
            i += 1

    return tokens[0]


def main():
    while True:
        expr = input(">>> ")

        if expr == "exit":
            break

        if expr == "history":
            for item in history:
                print(item)
            continue

        try:
            result = calculate(expr)
            record = f"{expr} = {result}"
            history.append(record)
            print(result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()