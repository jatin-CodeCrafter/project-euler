#By considering the terms in the fibonacci sequence whoe values do not exceed four million, find the sum of the even valued terms?
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
