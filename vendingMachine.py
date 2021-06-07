import decimal
from itertools import combinations_with_replacement
import beverage
import money
import random

"""Klasa VendingMachine odpowiedzialna za działanie automatu z napojami, dziedzicząca po klasie money.MoneyKeeper"""

class VendingMachine(money.MoneyKeeper):
    def __init__(self):
        money.MoneyKeeper.__init__(self)
        self.__currentBeverageList = []
        # self.createbeverageList()
        self.__currentSum = 0


    @property
    def currentSum(self):
        return self.__currentSum

    @property
    def currentBeverageList(self):
        return self.__currentBeverageList

    @currentSum.setter
    def currentSum(self, value: float):
        self.__currentSum = value

    # dodanie towaru - beverageKeeper do maszyny
    def addBeverageKeeper(self, bk):
        self.__currentBeverageList.append(bk)

    #utworzenie listy obiektów napojów o numerach z zakresu: <30,50> po 5 dla każdego rodzaju
    def createbeverageList(self, n0, nk):
        for i in range(n0, nk):
            itemName = "Item"+ str(i)
            randomPrice = decimal.Decimal(random.randrange(10, 1000))/100
            randomPrice = round(float(randomPrice), 2)
            beverageKeeper = beverage.BeverageKeeper(i)
            for j in range(0,5):
                b = beverage.Beverage(itemName, randomPrice)
                beverageKeeper.addItem(b)
            self.__currentBeverageList.append(beverageKeeper)

    # sprawdzanie czy dany element jest dostępny w automacie (liście)
    def isAvailable(self, number):
        for el in self.currentBeverageList:
            if el.itemNumber == number:

                if el.numberOfItems >0:

                    return True
                else:
                    print('f')
                    return False

    # usuwanie napoju z automatu po zakończonym sukcesem procesie kupna
    def removeBeverage(self, number):
        napoj = ""
        isAva = self.isAvailable(number)
        if isAva == True:
            for el in self.currentBeverageList:
                if el.itemNumber == number:
                    print(el.itemNumber)
                    length = el.numberOfItems
                    el.removeItem(length-1)
                    return True
        else:
            return "Brak towaru"

    # sprawdzanie czy numer produktu został podany z zakresu <30,50>
    def isNumberOK(self, numer):
        if numer in range(30, 51):
            return True
        else:
            return False

    # uzupełenie listy monet w automacie monetami o losowych nominałach
    def fillWithMoney(self, n):
        listOfCoins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]

        for i in range(0, n):
            randomCoinNr = random.randint(0, 8)
            randomCoin = listOfCoins[randomCoinNr]

            b = money.Coin(randomCoin, 'PLN')
            self.add_money(b)

    # metoda zwracająca cenę danego produktu
    def getPriceOfItem(self, number):
        if self.isNumberOK(number):
            # print("Numer: ", number)
            for el in self.currentBeverageList:
               if el.itemNumber == number:
                   if el.beverageList[0]:
                       itemPrice = el.beverageList[0].price
                       return itemPrice
                   else:
                       return False
        else:
            return False

    # metoda dodająca elementy do pól klasy
    def filledMoney(self, number):
        m = money.Coin(number, 'PLN')
        self.add_money(m)
        self.__currentSum +=number


    def isEnoughSum(self, itemPrice):
        if self.__currentSum >= itemPrice:
            return True
        else:
            return False

    def removeCurrentMoney(self):
        self.__currentSum =0

    # metoda zwracająca kwotę reszty, która należy się klientowi
    def getCharge(self, itemNumber):
        price = self.getPriceOfItem(itemNumber)
        try:
            # print(type(price))
            itemPrice = round(price, 2)
        except TypeError:
            return "Blad danych"
        if self.__currentSum==itemPrice:
            return 0
        if self.__currentSum>itemPrice:
            return round(self.__currentSum-float(itemPrice), 2)

    # metoda realizująca obsługę wydania reszty - sprawdza, czy jest możliwość
    def makeCharge(self, charge):
        try:
            if charge > self.moneySum:
                return False
            else:
                numbers = []
                for el in self.moneyList:
                    numbers.append(round(el.value, 2))
                chargeList = self.getCombination(numbers, charge)
                if chargeList == []:
                    return False
                else:
                    self.returnCharge(chargeList)
                    return True
            return False
        except TypeError:
            return 0


    # metoda zwracajaca reszte klientowi; usuwa zwrócone monety z listy monet w automacie
    def returnCharge(self, chargeList):
        for coin in chargeList:
            for elMoneyList in self.moneyList:
                if coin == elMoneyList.value:
                    self.moneyList.remove(elMoneyList)
                    self.moneySum - coin

    # metoda obsługująca sprzedaż napoju
    def sellBeverage(self, number):
        try:
            charge = self.getCharge(number)
            # print(charge)
            if charge== 0:
                self.removeBeverage(number)
                moneySum = self.getMoneySum()
                moneySum += self.currentSum
                self.currentSum =0.0
                return True
            else:
                makeCharge = self.makeCharge(charge)
                if makeCharge == True:
                    self.removeBeverage(number)
                    # print(self.moneySum)
                    self.moneySum += self.currentSum
                    # print(self.moneySum)
                    self.currentSum = 0.0
                    # print(self.currentSum)
                    return True

                if makeCharge == False:
                    self.currentSum =0
                    return False
        except TypeError:
            return 0

    # metoda obsługująca uzyskanie odpowiedniej kombinacji nominałów monet potrzebnych do wydania reszty
    def getCombination(self, numbers, price):
        coins = [0.01, 0.02, 0.03, 0.1, 0.2, 0.5, 1, 2, 5]
        comb = list(combinations_with_replacement(coins, len(coins)))
        coinLst = []
        for i in range(0, len(comb)):
            coinLst = self.sublist(comb[i], numbers)
            if float(sum(coinLst)) == float(price):
                return coinLst
        return coinLst

    # sprawdzanie czy dana kombinacja zawiera sie w liście dostępnych moent
    def sublist(self, lst1, lst2):
        flag = 0
        if (all(x in lst2 for x in lst1)):
            flag = 1
        if (flag):
            return lst1
        else:
            return []










