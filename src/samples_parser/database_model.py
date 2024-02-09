from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
)


DataBaseModel = declarative_base()

class SamplesAll(DataBaseModel):
    __tablename__ = 'samplesall'
    __table_args__ = {'schema': 'samples'}

    sample_note = Column(String, nullable=True),
    timestamps = Column(String, nullable=True),
    sample = Column(String),
    album = Column(String),
    song = Column(String),
    band = Column(String),
    groups = Column(Integer),
    songs = Column(Integer),
    samples = Column(Integer),
    points = Column(Integer),
    name = Column(String),
    order = Column(Integer),

[{'sample_note': 'Note: Police robot addressing crowd gathering after a shootout',
  'timestamps': None,
  'sample': 'Move on, move on.',
  'album': 'One Thousand Years of Trouble',
  'song': 'This is Crush Collision',
  'band': 'Age of Chance',
  'groups': 87,
  'songs': 116,
  'samples': 221,
  'points': 738,
  'name': 'Blade Runner',
  'order': 1},
 {'sample_note': 'Note: "All those moments will be lost in time"',
  'timestamps': "['0:12']",
  'sample': 'All diese Momente werden verloren sein in der Zeit',
  'album': 'Half Rotten and Decayed',
  'song': 'Silence besides the Sun',
  'band': 'Amgod',
  'groups': 87,
  'songs': 116,
  'samples': 221,
  'points': 738,
  'name': 'Blade Runner',
  'order': 1}]