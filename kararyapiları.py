Not = input("Lütfen notunuzu giriniz")
print(type(Not))
NotAsInteger = int(Not)
print(type(NotAsInteger))

if NotAsInteger >80:
    print("Harika,geçtiniz")
    if NotAsInteger >90:
        print("bravo")

elif NotAsInteger >50:
   print("başarılı")

else:
    print("kaldınız")


