from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Initialize Flask app
app = Flask(name)

# Initialize ChatterBot
bot = ChatBot('CollegeBot', storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3')

# Train the chatbot with some example conversations
trainer = ListTrainer(bot)
conversation = [
    "Hi there!",
    "Hello!",
    "How can I help you?",
    "I need information about courses.",
    "We offer various courses in computer science, engineering, and management.",
    "Thank you!",
    "You're welcome!"
]

trainer.train(conversation)

# Define a route for chatbot conversation
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = bot.get_response(user_message)
    return jsonify({'response': str(response)})

if name == 'main':
    app.run(debug=True)