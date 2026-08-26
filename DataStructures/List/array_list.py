from DataStructures.List import array_list as al
def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist


def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list


def first_element(my_list):
    return my_list["elements"][0]


def last_element(my_list):
    return my_list["elements"][my_list["size"] - 1]


def get_element(my_list, index):
    return my_list["elements"][index]


def is_empty(my_list):
    if my_list["size"] <= 0:
        return True
    else:
        return False


def size(my_list):
    return my_list["size"]


def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def delete_element(my_list, pos):
    my_list["elements"].pop(pos)
    my_list["size"] -= 1
    return my_list


def remove_first(my_list):
    elemento = my_list["elements"][0]
    delete_element(my_list, 0)
    return elemento


def remove_last(my_list):
    elemento = my_list["elements"][my_list["size"] - 1]
    delete_element(my_list, my_list["size"] - 1)
    return elemento


def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list


def change_info(my_list, pos, new_element):
    my_list["elements"][pos] = new_element
    return my_list


def exchange(my_list, pos1, pos2):
    temp = my_list["elements"][pos1]
    my_list["elements"][pos1] = my_list["elements"][pos2]
    my_list["elements"][pos2] = temp
    return my_list


def sub_list(my_list, pos, num_elements):
    lista = new_list()
    for i in range(num_elements):
        elemento = my_list["elements"][pos + i]
        add_last(lista, elemento)
    return lista