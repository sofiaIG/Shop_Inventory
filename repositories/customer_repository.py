from db.run_sql import run_sql


def save(customer):
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s) RETURNING *"
    values = [customer.name, customer.address]
    results = run_sql(sql, values)
    id = results[0]["id"]
    customer.id = id
    return customer


def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)
