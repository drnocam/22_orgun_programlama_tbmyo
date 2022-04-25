import math

h = int(input("Silindirin Yüksekliğini Giriniz: "))
D = int(input("Silindirin Çapını Giriniz: "))
pi = math.pi

print("Yüzey alanı:" , pi*(D/2)**2 + pi*D*h ," cm^2")
print("Hacmi:" , pi*(D/2)**2 *h ,"cm^3")