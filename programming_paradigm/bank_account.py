class BankAccount:
    """A simple bank account class that handles deposits, withdrawals, and balance display."""
    
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance.
        
        Args:
            initial_balance (float, optional): Starting balance. Defaults to 0.
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit.
        """
        self.account_balance += amount
    
    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds are available.
        
        Args:
            amount (float): The amount to withdraw.
            
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")