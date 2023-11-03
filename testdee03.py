# คุณสมบัติเด่น  OOP : Encapsulation (ซ่อนไว้ or ห่อหุ้ม)
# ห่อหุ้ม or ซ่อน โดยใส่ __ ไว้หน้า data หรือตัวเเปร
class MypuxxyA : 
    __data1 = 10
    data2 = 20

    # เมื่อ data ถูก Encaap. การกำหนดค่าหรือเอาค่ามาใช้
    # ให้ผ่านเมธอด get เอาค่ามาใช้/set กำหนดค่า
    def getData1(self):
        return self.data1
    
    def setData1(self,data1):
        self.__data1 = data1

    def getData3(self):
        return self.__data3
    
    def setData3(self,data3):
        self.__data3 = data3

    def __init__(self,data3):
        self.__data3 = data3

    def showData(self):
        print(f"__data1 มีค่า {self.__data1}")
        print(f"data2   มีค่า {self.data2}")
        print(f"__data3 มีค่า {self.__data3}")
        print("-------------------------------------")

aimerA = MypuxxyA(30)
aimerA.showData()
aimerA.data2 = 200
#aimerA.__data1 = 100
aimerA.setData1(100)
aimerA.setData3(999)
aimerA.showData()
print(aimerA.getData3())

