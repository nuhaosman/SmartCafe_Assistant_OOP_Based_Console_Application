import json

# This class handles reading data from the JSON and returning answers
class ResearchAgent:
    # Initialize the class and load data from the JSON file
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = self.load_data()

    # Open and read the JSON file
    def load_data(self):
        try:
            with open(self.data_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: cafe_data.json not found.")
            return {}

    # Get the list of ingredients for a menu item
    def get_ingredients(self, item):
        item = item.title().strip()
        try:
            ingredients = self.data['menu'][item]['ingredients']
            return f"The ingredients in {item} are: {', '.join(ingredients)}."
        except KeyError:
            return f"Sorry, I couldn't find ingredients for '{item}'."

    # Get calorie info for a menu item
    def get_calories(self, item):
        item = item.title().strip()
        try:
            calories = self.data['menu'][item]['nutrition']['calories']
            return f"{item} contains approximately {calories} calories."
        except KeyError:
            return f"Sorry, I couldn't find calorie info for '{item}'."

    # Get sugar info for a menu item
    def get_sugar_content(self, item):
        item = item.title().strip()
        try:
            sugar = self.data['menu'][item]['nutrition']['sugar_g']
            return f"{item} has about {sugar} grams of sugar."
        except KeyError:
            return f"Sorry, sugar info for '{item}' is unavailable."

    # Get price of a menu item
    def get_price(self, item):
        item = item.title().strip()
        try:
            price = self.data['menu'][item]['price_usd']
            return f"{item} costs ${price:.2f}."
        except KeyError:
            return f"Sorry, I couldn't find the price for '{item}'."

    # Get opening hours for a specific day
    def get_opening_hours(self, day):
        day = day.title().strip()
        try:
            hours = self.data['opening_hours'][day]
            return f"On {day}, we're open: {hours}."
        except KeyError:
            return f"Sorry, I couldn't find our hours for '{day}'."

    # Return list of all available drinks
    def get_available_drinks(self):
        drinks = self.data.get('drinks', [])
        return f"We currently serve: {', '.join(drinks)}."


# This part runs only if you run the file directly (not imported)
if __name__ == "__main__":
    agent = ResearchAgent("cafe_data.json")

    print(agent.get_ingredients("Mocha"))
    print(agent.get_calories("Hot Chocolate"))
    print(agent.get_opening_hours("Friday"))
    print(agent.get_available_drinks())
