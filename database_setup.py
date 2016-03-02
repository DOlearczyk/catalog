from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Base, Category, Item

engine = create_engine('sqlite:///app.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

user1 = User(name="Gal Anonim", email="daromajl@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# Categories
category1 = Category(name="Basketball", user=user1)
session.add(category1)
session.commit()
item1 = Item(name="Basketball",
             description="A basketball is a spherical inflated ball used in a game of basketball. Basketballs typically range in size from very small promotional items only a few inches in diameter to extra large balls nearly a foot in diameter.",
             category=category1, user=user1)
session.add(item1)
session.commit()
item2 = Item(name="Headband",
             description="Keep warm in this fleece headband. Made from polyester fleece with a touch of spandex: the soft fabric holds its shape while providing the perfect fit. One size fits most",
             category=category1, user=user1)
session.add(item2)
session.commit()
category2 = Category(name="Baseball", user=user1)
session.add(category2)
session.commit()
item3 = Item(name="Baseball bat",
             description="A baseball bat is a smooth wooden or metal club used in the sport of baseball to hit the ball after it is thrown by the pitcher.",
             category=category2, user=user1)
session.add(item3)
session.commit()
item4 = Item(name="Baseball glove",
             description="A baseball glove or mitt is a large leather glove worn by baseball players of the defending team which assist players in catching and fielding balls hit by a batter or thrown by a teammate.",
             category=category2, user=user1)
session.add(item4)
session.commit()
category3 = Category(name="Hockey", user=user1)
session.add(category3)
session.commit()
item5 = Item(name="Hockey stick",
             description="A hockey stick is a piece of equipment used in field hockey, ice hockey , roller hockey or underwater hockey to move the ball or puck.",
             category=category3, user=user1)
session.add(item5)
session.commit()