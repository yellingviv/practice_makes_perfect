# takes in an infinite list of arguments, uppercases them, sorts, and returns a list
# modified to accept both lists and strings as args

def get_lorge(*args):

    embiggened = []

    for item in args:
        if type(item) == list:
            for subitem in item:
                embiggened.append(subitem.upper())
        elif type(item) == str:
            embiggened.append(item.upper())
        else:
            continue

    return sorted(embiggened)

# test case:
# get_lorge('hi', ['box', 'apple'], 7, 'zebra') --> ['APPLE', 'BOX', 'HI', 'ZEBRA']
