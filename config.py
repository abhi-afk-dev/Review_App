import urllib.parse

class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Abhi2003@'
    MYSQL_DB = 'school_reviews_db'
    MYSQL_PORT = 3306
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{urllib.parse.quote_plus(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '22627d6cf6db49c4341e6d17dd685ebe0b278f35db589b75'
