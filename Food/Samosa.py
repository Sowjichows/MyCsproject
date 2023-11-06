from Food.food import Food

class Samosa(Food):
    def __init__(self, item, famous_place, calories, quantity, quality):
        super().__init__(item, famous_place, calories, quantity)
        self.quality = quality

    def category(self):
         return f"It is a best snack item"

    def price(self):
         return f"It costs around $15"
