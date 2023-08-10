class Araba:
    def __init__(self, marka, model,renk):
        self.__marka=marka # __(iki alt tire varrsa bu private olduğu anlamına gelir)
        self.__model=model # herheangi bir yerden buna ulasilmaz taa ki getter ve setter propertyleri yapılıncaya kadar)
        self.renk=renk
    
    def __str__(self):
        return f"Arabanizin ozellikleri : {self.marka} {self.model} {self.renk}"
    
    @property
    def marka(self):
        return self.__marka
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,value):
        self.__model=value
    @marka.setter
    def marka(self,value):
        self.__marka=value
   

if __name__=='__main__':
    araba = Araba(marka="mercedes",model=2002,renk="siyah")
    print(araba)
    araba.marka="bmw"
    araba.renk="beyaz"
    araba.model="2004"
    print(araba)
