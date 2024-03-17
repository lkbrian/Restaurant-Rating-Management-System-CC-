# Restaurant Rating Management System

This repository contains a Python solution for managing restaurant ratings. The solution comprises three classes: Customer, Restaurant, and Review, each implemented in separate files within the models folder.

### Functionality Overview:

#### Seed Database:

The seed_database() function initializes the database by creating necessary tables and populating them with sample data. It performs the following steps:

- Drops existing tables for Customer, Review, and Restaurant.
- Creates new tables for Customer, Review, and Restaurant.
  Seeds the database with sample data including customers, restaurants, and reviews.
- Displays information about customers, restaurants, and reviews for testing purposes.

#### Models:

1. Customer:

- Represents a customer with attributes such as first name and last name.
- Provides methods for creating a new customer, retrieving customer's reviews, favorite restaurant, full name, and more.

2. Restaurant:
- Represents a restaurant with attributes such as name and average rating.
- Provides methods for creating a new restaurant, retrieving all reviews for a restaurant, finding the fanciest restaurant, and more.

3. Review:
- Represents a review given by a customer to a restaurant.
- Provides methods for creating a new review, retrieving the associated customer and restaurant information, and displaying a full review.

#### How to Run:

To run the application, execute `python main.py `in your terminal. This will seed the database with sample data and display various information about customers, restaurants, and reviews.

#### Dependencies:
This solution utilizes SQLite for database management.
Ensure you have Python 3 installed on your system aswell.
