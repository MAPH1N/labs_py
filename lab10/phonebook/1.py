# Design tables for PhoneBook
import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='suppliers',
    user='postgres',
    password='1234'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE phonebook(
        id INTEGER PRIMARY KEY,
        username VARCHAR(20),
        number VARCHAR(12),
        email VARCHAR(30)
    )
    '''
)

config.commit()
current.close()
config.close()