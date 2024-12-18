# შეადარეთ თქვენი ასაკი მომხმარებლის შემოტანილ ასაკს, თუ თქვენი ასაკი მეტია მომხმარებლის
#  ასაკზე უთხარით რომ თქვენ მასზე დიდი ხართ, თუ მასზე პატარა ხართ დაუპრინტეთ რომ მასზე
#  პატარა ხართ და სხვა შემთხვევაში დაუპრინტეთ რომ ტოლები ხართ.


age = int(input("enter your age: "))

if age == 18:
    print("vaa chemi toli yofilxar: ")
elif age <= 18:
    print("chemze patara yofilxar samwuxarod: ")
else:
    print("chemze didi xar ra sakvirvelia ")