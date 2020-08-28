from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

myFirstRestaurant = Restaurant(name = "Dal's Cuisson")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()

mySecondRestaurant = Restaurant(name = "TFC")
session.add(mySecondRestaurant)
session.commit()
session.query(Restaurant).all()

fufueru = MenuItem(name = "Fufu and Eru",
description= "Traditional Bayangian meal", course ="Entree",
price ="1500FCFA", restaurant = myFirstRestaurant)
session.add(fufueru)
session.commit()
session.query(MenuItem).all()

ndoleplantain = MenuItem(name = "Ndole and Plantain",
description="Natural nutritive meal", course="Entree",
price="1500FCFA", restaurant = myFirstRestaurant)
session.add(ndoleplantain)
session.commit()
session.query(MenuItem).all()

achu = MenuItem(name="Achu",
description="Traditional yellow North West meal",course="Entree", price="2000FCFA", restaurant = myFirstRestaurant)
session.add(achu)
session.commit()
session.query(MenuItem).all()

ekwang = MenuItem(name="Ekwang",
description ="Traditional rapped grit cocoyam",
course="Entree", price="2000FCFA", restaurant= myFirstRestaurant)
session.add(ekwang)
session.commit()
session.query(MenuItem).all()

friedrice = MenuItem(name="Fried Rice & Chicken",
description="Spiced with natural ingredients", course="Entree",
price="1000FCFA", restaurant= mySecondRestaurant)
session.add(friedrice)
session.commit()
session.query(MenuItem).all()

dodosauce = MenuItem(name="Dodo, Sauce and Liver",
description="Fried ripped plantain with sauce",
course="Entree", price="1000FCFA", restaurant= mySecondRestaurant)
session.add(dodosauce)
session.commit()
session.query(MenuItem).all()

firstResult = session.query(Restaurant).first()
firstResult.name
session.query(Restaurant).all()

# The below code updates and existing item
CMRfriedrice = session.query(MenuItem).filter_by(id = 53).one()
CMRfriedrice.price = '1500FCFA'
session.add(CMRfriedrice)
session.commit()
friedrices = session.query(MenuItem).filter_by(name = 'Fried Rice & Chiken')

# Deleting an item
lowsales = session.query(MenuItem).filter_by(name = "Ekwang", id = 132).one()
session.delete(lowsales)
session.commit
