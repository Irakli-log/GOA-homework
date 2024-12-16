num = int(input("ჩაწერეთ ციფრი: "))

even_sum = 0
odd_sum = 0

for i in range(1, num +1):
    if i % 2 == 0:
        even_sum += 1
    else:
        odd_sum += 1

print(even_sum)
print(odd_sum)