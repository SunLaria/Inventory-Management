import sqlite3
def query(sql):
    with  sqlite3.connect("database.db") as conn:
        cur = conn.cursor()
        return cur.execute(sql)

# print(tuple(query(f'SELECT * FROM products WHERE id LIKE 1'))[0])

def create_database():
    query("CREATE TABLE IF NOT EXISTS products (id INTEGER, name TEXT, quantity INTEGER, category TEXT, availability TEXT, price INTEGER)")
    query("CREATE TABLE IF NOT EXISTS purchases (id INTEGER, products TEXT, quantity TEXT, buyer TEXT, date TEXT, price INTEGER)")
    query("CREATE TABLE IF NOT EXISTS listings (id INTEGER, products TEXT, quantity TEXT, buyer TEXT, availability TEXT, price INTEGER)")

def add_row(table_name,datadict):
    query(f"INSERT INTO {table_name} VALUES {tuple(datadict.values())}")
    return print('completed')


def load(table_name):
        data = query(f"SELECT * FROM {table_name}") 
        return [dict(zip([name[0] for name in data.description],i)) for i in data]

def delete(table_name,idd):
     for i in idd:
        query(f'DELETE FROM {table_name} WHERE id = {i}')
     return print('deleted')

def search(table_name,idd):
    try:
        data = [query(f"SELECT * FROM {table_name} WHERE id LIKE {z}") for z in str(idd).split(",")]
        return [[dict(zip([name[0] for name in i.description],z)) for z in i][0] for i in data]
    except:
         return []


def update_quantity(table_name,id,quantity):
    query(f"UPDATE {table_name} SET quantity = {quantity} WHERE id LIKE {id}")
    return print("updated")