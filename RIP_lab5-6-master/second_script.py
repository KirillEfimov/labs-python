from Connection import Connection
from RipLib import User, Plane, Booking

con = Connection("dbuser", "123456", "rip_course_db")

with con:
    user = User(con, 'Петр', 'Петров')
    user.save()
