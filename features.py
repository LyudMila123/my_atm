from exceptions import *


class Atm(object):
    __atm_balance = 10000
    __attempts = 2
    __client_can_get_money = False

    def rise_money(self, rise_money):
        """Method to add some money to the ATM"""
        return self.__atm_balance + rise_money

    def get_money(self, money):
        """Method to get some money for sweets from the ATM"""
        if self.__client_can_get_money:
            if money <= self.__atm_balance:
                self.__atm_balance = self.__atm_balance - money
                return money
            else:
                raise AtmBalance("Atm balance is no enough!!!")
       
    def check_balance(self):
        """Method to check ATM balance"""
        if self.__client_can_get_money:
            return self.__atm_balance
