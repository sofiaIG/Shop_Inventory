import pdb
from models.plant import Plant
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.plant_repository as plant_repository

plant_repository.delete_all()
manufacturer_repository.delete_all()
manufacturer = Manufacturer('Plants Limited')
manufacturer_repository.save(manufacturer)
plant = Plant("Wallace", "Monkey face plant; Monkey plant; Mini Swiss cheese plant", 2.55, 5, manufacturer, 2)
plant_repository.save(plant)


plant_2 = Plant("Pachira Aquatica", "Make sure they have enough space -\
    this plant can grow up to 2 metres tall! They’ll have to be pretty attentive too -\
        so it can grow evenly, it needs to be turned each time it’s watered.", 10, 32, manufacturer, 5)
plant_3 = Plant("Lionel", "Citrus calamondin", 12, 30, manufacturer, 0)
plant_repository.save(plant_2)
plant_repository.save(plant_3)
plants = plant_repository.select_all()
manufacturer_repository.select_all()


for plant in plants:
    print(plant.__dict__) 
# Line above shows that the id is None. Needs to be looked at.



pdb.set_trace()