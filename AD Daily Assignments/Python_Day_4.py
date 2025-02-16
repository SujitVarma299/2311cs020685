def sum_of_even_numbers(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total
n = int(input("Enter a positive integer: "))
result = sum_of_even_numbers(n)
print(f"The sum of all even numbers between 1 and {n} is: {result}")