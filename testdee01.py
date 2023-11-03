# สร้าง Class ใน Python
class Baramee :
    #data เหมือนกับตัวเเปร
    info1 = 20
    info2 = ""

    #method member เหมือนกับฟังก์ชั่น
    def showprint(self):
        print("NaHee")

    def showinfo(self):
        print(self.info1, self.info2)
        self.showprint()

# สร้าง Object
lastA = Baramee()
lastB = Baramee()
lastC = Baramee()

lastA.info1 = 100
print(lastA.info1 + lastB.info1) # 120
lastC.showinfo()
lastB.showinfo()

