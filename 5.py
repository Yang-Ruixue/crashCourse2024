class LogicGate:

    def __init__(self, n):
       self.label = n
       self.output = None

    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n):
        super().__init__(n)

        self.pinA=None
        self.pinB=None
    
    def getPinA(self):
        return int(input("Enter Pin A input for gate"+\
                         self.getLabel()+"-->"))
    
    def getPinB(self):
        return int(input("Enter Pin B input for gate"+\
                         self.getLabel()+"-->"))
    
class UnaryGate(LogicGate):

    def __init__(self,n):
        super().__init__(n)

        self.pin=None
    
    def getPin(self):
        return int(input("Enter Pin input for gate"+\
                         self.getLabel()+"-->"))

class AndGate(BinaryGate):

    def __init__(self,n):
        super().__init__(n)
    
    def performGateLogic(self):

        a=self.getPinA()
        b=self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    
    def performGateLogic(self):

        a=self.getPinA()
        b=self.getPinB()
        if a==0 and b==0:
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self,n):
        super().__init__(n)
    
    def performGateLogic(self):

        a=self.getPin()
        if a==1:
            return 0
        else:
            return 1
        
g1=AndGate("G1")
h1=g1.getOutput()

g2=OrGate("G2")
h2=g2.getOutput()

g3=NotGate("G3")
h3=g3.getOutput()

print(h1,h2,h3)
