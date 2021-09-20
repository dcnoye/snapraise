from collections import deque

opStack = deque()
operators = ["+", "-", "*", "/"]
msg = """
  Welcome to the Reverse Polish notation Calculator!

  Currently the calculator supports the basic four mathematical operators:
  
          +, -, *, /,

  Usage is simply!
      You can enter all right in a row like this 
         > 5 5 5 8 + + -

      Or one at a time
         >5
         5
         >8
         8
         >+
         13

  To exit, enter 'q'
       """

def main():
    print(msg)
    try:
        while True:
            expr = input('>')
            if expr == 'q':
                break
            else:
                res = postfix(expr)
                if res == 'e':
                    print('Invalid expression\n')
                else:
                    print(res)
    except KeyboardInterrupt:
        print('\nCancelling...')
    except EOFError:   # Catch the Ctrl-D
        print('\nCancelling...')


def postfix(expr):
    exprList = expr.split(" ")
    try:
        for op in exprList:
            if op in operators:
                op2 = opStack.pop()
                op1 = opStack.pop()
                result = calc(op, op1, op2)
                opStack.append(result)
            else:
                opStack.append(float(op))
    except Exception:
        return 'e'

    return opStack[-1]


def calc(op, op1, op2):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2


if __name__ == '__main__':
    main()
