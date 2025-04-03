def sum_divisors(a):
    sum = 0
    for i in range (2, a):
        if a % i == 0 and  i!=a :
            sum+=i
        
    return sum

amicable_no = set({})

for i in range(0,1000):
    for j in range(0,1000):
        if sum_divisors(i) == j:
            amicable_no.add(i)
            amicable_no.add(j)
        elif sum_divisors(j)==i:
            amicable_no.add(j)
            amicable_no.add(i)

print(amicable_no)