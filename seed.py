# #!/usr/bin/env python3
# from models.customer import Customer
# from models.restaurant import Restaurant
# from models.review import Review
# from models.__init__ import CONNECTION, CURSOR

# def seed_database():
#     # Table creations
#     Customer.drop_table()
#     Review.drop_table()
#     Restaurant.drop_table()

#     Customer.create_table()
#     Restaurant.create_table()
#     Review.create_table()

#     # Seeding the database
#     # customer_one = Customer.create("Brian", "Kiprono")
#     # shamiro = Customer.create("Allen", "Shamiro")
#     Customer.create("Clare", "Oparo")
#     Customer.create("Anne", "Shiko")
#     Customer.create("Mariam", "Senzia")
#     Customer.create("Dan", "Muchiri")

#     # meridian = Restaurant.create("Meridian hotel", 80000)
#     # movenpick = Restaurant.create("Movenpick hotel", 100000)
#     # villarossa = Restaurant.create("Villa Rosa Kempinski", 280000)
#     Restaurant.create("Radisson Blu hotel", 120000)
#     Restaurant.create("Tamarind Tree hotel", 60000)

#     # brians_meridian_review = Review.create(meridian.id, customer_one.id, 4)
#     # brians_movenpick_review = Review.create(movenpick.id, customer_one.id, 5)
#     # shamiros_review = Review.create(movenpick.id, shamiro.id, 3)

#     print("Seeded Database Successfully")

# if __name__ == "__main__":
#     seed_database()
