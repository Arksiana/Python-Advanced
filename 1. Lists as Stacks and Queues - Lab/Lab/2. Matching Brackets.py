# expr = input()
# stack = []
#
# for char in expr:
#     if char == '(':
#         stack.append("")
#
#     for index in range(len(stack)):
#         stack[index] += char
#
#     if char == ")":
#         sub_expression = stack.pop()
#         print(sub_expression)
#
#
# another way

def subexpression_printer(expression):
    stack = []
    for index, char in enumerate(expression):
        if char == "(":
            stack.append(index)
        elif char == ')':
            end_index = index
            start_index = stack.pop()
            print(expression[start_index:end_index + 1])


subexpression_printer(input())
