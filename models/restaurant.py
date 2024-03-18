from models.__init__ import CONNECTION, CURSOR
import sqlite3


class Restaurant:
    def __init__(self, name, price, id=None):
        self.id = id
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value):
            self._name = value
        else:
            raise ValueError("the name should be a non-empty string")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, int) and value > 0:
            self._price = value
        else:
            raise ValueError("invalid type")

    @classmethod
    def create_table(cls):
        CURSOR.execute(
            """CREATE TABLE IF NOT EXISTS restaurants(
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,   
                price INTEGER NOT NULL
            )
        """
        )
        CONNECTION.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """DROP TABLE IF EXISTS restaurants
        """
        )
        CONNECTION.commit()

    def save(self):
        CURSOR.execute(
            """INSERT INTO restaurants(name,price)
        VALUES (?, ?)
        """,
            (self.name, self.price),
        )
        CONNECTION.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, price):
        try:
            restaurant = cls(name, price)
            restaurant.save()
            return restaurant
        except sqlite3.IntegrityError:
            print("restaurant already exists")
    

    print("Created Restaurant Succesfully")

    def customers(self):
        customers = CURSOR.execute(
            """SELECT DISTINCT customers.* 
            FROM customers
            INNER JOIN reviews 
            ON customers.id == reviews.customer_id
            WHERE reviews.restaurant_id = ?
        """,
            (self.id,),
        ).fetchall()

        for customer in customers:
            print(customer) 

    def reviews(self):
        reviews = CURSOR.execute(
        """SELECT * FROM reviews WHERE restaurant_id = ?
        """,(self.id,)         
        ).fetchall()
        for review in reviews:
            print(review)

    @classmethod
    def fanciest(cls):
        fanciest = CURSOR.execute(
        """SELECT * FROM restaurants 
        WHERE restaurants.price = (SELECT MAX(price) FROM restaurants)
        """            
        ).fetchone()
        print(fanciest)

    @classmethod
    def all_reviews(cls):
        all_reviews = CURSOR.execute(
         """ SELECT restaurants.name AS restaurant,
            customers.first_name ||" "||customers.last_name AS fullnames,
            reviews.star_rating AS rating
            FROM reviews
            INNER JOIN restaurants ON restaurants.id == reviews.restaurant_id
            INNER JOIN customers ON customers.id == reviews.customer_id
        """             
        ).fetchall()
        print(">>>>>>Full review<<<<<<")
        for reviews in all_reviews:
            restaurant,fullnames,rating = reviews
            print(f"Review for {restaurant} by {fullnames}: {rating} stars")