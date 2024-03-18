#!/usr/bin/env python3
# import sqlite3
from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review
from models.__init__ import CONNECTION, CURSOR


def seed_database():
    # Table creations
    Customer.drop_table()
    Review.drop_table()
    Restaurant.drop_table()

    Customer.create_table()
    Restaurant.create_table()
    Review.create_table()

    # Seeding the database
    customer_one = Customer.create("Brian", "Kiprono")
    shamiro = Customer.create("Allen", "Shamiro")
    Customer.create("Clare", "Oparo")
    Customer.create("Anne", "Shiko")
    Customer.create("Mariam", "Senzia")
    Customer.create("Dan", "Muchiri")

    meridian = Restaurant.create("Meridian hotel", 80000)
    movenpick = Restaurant.create("Movenpick hotel", 100000)
    villarossa = Restaurant.create("Villa Rosa Kempinski", 280000)
    Restaurant.create("Radisson Blu hotel", 120000)
    Restaurant.create("Radisson Blu hotel", 120000)
    Restaurant.create("Tamarind Tree hotel", 60000)

    brians_meridian_review = Review.create(meridian.id, customer_one.id, 4)
    brians_movenpick_review = Review.create(movenpick.id, customer_one.id, 5)
    shamiros_review = Review.create(movenpick.id, shamiro.id, 3)

    print("Seeded Database Sucessfully")

    print("*****Reviews from customers for restaurants******")
    print(shamiros_review.customer())
    print(shamiros_review.restaurant())

    print(f"*****{movenpick.name}'s customers*****")
    # print(movenpick.customers())
    movenpick.customers()

    print("*****Restaurant Reviews****")
    meridian.reviews()

    print("******Customers review*******")
    customer_one.reviews()

    print(f">>>>>>{customer_one.first_name.upper()}'S RESTAURANTS<<<<")
    customer_one.restaurants()

    print(f">>>>>>{customer_one.first_name.upper()}'S FAVOURITE RESTAURANT<<<<")
    customer_one.favourite_restaurant()

    print(f">>>>>Customer's full names <<<<<<<")
    customer_one.full_names()

    print(">>>>>>Added review<<<<")
    customer_one.add_review(villarossa, 5)

    # customer_one.delete_reviews(movenpick)

    brians_meridian_review.full_review()

    print(">>>> The most fanciest restaurants <<<<")
    Restaurant.fanciest()

    Restaurant.all_reviews()


if __name__ == "__main__":

    try:
        seed_database()
    except ValueError as error:
        print(error)
