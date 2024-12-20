"""updated indexes

Revision ID: 1dc2adaed0b3
Revises: aa868e0f7cab
Create Date: 2024-12-05 05:59:02.591250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1dc2adaed0b3'
down_revision: Union[str, None] = 'aa868e0f7cab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_csv_data_appid_name', table_name='csv_data')
    op.drop_index('ix_csv_data_appid_name_release_date', table_name='csv_data')
    op.drop_index('ix_csv_data_appid_release_date', table_name='csv_data')
    op.drop_index('ix_csv_data_id', table_name='csv_data')
    op.drop_index('ix_csv_data_name_price', table_name='csv_data')
    op.drop_index('ix_csv_data_name_release_date', table_name='csv_data')
    op.drop_index('ix_csv_data_release_date_price', table_name='csv_data')
    op.create_index('ix_csv_data_price', 'csv_data', ['price'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_csv_data_price', table_name='csv_data')
    op.create_index('ix_csv_data_release_date_price', 'csv_data', ['release_date', 'price'], unique=False)
    op.create_index('ix_csv_data_name_release_date', 'csv_data', ['name', 'release_date'], unique=False)
    op.create_index('ix_csv_data_name_price', 'csv_data', ['name', 'price'], unique=False)
    op.create_index('ix_csv_data_id', 'csv_data', ['id'], unique=False)
    op.create_index('ix_csv_data_appid_release_date', 'csv_data', ['appid', 'release_date'], unique=False)
    op.create_index('ix_csv_data_appid_name_release_date', 'csv_data', ['appid', 'name', 'release_date'], unique=False)
    op.create_index('ix_csv_data_appid_name', 'csv_data', ['appid', 'name'], unique=False)
    # ### end Alembic commands ###
