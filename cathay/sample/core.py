from cathay.sample.customer import Customer
from decimal import Decimal

class CustomerDataProcess():
    """
    Simulate some actions that banks will perform
    ...
    Attributes
    ----------
    None

    Methods
    -------
    add_interest(customer, rate)
        add interest to customer's balance
    """
    @staticmethod
    def add_interest(customer, rate): # python 2
    #def add_interest(customer: Customer, rate:float)->Decimal: # python 3
        """ add interest
  
        Parameters
        ----------
        customer: Customer
            customer object
        rate: float
            our bank rate

        Raises
        ------
        RuntimeError
            if balance < amount 
        """

        if isinstance(customer, Customer):
            customer.balance=customer.balance * Decimal(1.0+rate)
            return customer.balance
        raise TypeError("unsupport input type: customer")

    
