#By considering the terms in the fibonacci sequence whoe values do not exceed four million, find the sum of the even valued terms?
set1 = [1, 2]
set2 = []
n = 0
f = 1
j = 0
k = 0
while j < 4000000:
    j = set1[n] + set1[f]
    set1.append(j)
    n += 1
    f += 1

while k < len(set1):
    if set1[k] % 2 == 0:
        set2.append(set1[k])
    k += 1
total = 0
for number in set2:
    total += number

print(f"{total}")
