from db.run_sql import run_sql

from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository



def save(manufacturer):
    sql = "INSERT INTO manufacturers (name) VALUES (%s) RETURNING *"
    values = [manufacturer.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer
