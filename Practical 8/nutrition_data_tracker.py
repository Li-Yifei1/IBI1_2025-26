class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

    def __str__(self):
        return f"{self.name}: {self.calories} kcal, {self.protein}g protein, {self.carbs}g carbs, {self.fat}g fat"

def calculate_daily_nutrition(food_list):
    total_cal = 0.0
    total_pro = 0.0
    total_carbs = 0.0
    total_fat = 0.0

    for food in food_list:
        if not isinstance(food, food_item):
            raise TypeError("All items must be instances of food_item")
        total_cal += food.calories
        total_pro += food.protein
        total_carbs += food.carbs
        total_fat += food.fat

    print("DAILY NUTRITION SUMMARY")
    print(f"Total Calories: {total_cal:.1f} kcal")
    print(f"Total Protein: {total_pro:.1f} g")
    print(f"Total Carbohydrates: {total_carbs:.1f} g")
    print(f"Total Fat: {total_fat:.1f} g")
   
    warning = False
    if total_cal > 2500:
        print("WARNING: Calories exceed 2500 kcal limit!")
        warning = True
    if total_fat > 90:
        print("WARNING: Fat exceeds 90 g limit!")
        warning = True
    if not warning:
        print("All limits are within safe levels.")


 # Test nutrition tracker
apple = food_item("Apple", 60, 0.3, 15.0, 0.5)
rice = food_item("Rice (100g)", 130, 2.6, 28.0, 0.3)
beef = food_item("Beef (100g)", 125, 20.0, 0.0, 4.5)
fried_chicken = food_item("Fried Chicken (100g)", 270, 20.0, 10.0, 18.0)
daily_meals = [apple, rice, beef, fried_chicken]
calculate_daily_nutrition(daily_meals)

# Test exceeding limits
print("\n Testing Excessive Intake (10 fried_chicken intake)")
excess_meals = [fried_chicken] * 10
calculate_daily_nutrition(excess_meals)