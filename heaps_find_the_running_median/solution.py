import math

def get_list_size(lst):
    return len(lst)

def list_has_even_items(lst):
    return is_even_number(get_list_size(lst))

def is_even_number(num):
    return num % 2 == 0

def find_mid_index(lst, start = None, end = None):
    if not lst:
        return None

    lst_len = get_list_size(lst)

    if start == None and end == None:
        mid_index = math.floor(lst_len / 2)
    elif end != None:
        if end < 0:
            end = 0
        elif end > lst_len - 1:
            end = lst_len - 1

        lst_len = end + 1

        mid_index = math.floor(lst_len / 2)
    elif start != None:
        if start < 0:
            start = 0
        elif start > lst_len - 1:
            start = lst_len - 1

        lst_len -= start
        mid_index = math.floor(lst_len / 2)
        mid_index += start

    if is_even_number(lst_len):
        mid_index -= 1

    return int(mid_index);
