#sum of all the multiples of 3 or 5 below 1000?
set1 = set()
i = 0
total = 0
while i< 1000:
    if i%3 == 0:
        set1.add(i)
    elif i%5 == 0:
        set1.add(i)
    i+=1
for n in set1:
    total += n
        
print(total)
