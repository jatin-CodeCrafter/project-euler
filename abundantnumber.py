def get_divisors_sum(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

# Generate list of abundant numbers
LIMIT = 28123
abundant_numbers = [i for i in range(12, LIMIT + 1) if get_divisors_sum(i) > i]

# Create a boolean array to mark sums of two abundant numbers
can_be_written = [False] * (LIMIT + 1)

for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        s = abundant_numbers[i] + abundant_numbers[j]
        if s <= LIMIT:
            can_be_written[s] = True
        else:
            break

# Sum all numbers which cannot be written as the sum of two abundant numbers
non_abundant_sum = sum(i for i, can_write in enumerate(can_be_written) if not can_write)

print("The sum of all the positive integers which cannot be written as the sum of two abundant numbers is:", non_abundant_sum)
