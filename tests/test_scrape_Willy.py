# -*- coding: utf-8 -*-
import pytest
import requests


#################################
#
# 假設這位客戶, name是 Test User, account為100-1100
# 一開始帳戶會先存100元, 要測試下面項目: 
#
# Test Case1. 之後存款 1000 元, 確認帳戶總金額為 1100 元
# Test Case2. 下一步提款 500 元, 確認帳戶總金額為 600 元
# Test Case3. 假設銀行年利率是10%, 經過一年之後確認帳戶餘額為660元
# Test Case4. 之後提款 700 元, pytest 預期會接到 RuntimeError
#
#################################


# Test Case1
def test_customer_deposit(self):
    self.customer.deposit(1000)
    assert self.customer.balance == 1100
        
# Test Case2
def test_customer_withdraw_1st(self):
    self.customer.withdraw(500)
    assert self.customer.balance == 600






