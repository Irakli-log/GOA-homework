num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
num2 = float(input("შეიტანეთ მეორე რიცხვი: "))
mimateba = num1 + num2
gamokleba = num1 - num2
gamravleba = num1 * num2
gayofa = num1 / num2 if num2 != 0 else "შეუძლებალია ნულზე გაყოფა"

print(f"{num1} + {num2} = {mimateba}")
print(f"{num1} - {num2} = {gamokleba}")
print(f"{num1} * {num2} = {gamravleba}")
print(f"{num1} / {num2} = {gayofa}")


