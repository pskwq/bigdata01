number = int(input())
count = 0

for i in range(1, number+1):
    if number % i == 0:
        count = count + 1
    print(i, end=" ")

if count == 2:
    print(f"{number}는 소수입니다")
else:
    print(f"{number}는 소수가아닙니다")