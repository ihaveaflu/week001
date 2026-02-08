two = input("Expression: ")
parts = two.split()
num1 = int(parts[0])
op = parts[1]
num2 = int(parts[2])

if op == "+":
    ans = num1 + num2
elif op == "-":
    ans = num1 - num2
elif op == "*":
    ans = num1 * num2
else:
    ans = num1 / num2

print(f"{ans:.1f}")
