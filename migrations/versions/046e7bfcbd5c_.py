"""empty message

Revision ID: 046e7bfcbd5c
Revises: ebb17dc437d0
Create Date: 2020-05-17 23:44:25.218325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '046e7bfcbd5c'
down_revision = 'ebb17dc437d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genre', sa.ARRAY(sa.String(length=120)), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genre')
    # ### end Alembic commands ###