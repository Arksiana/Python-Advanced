def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


def fibonacci_seq(num):
    fibonacci_list = []
    for n in range(num):
        fibonacci_list.append(recur_fibo(n))
    return fibonacci_list


def fibonacci_locate(list, num):
    if num in list:
        return f'The number - {num} is at index {list.index(num)}'
    else:
        return f'The number {num} is not in the sequence'