a=int (input(" Multiplication table starts with the number: "))
b=int(input(" Multiplication table ends with the number:"))
for i in range(a,b+1):
    for j in range (1,11):
        print(f"{i}x{j}={j*i}")
    print()