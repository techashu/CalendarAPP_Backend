"""empty message

Revision ID: ae46c015bc5f
Revises: 
Create Date: 2019-09-03 15:32:55.397326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae46c015bc5f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('start_date', sa.TIMESTAMP(), nullable=False),
    sa.Column('end_date', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###
