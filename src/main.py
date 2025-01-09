from fastapi import FastAPI
from models.food import Food
from pydantic import BaseModel

app = FastAPI()
rice = Food(1, "Rice", True, 1, 206, 0.4, 0.1, None, 0, 0.0016, 45, 0.6, 0.1, 0, 4.3, 0, 0.016, 0.0003, 0.0553)
white_sugar = Food(2, "White Sugar", True, 0.0625, 49, 0, 0, None, 0, 0.001, 13, 0, 13, 0, 0, 0, 0.0001, 0, 0.0003)
chicken = Food(3, "Chicken", False, 8.4, 19, 1.1, 0.3, None, 0.0079, 0.006, 0, 0, None, None, 2, None, 0.0011, 0.0001, 0.0172)
list_of_foods = [rice, white_sugar, chicken]


@app.get("/foods/")
async def get_all_foods():
    return [food_item.to_dict() for food_item in list_of_foods]

@app.get("/foods/{id}")
async def get_food(id: int):
    return [food_item.to_dict() for food_item in list_of_foods]

# @app.post("/foods/")

# @app.put("/foods/{id}")

# @app.delete("/foods/{id}")