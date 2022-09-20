"""craete vote table

Revision ID: 95789b2b91d5
Revises: a1d9267670cd
Create Date: 2022-09-20 14:36:20.411959

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '95789b2b91d5'
down_revision = 'a1d9267670cd'
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
