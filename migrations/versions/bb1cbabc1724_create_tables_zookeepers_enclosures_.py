"""Create tables zookeepers, enclosures, animals

Revision ID: bb1cbabc1724
Revises: 
Create Date: 2024-03-01 10:13:59.708607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb1cbabc1724'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enclosures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('environment', sa.String(), nullable=True),
    sa.Column('open_to_visitors', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('zookeepers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('birthday', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('animals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.Column('zookeeper_id', sa.Integer(), nullable=True),
    sa.Column('enclosure_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enclosure_id'], ['enclosures.id'], name=op.f('fk_animals_enclosure_id_enclosures')),
    sa.ForeignKeyConstraint(['zookeeper_id'], ['zookeepers.id'], name=op.f('fk_animals_zookeeper_id_zookeepers')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('animals')
    op.drop_table('zookeepers')
    op.drop_table('enclosures')
    # ### end Alembic commands ###
