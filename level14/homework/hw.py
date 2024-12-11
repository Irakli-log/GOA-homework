age = int(input("შეიტანეთ თქვენი ასაკი: "))

if age >= 18 and age < 50:
    print("თქვენ ხართ ახალგაზრდა.")
elif age < 18 or age > 50:
    print("თქვენ ხართ მოხუცი.")
else:
    print("არასწორია მონაცემი")