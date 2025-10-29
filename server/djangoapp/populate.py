from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make = CarMake.objects.create(
            name=data["name"],
            description=data["description"]
        )
        car_make_instances.append(car_make)

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        # Add other car models similarly
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            type=data["type"],
            year=data["year"],
            car_make=data["car_make"],
            dealer_id=data["dealer_id"]
        )