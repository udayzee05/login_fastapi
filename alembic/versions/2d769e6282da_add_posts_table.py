"""add posts table

Revision ID: 2d769e6282da
Revises: 27835f1d376d
Create Date: 2022-09-21 11:20:50.181615

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '2d769e6282da'
down_revision = '27835f1d376d'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
    sa.Column('title',sa.String(),nullable=False),
    sa.Column('content',sa.String(),nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')),
    sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")

    pass

    


def downgrade() -> None:
    op.drop_table('posts')
    op.drop_constraint('post_users_fk', table_name="posts")
    pass
