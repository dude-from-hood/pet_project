import pytest


class BankAccount:

    def __init__(self,
                 account_number: str,
                 initial_balance: float
                 ):

        if not len(account_number) >= 5:
            raise ValueError("account_number should be >= 5")
        if not account_number.isdigit():
            raise ValueError("account_number should be string of digits")
        self.__account_number = account_number


        if not isinstance(initial_balance, (int, float)):
            raise ValueError("initial_balance should be int or float")
        if initial_balance < 0:
            raise ValueError("initial_balance should be int and >= 0")

        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("amount should be > 0")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount should be > 0")
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.__balance -= amount

    def __str__(self):
        return f"BankAccount(acc={self.account_number}, balance={self.balance})"


class TestBankAccount:

    @pytest.mark.parametrize("acc, balance", [
        ('12345', 100),
        ('123456', 1000.00),
        ('12345', 1),
        ('12345', 0),
    ])
    def test_create_ba(self, acc, balance):
        ba = BankAccount(acc, balance)
        assert ba.account_number == acc
        assert ba.balance == balance
        assert isinstance(ba.balance, (int, float))


    @pytest.mark.parametrize("acc_num, balance", [
        ("1234", 100),  # короткий номер
        ("abcde", 100),  # не цифры
        ("12345", -50),  # отрицательный баланс
        ("12345", "100"),  # нечисловой баланс
        ("12345abc", 100),  # асс_num с буквами
    ])
    def test_invalid_account_creation_raises_error(self, acc_num, balance):
        with pytest.raises(ValueError):
            BankAccount(acc_num, balance)

    # ввести наследование, использовать super.init()