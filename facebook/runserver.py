from flask import Flask
from feed import feed
from chat import chat
from picture import picture
app = Flask(__name__)
app.register_blueprint(feed)
app.register_blueprint(chat)
app.register_blueprint(picture)
app.run(debug=True)