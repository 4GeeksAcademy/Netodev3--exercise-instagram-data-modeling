import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False, unique=True)


class Follower(Base):
    __tablename__ = 'follower'
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.ID'))
    user_from_id_relationship = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.ID'))
    user_to_id_relationship = relationship(User)


class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    user_id_relationship = relationship(User)


class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(200))
    author_id = Column(Integer, ForeignKey('user.ID'))
    author_id_relationship = relationship(User)
    post_id = Column(Integer, ForeignKey('post.ID'))
    post_id_relationship = relationship(Post)


class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String(30))
    post_id = Column(Integer, ForeignKey('post.ID'))
    post_id_relationship = relationship(Post)


# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
