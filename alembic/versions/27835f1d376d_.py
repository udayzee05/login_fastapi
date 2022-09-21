"""empty message

Revision ID: 27835f1d376d
Revises: 
Create Date: 2022-09-21 11:17:47.871667

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '27835f1d376d'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass

def downgrade() -> None:
    op.drop_table('users')
    pass
