# Write a program to sort a stack such that the smallest items are on the top.


def sort_stack(stack):
    temp = Stack()
    prev = stack.pop()
    current = stack.pop()

    while current:
        if current < prev:
            temp.push(current)

        else:
            temp.push(prev)
            prev = current
        current = stack.pop()
    is_sorted = True
    current = temp.pop()
    while current:
        if current > prev:
            is_sorted = False
            stack.push(current)
        else:
            stack.push(prev)
            prev = current
        current = temp.pop()

    stack.push(prev)
    if is_sorted:
        return stack

    return sort_stack(stack)