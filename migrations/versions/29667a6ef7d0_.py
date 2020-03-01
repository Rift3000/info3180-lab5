"""empty message

Revision ID: 29667a6ef7d0
Revises: dbe43142d127
Create Date: 2020-02-29 22:50:09.319366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29667a6ef7d0'
down_revision = 'dbe43142d127'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
