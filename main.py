class Lugat:
    def __init__(self):
        self.lugat = {}

    def qoshish(self):
        kalit = input("Kalitni kiriting: ")
        qiymat = input("Qiymatni kiriting: ")
        self.lugat[kalit] = qiymat

    def ochirish(self):
        kalit = input("O'chiriladigan kalitni kiriting: ")
        if kalit in self.lugat:
            del self.lugat[kalit]
        else:
            print("Bunday kalit mavjud emas")

    def ko'rish(self):
        print(self.lugat)

    def boshqarish(self):
        while True:
            print("1. Kalit va qiymat qo'shish")
            print("2. Kalit va qiymat o'chirish")
            print("3. Lug'atni ko'rish")
            print("4. Chiqish")
            tanlov = input("Tanlovni kiriting: ")
            if tanlov == "1":
                self.qoshish()
            elif tanlov == "2":
                self.ochirish()
            elif tanlov == "3":
                self.ko'rish()
            elif tanlov == "4":
                break
            else:
                print("Noto'g'ri tanlov")

lugat = Lugat()
lugat.boshqarish()