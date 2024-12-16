
num = int(input("შეიყვანეთ რიცხვი: "))

num5 = 0
num3 = 0

i = 1

while i <= num:
    if i % 5 == 0:
        num5 += i 
    if i % 3 == 0:
        num3 += i 
    i += 1 

print("5-ის ჯერადი რიცხვების ჯამი: " + str(num5))
print("3-ის ჯერადი რიცხვების ჯამი: " + str(num3))