from models.__init__ import CURSOR, CONNECTION
import re
pattern = r'^[a-zA-Z]+$'

class Customer:

    def __init__(self, first_name, last_name, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self,value):
        if re.match(pattern,value) and len(value):
            self._first_name = value
        else:
            raise ValueError("should be a non-empty string with letters only")

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self,value):
        if re.match(pattern,value) and len(value):
            self._last_name = value
        else:
            raise ValueError("should be a non-empty string with letters only")

    @classmethod
    def create_table(cls):
        CURSOR.execute(
            """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        """
        )
        CONNECTION.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """DROP TABLE IF EXISTS customers
        """
        )
        CONNECTION.commit()

    def save(self):
        CURSOR.execute(
            """INSERT INTO customers (first_name,last_name)
        VALUES (?, ?)
        """,
            (self.first_name, self.last_name),
        )
        CONNECTION.commit()
        self.id = CURSOR.lastrowid

    def update(self):
        CURSOR.execute(
            """UPDATE customers
        SET first_name = ?,last_name = ? WHERE id = ?
        """,
            (self.first_name, self.last_name, self.id),
        )
        CONNECTION.commit()
    def delete(self):
        CURSOR.execute("""DELETE FROM customers WHERE id = ?""",(self.id,))
        CONNECTION.commit()

    @classmethod
    def create(cls,first_name,last_name):
        customer = cls(first_name,last_name)
        customer.save()        
        return customer
    print("Created Customer Succesfully")

    def reviews(self):
        reviews = CURSOR.execute(
        """SELECT * FROM reviews WHERE customer_id =?
        """,(self.id,)          
        ).fetchall()
        for review in reviews:
            print(review)
    
    def restaurants(self):
        restaurants = CURSOR.execute(
        """SELECT DISTINCT restaurants.*
            FROM restaurants
            INNER JOIN reviews
            ON restaurants.id == reviews.restaurant_id
            WHERE reviews.customer_id = ?
        """,(self.id,)           
        ).fetchall()

        for restaurant in restaurants:
            print(restaurant)

    def full_names(self):
        full_name = CURSOR.execute(
        """SELECT customers.first_name ||" "||customers.last_name AS full_names
        FROM customers WHERE id = ?
        """,(self.id,)         
        ).fetchone()
        print(full_name)

    def favourite_restaurant(self):
        fave_restaurant = CURSOR.execute(
        """SELECT restaurants.* , reviews.star_rating FROM restaurants
        INNER JOIN reviews 
        ON restaurants.id == reviews.restaurant_id
        WHERE reviews.star_rating = (SELECT MAX(star_rating) FROM reviews)
        AND
        reviews.customer_id = ?
        """,(self.id,)           
        ).fetchall()
        for fave in fave_restaurant:
            print(fave)

    def add_review(self,restaurant,rating):
        restaurant_id = restaurant.id
        CURSOR.execute(
        """INSERT INTO reviews (restaurant_id,customer_id,star_rating)
        VALUES (?, ?, ?)
        """,(restaurant_id,self.id,rating) 
        )
        CONNECTION.commit()
        new_review_id = CURSOR.lastrowid
        new_review = (new_review_id, restaurant_id,self.id,rating)
        print(new_review)

    def delete_reviews(self,restaurant):
        try:
            CURSOR.execute(
            """DELETE FROM reviews WHERE reviews.restaurant_id = ?
            """,(restaurant.id,)
            )
            CONNECTION.commit()
            print(f"Deleted {restaurant.name}'s  reviews succesfully")
        except:
            print("Deletion Unsuccesfull")