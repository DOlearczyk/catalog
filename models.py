from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, \
    func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    """Represents user in database.

    Attributes:
        id: Primary key in table.
        name: User's username.
        email: User's email address.
        picture: Url linking to user's picture. Currently not used in project.
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    """Represents category in catalog.

    Attributes:
        id: Primary key in table.
        name: Category's name.
        items: List of items under category object.
        added_date: Category creation date.
        recent_update_date: Field which shows latest category update date.
        user: Relationship to the creator of the category.
        user_id: Id of the category's creator.

    """
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    items = relationship(
        "Item", backref="Category")
    added_date = Column(DateTime, default=func.now())
    recent_update_date = Column(DateTime, default=func.now(),
                                onupdate=func.now())
    user = relationship("User")
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'added_date': self.added_date,
            'recent_update_date': self.recent_update_date,
            'items': [i.serialize for i in self.items]
        }


class Item(Base):
    """Represents item in catalog.

    Attributes:
        id: Primary key in table.
        name: Item's name.
        description: Description of the item.
        added_date: Item creation date.
        recent_update_date: Field which shows latest item update date.
        category: Shows to which category does item belong.
        category_id: Id of the category, to which item belongs.
        user: Relationship to the creator of the item.
        user_id: Id of the item's creator.

    """
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(Text)
    added_date = Column(DateTime, default=func.now())
    recent_update_date = Column(DateTime, default=func.now(),
                                onupdate=func.now())
    category = relationship(Category)
    category_id = Column(Integer, ForeignKey('category.id'))
    user = relationship("User")
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'added_date': self.added_date,
            'recent_update_date': self.recent_update_date,
            'category_id': self.category_id,
        }


engine = create_engine('sqlite:///app.db')

Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
