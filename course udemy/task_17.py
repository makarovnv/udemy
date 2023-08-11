def is_cat_here(*args):
    for i in args:
        if 'cat' in i.lower():
            return True
        else:
            return False


def is_item_here(item, *args):
    if item in args:
        return True
    else:
        return False


def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is ' + str(my_color) +
              ', but ' + kwargs['color'] + ' is also pretty good!')
    else:
        print('My favorite color is ' + str(my_color) +
              ', what is your favorite color?')
