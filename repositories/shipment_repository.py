from db.run_sql import run_sql


def save(shipment):
    sql = "INSERT INTO shipments (order_id, shipping_date, shipping_company_id) VALUES (%s, %s, %s) RETURNING *"
    values = [shipment.order_id, shipment.shipping_date, shipment.shipping_company_id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    shipment.id = id
    return shipment


def delete_all():
    sql = "DELETE FROM shipments"
    run_sql(sql)
