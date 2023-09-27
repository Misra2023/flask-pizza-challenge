from app import app,db
from models import Restaurant,Pizza,RestaurantPizza
import random
from faker import Faker

with app.app_context():
    fake=Faker()

    db.drop_all()
    db.create_all()

    restaurants=[]
    for i in range(50):
        restaurant=Restaurant( 
            name=fake.unique.company(),
            address=fake.address()
        )
        restaurants.append(restaurant)
    db.session.add_all(restaurants)
    db.session.commit() 


    pizzas=[]
    for i in range(50):
        pizza=Pizza( 
            name=fake.name(),
            ingredients=fake.address()
        )
        pizzas.append(pizza)
    db.session.add_all(pizzas)
    db.session.commit() 


    restaurantpizzas=[]
    for i in range (50):
        restaurantpizza=RestaurantPizza( 
            price=random.randint(1,30),
            pizza_id=random.choice(pizzas).id,
            restaurant_id=random.choice(restaurants).id,
        )
        restaurantpizzas.append(restaurantpizza)
    db.session.add_all(restaurantpizzas)
    db.session.commit()

