class Shuttichuai:
    # data
    yee = 100
    mee = ""

    # construtor ไม่ใช่ method member เเต่จะทำงานทุกครั้งที่มีการสร้าง Object 
    # ให้ object ทำงานเหมือนกันบ้างไม่เหมือนกันบ้างโดยกำหนดค่าใน parameter
    def __init__(self,ree,oee,mee):
        self.ree = ree
        self.oee = oee
        self.mee = mee

    # method
    def showData(self):
        print(self.yee * 20)

deeA = Shuttichuai(5,20,30)
deeB = Shuttichuai(40,50,60)
deeC = Shuttichuai(10,20,30)
deeD = Shuttichuai(8,9,10)
print (deeA.mee + deeB.mee)
deeC.showData()


