import doctest
import json
import copy
way = []
user = []


def pretty_print_list(position, level=0):
    '''
    (list,int) -> None
    Outputs the data list beautifully
    >>> pretty_print([1,2,3])
    [
    0 : 1
    1 : 2
    2 : 3
    ]
    '''
    print(' ' * 4 * level + '[')
    for now in range(len(position)):
        if type(position[now]) == dict:
            print(' ' * 4 * level + str(now) + ' :')
            pretty_print_dict(position[now], level+1)
        elif type(position[now]) == list:
            print(' ' * 4 * level + str(now) + ' :')
            pretty_print_list(position[now], level+1)
        else:
            print(' ' * 4 * level + str(now) + ' : ' + str(position[now]))
    print(' ' * 4 * level + ']')


def pretty_print_dict(position, level=0):
    '''
    (list,int) -> None
    Outputs the data dict beautifully
    >>> pretty_print({1:1,2:2,3:3})
    {
    1 : 1
    2 : 2
    3 : 3
    }
    '''
    print(' ' * 4 * level + '{')
    for now in position:
        if type(position[now]) == dict:
            print(' ' * 4 * level + str(now) + ' :')
            pretty_print_dict(position[now], level+1)
        elif type(position[now]) == list:
            print(' ' * 4 * level + str(now) + ' :')
            pretty_print_list(position[now], level+1)
        else:
            print(' ' * 4 * level + str(now) + ' : ' + str(position[now]))
    print(' ' * 4 * level + '}')


def pretty_print(position, level=0):
    '''
    (any,int) -> None
    Outputs the data beautifully
    >>> pretty_print('Some text')
    Some text
    >>> pretty_print([1,2,3])
    [
    0 : 1
    1 : 2
    2 : 3
    ]
    '''
    position = copy.deepcopy(position)
    if type(position) == dict:
        pretty_print_dict(position)
    elif type(position) == list:
        pretty_print_list(position)
    else:
        print(position)


def get_position_by_way():
    '''
    None -> dict or list
    Return a current position in json file
    '''
    position = copy.deepcopy(user)
    for i in way:
        position = position[i]
    return position


def read_json(src):
    '''
    str(src) -> json
    Return a json file

    '''
    f = open(src)
    user = f.read()
    user = json.loads(user)
    return user


def get_next(position):
    '''
    (dict or list) -> any
    Read and get position of next element
    '''
    print('------------------------------------------')
    if len(way) != 0:
        print('Your current position is', '/'.join([str(x) for x in way]))
        print('If you want to go back print ..')
    print('If you want to stop navigation now, print stop')
    now = input('Print where you want to go next: ')
    print(now)
    if now == '..' and len(way) != 0:
        way.pop()
        position = get_position_by_way()
        return position
    elif now == '..':
        print('------------------------------------------')
        print('You are already in the start')
        print('------------------------------------------')
        return position
    if now.lower() == 'stop':
        return now
    if type(position) == dict:
        if now in position:
            way.append(now)
            return position[now]
        else:
            print('------------------------------------------')
            print('There is no this key in dictionary')
            print('------------------------------------------')
            return print_json(position)
    else:
        try:
            now = int(now)
            if now < len(position):
                way.append(now)
                return position[now]
            else:
                print('------------------------------------------')
                print('To big index')
                print('------------------------------------------')
                return print_json(position)
        except:
            print('------------------------------------------')
            print('You must write an index')
            print('------------------------------------------')
            return print_json(position)


def print_json(position):
    '''
    json -> any
    Print short information about json file
    If this is a dict or list additionaly give you opportunity to get to next item
    >>> print_json('Some text')
    'Some text'
    >>> print_json(213214)
    213214
    '''
    if type(position) == dict or type(position) == list:
        if len(position) == 0:
            return position
        k = 0
        for info in position:
            if type(position) == list:
                info = k
            types = str(type(position[info])).split("'")[1]
            k += 1
            print(str(info) + ', type: ' + types)
        position1 = get_next(position)
        if position1 == 'stop':
            return position
        return print_json(position1)
    else:
        return position


if __name__ == "__main__":
    user = read_json('twitter.json')
    navigation = print_json(copy.deepcopy(user))
    print('\n\n\n\n\n')
    pretty_print(navigation)

doctest.testmod()