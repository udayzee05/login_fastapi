from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP, String

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key =True, nullable= False)
    title = Column(Text,nullable=False)
    content =Column(Text,nullable=False)
    published = Column(Boolean,server_default='True',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id", ondelete = "CASCADE"),nullable = False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key =True, nullable= False)
    email = Column(String, nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)


