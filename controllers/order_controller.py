from flask import Flask, make_response, render_template, request, redirect
from models.customer import Customer
from models.shipment import Shipment
from models.shipping_company import Shipping_Company
from repositories import order_repository
from flask import Blueprint
from models.order import Order
from repositories import plant_repository
from repositories import customer_repository
from datetime import datetime, timedelta
from repositories import shipping_company_repository
from repositories import shipment_repository


order_blueprint = Blueprint("order", __name__)

@order_blueprint.route("/orders",  methods=['POST'])
def create_order():
    try:
        request_data = request.get_json()
        plant_id = request_data['plantId']
        quantity = request_data['quantity']
        customer_address= request_data['customerAddress']
        customer_name = request_data['customerName']
        order_number = request_data['orderNumber']
    except:
        return 'Fields (plantId, quantity, customerAddress, customerName, orderNumber) not specified', 400

    plant = plant_repository.select(plant_id)
    customer = Customer(customer_name, customer_address)
    customer_repository.save(customer)
    time = datetime.now().isoformat()
    order = Order(time, plant_id, quantity, customer.id, order_number)
    plant.stock_quantity -= quantity
    plant_repository.update(plant)
    order_repository.save(order)
    shipping_date = datetime.now() + timedelta(days=2)
    shipping_company_id = shipping_company_repository.select_first().id
    shipment = Shipment(order.id, shipping_date, shipping_company_id )
    shipment_repository.save(shipment)
    return 'Order placed', 200
