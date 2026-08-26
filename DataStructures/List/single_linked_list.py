def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0
    }
    return newlist


def add_first(my_list, element):
    new_node = {"info": element, "next": my_list["first"]}
    my_list["first"] = new_node
    if my_list["size"] == 0:
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    new_node = {"info": element, "next": None}
    if my_list["size"] == 0:
        my_list["first"] = new_node
    else:
        my_list["last"]["next"] = new_node
    my_list["last"] = new_node
    my_list["size"] += 1
    return my_list


def first_element(my_list):
    return my_list["first"]["info"]


def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]


def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count


def is_empty(my_list):
    return my_list["size"] == 0


def size(my_list):
    return my_list["size"]


def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    return my_list["last"]["info"]


def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise Exception("IndexError: list index out of range")
    if pos == 0:
        deleted_node = my_list["first"]
        my_list["first"] = deleted_node["next"]
    else:
        prev_node = my_list["first"]
        for _ in range(pos - 1):
            prev_node = prev_node["next"]
        deleted_node = prev_node["next"]
        prev_node["next"] = deleted_node["next"]
        if deleted_node == my_list["last"]:
            my_list["last"] = prev_node
    my_list["size"] -= 1
    return my_list


def remove_first(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    elemento = my_list["first"]["info"]
    delete_element(my_list, 0)
    return elemento


def remove_last(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    elemento = my_list["last"]["info"]
    delete_element(my_list, my_list["size"] - 1)
    return elemento


def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        raise Exception("IndexError: list index out of range")
    new_node = {"info": element, "next": None}
    if pos == 0:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node
        if my_list["size"] == 0:
            my_list["last"] = new_node
    else:
        prev_node = my_list["first"]
        for _ in range(pos - 1):
            prev_node = prev_node["next"]
        new_node["next"] = prev_node["next"]
        prev_node["next"] = new_node
        if new_node["next"] is None:
            my_list["last"] = new_node
    my_list["size"] += 1
    return my_list


def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list["size"]:
        raise Exception("IndexError: list index out of range")
    node = my_list["first"]
    for _ in range(pos):
        node = node["next"]
    node["info"] = new_info
    return my_list


def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list["size"] or pos2 < 0 or pos2 >= my_list["size"]:
        raise Exception("IndexError: list index out of range")
    if pos1 == pos2:
        return my_list
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    prev1 = None
    node1 = my_list["first"]
    for _ in range(pos1):
        prev1 = node1
        node1 = node1["next"]
    prev2 = node1
    node2 = node1["next"]
    for _ in range(pos2 - pos1 - 1):
        prev2 = node2
        node2 = node2["next"]
    after2 = node2["next"]
    if prev2 is node1:
        node2["next"] = node1
        node1["next"] = after2
    else:
        after1 = node1["next"]
        node2["next"] = after1
        prev2["next"] = node1
        node1["next"] = after2
    if prev1 is not None:
        prev1["next"] = node2
    else:
        my_list["first"] = node2
    if my_list["last"] is node2:
        my_list["last"] = node1
    return my_list


def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= my_list["size"] or num_elements < 0 or (pos + num_elements) > my_list["size"]:
        raise Exception("IndexError: list index out of range")
    sublist = new_list()
    current_node = my_list["first"]
    for _ in range(pos):
        current_node = current_node["next"]
    for _ in range(num_elements):
        insert_element(sublist, current_node["info"], size(sublist))
        current_node = current_node["next"]
    return sublist