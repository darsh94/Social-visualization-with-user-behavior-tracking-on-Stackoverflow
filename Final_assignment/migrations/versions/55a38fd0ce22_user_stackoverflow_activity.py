"""user_stackoverflow_activity

Revision ID: 55a38fd0ce22
Revises: 8d079a8c4879
Create Date: 2018-09-18 04:12:46.202084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55a38fd0ce22'
down_revision = '8d079a8c4879'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_stackoverflow_activity', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_stackoverflow_activity_timestamp'), 'user_stackoverflow_activity', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_stackoverflow_activity_timestamp'), table_name='user_stackoverflow_activity')
    op.drop_column('user_stackoverflow_activity', 'timestamp')
    # ### end Alembic commands ###