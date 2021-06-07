"""Klasa Coin służąca do przechowywania obiektu monety"""

class Coin:
    def __init__(self, v, c):
        if v in {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5}:
            self.__value = v
        else:
            self.__value = 0

        if c in {'PLN'}:
            self.__currency = c
        else:
            self.__currency = 'PLN'
            print("Nieznana waluta. Przypisano PLN")

    # gettry
    @property
    def value(self):
        return (self.__value)

    @property
    def currency(self):
        return (self.__currency)

    # settery
    @value.setter
    def value(self, v):
        self.__value = v

    @currency.setter
    def currency(self, c):
        self.__currency = c

"""Klasa MoneyKeeper odpowiedzialna za przechowywanie obiektów klasy Coin"""

class MoneyKeeper:
    def __init__(self):
        self.__moneyList = []
        self.__moneySum = 0

    # dodawanie monet do listy
    def add_money(self, m):
        if isinstance(m, Coin):
            if m.currency == 'PLN':
                self.__moneyList.append(m)
                self.__moneySum+=m.value
            else:
                print("Nieznana moneta")
        else:
            print("Przesłany obiekt nie jest monetą")


    # gettery
    @property
    def moneySum(self):
        return self.__moneySum

    @moneySum.setter
    def moneySum(self, value: float):
        self.__moneySum = value

    def getMoneySum(self):
        return self.__moneySum

    @property
    def moneyList(self):
        return self.__moneyList

    def getMoney(self):
        moneyList = []
        for el in self.__moneyList:
            moneyList.append([el.value, el.currency])
        return moneyList

    # usuwanie monety
    def popMoney(self, m):
        if isinstance(m, Coin):
            for el in self.__moneyList:
                if el.value == m.value:
                    self.__moneyList.remove(el)
                    return True

        else:
            return False
    # uzupełnienie listy monetami
    def fillWithMoney(self):
        pass








