account_array = []


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_account_open = False
        self.closed = False
        self.currently_open = False

    def get_balance(self):
        if self.is_account_open:
            return self.balance
        else:
            raise ValueError("Account not open")

    def open(self):
        self.is_account_open = True
        if self.is_account_open:
            if self.currently_open and self.is_account_open:
                raise ValueError("account already open")
            elif not self.currently_open and self.is_account_open:
                self.currently_open = True
                return True
        else:
            raise ValueError("Account not open")

    def deposit(self, amount):
        self.is_account_open = True
        self.currently_open = True

        if self.is_account_open:
            if amount >= 0:
                self.balance += amount
                return True
            else:
                raise ValueError("amount must be greater than 0")
        # for closed account
        elif self.closed is True and self.is_account_open is False:
            raise ValueError("account closed")
        # for unopened account
        elif self.is_account_open is False:
            raise ValueError("account not open")


    def withdraw(self, amount):
        self.is_account_open = True
        if self.is_account_open:
            if amount >= 0:
                if self.balance >= amount:
                    self.balance = self.balance - amount
                else:
                    raise ValueError ("amount must be less than balance")
            else:
                raise AssertionError("Cannot use negative amount!")

    def close(self):
        if self.is_account_open and self.closed is False:
            if self.get_balance() > 0:
                self.withdraw(self.balance)

            self.closed = True
            self.is_account_open = False
            self.currently_open = False

            return self.__init__ is False
        else:
            raise ValueError("account not open")
