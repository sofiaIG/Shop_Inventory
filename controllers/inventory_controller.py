from flask import Flask, render_template
from repositories import plant_repository

from flask import Blueprint

inventory_blueprint = Blueprint("inventory", __name__)


@inventory_blueprint.route("/inventory")
def inventory():
    inventory = plant_repository.select_all()
    return render_template("inventory/index.html", inventory = inventory)