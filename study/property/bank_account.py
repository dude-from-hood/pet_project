import pytest


class BankAccount:

    def __init__(
        self,
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

class LimitedWithdrawAccount(BankAccount):

    def __init__(
        self,
        account_number: str,
        initial_balance: float,
        max_withdrawal: float,
    ):
        # вызываем конструктор родителя
        super().__init__(account_number, initial_balance)

        if not isinstance(max_withdrawal, (int, float)):
            raise ValueError("max_withdrawal must be a number")
        if max_withdrawal <= 0:
            raise ValueError("max_withdrawal must be positive")

        # инициализируем новый параметр
        self.__max_withdrawal = max_withdrawal


    def withdraw(self, amount):
        if not amount <= self.__max_withdrawal:
            raise ValueError("withdrawal exceeds max limit")

        super().withdraw(amount)

class TestAccount:

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

    #========== Вариант через фикстуру =========

    # фикстура валидных тест-кейсов
    @pytest.fixture(params=[
        ('12345', 100),
        ('123456', 1000.00),
        ('12345', 1),
        ('12345', 0),
    ])
    def create_valid_cases(self, request):
        return request.param

    # тест
    def test_valid_cases(self, create_valid_cases):
        # распаковываем кортежи
        acc, balance = create_valid_cases
        # создаем объект
        ba = BankAccount(acc, balance)

        # делаем проверки
        assert ba.account_number == acc
        assert ba.balance == balance
        assert isinstance(ba.balance, (int, float))


    @pytest.fixture(params=[
        ('12345', 100, 30, 10, 90), # снимаем 10, получаем баланс 90
    ])
    def create_positive_cases_max_withdrawal(self, request):
        return request.param

    def test_max_withdrawal_positive(self, create_positive_cases_max_withdrawal):

        acc, balance, max_withdrawal, withdrawal, final_balance = create_positive_cases_max_withdrawal
        obj = LimitedWithdrawAccount(acc, balance, max_withdrawal)

        obj.withdraw(withdrawal)

        print(f"\n{obj.balance}")

        assert obj.account_number == acc
        assert obj.balance == final_balance


    @pytest.mark.parametrize("acc, balance, max_wd, amount", [
        ("22222", 100, 50, 60),  # превышение лимита при снятии
    ])
    def test_withdraw_exceeds_limit(self, acc, balance, max_wd, amount):
        acc_obj = LimitedWithdrawAccount(acc, balance, max_wd)
        with pytest.raises(ValueError, match="exceeds max limit"):
            acc_obj.withdraw(amount)


    @pytest.mark.parametrize("acc, balance, max_wd", [
        ("33333", 100, "2"),  # неверный тип max_withdrawal
    ])
    def test_invalid_max_withdrawal_type(self, acc, balance, max_wd):
        with pytest.raises(ValueError, match="must be a number"):
            LimitedWithdrawAccount(acc, balance, max_wd)

