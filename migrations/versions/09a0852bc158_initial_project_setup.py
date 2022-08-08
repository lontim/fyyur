"""1) Initial project setup

Revision ID: 09a0852bc158
Revises: 
Create Date: 2022-08-06 13:00:58.170462

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import Sequence, CreateSequence

# revision identifiers, used by Alembic.
revision = '09a0852bc158'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
#    artist_id_seq = op.execute(CreateSequence(Sequence('artist_id_seq')))
    artist_table = op.create_table('Artist',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('city', sa.String(length=120), nullable=True),
        sa.Column('state', sa.String(length=120), nullable=True),
        sa.Column('phone', sa.String(length=120), nullable=True),
        sa.Column('website', sa.String(length=500), nullable=True),
        sa.Column('image_link', sa.String(length=500), nullable=True),
        sa.Column('facebook_link', sa.String(length=120), nullable=True),
        sa.Column('seeking_venue', sa.Boolean(), nullable=True),
        sa.Column('seeking_desc', sa.String(), nullable=True),

        sa.PrimaryKeyConstraint('id')
    )
    venue_table = op.create_table('Venue',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('city', sa.String(length=120), nullable=True),
        sa.Column('state', sa.String(length=120), nullable=True),
        sa.Column('address', sa.String(length=120), nullable=True),
        sa.Column('phone', sa.String(length=120), nullable=True),
        sa.Column('website', sa.String(length=500), nullable=True),
        sa.Column('image_link', sa.String(length=500), nullable=True),
        sa.Column('facebook_link', sa.String(length=120), nullable=True),
        sa.Column('seeking_talent', sa.Boolean(), nullable=True),
        sa.Column('seeking_desc', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.bulk_insert(venue_table,
    [
        { 'id':1, 'name': 'The Musical Hop',
            'address': '1015 Folsom Street',
            'city': 'San Francisco',
            'state': 'CA',
            'phone': '123-123-1234',
            'website': 'https://www.themusicalhop.com',
            'facebook_link': 'https://www.facebook.com/TheMusicalHop',
            'image_link': 'https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60',
            'seeking_talent': True,
            'seeking_desc': 'We are on the lookout for a local artist to play every two weeks. Please call us.'
        },
        { 'id':2, 'name': 'The Dueling Pianos Bar',
            'address': '335 Delancey Street',
            'city': 'New York',
            'state': 'NY',
            'phone': '914-003-1132',
            'website': 'https://www.theduelingpianos.com',
            'facebook_link': 'https://www.facebook.com/theduelingpianos',
            'image_link': "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80",
            'seeking_talent': False,
            'seeking_desc': ''
        },
        { 'id':3, 'name': 'Park Square Live Music & Coffee',
            'address': '34 Whiskey Moore Ave',
            'city': 'San Francisco',
            'state': 'CA',
            'phone': '415-000-1234',
            'website': 'https://www.parksquarelivemusicandcoffee.com',
            'facebook_link': 'https://www.facebook.com/ParkSquareLiveMusicAndCoffee',
            'image_link': "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
            'seeking_talent': False,
            'seeking_desc': ''
        },
        { 'id':4, 'name': "Mr Tipple's Recording Studio",
            'address': '39 Fell Street',
            'city': 'San Francisco',
            'state': 'CA',
            'phone': '+1 415-384-9365',
            'website': 'www.mrtipplessf.com',
            'facebook_link': 'https://www.facebook.com/Mr.TipplesRecordingStudio',
            'image_link': "https://mrtipplessf.com/wp-content/uploads/2019/03/mrt-gallery-18-1030x743.jpg",
            'seeking_talent': True,
            'seeking_desc': 'We hold open jam sessions every Thursday! Local & national bands welcome.'
        },
        { 'id':5, 'name': 'The Hole in the Wall',
            'address': '2538 Guadalupe St',
            'city': 'Austin',
            'state': 'TX',
            'phone': '555-111-1111',
            'website': 'https://www.holeinthewallaustin.com/',
            'facebook_link': 'https://www.facebook.com/HITWaustin/',
            'image_link': 'https://static.wixstatic.com/media/58d7b5_a4ca66ff09754240b0a42aa1421676ab~mv2_d_2048_1365_s_2.jpg/v1/fit/w_3198,h_874,q_90/58d7b5_a4ca66ff09754240b0a42aa1421676ab~mv2_d_2048_1365_s_2.jpg',
            'seeking_talent': True,
            'seeking_desc': "Speak to Doris in reception booth. Seeking talented bands in the area!"
        }
    ] )
    op.execute('alter sequence "Venue_id_seq" restart with 6')

    op.bulk_insert(artist_table,
    [
        { 'id':4, 'name': "Guns'n'Petals",
          'city': 'San Francisco', 'state': 'CA',
          'phone': '326-123-5000', 'website': 'https://www.gunsnpetalsband.com',
          'facebook_link': 'https://www.facebook.com/GunsNPetals',
          'seeking_venue': True,
          'seeking_desc': 'Looking for shows to perform at in the San Francisco Bay Area!',
          'image_link': 'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80'
        },
        { 'id':5, 'name': 'Matt Quevedo',
          'city': 'New York', 'state': 'NY',
          'phone': '300-400-5000', 'website': '',
          'facebook_link': 'https://www.facebook.com/mattquevedo923251523',
          'seeking_venue': False,
          'seeking_desc': '',
          'image_link': 'https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80'
        },
        { 'id':6, 'name': 'The Wild Sax Band',
          'city': 'San Francisco', 'state': 'CA',
          'phone': '432-325-5432', 'website': '',
          'facebook_link': '',
          'seeking_venue': False,
          'seeking_desc': '',
          'image_link': 'https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80'
        },
        { 'id':7, 'name': 'Sound Team',
          'city': 'Austin', 'state': 'TX',
          'phone': '555-321-1234', 'website': 'https://web.archive.org/web/20060612220620/http://www.soundteam.net/',
          'facebook_link': '',
          'seeking_venue': True,
          'seeking_desc': 'New venue wanted, original venue closed for refurb',
          'image_link': 'https://images.unsplash.com/flagged/photo-1568045062664-fe4aaab61376?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2075&q=80'
        }
    ] )
    op.execute('alter sequence "Artist_id_seq" restart with 8')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Venue')
    op.drop_table('Artist')
    # ### end Alembic commands ###
