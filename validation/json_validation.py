    
def json_validation(customer_address, customer_name, quantity, plant_id, order_number, plant):
        if type(customer_address) != str or len(customer_address) < 5:
            return "customerAddress needs to be a string longer than 5", 400
    
        if type(customer_name) != str or len(customer_name) < 1:
            return "customerName needs to be a string longer than 1", 400

        if type(quantity) != int or quantity < 1:
            return "quantity needs to be an int greater than 1", 400

        if type(plant_id) != int or plant_id < 1:
             return "plantId needs to be an int greater than 1", 400

        if type(order_number) != str or len(order_number) < 1:
            return "orderNumber needs to be a string longer than 1", 400

        if plant == None:
            return "plantId not found", 400 # maybe 404?
        
        if  plant.stock_quantity < quantity:
            return 'not enough stock to complete the order', 400