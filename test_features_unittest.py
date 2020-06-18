import unittest

from features import *

class TestFeatures(unittest.TestCase):

    def setUp(self):
        self.my_features = Atm()
        self.atm_balance = 10000
        self.attempts = 2
        self.correct_pin = 777

    def test_rise_money(self):
        self.assertTrue(self.my_features.rise_money(1000))

    def test_rise_money_fact_equal(self):
        self.my_features.rise_money(500)
        self.assertEqual(self.my_features.rise_money(500), self.atm_balance+500)

    def test_rise_money_fact_not_equal(self):
        self.my_features.rise_money(500)
        self.assertNotEqual(self.atm_balance, self.my_features.rise_money(500))

    def test_rise_money_sequentially(self):
        self.my_features.rise_money(500)
        self.my_features.rise_money(300)
        self.assertEqual(self.my_features.rise_money(800), self.atm_balance+800)

    def test_rise_money_add_null(self):
        self.my_features.rise_money(0)
        self.assertEqual(self.atm_balance, self.my_features.rise_money(0))

    def test_get_money(self):
        self.assertTrue(self.my_features.get_money(500))

    def test_get_money_equal(self):
        my_money = 300
        self.my_features.get_money(my_money)
        self.atm_balance_after_get = self.atm_balance - my_money
        self.assertEqual(self.atm_balance_after_get, self.atm_balance - my_money)
        if my_money <= self.atm_balance:
            self.assertEqual(self.my_features.get_money(my_money), my_money)
        else:
            self.assertRaises(AtmBalance)

    def test_get_money_sequentially(self):
        money_one = 500
        money_two = 100
        money_sequentially = money_one + money_two
        self.my_features.get_money(money_sequentially)
        # self.atm_balance_one = self.atm_balance - money_one
        # self.atm_balance_two = self.atm_balance_one - money_two
        self.assertEqual(self.my_features.get_money(money_sequentially), money_sequentially)

    def test_get_money_more_balance(self):
        more_money = 1000000
        self.assertTrue(self.my_features.get_money(more_money))

    def test_get_money_raise_atm_balance(self):
        money = 100000
        # self.atm_balance_after_get = self.atm_balance - money
        # self.my_features.get_money(money)
        if money != self.atm_balance or money > self.atm_balance:
            self.assertRaises(AtmBalance)

    def test_check_balance_true(self):
        money = 500
        self.my_features.get_money(money)
        self.assertTrue(self.my_features.check_balance(money))

    def test_check_balance_false(self):


    # def test_if_incorrect_pin_raise_enter_pin(self):
    #     self.my_features.enter_pin(self.correct_pin)
    #     if self.correct_pin != self.correct_pin:
    #         self.assertRaises(EnterPin)

        # if self.my_features.check_balance(self.correct_pin) != self.correct_pin:

    # def test_check_balance_raise(self):
    #     self.my_features.enter_pin(self.correct_pin)
    #     # self.atm_balance >= self.my_features.get_money(self.atm_balance)
    #     with self.assertRaises(EnterPin):
    #         self.my_features.get_money(self.atm_balance)
    # my_test_rise_money = self.my_features.rise_money(1000)

 # def test_enter_pin_correct_true(self):
    #     self.assertTrue(self.my_features.enter_pin(self.correct_pin))
    #
    # def test_enter_pin(self):
    #     self.my_features.enter_pin(self.correct_pin)
    #     if self.attempts == 0:
    #         self.assertRaises(AttemptsOver)

        # self.attempts = self.attempts - 2
        # with self.assertRaises(AttemptsOver):
        #     self.my_features.enter_pin(self.correct_pin)
        #     if self.assertTrue(self.my_features.enter_pin(777), self.correct_pin):
        #         self.attempts == 0
        # self.my_features.enter_pin(self.correct_pin)
        # self.my_features.enter_pin(self.correct_pin)
        # self.assertTrue(self.my_features.enter_pin(self.correct_pin))

    # def test_enter_pin_raises_incorrect_pin(self):
    #     self.my_features.enter_pin(self.correct_pin)
    #     self.attempts = self.attempts - 1
    #     with self.assertRaises(IncorrectPin):
    #         self.my_features.enter_pin(888)
    #
    # def test_enter_pin_correct_equal(self):
    #     my_pin_correct = self.my_features.enter_pin(self.correct_pin)
    #     self.assertEqual(my_pin_correct, True)
    #
    # def test_enter_pin_incorrect(self):
    #     self.my_features.enter_pin(self.correct_pin)
    #     self.assertNotEqual(999, self.correct_pin)
    #
    # def test_my_enter_pin_correct_not_equal(self):
    #     self.assertNotEqual(self.my_features.enter_pin(self.correct_pin), IncorrectPin)

    # def test_my_enter_pin_correct_not_equal_null(self):
    #     self.assertNotEqual(self.my_features.enter_pin(self.correct_pin), AttemptsOver)
# def test_get_money_raise(self):
    #     self.my_features.enter_pin(self.correct_pin)
    #     self.atm_balance >= self.my_features.get_money(self.atm_balance)
    #     with self.assertRaises(AtmBalance):
    #         self.my_features.get_money(self.atm_balance)
