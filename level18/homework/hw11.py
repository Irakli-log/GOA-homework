#) მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ კენტი რიცხვები




num = int(input("ჩაწერეთ რიცხვი"))

for i in range(num + 1):
      if i % 3 == 0:
        print(i)