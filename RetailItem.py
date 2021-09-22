class RetailItem:

    def __init__(self, description, units, price):
        self.__description = description
        self.__units_in_inventory = units 
        self.__price = price

    def set__description(self, description):
        self.__description = description

    def set_unitsininventory(self, units):
        self.__units_in_inventory = units 

    def set_price(self, price):
        self.__price = price

# return type
    def get_description(self):
        return self.__description
# return number of items
    def get_unitsininventory(self):
        return self.__units_in_inventory
#return cost

    def get_price(self):
        return self.__price

