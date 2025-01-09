
class Food():
    def __init__(
                 self,
                 id: int,
                 name: str, 
                 mass_by_vol: bool,
                 serv_size_cup_or_gram: float,
                 calories: float, 
                 total_fat: float | None = None, 
                 saturated_fat: float | None = None, 
                 trans_fat: float | None = None, 
                 colestrol: float | None = None, 
                 sodium: float | None = None, 
                 total_carbohydrate: float | None = None,
                 dietary_fiber: float | None = None,
                 total_sugars: float | None = None,
                 added_sugar: float | None = None,
                 protein:float | None = None,
                 vitamin_d: float | None = None,
                 calcium: float | None = None,
                 iron: float | None = None,
                 potassium: float | None = None):
        self.id = id
        self.name = name
        self.mass_by_vol = mass_by_vol
        self.serv_size_cup_or_gram= serv_size_cup_or_gram
        self.calories = calories
        self.total_fat = total_fat
        self.saturated_fat = saturated_fat
        self.trans_fat = trans_fat
        self.colestrol = colestrol
        self.sodium = sodium
        self.total_carbohydrate = total_carbohydrate
        self.dietary_fiber = dietary_fiber
        self.total_sugars = total_sugars
        self.added_sugar = added_sugar
        self.protein = protein
        self.vitamin_d = vitamin_d
        self.calcium = calcium
        self.iron = iron
        self.potassium = potassium

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "massByVol": self.mass_by_vol,
            "servSizeCupOrGram": self.serv_size_cup_or_gram,
            "calories": self.calories,
            "totalFat": self.total_fat,
            "saturatedFat": self.saturated_fat,
            "transFat": self.trans_fat,
            "colestrol": self.colestrol,
            "sodium": self.sodium,
            "totalCarbohydrate": self.total_carbohydrate,
            "dietaryFiber": self.dietary_fiber,
            "totalSugars": self.total_sugars,
            "addedSugar": self.added_sugar,
            "protein": self.protein,
            "vitaminD": self.vitamin_d,
            "calcium": self.calcium,
            "iron": self.iron,
            "potassium": self.potassium,
        }