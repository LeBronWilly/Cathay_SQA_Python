# -*- coding: utf-8 -*-
import pytest
import requests
from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY=100.0

customer = Customer("Test User","account")


class TestCoreSuites(Customer):
#################################
#
# 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目: 
#
# 1. 之後存款 1000 元, 確認帳戶總金額為 1100 元
# 2. 下一步提款 500 元, 確認帳戶總金額為 600 元
# 3. 假設銀行年利率是10%, 經過一年之後確認帳戶餘額為660元
# 4. 之後提款 700 元, pytest 預期會接到 RuntimeError
#
#################################


    # @pytest.fixture(autouse=True)
    # def test_setup(self, name, account,INIT_MONEY):
    #     self.name = "Test User"
    #     self.account = "100-1100"
    #     self.INIT_MONEY = INIT_MONEY

    # Test Case
    def test_customer_account(self):
        # self.name = "Test User"
        # self.account = "100-1100"
        # self.INIT_MONEY = INIT_MONEY
        assert self.balance+1000 == 1100






