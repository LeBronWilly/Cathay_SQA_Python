# Cathay_SQA_Python
 
##Test Cases
<br>
假設這位客戶customer：name是"Test User"、account為"100-1100"
<br>
一開始帳戶會先存100元，要測試下面項目：
1. Test Case1. 之後存款 1000 元, 確認帳戶總金額為 1100 元
2. Test Case2. 下一步提款 500 元, 確認帳戶總金額為 600 元
3. Test Case3. 假設銀行年利率是10%, 經過一年之後確認帳戶餘額為660元
4. Test Case4. 之後提款 700 元, pytest 預期會接到 RuntimeError


##避免Deprecation Warning
```Python
pytest -W ignore::DeprecationWarning
```


