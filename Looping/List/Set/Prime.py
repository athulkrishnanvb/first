my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
prime_numbers = []
for num in my_set:
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print("Prime numbers in the set:", prime_numbers)
