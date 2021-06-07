from tkinter import *
from vendingMachine import *
from money import *

"""Klasa MachineInterface odpowiedzialna za interfejs automatu z napojami z wykorzystaniem biblioteki tkinter"""
class MachineInterface():

    def __init__(self, vm: VendingMachine):
        self.action = 0
        self.price_temp = 0
        self.vm = vm
        self.root = Tk()

        self.root.title("Automat z napojami")
        # suma monet wrzuconych
        self.coinSum = 0
        # lista obiektów wrzuconych monet
        self.coinList = []

        # wyświetlacz główny
        self.textDisplay = Text(self.root, height=1, width=50, bd=3, font="Calibri")
        self.textDisplay.grid(row=0, column=1, columnspan=4)
        self.textDisplay.insert(END, "Wybierz numer napoju")

        # okno wprowadzanych danych
        self.entryTextBox = Entry(self.root, width=20, borderwidth=3)
        self.entryTextBox.grid(row=1, column=0, columnspan=6, padx=20, pady=10)

        # wyświetlacz akcji
        self.actionDisplay = Text(self.root, height=1, width=30, bd=3, font="Calibri")
        self.actionDisplay.grid(row=2, column=1, columnspan=4)

        # zdefiniowanie przycisków
        # przyciski cyfr
        # wykorzystanie wyrażeń lambda
        self.button_1 = Button(self.root, text="1", padx=30, pady=20, command=lambda: self.clickNumberButton("1"))
        self.button_2 = Button(self.root, text="2", padx=30, pady=20, command=lambda: self.clickNumberButton("2"))
        self.button_3 = Button(self.root, text="3", padx=30, pady=20, command=lambda: self.clickNumberButton("3"))
        self.button_4 = Button(self.root, text="4", padx=30, pady=20, command=lambda: self.clickNumberButton("4"))
        self.button_5 = Button(self.root, text="5", padx=30, pady=20, command=lambda: self.clickNumberButton("5"))
        self.button_6 = Button(self.root, text="6", padx=30, pady=20, command=lambda: self.clickNumberButton("6"))
        self.button_7 = Button(self.root, text="7", padx=30, pady=20, command=lambda: self.clickNumberButton("7"))
        self.button_8 = Button(self.root, text="8", padx=30, pady=20, command=lambda: self.clickNumberButton("8"))
        self.button_9 = Button(self.root, text="9", padx=30, pady=20, command=lambda: self.clickNumberButton("9"))
        self.button_0 = Button(self.root, text="0", padx=30, pady=20, command=lambda: self.clickNumberButton("0"))
        # przyciski akcji
        self.button_enter = Button(self.root, text="ENTER", padx=75, pady=20, command=self.clickEnterButton, bg='#66ccff')
        self.button_clear = Button(self.root, text="CLEAR", padx=62, pady=20, command=self.clickClearButton,  bg='#996699')
        self.button_stop = Button(self.root, text="STOP", padx=28, pady=20, command=lambda: self.clickStopButton("Wpisz numer napoju"),  bg='#996699')
        # przyciski monet
        # wykorzystanie wyrażeń lambda
        self.button_coin_001 = Button(self.root, text="0.01zł", padx=27, pady=20, command=lambda: self.dropCoin("0.01"))
        self.button_coin_002 = Button(self.root, text="0.02zł", padx=27, pady=20, command=lambda: self.dropCoin("0.02"))
        self.button_coin_005 = Button(self.root, text="0.05zł", padx=27, pady=20, command=lambda: self.dropCoin("0.05"))
        self.button_coin_010 = Button(self.root, text="0.1zł", padx=30, pady=20, command=lambda: self.dropCoin("0.1"))
        self.button_coin_020 = Button(self.root, text="0.2zł", padx=30, pady=20, command=lambda: self.dropCoin("0.2"))
        self.button_coin_050 = Button(self.root, text="0.5zł", padx=30, pady=20, command=lambda: self.dropCoin("0.5"))
        self.button_coin_100 = Button(self.root, text="1.0zł", padx=30, pady=20, command=lambda: self.dropCoin("1.0"))
        self.button_coin_200 = Button(self.root, text="2.0zł", padx=30, pady=20, command=lambda: self.dropCoin("2.0"))
        self.button_coin_500 = Button(self.root, text="5.0zł", padx=30, pady=20, command=lambda: self.dropCoin("5.0"))

        # ustawinie przycisków
        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)
        self.button_4.grid(row=4, column=0)
        self.button_5.grid(row=4, column=1)
        self.button_6.grid(row=4, column=2)
        self.button_7.grid(row=5, column=0)
        self.button_8.grid(row=5, column=1)
        self.button_9.grid(row=5, column=2)
        self.button_0.grid(row=6, column=0)
        self.button_enter.grid(row=6, column=4, columnspan=2)
        self.button_clear.grid(row=6, column=1, columnspan=2)
        self.button_stop.grid(row=6, column=3, columnspan=1)
        self.button_coin_001.grid(row=3, column=3)
        self.button_coin_002.grid(row=3, column=4)
        self.button_coin_005.grid(row=3, column=5)
        self.button_coin_010.grid(row=4, column=3)
        self.button_coin_020.grid(row=4, column=4)
        self.button_coin_050.grid(row=4, column=5)
        self.button_coin_100.grid(row=5, column=3)
        self.button_coin_200.grid(row=5, column=4)
        self.button_coin_500.grid(row=5, column=5)

        self.root.mainloop()

    # wyświetlenie wyświetlacza akcji
    def displayActionText(self, info: str):
        self.actionDisplay.delete("1.0", END)
        self.actionDisplay.insert(END, info)

    # wyświetlenie wyświetlacza głównego
    def displayText(self, info: str):
        self.textDisplay.delete("1.0", END)
        self.textDisplay.insert(END, info)

    # funckja odpowiedzialna za obsługę przycisku STOP
    # powoduje zakończenie obecnej transakcji oraz zwrot kwoty do klienta
    def clickStopButton(self, info):
        self.itemNumber =""
        self.coinSum = 0
        self.coinList =[]
        self.vm.removeCurrentMoney()
        self.entryTextBox.delete(0, END)
        self.displayText(info)
        self.actionDisplay.delete("1.0", END)
        self.action = 0;

    # metoda odpowiedzialna za obsługę przycisku CLEAR
    # czyści okno wprowadzania; użytkownik ma możliwość ponownego wpisania wybranego numeru
    def clickClearButton(self):
        self.entryTextBox.delete(0, END)
        self.itemNumber =""

    # metoda obsługująca przycisk ENTER
    # pozwala na zatwierdzenie wybrania konkretnego numeru produktu
    def clickEnterButton(self):
        try:
            isNumberCorrect = self.vm.isNumberOK(self.itemNumber)
            self.action = 1;
            if isNumberCorrect == False:
                info = "Niepoprawny numer: " + str(self.itemNumber) + ". Spróbuj jeszcze raz"
                # self.displayText(info)
                # self.entryTextBox.delete(0, END)
                # self.actionDisplay.delete("1.0", END)
                self.clickStopButton(info)
            else:
                # sprawdzenie dostępności towaru
                if self.vm.isAvailable(self.itemNumber) == True:
                    self.price_temp = round(self.vm.getPriceOfItem(self.itemNumber), 2)
                    info = "Cena: " + str(self.price_temp)
                    self.displayText(info)
                    self.actionDisplay.delete("1.0", END)

                else:
                    self.clickStopButton("Wpisz numer napoju")
                    self.entryTextBox.delete(0, END)
                    self.actionDisplay.delete("1.0", END)
                    self.displayActionText("Brak towaru")
        except TypeError or ValueError:
            self.clickStopButton("Na początku wpisz numer napoju!")

    # metoda obsługująca przyciski wprowadzania cyfr
    def clickNumberButton(self, number):
        current = self.entryTextBox.get()
        self.entryTextBox.delete(0, END)
        self.entryTextBox.insert(0, str(current) + str(number))

        itemNumber = current + str(number)
        try:
            self.itemNumber = int(itemNumber)
        except ValueError:
            self.clickStopButton("Na początku wpisz numer napoju!")
        except GetStopActionException:
            GetStopActionException("Wpisz prawidłowy numer produktu z przedziału <30;50>", self)



    # wrzucanie monet
    # metoda wywowaływana po kliknięciu przycisku z monetami
    def dropCoin(self, coin):
        try:
            if self.action == 0:
                raise GetStopActionException("Wpisz prawidłowy numer produktu!", self)
            self.entryTextBox.delete(0, END)
            self.entryTextBox.insert(0, str(coin))
            self.coinSum = self.coinSum + float(coin)
            self.coinList.append(Coin(float(coin), 'PLN'))

            coinSumRound = round(float(self.coinSum), 2)
            priceTempRound = round(float(self.price_temp),2)
            charge = round(coinSumRound-priceTempRound,2)

            label = "Wrzucono: " + str(coinSumRound)
            self.displayActionText(label)
            print(self.coinSum)
            print(self.price_temp)

            # sprawdzanie dokładności wprowadzonych monet z ceną produktu
            # wyrażanie lambda
            f_equal = lambda a,b: abs(a - b) <= epsilon

            # sprawdzanie czy suma wprowadzonych monet jest większa bądź równa cenie produktu
            if coinSumRound > priceTempRound or f_equal(coinSumRound, priceTempRound):
                self.vm.currentSum = self.coinSum
                selling = self.vm.sellBeverage(self.itemNumber)
                if selling == 0:
                    raise GetStopActionException("Wpisz najpierw numer napoju", self)
                if selling == False:
                    info = "Tylko odliczona kwota"
                    self.displayActionText(info)
                    self.clickStopButton("Wpisz numer napoju")
                else:
                    info = "Wydanie towaru. Reszta: "+str(charge)
                    for el in self.coinList:
                        self.vm.moneyList.append(el)
                    self.vm.currentSum+=self.coinSum
                    self.displayActionText(info)
                    self.itemNumber = ""
                    self.coinSum = 0
                    self.coinList = []
                    self.entryTextBox.delete(0, END)
                    self.displayText("Wybierz numer napoju")
                    self.action=0

        except AttributeError or TypeError or ValueError:
            self.clickStopButton("Na początku wpisz numer napoju!")
        except GetStopActionException:
            GetStopActionException("Wpisz najpierw numer napoju!", self)

class GetStopActionException(Exception):
    def __init__(self, info, vm):
        super().__init__()
        MachineInterface.clickStopButton(vm, info)
        # MachineInterface.displayText(vm, info)
        # MachineInterface.displayActionText(vm, " ")


epsilon = 0.001







