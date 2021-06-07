import decimal

from money import  *
from beverage import *
from vendingMachine import *
from machineInterface import *


if __name__ == '__main__':

    vm = VendingMachine()
    vm.createbeverageList(30, 50)
    vm.fillWithMoney(100)
    vmi = MachineInterface(vm)




















