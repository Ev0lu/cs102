"""func from str to num"""
def to_number(num):
    try:
        if (float(num) - int(num)) == 0:
            return int(num)
    except:
        try:
            return float(num)
        except:
            return "string"
while True:
    s = input("Знак (+, -, *, /): ")
    if s == "0":
        break
    if s in ("+", "-", "*", "/"):
        a = to_number(input("a = "))
        b = to_number(input("b = "))
        if isinstance(a, str) is not True and isinstance(b, str) is not True:
            if s == "+":
                print(a + b)
            elif s == "-":
                print(a - b)
            elif s == "*":
                print(a * b)
            elif s == "/":
                if b != 0:
                    print(a / b)
                else:
                    print("Деление на ноль")
        else:
            print("Введите число")

    else:
        print("Неверный знак операции")
