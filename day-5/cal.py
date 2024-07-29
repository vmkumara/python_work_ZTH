import sys

def add(num1, num2, num3):
    add = num1 + num2 + num3
    return add

def sub(num3, num2):
    sub = num3 - num2
    return sub

def mul(num1, num2, num3, num4):
    mul = num1 * num2 * num3 * num4
    return mul

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])
operator = sys.argv[4]
num3 = float(sys.argv[5])
operator = sys.argv[6]
num4 = int(sys.argv[7])


if operation == "mul":
    output = mul(num1, num2, num3, num4)
    print(output)

