import unittest

def decimal_to_roman(decimal):
    total = ""
    if decimal >= 100:
        centena = decimal // 100
        total = "C" * centena
        decimal = decimal % 100
    if decimal <= 3:
        total += "I" * decimal
    elif decimal == 5:
        total += "V"
    elif decimal == 10:
        total += "X"
    return total

if __name__ == "__main__":
    unittest.main()


