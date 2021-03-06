"""atualizando banco de dados

Revision ID: 249aa92c43c1
Revises: 
Create Date: 2019-07-04 12:45:06.288674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '249aa92c43c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alunos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('idade', sa.Integer(), nullable=True),
    sa.Column('curso', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('telefone', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('telefone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alunos')
    # ### end Alembic commands ###
