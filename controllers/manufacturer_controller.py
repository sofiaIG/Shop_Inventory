from flask import Flask, render_template, request, redirect
from repositories import manufacturer_repository
from flask import Blueprint
from models.manufacturer import Manufacturer

manufacturer_blueprint = Blueprint("manufacturers", __name__)


@manufacturer_blueprint.route("/manufacturers")
def manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers = manufacturers)

@manufacturer_blueprint.route("/manufacturers/new", methods=['GET'])
def new_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/new.html", manufacturers = manufacturers)


@manufacturer_blueprint.route("/manufacturers",  methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    manufacturer = Manufacturer(name)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')


@manufacturer_blueprint.route("/manufacturers/<id>", methods=['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/show.html', manufacturer = manufacturer)


@manufacturer_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/edit.html', manufacturer = manufacturer, manufacturers = manufacturers)



@manufacturer_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturer(id):
    manufacturer_object = manufacturer_repository.select(id)
    manufacturer_object.name = request.form['name']
    print(manufacturer_object.name)
    print(id)
    print(manufacturer_object.id)   
    manufacturer_repository.update(manufacturer_object)
    return redirect('/manufacturers')


