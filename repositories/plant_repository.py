from db.run_sql import run_sql

from models.plant import Plant

import repositories.plant_repository as plant_repository



def save(plant):
    sql = "INSERT INTO plant (name, description, stock_quantity, buying_cost,\
    selling_price, manufacturers_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    stock_quantity = plant.stock_quantity_sum()
    values = [plant.name, plant.description,\
        stock_quantity, plant.buying_cost, plant.selling_price, plant.manufacturers_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    plant.id = id
    return plant

