import pdb
from models.plant import Plant
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.plant_repository as plant_repository

manufacturer = Manufacturer('Plants Limited')
id = manufacturer_repository.save(manufacturer)
print(id)

plant = Plant("Wallace", "Monkey face plant; Monkey plant; Mini Swiss cheese plant",
        2.55, 5, manufacturer)


plant_repository.save(plant)
print('statement below')
plants = plant_repository.select_all()
for plant in plants:
    print(plant.__dict__)




pdb.set_trace()