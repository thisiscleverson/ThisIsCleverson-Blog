"""contents

Revision ID: e9e91c3c7794
Revises: 
Create Date: 2023-12-06 19:34:29.551344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9e91c3c7794'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contents',
    sa.Column('id', sa.String(length=36), nullable=True),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contents')
    # ### end Alembic commands ###