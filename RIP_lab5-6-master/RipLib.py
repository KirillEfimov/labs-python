class User:
    def __init__(self, db_connection, first_name, last_name, phone=None):
        self.db_connection = db_connection.connection
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO users (first_name, last_name, phone) VALUES (%s, %s, %s);",
                  (self.first_name, self.last_name, self.phone))
        self.db_connection.commit()
        c.close()

class Plane:
    def __init__(self, db_connection, name,number,description=None):
        self.db_connection = db_connection.connection
        self.name = name
        self.number = number
        self.description = description

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO planes (name, number, description) VALUES (%s, %s, %s);",
                  (self.name, self.number, self.description))
        self.db_connection.commit()
        c.close()


class Booking:
    def __init__(self, db_connection, user_id,plane_id,price,departure_date):
        self.db_connection = db_connection.connection
        self.user_id = user_id
        self.plane_id = plane_id
        self.price = price
        self.departure_date = departure_date
        

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO bookings (user_id, plane_id, price, departure_date) VALUES (%d, %d, %d, %s);",
                  (self.user_id, self.plane_id, self.price, self.departure_date))
        self.db_connection.commit()
        c.close()
