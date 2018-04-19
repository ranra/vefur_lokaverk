
"""add language to posts
Revision ID: 2b017edaa91f
Revises: ae346256b650
Create Date: 2017-10-04 22:48:34.494465
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b017edaa91f'
down_revision = 'ae346256b650'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###