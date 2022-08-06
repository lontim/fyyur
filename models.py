from sqlalchemy import ForeignKey, Column, Table
from sqlalchemy.orm import declarative_base, relationship

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

def create_models(app, db):

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

    class Genres(db.Model):
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
        image_link = db.Column(db.String(500))
        facebook_link = db.Column(db.String(120))

        # TODO: implement any missing fields, as a database migration using Flask-Migrate

        genres = relationship("Child", secondary=genre_venue_association_table)
        seeking_talent = db.Column(db.Boolean, default=False)
        seeing_desc = db.Column(db.String)


    class Artist(db.Model):
        __tablename__ = 'Artist'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String)
        city = db.Column(db.String(120))
        state = db.Column(db.String(120))
        phone = db.Column(db.String(120))
        genres = db.Column(db.String(120))
        image_link = db.Column(db.String(500))
        facebook_link = db.Column(db.String(120))

        # TODO: implement any missing fields, as a database migration using Flask-Migrate

    # TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
