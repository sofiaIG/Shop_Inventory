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
    sql = "DELETE FROM plants WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM plants"
    run_sql(sql)

def update(plant):
    sql = "UPDATE plants SET (name, description, buying_cost, \
        selling_price, manufacturer_id, stock_quantity) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [plant.name, plant.description, plant.buying_cost, plant.selling_price,\
        plant.manufacturer.id, plant.stock_quantity, plant.id]
    run_sql(sql, values)

