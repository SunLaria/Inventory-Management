import sqlite3
def query(sql):
    with  sqlite3.connect("database.db") as conn:
        cur = conn.cursor()
        return cur.execute(sql)

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

def delete(table_name,id):
     query(f'DELETE FROM {table_name} WHERE id = {id}')
     return print('deleted')

def search(table_name,idd):
    if len(idd) == 1:
        data = query(f"SELECT * FROM {table_name} WHERE id LIKE {idd}") 
        return [dict(zip([name[0] for name in data[0].description],i)) for i in data]
    else:
         data = [query(f"SELECT * FROM {table_name} WHERE id LIKE {i}") for i in idd]
         return [dict(zip([name[0] for name in data[0].description],i)) for i in data]

         
              
              

def update_quantity(table_name,id,quantity):
    query(f"UPDATE {table_name} SET quantity = {quantity} WHERE id LIKE {id}")
    return print("updated")