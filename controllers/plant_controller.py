from flask import Flask, render_template, request, redirect
from repositories import plant_repository
from repositories import manufacturer_repository
from flask import Blueprint
from models.plant import Plant

inventory_blueprint = Blueprint("inventory", __name__)


@inventory_blueprint.route("/inventory")
# This one works
def inventory():
    inventory = plant_repository.select_all()
    return render_template("inventory/index.html", inventory = inventory)

@inventory_blueprint.route("/inventory/new", methods=['GET'])
def new_plant():
    manufacturers = manufacturer_repository.select_all()
    print(manufacturers)
    return render_template("inventory/new.html", all_manufacturers = manufacturers)


@inventory_blueprint.route("/inventory",  methods=['POST'])
def create_plant():
    name = request.form['name']
    description= request.form['description']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer_id = request.form["manufacturer_id"]
    stock_quantity = request.form['stock_quantity']
    manufacturer_object = manufacturer_repository.select(manufacturer_id)
    plant = Plant(name, description, buying_cost, selling_price, manufacturer_object, stock_quantity)
    plant_repository.save(plant)
    return redirect('/inventory')


@inventory_blueprint.route("/inventory/<id>", methods=['GET'])
def show_inventory_plant(id):
    plant = plant_repository.select(id)
    return render_template('inventory/index.html', plant = plant)


@inventory_blueprint.route("/inventory/<id>/edit", methods=['GET'])
def edit_plant(id):
    plant = plant_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('inventory/edit.html', plant = plant, manufacturers = manufacturers)



@inventory_blueprint.route("/inventory/<id>", methods=['POST'])
def update_plant(id):
    name = request.form['name']
    description= request.form['description']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer_id  = manufacturer_repository.select(request.form[''])
    stock_quantity = request.form['stock_quantity']
    plant = Plant(name, description, buying_cost, selling_price, manufacturer_id, stock_quantity, id)
    plant_repository.update(plant)
    return redirect('/inventory')

