"""empty message

Revision ID: af6d9dae9a0b
Revises: a598e58eb6ac
Create Date: 2024-07-24 20:44:01.160565

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "af6d9dae9a0b"
down_revision: Union[str, None] = "a598e58eb6ac"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("user", "avatar", existing_type=sa.VARCHAR(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("user", "avatar", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###
