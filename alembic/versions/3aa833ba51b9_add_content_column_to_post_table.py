"""add content column to post table

Revision ID: 3aa833ba51b9
Revises: 354f6f60589d
Create Date: 2023-10-29 21:43:03.089722

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3aa833ba51b9'
down_revision: Union[str, None] = '354f6f60589d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
