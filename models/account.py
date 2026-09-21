from dataclasses import dataclass
from enum import Enum

from models.money import Money


class AccountType(str, Enum):
	CHECKING = "Checking"
	SAVINGS = "Savings"
	CREDIT = "Credit"


@dataclass(frozen=True)
class Account:
	name: str
	type: AccountType
	starting_balance: Money

	def __post_init__(self) -> None:
		if isinstance(self.type, str):
			try:
				object.__setattr__(self, "type", AccountType(self.type))
			except ValueError as error:
				raise ValueError(f"Invalid account type: {self.type!r}") from error
		elif not isinstance(self.type, AccountType):
			raise TypeError("Account type must be an AccountType")

		if not isinstance(self.starting_balance, Money):
			raise TypeError("Starting balance must be a Money instance")