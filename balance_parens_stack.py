# Balance Parens with a Stack
def are_parens_balanced(symbols):
  """Are parentheses balanced in expression?"""

  # make a stack
  parens = Stack()

  for char in symbols:

    if char == "(":
      parens.push(char)   # push onto stack

    elif char == ")":
      if parens.is_empty():
          return False
      else:
          parens.pop()      # pop from stack

  return parens.is_empty()

are_parens_balanced("((3+4)-(1+2))/(1+1)")
