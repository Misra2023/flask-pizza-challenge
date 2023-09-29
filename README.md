# flask-pizza-challenge
# Misra's Pizza Restaurant API 
This is a Flask-based RESTful API for managing pizza restaurants, pizzas, and their associations. The API provides endpoints for retrieving information about restaurants, pizzas, and the relationships between them, as well as creating new associations between restaurants and pizzas.

# Prerequisites
Before you begin, make sure you have the following installed on your system:

Python (3.7 or higher)
Virtualenv
SQLite (optional, for local development)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/misras-pizza-restaurant-api.git
Navigate to the project directory:

bash
Copy code
cd misras-pizza-restaurant-api
Create a virtual environment (recommended):

bash
Copy code
virtualenv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Configuration
The application uses an SQLite database by default for simplicity. You can configure the database connection in the app.py file:

python
Copy code
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
You can change the database URI to a different database system if needed.

# Database Initialization
To set up the database with sample data, run the following commands:

bash
Copy code
python seed.py
This will create the SQLite database (pizza_restaurants.db) and populate it with sample restaurants, pizzas, and restaurant-pizza associations.

# Running the Application
Start the Flask application:

bash
Copy code
python app.py
The API should now be accessible at http://localhost:5000/.

API Endpoints
# Home
Endpoint: /
Method: GET
Description: Welcome message for Misra's Pizza Restaurant API.
# Get All Restaurants
Endpoint: /restaurants
Method: GET
Description: Get a list of all restaurants.
# Get Restaurant by ID
Endpoint: /restaurants/<id>
Method: GET
Description: Get restaurant details by its ID.
Parameters:
id (integer): The ID of the restaurant.
# Delete Restaurant by ID
Endpoint: /restaurants/<id>
Method: DELETE
Description: Delete a restaurant by its ID.
Parameters:
id (integer): The ID of the restaurant.
# Get All Pizzas
Endpoint: /pizza
Method: GET
Description: Get a list of all pizzas.
# Create Restaurant-Pizza Association
Endpoint: /restaurant_pizza
Method: POST
Description: Create a new association between a restaurant and a pizza.
Request Body: JSON object with the following fields:
price (integer): The price of the pizza at the restaurant.
pizza_id (integer): The ID of the pizza.
restaurant_id (integer): The ID of the restaurant.
Example Request Body:
json
Copy code
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
Response: Returns details of the associated pizza.
# Error Handling
The API includes error handling for various scenarios, such as validation errors and resource not found errors. Error responses are returned with appropriate status codes and error messages in JSON format.

# Data Models
The API uses three data models:

# Restaurant:

Fields: id, name, address
Relationships: One-to-many with RestaurantPizza
# Pizza:

Fields: id, name, ingredients
Relationships: One-to-many with RestaurantPizza
# RestaurantPizza:

Fields: id, price, pizza_id, restaurant_id
Relationships: Many-to-one with Restaurant and Pizza
# Sample Data
The seed.py script populates the database with sample data for restaurants, pizzas, and restaurant-pizza associations. You can use this script to initialize the database.

# Built With
Flask - Web framework for Python
SQLAlchemy - SQL toolkit and Object-Relational Mapping (ORM) library
Flask-Migrate - Database migration support for Flask applications
Faker - Python library for generating fake data
# Authors
MISRA ABDI
 # License
This project is licensed under the MIT License - see the LICENSE file for details.