from db.run_sql import run_sql
from models.manufacturer import Manufacturer


def save(manufacturer):
    sql = "INSERT INTO manufacturers (name) VALUES (%s) RETURNING *"
    values = [manufacturer.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer


def select_all():
    manufacturers = []
    sql = "SELECT * FROM manufacturers"
    result = run_sql(sql)
    
    for row in result:
        manufacturer = Manufacturer(row['name'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers


def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        manufacturer = Manufacturer(result['name'], result['id'])
    return manufacturer


    
def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def update(manufacturer):
    sql = "UPDATE manufacturers SET name = %s WHERE id = %s"
    values = [manufacturer.name, manufacturer.id]
    run_sql(sql, values)



