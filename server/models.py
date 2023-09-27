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
    __tablename__='restaurants'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.String,unique=True, nullable=False)

    pizzas = db.relationship('RestaurantPizza', backref='restaurants')

    def restaurants_dict(self):
                return{
                    
                    "id":self.id,
                    "name":self.name,
                    "address":self.address,
                }

    @validates(name)
    def validate_name(self, key, value):
            if  len(value) >50:
                raise ValueError("Name must be at less than 50 characters long.")
                
            return value

# Define Pizza Model
class Pizza(db.Model,SerializerMixin):
    __tablename__='pizzas'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column( db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant= db.relationship('RestaurantPizza', backref='pizzas')

    def pizza_dict(self):
                return{
                    
                    "id":self.id,
                    "name":self.name,
                    "ingredients":self.ingredients,
                }
# Define RestaurantPizza Model
class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__='restaurantpizzas'

    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id') )
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates(price)
    def validate_price(self, key, value):
        if not 1<=value<=30:
            raise ValueError("price must found btwn 1 and 30")
            
        return value
    
    def restaurantpizza_dict(self):
                return{
                    
                    "id":self.id,
                    "price":self.price,
                    "restaurant_id":self.restaurant_id,
                    "pizza_id":self.pizza_id,
                }


    


