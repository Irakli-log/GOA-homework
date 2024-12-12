num = int(input("გთხოვთ შეიყვანოთ რიცხვი: "))

if num <= 10:
    for i in range(1, num + 1):
        print(i)
else:
    print("რიცხვი მეტია 10-ისგან")
