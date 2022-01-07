# Cathay_SQA_Python
 
## Problem 1's Test Cases
<br>
假設這位客戶customer：name是"Test User"、account為"100-1100"
<br>
一開始帳戶會先存100元，要測試下面項目：
<br>
1. Test Case1. 之後存款 1000 元, 確認帳戶總金額為 1100 元
2. 
3. Test Case2. 下一步提款 500 元, 確認帳戶總金額為 600 元
4. 
5. Test Case3. 假設銀行年利率是10%, 經過一年之後確認帳戶餘額為660元
6. 
7. Test Case4. 之後提款 700 元, pytest 預期會接到 RuntimeError

## Problem 2's Test Cases
<br>
1. Test Case1：使用 Python 抓取 https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/user_info?userid=A123456789, 並利用 assert 確認 http response status code 為 200
2. 
3. Test Case2：使用 Python 抓取 https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/company_info?companyid=1, 並利用 assert 確認 http response status code 為 403

## Run Pytest
```Python
cd /d D:
cd D:\GitHub\Cathay_SQA_Python
pytest -W ignore::DeprecationWarning -v
```
