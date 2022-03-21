import pdb
from models.plant import Plant
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.plant_repository as plant_repository

manufacturer = Manufacturer('Plants Limited')
manufacturer_repository.save(manufacturer)
manufacturers = manufacturer_repository.select_all()
manufacturer_repository.delete() 




for manufacturer in manufacturers:
    print(manufacturer.__dict__) 
# Line above shows that the id is None. Needs to be looked at.



pdb.set_trace()