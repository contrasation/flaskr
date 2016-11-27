from . import feed

@feed.route('/feed')
def feed():
    return "This is feed!!"