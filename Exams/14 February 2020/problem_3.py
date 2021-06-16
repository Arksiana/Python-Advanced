def stock_availability(*args):
    inventory = args[0]
    command = args[1]

    if command == 'delivery':
        to_add = args[2:]
        for el in to_add:
            inventory.append(el)

    if command == 'sell':
        extra = args[2:]
        if extra:
            for el in extra:
                if type(el) == int:
                    inventory = inventory[el:]
                else:
                    inventory = [el for el in inventory if el not in extra]
        else:
            inventory.pop(0)

    return inventory


import unittest


class Tests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"),
                         ['choco', 'vanilla', 'banana', 'caramel', 'berry'])
        self.assertEqual(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"),
                         ['chocolate', 'vanilla', 'banana', 'cookie', 'banana'])
        self.assertEqual(stock_availability(["chocolate", "vanilla", "banana"], "sell"), ['vanilla', 'banana'])
        self.assertEqual(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3), [])
        self.assertEqual(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"), ['banana'])
        self.assertEqual(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"),
                         ['cookie', 'banana'])
        self.assertEqual(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"),
                         ['chocolate', 'vanilla', 'banana'])


if __name__ == "__main__":
    unittest.main()
