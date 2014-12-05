"""Add tickets table

Revision ID: 516b5a4829e
Revises: 31cde2cf5e6
Create Date: 2014-12-05 11:13:14.203925

"""

# revision identifiers, used by Alembic.
revision = '516b5a4829e'
down_revision = '31cde2cf5e6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('closed', sa.Boolean(), nullable=False),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.Column('subject', sa.String(), nullable=False),
    sa.Column('notify_owner', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ticket_messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticket_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticket_messages')
    op.drop_table('tickets')
    ### end Alembic commands ###