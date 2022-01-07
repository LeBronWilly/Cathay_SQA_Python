# -*- coding: utf-8 -*-
import pytest
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}

#################################
# Test Case1. 請嘗試使用 Python 抓取 https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/user_info?userid=A123456789, 並利用 assert 確認 http response status code 為 200

# Test Case2. 請嘗試使用 Python 抓取 https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/company_info?companyid=1, 並利用 assert 確認 http response status code 為 403
#################################

# Test Case1
def test_scrape_1():
    url = "https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/user_info?userid=A123456789"
    r = requests.get(url, headers=headers)
    assert r.status_code == 200


# Test Case2
def test_scrape_2():
    url = "https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/company_info?companyid=1"
    r = requests.get(url, headers=headers)
    assert r.status_code == 403



