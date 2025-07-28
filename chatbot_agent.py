class ChatBotAgent:
    def __init__(self):
        self.responses = {
            "hi": "Hi!\nWelcome to SmartCafe Assistant!\nAsk me about drinks, ingredients, calories, sugar, prices, or opening hours.\nType 'exit' or 'quit' to leave at any time.",
            "menu": "We currently serve: Caramel Latte, Matcha Latte, Espresso, Iced Americano, Vanilla Cold Brew, Chai Latte, Mocha, Flat White, Iced Latte, Hot Chocolate.",
            "price matcha latte": "Matcha Latte costs $3.40.",
            "calories matcha latte": "Matcha Latte contains approximately 180 calories.",
            "calories hot chocolate": "Hot Chocolate contains approximately 250 calories.",
            "ingredients mocha": "The ingredients in Mocha are: espresso, chocolate syrup, steamed milk.",
            "hours friday": "On Friday, we're open: 8:00 AM - 10:00 PM."
        }

    def run(self):
        print("👋 Welcome to SmartCafe Assistant!")
        print("Ask me about drinks, ingredients, calories, sugar, prices, or opening hours.")
        print("Type 'exit' or 'quit' to leave at any time.")

        while True:
            user_input = input("• You: ").strip().lower()

            if user_input in ['exit', 'quit']:
                print("Goodbye! Have a great day ☕")
                break
            elif user_input == "hi":
                print(self.responses["hi"])
            else:
                found = False
                for key in self.responses:
                    if key in user_input:
                        print(self.responses[key])
                        found = True
                        break
                if not found:
                    print("I’m checking your question...")

if __name__ == "__main__":
    bot = ChatBotAgent()
    bot.run()