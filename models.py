#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Column, Table
from sqlalchemy.orm import declarative_base, relationship
from common_handles import db, migrate

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column("venue_id", ForeignKey("Venue.id"))
    artist_id = db.Column("artist_id", ForeignKey("Artist.id"))
    show_start_time = db.Column(db.DateTime)

    def __repr__(self):
        genre = "Show(id:" + str(self.id) + ", Venue: id:" + self.venue_id + ", Artist: id:" + self.artist_id + ")" + '\n'
        return genre

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

    def __repr__(self):
        genre = "Genre(" + str(self.id) + ", " + self.name + ")" + '\n'
        return genre

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
        venue = "Venue(" + str(self.id) + ", " + self.name + ")" + '\n'
        return venue

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_desc = db.Column(db.String)
    genres = relationship("Genre", secondary=genre_artist_association_table)
   
    def __repr__(self):
      artist = "Artist(" + str(self.id) + ", " + self.name + ", " + self.city + ")" + '\n'
      return artist
