import sqlite3

CONNECTION = sqlite3.connect('Rating_management_system.db')
CURSOR = CONNECTION.cursor()

# from .restaurant import Restaurant
# from .customer import Customer
# from .review import Review