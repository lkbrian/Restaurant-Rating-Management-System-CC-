from models.__init__ import CONNECTION, CURSOR
from models.customer import Customer
from models.restaurant import Restaurant


class Review:
    def __init__(self, restaurant_id, customer_id, star_rating, id=None):
        self.id = id
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.star_rating = star_rating

    @property
    def star_rating(self):
        return self._star_rating

    @star_rating.setter
    def star_rating(self, value):
        if isinstance(value, int) and 0 <= value <= 5:
            self._star_rating = value
        else:
            raise ValueError("Invalid Rate, Rates fall between  0 and 5")

    @property
    def restaurant_id(self):
        return self._restaurant_id

    @restaurant_id.setter
    def restaurant_id(self, value):
        id_ = CURSOR.execute(
            "SELECT id FROM restaurants WHERE id = ?", (value,)
        ).fetchone()
        if id_:
            self._restaurant_id = value
        else:
            raise ValueError("customer_id must reference a customer in the database")

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        id_ = CURSOR.execute(
            "SELECT id FROM customers WHERE id = ?", (value,)
        ).fetchone()
        if id_:
            self._customer_id = value
        else:
            raise ValueError(
                "restaurant_id must reference a restaurant in the database"
            )

    @classmethod
    def create_table(cls):
        CURSOR.execute(
            """
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY,
                restaurant_id INTEGER ,
                customer_id INTEGER,
                star_rating INTEGER,
                FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
                FOREIGN KEY (customer_id) REFERENCES customers(id),
                UNIQUE(restaurant_id,customer_id) 
                -- Ensure uniqueness of (restaurant_id, customer_id) combination
            )
        """
        )
        CONNECTION.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """DROP TABLE IF EXISTS reviews
        """
        )
        CONNECTION.commit()

    def save(self):
        CURSOR.execute(
            """INSERT INTO reviews(restaurant_id,customer_id,star_rating)
            VALUES (?, ?, ?)
        """,
            (self.restaurant_id, self.customer_id, self.star_rating),
        )
        CONNECTION.commit()
        self.id = CURSOR.lastrowid

    def delete(self):
        CURSOR.execute(
            """DELETE FROM reviews WHERE id = ?
        """,
            (self.id),
        )
        CONNECTION.commit()

    @classmethod
    def create(cls, restaurant_id, customer_id, star_rating):
        review = cls(restaurant_id, customer_id, star_rating)
        review.save()
        print("Reviewed Succesfully")
        return review

    def customer(self):
        customer = CURSOR.execute(
            "SELECT * FROM customers WHERE id = ?", (self.customer_id,)
        ).fetchone()
        return customer

    def restaurant(self):
        restaurant = CURSOR.execute(
            """SELECT * FROM restaurants WHERE id = ?
        """,
            (self.restaurant_id,)
        ).fetchone()
        return restaurant
    
    def full_review(self):
        full_reviews = CURSOR.execute(
        """ SELECT restaurants.name AS restaurant,
            customers.first_name ||" "||customers.last_name AS fullnames,
            reviews.star_rating AS rating
            FROM reviews
            INNER JOIN restaurants ON restaurants.id == reviews.restaurant_id
            INNER JOIN customers ON customers.id == reviews.customer_id
        """            
        ).fetchall()
        print(">>>>>>Full review<<<<<<")
        for full_review in full_reviews:
            restaurant,fullnames,rating = full_review
            print(f"Review for {restaurant} by {fullnames}: {rating} stars")
