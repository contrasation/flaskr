from . import chat

@chat.route('/chat')
def chat():
    return "This is chat"
