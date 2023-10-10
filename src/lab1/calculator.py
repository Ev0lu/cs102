"""calculator"""
def to_number(num):
    """func to convert str to num"""
    try:
        if (float(num) - int(num)) == 0:
            return int(num)
    except:
        try:
            return float(num)
        except:
            return "string"

def sum(first,second):
    """func for sum"""
    return first + second

def multiply(first,second):
    """func for mult"""
    return first * second

def sub(first,second):
    """func for sub"""
    return first - second

def div(first,second):
    """func for div"""
    if second != 0:
        return first / second
    else:
        return 'Деление на ноль'
def main():
    """func for calculating"""
    sign = input("Знак (+, -, *, /): ")
    if sign in ("+", "-", "*", "/"):
        first = to_number(input("first = "))
        second = to_number(input("second = "))
        if isinstance(first, str) is not True and isinstance(second, str) is not True:
            if sign == "+":
                print(sum(first,second))
            elif sign == "-":
                print(sub(first,second))
            elif sign == "*":
                print(multiply(first,second))
            elif sign == "/":
                print(div(first,second))
        else:
            print("Введите число")

    else:
        print("Неверный знак операции")
if __name__ == "__main__":
    main()