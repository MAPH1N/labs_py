#Implement deleting data from tables by username of phone
import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='1234'
)

name = input('Enter a name to delete it:\n')
name = name.lower()

current = config.cursor()

sql1 = f'''
 DELETE FROM phonebook WHERE username='{name}';
'''

current.execute(sql1)

current.close()
config.commit()
config.close()