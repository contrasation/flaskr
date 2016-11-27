from flask import Flask
from feed import feed
from chat import chat
app = Flask(__name__)
app.register_blueprint(feed)
app.register_blueprint(chat)
app.run(debug=True)