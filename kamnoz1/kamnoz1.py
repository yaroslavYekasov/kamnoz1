import random
raund=1
point=0
print('Mäng "Kivi Käärid Paber"')
print()
print('Mängijad loevad koos kõva häälega "Kivi... Käärid... paber... üks... kaks... kolm", samal ajal rusikatega vehkides.  "Kolme" kontol näitavad nad korraga ühte kolmest märgist: kivi, käärid või paber.')
for i in range (3):
    print()
    print("round", raund)
    print()
    v=input("Valige kivi, käärid, paber> ")                  
    #if v == "kivi" or "käärid" or "paber":
    #    print("Sellist vastust ei ole.")
    #    break
    vibor2=["kivi", "käärid", "paber"]   
    v2=random.choice(vibor2)
    print("1 inimese valimine:", v)
    print("2 inimese valimine:", v2)
    if v == "käärid" and v2 == "paber":
        print( '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.(___)
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''')
        print("SA OLED PAAAAARIM")
        point+=1
    elif v == "paber" and v2 == "kivi":
        print( '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.(___)
    ''')
        print("SA OLED PAAAAARIM")
        point+=1
    elif v == "kivi" and v2 == "käärid":
        print( '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.(___)
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.(___)
    ''')
        print("SA OLED PAAAAARIM")
        point+=1
    elif v=="kivi" and v2=="kivi" or v == "käärid" and v2 == "käärid" or v == "paber" and v2 == "paber":
        print( '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.(___)
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.(___)
    ''')
        print("kasha")
    else:
        print("ahahahah, mis valesti läks :)")
    raund+=1
print()
print("point",point)
if point>=2:
    print("SA MÄNGID SEDA MÄNGU KÕIGE PAREMINIIII")
else:
    print(":(...")
