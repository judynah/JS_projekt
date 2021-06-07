import unittest
from vendingMachine import *
from beverage import *
from money import *
from machineInterface import *

class MyTestCase(unittest.TestCase):

    # self.vm = VendingMachine()
    # self.m1 = Coin(1, 'PLN')
    #     self.m3 = Coin(1, 'PLN')
    #     self.m2 = Coin(2, 'PLN')
    #
    #     self.p1 = MoneyKeeper()
    #     #
    #     self.b1 = Beverage('Cola', 3.5)
    #     self.bk = BeverageKeeper()
    #     self.bk.addItem(self.b1)
    #     self.bk.itemNumber = 30
    #     self.vm.fillWithMoney(30)


    def test_checkPrice(self):
        # given
        vm = VendingMachine()
        b1 = Beverage('Cola', 2.5)
        bk = BeverageKeeper(30)
        bk.addItem(b1)
        vm.addBeverageKeeper(bk)

        priceOfAnItem = b1.price
        # when
        getPrice = vm.getPriceOfItem(30)
        # then
        assert getPrice == 2.5

    def test_accurateAmountNoCharge(self):
        # given
        vm = VendingMachine()
        b1 = Beverage('Cola', 2.5)
        bk = BeverageKeeper(30)
        bk.addItem(b1)
        vm.addBeverageKeeper(bk)
        vm.currentSum = 2.5

        # when
        charge =vm.getCharge(30)

        # then
        assert charge == 0


    def test_BiggerAmoutGivenCharge(self):
        # given
        vm = VendingMachine()
        b1 = Beverage('Cola', 2.5)
        bk = BeverageKeeper(30)
        bk.addItem(b1)
        vm.addBeverageKeeper(bk)
        vm.currentSum = 4

        # when
        charge = vm.getCharge(30)

        # then
        assert charge == 1.5

    def test_BuyWhenNothingInStore(self):
        vm = VendingMachine()
        b1 = Beverage('Cola', 2.5)
        bk = BeverageKeeper(30)
        bk.addItem(b1)
        vm.addBeverageKeeper(bk)
        vm.currentSum = 2.5

        # when
        isAvailableOne = vm.isAvailable(30)
        if isAvailableOne == True:
            vm.sellBeverage(30)

        isAvailableTwo = vm.isAvailable(30)

        # then
        assert isAvailableTwo == False

    def test_checkItemPriceWithWrongNumber(self):
        # given
        vm = VendingMachine()

        # when
        getPrice = vm.getPriceOfItem(60)

        # then
        assert not getPrice

    def test_GetMoneyBackWhileStop(self):
        # given
        vm = VendingMachine()
        vm.currentSum = 3.0

        # when
        vm.removeCurrentMoney()
        coinSum = vm.currentSum

        # then
        assert coinSum == 0.0

    def test_tooSmallAmoutOfMoney(self):
        vm = VendingMachine()
        b1 = Beverage('Cola', 2.5)
        bk = BeverageKeeper(30)
        bk.addItem(b1)
        vm.addBeverageKeeper(bk)
        vm.currentSum = 1.5
        action = vm.isNumberOK(30)
        vm.currentSum+=1

        # when
        charge = vm.getCharge(30)

        # then
        assert charge == 0

    def test_BuyPayWith001g(self):
        # given
        vm = VendingMachine()
        b1 = Beverage('Cola', 2.5)
        bk = BeverageKeeper(30)
        bk.addItem(b1)
        vm.addBeverageKeeper(bk)
        iter = 2.5/0.01
        moneySum = 0
        # when
        for i in range(int(iter)):
            moneySum+=0.01
        vm.currentSum = moneySum
        selling = vm.sellBeverage(30)

        # then
        assert selling == False

if __name__ == '__main__':
    unittest.main()

