"""5) Artist-genres association added

Revision ID: 38f6c02025e5
Revises: a920576e1016
Create Date: 2022-08-07 12:56:54.714339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38f6c02025e5'
down_revision = 'a920576e1016'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    genre_artist_table = op.create_table('genre_artist_assoc',
        sa.Column('artist_id', sa.Integer(), nullable=False),
        sa.Column('genre_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
        sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], ),
        sa.PrimaryKeyConstraint('artist_id', 'genre_id')
    )
    op.bulk_insert(genre_artist_table,
    [
        { 'artist_id': 4, 'genre_id': 17 },
        { 'artist_id': 5, 'genre_id': 11 },
        { 'artist_id': 6, 'genre_id': 11 },
        { 'artist_id': 6, 'genre_id': 3 },
        { 'artist_id': 7, 'genre_id': 1 },
        { 'artist_id': 7, 'genre_id': 5 },

    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genre_artist_assoc')
    # ### end Alembic commands ###
