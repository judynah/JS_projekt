"""Klasa Beverage jako poszczególny napój"""

class Beverage:

    def __init__(self, n, p):
        self.__name = n
        self.__price = p


    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, n):
        self.__name = n

    @price.setter
    def price(self, p):
        self.__price = p


"""klasa BeverageKeeper odpowiedzialna jako przechowywacz obiektów napojów"""

class BeverageKeeper:
    def __init__(self, itemNr):
        self.__beverageList = []
        self.__numberOfItems = 0
        self.__itemNumber = itemNr

    @property
    def beverageList(self):
        return self.__beverageList

    @property
    def numberOfItems(self):
        return self.__numberOfItems

    @property
    def itemNumber(self):
        return self.__itemNumber

    @itemNumber.setter
    def itemNumber(self, number):
        self.__itemNumber = number



    # dodanie napoju do listy
    def addItem(self, b):
        self.__beverageList.append(b)
        self.__numberOfItems +=1

    # usunięcie napoju z listy
    def removeItem(self, number):
        self.__numberOfItems-=1
        del self.__beverageList[-1]





