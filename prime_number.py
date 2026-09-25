# Check whether a number is prime

num = int(input("Enter a number: "))

if num <= 1:
    print("It is not a Prime Number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")
