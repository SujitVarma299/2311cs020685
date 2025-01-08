# 1
n = int(input("Enter a positive integer: "))
print("Numbers from 1 to", n, ":")
for i in range(1, n + 1):
    print(i)
sum_of_numbers = 0
i = 1
while i <= n:
    sum_of_numbers += i
    i += 1
print("The sum of all numbers from 1 to", n, "is:", sum_of_numbers)

# 2
def calculate_square(m):
    return n * n
m = int(input("Enter a positive integer: "))
square_of_m = calculate_square(m)
print(f"The square of {m} is: {square_of_m}")