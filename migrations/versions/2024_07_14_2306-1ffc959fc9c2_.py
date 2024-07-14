"""empty message

Revision ID: 1ffc959fc9c2
Revises: 6370e7a01ef5
Create Date: 2024-07-14 23:06:44.870210

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1ffc959fc9c2"
down_revision: Union[str, None] = "6370e7a01ef5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "importantevent", sa.Column("character_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key(None, "importantevent", "character", ["character_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "importantevent", type_="foreignkey")
    op.drop_column("importantevent", "character_id")
    # ### end Alembic commands ###
