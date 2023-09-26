from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
metadata=MetaData(naming_convention={
    "fk":"fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)



# Define Restaurant Model
class Restaurant(db.Model,SerializerMixin):
  __tablename__='restaurant'

serialize_rules=('-pizzas.restaurant','-restaurant.pizza')
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String, unique=True, nullable=False)
address = db.Column(db.String,unique=True, nullable=False)

pizzas = db.relationship('RestaurantPizza', backref='restaurants')

@validates(name)
def validate_name(self, key, value):
        if  len(value) >50:
            raise ValueError("Name must be at less than 50 characters long.")
            
        return value

# Define Pizza Model
class Pizza(db.Model,SerializerMixin):
    __tablename__='pizza'

    serialize_rules=('-restaurant.pizza','-pizzas.restaurant')
id = db.Column(db.Integer, primary_key=True)
name = db.Column(unique=True, nullable=False)
ingredients = db.Column( db.string)
created_at = db.Column(db.DateTime, server_default=db.func.now())
updated_at = db.Column(db.DateTime, onupdate=db.func.now())

restaurant= db.relationship('RestaurantPizza', backref='pizza')


# Define RestaurantPizza Model
class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__='restaurantpizza'

    serialize_rules=('-restaurant','pizza')
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id') )
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates(price)
    def validate_price(self, key, value):
        if not 1<=value<=30:
            raise ValueError("price must found btwn 1 and 30")
            
        return value


    


