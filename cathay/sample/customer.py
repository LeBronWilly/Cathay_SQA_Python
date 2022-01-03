from decimal import Decimal

class Customer():
    """
    A class that represents a customer (python docs follows Numpy/Scipy format)
    ...
    Attributes
    ----------
    name: str
        customer name
    account: str
        customer's account
    balance: decimal.Decimal
        customer's balance
   
    Methods
    -------
    deposit(amount)
        a customer deposits money
    withdraw(amount)
        a customer withdraw money
    """
    #def __init__(self, name:str, account:str): # python 3
    def __init__(self, name, account): # python 2
        """
        Parameters
        ----------
        name: str
            customer name
        account: str
            customer's account
        balance: decimal.Decimal
            customer's balance

        """
        self.name=name
        self.account=account
        self.balance=Decimal(0)
    #def deposit(self, amount:float): # python 3
    def deposit(self, amount):        # python 2
        """Deposit money
  
        Parameters
        ----------
        amount: float
            amount of money that the customer wants to deposit

        Raises
        ------
        ValueError
            if balance < 0 
        """

        if self.balance >= 0 and amount >= 0:
            self.balance=self.balance+Decimal(amount)
        else:
            raise ValueError('balance and amount must be positive')
    #def withdraw(self, amount:float): # python 3
    def withdraw(self, amount):        # python 2
        """withdraw money
  
        Parameters
        ----------
        amount: float
            amount of money that the customer wants to withdraw

        Raises
        ------
        RuntimeError
            if balance < amount 
        """

        if amount <= self.balance:
            self.balance -= Decimal(amount)
        else:
            raise RuntimeError('balance not enough')


