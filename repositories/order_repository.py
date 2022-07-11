from db.run_sql import run_sql
from models.order import Order


def save(order):
    sql = "INSERT INTO orders (order_date, customer_id,\
        plant_id, quantity, order_number) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [
        order.order_date,
        order.customer_id,
        order.plant_id,
        order.quantity,
        order.order_number,
    ]
    results = run_sql(sql, values)

    print(results)

    id = results[0]["id"]
    order.id = id
    return order


def delete_all():
    sql = "DELETE FROM orders"
    run_sql(sql)
