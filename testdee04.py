# คุณสมบัติเด่น  OOP : Inheritance สืบทอด
# คือ คลาสหนึ่งสืบทอดอีกคลาสหนึ่ง (มีเเม่ super/มีลูก sub)
# พอเป็นเเม่ลูกกัน เเม่มีอะไรลูกมีด้วย
class YooA :
    data1 = 10
    data2 = 20

    def showGu() :
        print("Yoooooo....")

class YooB(YooA) :
    data3 = 30

    def showGa():
        print("Hooooooo....")

class YooC(YooA):
    data4 = 40

class YooD(YooB):
    data5 = 50

japanA = YooA()
japanB = YooB()
japanC = YooD()

# คุณสมบัติเด่น  OOP : Polymorphism พ้องรูป
# คือ พฤติกรรมเดียวกัน เเต่วิธีการต่างกัน (ต้องเป็นเเม่ ลูกกัน)
# คือ การที่ลูกเอา method ของเเม่ มาเขียนใหม่
class PklaA(YooA) :
    data6 = 60
    
    #Polymorphism : โด้ method ของเเม่มาใช้เป็นของตัวเอง (Overiding)
    def showGu():
        print("hahahahhahahaha")

japanD = PklaA()