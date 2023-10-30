""" for i in range(0,10,1):
    print(i)

biggestValue = 0
for i in range(5):
    sayi = int(input(f"{i+1}, sayi giriniz. "))
    if sayi > biggestValue:
        biggestValue = sayi

print(f"Girdiginiz sayilar arasinda en büyük olanı: {biggestValue}") """
""" 
forRangeMin = int(input("Döngünün alt limitini belirleyiniz"))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz"))

for i in range(forRangeMin, forRangeMax+1):
    if i % 2 == 0:
        print(i) """

""" sayilar = []
for i in range(3):
    sayilar.append(int(input(f"{i+1}. sayiyi giriniz.")))
sayilar.sort(reverse=True)
print(sayilar) """

ögrenciler = ["Gunes ", "Recep ", "Betül" , "Yunus" , "İrem"]
print(len(ögrenciler))

for i in range(len(ögrenciler)):
    if i>3:
        break
    print(ögrenciler[i])
    











