import re
from dataclasses import dataclass
from decimal import Decimal
from typing import Self


@dataclass(frozen=True)
class Money:
	value: Decimal

	@classmethod
	def from_text(cls, text: str) -> Self:
		value = re.sub(r"[^\d.-]", "", text)
		if not value:
			raise ValueError(f"Could not parse monetary value from: {text!r}")
		return cls(Decimal(value))

	@classmethod
	def zero(cls) -> Self:
		return cls(Decimal("0"))

	def __add__(self, other: Self) -> Self:
		if not isinstance(other, Money):
			return NotImplemented
		return type(self)(self.value + other.value)

	def __sub__(self, other: Self) -> Self:
		if not isinstance(other, Money):
			return NotImplemented
		return type(self)(self.value - other.value)

	def __lt__(self, other: Self) -> bool:
		if not isinstance(other, Money):
			return NotImplemented
		return self.value < other.value

	def __le__(self, other: Self) -> bool:
		if not isinstance(other, Money):
			return NotImplemented
		return self.value <= other.value

	def __gt__(self, other: Self) -> bool:
		if not isinstance(other, Money):
			return NotImplemented
		return self.value > other.value

	def __ge__(self, other: Self) -> bool:
		if not isinstance(other, Money):
			return NotImplemented
		return self.value >= other.value