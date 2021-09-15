class CellClass:

    # attributes that are inside of this method
    def __init__(self):
        self.__manufact = 0
        self.__model = ''
        self.__retail_price = 0 


    def set_manufact(self,man):
        self.__manufact = man

    def set_model(self, model):
        self.__model = model

    def get_retail_price(self,rp):
        self.__retail_price = rp

    def get_manufact(self,man):
        return self.__manufact

    def get_model(self, model):
        return self.__model
        
    def get_retail_price(self,rp):
        return self.__retail_price

        