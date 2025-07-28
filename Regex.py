# Import regular expressions module to work with patterns in text
import re

# Import JSON module to read data from a .json file  
import json

# Load the cafe menu data 
with open('cafe_data.json') as f:
    cafe_data = json.load(f)

# This function takes what the user writes and tries to understand their intent (what they want)
def detect_intent(user_input):
    user_input = user_input.lower() # Convert the input to lowercase to make matching easier

# Check if the user is asking about ingredients in a drink
    match = re.search(r"what(?:'s| is) in (.+)", user_input)
    if match:
        return ("ingredients", match.group(1).strip().rstrip("?"))  #Return "ingredients" and the drink name

# Check if the user is asking about calories in a drink
    match = re.search(r"how many calories in (.+)", user_input)
    if match:
        return ("nutrition", match.group(1).strip().rstrip("?")) # Return "nutrition" and the drink name

 # Check if the user is asking about opening hours on a specific day
    match = re.search(r"when are you open on (.+)", user_input)
    if match:
        return ("hours", match.group(1).capitalize().strip().rstrip("?"))  # Return "hours" and the day name

 # Check if the user is asking to see the list of drinks
    match = re.search(r"(what|which) drinks do you have", user_input)
    if match:
        return ("drinks", None)  # Return "drinks" without a specific keyword

 # Check if the user is asking about the price of a drink
    match = re.search(r"(?:how much(?: is)?|price of) (.+)", user_input)
    if match:
        return ("price", match.group(1).strip().rstrip("?")) # Return "price" and the drink name

  # If the question doesn't match any known pattern, return "unknown"
    return ("unknown", None)


if __name__ == "__main__":
 
    questions = [
        "What's in a Mocha?",
        "How many calories in Hot Chocolate?",
        "When are you open on Friday?",
        "What drinks do you have?",
        "Do you have any desserts?"
    ]


    for question in questions:
        intent, keyword = detect_intent(question)
        print(f"User question: {question}")
        print(f"Detected Intent: {intent}")
        print(f"Keyword: {keyword}")
        print("-" * 40)