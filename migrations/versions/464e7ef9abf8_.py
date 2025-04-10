"""empty message

Revision ID: 464e7ef9abf8
Revises: 012bb47cf028
Create Date: 2025-03-20 23:14:18.041748

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '464e7ef9abf8'
down_revision = '012bb47cf028'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(collation='utf8mb3_bin', length=120),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(collation='utf8mb3_bin', length=120),
               existing_nullable=False)

    # ### end Alembic commands ###
