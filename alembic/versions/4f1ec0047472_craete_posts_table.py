"""craete posts table

Revision ID: 4f1ec0047472
Revises: 
Create Date: 2022-09-20 14:23:01.527187

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '4f1ec0047472'
down_revision = None
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
