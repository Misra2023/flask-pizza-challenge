# seed.py

from app import app, db
from models import Restaurant, Pizza, RestaurantPizza



# Use the app context to work with the database
with app.app_context():
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()
    db.session.query(RestaurantPizza).delete()

    # Create sample data
    dominion_pizza = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
    pizza_hut = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")
    cheese_pizza = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni_pizza = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Add data to the session
    db.session.add(dominion_pizza)
    db.session.add(pizza_hut)
    db.session.add(cheese_pizza)
    db.session.add(pepperoni_pizza)

    # Create RestaurantPizza relationships
    dominion_cheese = RestaurantPizza(price=10.99, pizza_id=cheese_pizza.id, restaurant_id=dominion_pizza.id)
    pizza_hut_pepperoni = RestaurantPizza(price=12.99, pizza_id=pepperoni_pizza.id, restaurant_id=pizza_hut.id)

    # Add RestaurantPizza relationships to the session
    db.session.add(dominion_cheese)
    db.session.add(pizza_hut_pepperoni)

    # Commit the changes to the database
    db.session.commit()

# The script can be run as-is without issues
