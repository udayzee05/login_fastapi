"""add vote table

Revision ID: 6bf237276b8b
Revises: 2d769e6282da
Create Date: 2022-09-21 11:22:05.708276

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '6bf237276b8b'
down_revision = '2d769e6282da'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    pass


def downgrade() -> None:
    op.drop_table('votes')
    pass
