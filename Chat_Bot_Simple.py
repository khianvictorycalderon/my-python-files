# Initialize conversation state
over = False

def getResponse(ui):
    """Process user input and return a response."""
    # Trim whitespace and convert to lowercase
    ui = ui.strip().lower()
    # Split the input into words
    words = ui.split(" ")

    # Respond based on specific keywords
    if "thank" in words:
        return "You're welcome!"
    elif "hello" in words:
        return "Hello! How can I assist you today?"
    elif "how" in words and "you" in words:
        return "I'm just a program, but I'm here to help you!"
    else:
        return "Sorry, I couldn't understand you."

def Conversate():
    """Handle the conversation flow."""
    global over
    if not over:
        ui = input(" You: ")  # Get user input
        if ui.lower() == "exit":
            over = True
            print("Thank you for using me.")
        else:
            response = getResponse(ui)  # Get response based on user input
            print(" Bot:", response)      # Print the bot's response
            Conversate()                # Recursion to continue the conversation

# Start the conversation
print("Hello user! Type 'exit' to end the conversation.\n")
Conversate()