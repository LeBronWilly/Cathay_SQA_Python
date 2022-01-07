# Cathay_SQA_Python
 
## Problem 1's Test Cases
假設這位客戶customer：name是"Test User"、account為"100-1100"，一開始帳戶會先存100元，要測試下面項目：
<br>
https://github.com/LeBronWilly/Cathay_SQA_Python/tree/main/tests/Problem%201
1. Test Case1：之後存款 1000 元, 確認帳戶總金額為 1100 元
2. Test Case2：下一步提款 500 元, 確認帳戶總金額為 600 元
3. Test Case3：假設銀行年利率是10%, 經過一年之後確認帳戶餘額為660元
4. Test Case4：之後提款 700 元, pytest 預期會接到 RuntimeError

## Problem 2's Test Cases
https://github.com/LeBronWilly/Cathay_SQA_Python/tree/main/tests/Problem%202
1. Test Case1：使用 Python 抓取 https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/user_info?userid=A123456789 ，並利用 assert 確認 http response status code 為 200
2. Test Case2：使用 Python 抓取 https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/company_info?companyid=1 ，並利用 assert 確認 http response status code 為 403

## Run Pytest
```Command Line Interface
cls
cd /d D:
cd D:\GitHub\Cathay_SQA_Python
pytest -W ignore::DeprecationWarning -v

```

## Some References
1. https://myapollo.com.tw/zh-tw/pytest/
2. https://blog.cti.app/archives/20220
3. https://zwindr.blogspot.com/2019/01/python-pytest.html
4. https://www.796t.com/article.php?id=164187
5. https://iter01.com/504335.html
6. https://docs.pytest.org/en/latest/how-to/fixtures.html
7. https://stackoverflow.com/questions/39395731/testing-class-methods-with-pytest/39395889
8. https://kirin.idv.tw/python-decimal-module-tutorial/
9. https://www.maxlist.xyz/2019/12/12/python-oop/
10. https://www.learncodewithmike.com/2020/01/python-inheritance.html
11. https://stackoverflow.com/questions/40710094/how-to-suppress-py-test-internal-deprecation-warnings
12. https://github.com/LeBronWilly/Basic_Web_Crawler/blob/master/Web%20Scraper.ipynb
13. https://stackoverflow.com/questions/55944961/python-403-access-denied-when-post-request
14. https://ithelp.ithome.com.tw/articles/10191165
15. https://www.learncodewithmike.com/2020/09/7-tips-to-avoid-getting-blocked-while-scraping.html
