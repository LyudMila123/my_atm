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
        self.my_features.enter_pin(self.correct_pin)
        self.my_features.rise_money(500)
        self.assertEqual(self.my_features.rise_money(500), self.atm_balance+500)

    def test_rise_money_fact_not_equal(self):
        self.my_features.enter_pin(self.correct_pin)
        self.my_features.rise_money(500)
        self.assertNotEqual(self.atm_balance, self.my_features.rise_money(500))

    def test_rise_money_sequentially(self):
        self.my_features.enter_pin(self.correct_pin)
        self.my_features.rise_money(500)
        self.my_features.rise_money(300)
        self.assertEqual(self.my_features.rise_money(800), self.atm_balance+800)

    def test_rise_money_add_null(self):
        self.my_features.enter_pin(self.correct_pin)
        self.my_features.rise_money(0)
        self.assertEqual(self.atm_balance, self.my_features.rise_money(0))

    def test_enter_pin_correct_true(self):
        self.assertTrue(self.my_features.enter_pin(self.correct_pin))

    # def test_enter_pin(self):
    #     self.my_features.enter_pin(self.correct_pin)
    #     self.attempts = self.attempts - 2
    #     with self.assertRaises(AttemptsOver):
    #         self.my_features.enter_pin(self.correct_pin)

    def test_enter_pin_raises_incorrect_pin(self):
        self.my_features.enter_pin(self.correct_pin)
        self.attempts = self.attempts - 1
        with self.assertRaises(IncorrectPin):
            self.my_features.enter_pin(888)

    def test_enter_pin_correct_equal(self):
        my_pin_correct = self.my_features.enter_pin(self.correct_pin)
        self.assertEqual(my_pin_correct, True)

    def test_enter_pin_incorrect(self):
        self.my_features.enter_pin(self.correct_pin)
        self.assertNotEqual(999, self.correct_pin)

    def test_my_enter_pin_correct_not_equal(self):
        self.assertNotEqual(self.my_features.enter_pin(self.correct_pin), IncorrectPin)

    def test_my_enter_pin_correct_not_equal_null(self):
        self.assertNotEqual(self.my_features.enter_pin(self.correct_pin), AttemptsOver)

    def test_get_money(self):
        self.my_features.enter_pin(self.correct_pin)
        self.assertTrue(self.my_features.get_money)

    def test_get_money_equal(self):
        self.my_features.enter_pin(self.correct_pin)
        self.assertEqual(self.my_features.get_money(9500), self.atm_balance - 500)

    def test_get_money_sequentially(self):
        self.my_features.enter_pin(self.correct_pin)
        self.atm_balance = self.atm_balance - 500
        self.atm_balance = self.atm_balance - 100
        self.assertEqual(self.my_features.get_money(9400), self.atm_balance)

    def test_get_money_raise(self):
        self.my_features.enter_pin(self.correct_pin)
        self.atm_balance >= self.my_features.get_money(self.atm_balance)
        with self.assertRaises(AtmBalance):
            self.my_features.get_money(self.atm_balance)

    def test_check_balance(self):
        self.my_features.enter_pin(self.correct_pin)
        self.assertTrue(self.my_features.check_balance)

    # def test_check_balance_raise(self):
    #     self.my_features.enter_pin(self.correct_pin)
    #     # self.atm_balance >= self.my_features.get_money(self.atm_balance)
    #     with self.assertRaises(EnterPin):
    #         self.my_features.get_money(self.atm_balance)





        # my_test_rise_money = self.my_features.rise_money(1000)

