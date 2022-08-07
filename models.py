#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask
from flask_moment import Moment
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Column, Table
from sqlalchemy.orm import declarative_base, relationship

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column("venue_id", ForeignKey("Venue.id"))
    artist_id = db.Column("artist_id", ForeignKey("Artist.id"))
    show_start_time = db.Column(db.DateTime)

genre_venue_association_table = Table(
    "genre_venue_assoc",
    db.Model.metadata,
    Column("venue_id", ForeignKey("Venue.id"), primary_key=True),
    Column("genre_id", ForeignKey("Genre.id"), primary_key=True),
)

genre_artist_association_table = Table(
    "genre_artist_assoc",
    db.Model.metadata,
    Column("artist_id", ForeignKey("Artist.id"), primary_key=True),
    Column("genre_id", ForeignKey("Genre.id"), primary_key=True),
)

class Genre(db.Model):
    __tablename__ = 'Genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_desc = db.Column(db.String)
    genres = relationship("Genre", secondary=genre_venue_association_table)

    def __repr__(self):
        venue = "Venue(" + self.id + ", " + str(self.name) + ")"
        return venue

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = relationship("Genre", secondary=genre_artist_association_table)
   
    def __repr__(self):
      artist = "Artist(" + self.id + ", " + self.name + ", " + self.city + ")"
      return artist

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
