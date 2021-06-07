import decimal

from money import  *
from beverage import *
from vendingMachine import *
from machineInterface import *

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # m1 = Coin(1, 'PLN')
    # m3 = Coin(1, 'PLN')
    # m2 = Coin(2, 'PLN')
    #
    # p1 = MoneyKeeper()
    #
    # b1 = Beverage('Cola', 3.5)
    # bk1 = BeverageKeeper()
    # bk1.addItem(b1)

    vm = VendingMachine()
    vm.createbeverageList(30, 50)
    vm.fillWithMoney(30)
    #
    # print(vm.currentBeverageList[0].itemNumber)
    # print(vm.currentBeverageList[1].itemNumber)
    # print(vm.currentBeverageList[-2].itemNumber)
    # print(vm.currentBeverageList[-1].itemNumber)
    # print(vm.currentBeverageList[0].beverageList[0].name)
    # print(vm.currentBeverageList[1].beverageList[0].name)
    # print(vm.currentBeverageList[-2].beverageList[0].name)
    # print(vm.currentBeverageList[-1].beverageList[0].name)
    #
    # vm.removeBeverage(30)
    # print(vm.currentBeverageList[0].beverageList)
    # vm.removeBeverage(30)
    # print(vm.currentBeverageList[0].beverageList)
    # vm.removeBeverage(30)
    # print(vm.currentBeverageList[0].beverageList)
    # vm.removeBeverage(30)
    # print(vm.currentBeverageList[0].beverageList)
    # vm.removeBeverage(30)
    # print(vm.currentBeverageList[0].beverageList)
    # # vm.removeBeverage(30)
    # # print(vm.currentBeverageList[0].beverageList)
    # # price = round(vm.getPriceOfItem(36), 2)
    # # print("Suma: ", vm.moneySum)
    # #
    # vm.sellBeverage(30)

    # vm.sellBeverage(36)
    # vm.sellBeverage(36)
    # vm.sellBeverage(36)
    # vm.sellBeverage(36)
    # vm.sellBeverage(36)

    # print(vm.moneySum)


    vmi = MachineInterface(vm)
    # vmi.createWindow()



















