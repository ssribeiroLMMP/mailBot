#!./env/bin/python3
## Importing Own Libraries
from mail.utils import EmailServer
## Importing Third Party Libraries
import os

def main():
    


# # from flask_sqlalchemy import SQLAlchemy
# # from flask_mail import Mail

# # Setting app Variable
# # app = Flask(__name__)
# # app.debug = True

# # Set Secret Key
# # app.config['SECRET_KEY'] = '70fa112fb94e2d107151092d028d11f3'
# # import secrets
# # secrets.token_hex(26)

# # Database - SQLAlchemy API
# # Data structures are classes in python
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/webSite.db'
# # db = SQLAlchemy(app)


# # Main Configuration
# # app.config['MAIL_SERVER']='smtp.gmail.com'
# # app.config['MAIL_PORT'] = 465
# # app.config['MAIL_USERNAME'] = 'ssribeiro@gmail.com'
# # app.config['MAIL_PASSWORD'] = 'xqhvvrfheeybhrfx'
# # app.config['MAIL_USE_TLS'] = False
# # app.config['MAIL_USE_SSL'] = True

# # Instanciate Mail Object
# # mail = Mail(app)

# # Importing own Package Libraries
# # from app.mail import mailBP

# # app.register_blueprint(mailBP)
# # app.register_blueprint(posts)

# # # Use os.getenv("key") to get environment variables
# # app_name = os.environ.get("APP_NAME")

# # Connect to Database
# conn = sqlite3.connect(DATABASE_CONN)

# c = conn.cursor()
# try:
#     c.execute("""CREATE TABLE clients (
#             cpf text PRIMARY KEY,
#             name text,
#             email text,
#             mobile text,
#             address blob)""")

#     c.execute("""CREATE TABLE orders (
#             number integer PRIMARY KEY,
#             dateTime integer,
#             clientid integer references clients(cpf),
#             shipmentType text,
#             shipmentPrice text,
#             subtotal real)""")

#     c.execute("""CREATE TABLE orderItems (
#                 orderNumber integer references orders(number),
#                 id text,
#                 description blob,
#                 quantity integer,
#                 price real,
#                 UNIQUE(orderNumber,id))""")
                
# except:
#     pass

# c.close()    
