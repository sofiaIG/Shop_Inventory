from db.run_sql import run_sql
from models.manufacturer import Manufacturer

from models.plant import Plant

import repositories.plant_repository as plant_repository
import repositories.manufacturer_repository as manufacturer_repository



def save(plant):
    sql = "INSERT INTO plants (name, description, stock_quantity, buying_cost,\
    selling_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    stock_quantity = plant.stock_quantity_sum()
    values = [plant.name, plant.description, stock_quantity,\
         plant.buying_cost, plant.selling_price, plant.manufacturer.id]
    results = run_sql(sql, values)
    print(results)
    id = results[0]['id']
    plant.id = id
    return plant


# def select_all():
#     plants = []
#     sql = "SELECT * FROM plants"
#     result = run_sql(sql)
    
#     for row in result:
#         plant = Plant(row['name'], row['description'], row['buying_cost'],
#         row['selling_price'], row['manufacturer'])
#         plants.append(plant)
#     return plants


# def select(id):
#     plant = None
#     sql = "SELECT * FROM plants WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     if result is not None:
#         plant = Plant(result['name'], result['description'], result['buying_cost'], result['selling_price'],
#         result['manufacturer'])
#     return plant
    
# def delete(id):
#     sql = "DELETE FROM plants WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)
    
# def delete_all():
#     sql = "DELETE FROM plants"
#     run_sql(sql)

# def update(plant):
#     sql = "UPDATE plants SET (name, description, buying_cost, selling_price, manufacturer)\
#     = (%s, %s, %s, %s, %s) WHERE id = %s"
#     values = [plant.name, plant.description, plant.buying_cost, plant.selling_price,\
#         plant.manufacturer.id]
#     run_sql(sql, values)

