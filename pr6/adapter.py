class PowerSocket():
    """
       PowerSocket base class 
    """
    def __init__ (self, holeNum, Shape, Volt):
        self.__num_holes = holeNum
        self.__hole_shape = Shape
        self.__volt = Volt

    def getHoleNum (self):
        return self.__num_holes 

    def getHoleShape (self):
        return self.__hole_shape 

    def getVolt (self):
        return self.__volt 


### some concrete PowerSocket classes
class chineseSocket(PowerSocket):
    def __init__ (self):
        super().__init__( 3, "FLAT", 220)
class europeanSocket(PowerSocket):
    def __init__ (self):
        super().__init__( 2, "ROUND", 220)   
class taiwaneseSocket(PowerSocket):
    def __init__ (self):
        super().__init__( 2, "FLAT", 110)  
class martianSocket(PowerSocket):
    def __init__ (self):
        super().__init__( 2, "FLAT", 300)
class chinise3pinPlug():
    def __init__ (self):
        self.pins = 3
        self.volt = 220
        self.pinshape = "FLAT"    

class RedmiLaptop():
    def __init__ (self):
        self.plug = chinise3pinPlug()
        self.__adapter = None

    def addAdapter(self, adpt):
        self.__adapter = adpt

    def charge(self, inSocket, powerInWatt):
        res = False   
        if (isinstance(inSocket, PowerSocket)) :
            if self.__adapter.convert(inSocket):
                socket = self.__adapter.getSocket()
                res = (self.plug.pins == socket.getHoleNum() )  and \
                (self.plug.pinshape == socket.getHoleShape() ) and  \
                (self.plug.volt == socket.getVolt() )
            else:
                res = False 
        else:
            print ("Неизвестная розетка")

        if res:
            current = round(powerInWatt / self.plug.volt, 2) * self.__adapter.getVoltRatio()
            print("Зарядка... Напряжение: {} Вт; Текущий зарядник: {} время ...".format(str(powerInWatt), str(current)))
        else:
            print("Розетка и вилка несовместимы, зарядить их невозможно.")
        return res
class SocketAdapter():
    """
       SocketAdapter base class 
    """
    def __init__ (self ):
        pass

    def convert(self ):
        pass

    def getSocket (self):
        pass


class AnyToChineseAdapter(SocketAdapter):
    """
       A concrete SocketAdapter class that can convert any socket to chinese socket
    """

    def __init__ (self):
        super().__init__()
        self.__outSocket = chineseSocket()
        self.__voltRatio = 1
        self.__plug = ""

    def convert(self, fromSocket):
        res = True
        if  isinstance (fromSocket,  chineseSocket):
            self.__voltRatio = 1
            self.__plug = "Китайский формат вилки"
            print("Китайский в китайский с помощью {}".format(self.__plug))
        elif isinstance (fromSocket,  europeanSocket):
            self.__voltRatio = 1
            self.__plug = "Европейский формат вилки"
            print("European to Chinese using {}".format(self.__plug))
        elif isinstance (fromSocket,  taiwaneseSocket):
            self.__voltRatio = 2
            self.__plug = "Тайваньский формат вилки"
            print("Тайванский в китайский переходник {}".format(self.__plug))
        # elif     isinstance (fromSocket,  someSocket):
        #    do converting stuff...
        else:        
            print("Неизвестная розетка, невозможно выбрать формат вилки и коэффициент преобразования напряжения")
            res = False
        return res

    def getSocket(self):
        return self.__outSocket

    def getVoltRatio(self):
        return self.__voltRatio
if __name__ == "__main__":

    redmiAd = AnyToChineseAdapter()
    laptop = RedmiLaptop()
    laptop.addAdapter(redmiAd)


    # I am in china mainland
    chSocket = chineseSocket()
    laptop.charge(chSocket, powerInWatt=235)

    # I am in France
    euSocket = europeanSocket()
    laptop.charge(euSocket, powerInWatt=235)

    # I am in Taipei 
    twSocket = taiwaneseSocket() 
    laptop.charge(twSocket, powerInWatt=235)

    # I am on Mars
    msSocket = martianSocket()
    laptop.charge(msSocket, powerInWatt=235) 