from flask import Flask, render_template, request, redirect
from repositories import manufacturer_repository
from flask import Blueprint
from models.manufacturer import Manufacturer

inventory_blueprint = Blueprint("manufacturers", __name__)


@inventory_blueprint.route("/manufacturers")
def manufacturer():
    manufacturer = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturer = manufacturer)

@inventory_blueprint.route("manufacturers/new", methods=['GET'])
def new_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    print(manufacturers)
    return render_template("manufacturers/new.html", manufacturers = manufacturers)


@inventory_blueprint.route("/manufacturers",  methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    manufacturer = Manufacturer(name)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')


@inventory_blueprint.route("/manufacturers/<id>", methods=['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/show.html', manufacturer = manufacturer)


@inventory_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_plant(id):
    manufacturer = manufacturer_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('inventory/edit.html', manufacturer = manufacturer, manufacturers = manufacturers)



@inventory_blueprint.route("/inventory/<id>", methods=['POST'])
def update_plant(id):
    name = request.form['name']
    manufacturer = Manufacturer(name)
    manufacturer_repository.update(manufacturer)
    return redirect('/inventory')

