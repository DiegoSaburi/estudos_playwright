from dataclasses import dataclass
from enum import Enum

from models.account import Account
from models.money import Money


class TransferDate(str, Enum):
	TODAY = "Today"
	SCHEDULE_FOR_LATER = "Schedule for later"


@dataclass(frozen=True)
class Transfer:
	from_account: Account
	to_account: Account
	amount: Money
	transfer_date: TransferDate

	def __post_init__(self) -> None:
		if not isinstance(self.from_account, Account):
			raise TypeError("From account must be an Account instance")
		if not isinstance(self.to_account, Account):
			raise TypeError("To account must be an Account instance")
		if not isinstance(self.amount, Money):
			raise TypeError("Transfer amount must be a Money instance")
		if isinstance(self.transfer_date, str):
			try:
				object.__setattr__(
					self, "transfer_date", TransferDate(self.transfer_date)
				)
			except ValueError as error:
				raise ValueError(
					f"Invalid transfer date: {self.transfer_date!r}"
				) from error
		elif not isinstance(self.transfer_date, TransferDate):
			raise TypeError("Transfer date must be a TransferDate")