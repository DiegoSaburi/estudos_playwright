from models.user import User


STANDARD_USER = User(
    username="standard_user",
    password="bank_sauce",
    description="Full access",
)

LOCKED_USER = User(
    username="locked_user",
    password="bank_sauce",
    description="Locked account",
)

FROZEN_USER = User(
    username="frozen_user",
    password="bank_sauce",
    description="Frozen — no transfers",
)

OVERDRAFT_USER = User(
    username="overdraft_user",
    password="bank_sauce",
    description="Negative balance",
)

SLOW_USER = User(
    username="slow_user",
    password="bank_sauce",
    description="Slow loading",
)

ERROR_USER = User(
    username="error_user",
    password="bank_sauce",
    description="Wrong loan total",
)

ADMIN_USER = User(
    username="admin_user",
    password="admin_sauce",
    description="Admin view",
)
