# data/account_factory.py

import random

from models.account import Account, AccountType
from models.money import Money


class AccountFactory:
    def __init__(self, rng: random.Random | None = None):
        self._rng = rng or random.Random()

    def create(
        self,
        *,
        name: str | None = None,
        account_type: AccountType | None = None,
        starting_balance: Money | None = None,
    ) -> Account:
        return Account(
            name=name or self._generate_name(),
            type=account_type or self._generate_account_type(),
            starting_balance=(
                starting_balance
                if starting_balance is not None
                else self._generate_balance()
            ),
        )

    def _generate_name(self) -> str:
        return f"Automation Account {self._rng.randint(1000, 9999)}"

    def _generate_account_type(self) -> AccountType:
        return self._rng.choice(list(AccountType))

    def _generate_balance(self) -> Money:
        cents = self._rng.randint(0, 1_000_000)
        return Money.from_text(f"{cents / 100:.2f}")