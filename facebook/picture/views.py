from . import picture

@picture.route('/picture')
def picture():
    return 'This is the picture!'