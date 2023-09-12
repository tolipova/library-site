print("\n Onlayn darsliklar kutibxonasiga Xush Kelibsiz!!!")
print("Kirish uchun login va tug'ri parol kiriting")

while True:
    login=input("login = ")
    parol=input("parol = ")

    if parol == '6-sinf':
        print("\n Marhamat 6-sinlar uchun kerakli kitoblar ruyxati bilan tanshing:")
        break
    else:
        print("Xato parol")
        continue
kitoblar=['ona tili','adabiyot','algebra','geografiya','tarix','rus tili','biologiya']
print(kitoblar)
print()

class Darsliklar:
    def __init__(self,name,aftor,page,chiqgan_vaqti,ijara):
        self.name = name 
        self.aftor = aftor 
        self.page = page
        self.chiqgan_vaqti = chiqgan_vaqti
        self.ijara = ijara
    def darslik_malumoti(self) :
        print("Darslikning nomi", self.name)
        print("Darslikni", self.aftor , "yozgan")
        print("Kitob", self.page, "dan iborat")
        print("Kitob", self.chiqgan_vaqti,"da sotuvga chiqgan")
        print("Kitobning ijara narxi", self.ijara,"so'm 6-sinflar uchun")



a = Darsliklar("biologiya","To'xtamurod Ochilov", 324 ,"2016-yil",26.000)
a.darslik_malumoti()
print()


a = Darsliklar("algebra","Murod Tursunov", 238 ,"2016-yil",28.300)
a.darslik_malumoti()
print()


a = Darsliklar("ona tili","Mansur Yo'ldoshev", 350 ,"2015-yil",17.600)
a.darslik_malumoti()
print()


a = Darsliklar("adabiyot","Lochin Ergashev va Saodat Qobilova", 290 ,"2015-yil",17.000)
a.darslik_malumoti()
print()


a = Darsliklar("tarix","Yusuf Ergashev", 267 ,"2023-yil",40.000)
a.darslik_malumoti()
print()


a = Darsliklar("geografiya","Olim Mamadaliyev", 187 ,"2022-yil",19.000)
a.darslik_malumoti()
print()

a = Darsliklar("rus tili","Alisher Shuhratov", 221 ,"2023-yil",25.000)
a.darslik_malumoti()
print()


total=26.0+28.3+17.6+17.0+40.0+19.0+25.0
print("Jami kitoblar narxi: ",total,"so'm")


while True:

  k=input("kerakli kitob nomini kiriting: ")
  if k == a:
    print("Bu kitob uchun belgilangan narxni carta orqali to'lang va sizga kitobni jo'natamiz")
  else:
    print("Ruyxatda yo'q kitobni kirittiz yoki xato bor")    
