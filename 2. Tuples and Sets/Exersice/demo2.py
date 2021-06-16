budget = int(input())
product = input()
result_cash = 0
result_card = 0
result = 0
counter = 0
counter_cash = 0
counter_card = 0
average_cs = 0
average_cc = 0
while product != "End":
    product = int(product)
    counter += 1
    if counter % 2 != 0:
        if product > 100:
            print("Error in transaction!")
        else:
            result_cash += product
            counter_cash += 1
            print("Product sold!")
    elif counter % 2 == 0:
        if product <= 10:
            print("Error in transaction!")
        else:
            result_card += product
            counter_card += 1
            print("Product sold!")
    result = result_cash + result_card
    if result >= budget:
        average_cs = result_cash / counter_cash
        average_cc = result_card / counter_card
        print(f"Average CS: {average_cs:.2f}")
        print(f"Average CC: {average_cc:.2f}")
        break
    product = input()


if product == "End":
    print("Failed to collect required money for charity.")

