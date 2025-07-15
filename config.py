SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
SECRET_KEY = "UYDGSYUFGCDEDVFVTY22FT56354341GBBVUYGr@##@werfV"

ADMIN_USERNAME = "fariba"
ADMIN_PASSWORD = "1234"

PAYMENT_MERCHANT = 'sandbox'
PAYMENT_CALLBACK = 'http://127.0.0.1:5000/verify'
PAYMENT_FIRST_REQUEST_URL = 'https://sandbox.shepa.com/api/v1/token'
PAYMENT_VERIFY_REQUEST_URL = 'https://sandbox.shepa.com/api/v1/verify'