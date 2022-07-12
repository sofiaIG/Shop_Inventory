from db.run_sql import run_sql
from models.shipping_company import Shipping_Company


def save(shipping_company):
    sql = "INSERT INTO shipping_companies (name) VALUES (%s) RETURNING *"
    values = [shipping_company.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    shipping_company.id = id
    return shipping_company


def delete_all():
    sql = "DELETE FROM shipping_companies"
    run_sql(sql)


def select_first():
    ship_companies = []
    sql = "SELECT * FROM shipping_companies"
    result = run_sql(sql)

    for row in result:
        shipping_company = Shipping_Company(row["name"], row["id"])
        ship_companies.append(shipping_company)
    return ship_companies[0]
