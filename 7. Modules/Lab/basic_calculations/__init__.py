def print_calculations(ex):
    num_1, sign, num_2 = ex.split(" ")
    num_1 = float(num_1)
    num_2 = int(num_2)

    if sign == "/":
        return num_1 / num_2
    elif sign == "*":
        return num_1 * num_2
    elif sign == "-":
        return num_1 - num_2
    elif sign == "+":
        return num_1 + num_2
    elif sign == "^":
        return num_1 ** num_2

