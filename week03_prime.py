number = int(input())
is_prime = True

if number >= 2:
    for i in range(2, number):
        if number % i == 0:
            count = count + 1
        print(i, end=" ")
else:
    is_prime = False

if is_prime == 2:
     print(f"{number}는 소수입니다")
else:
     print(f"{number}는 소수가아닙니다")