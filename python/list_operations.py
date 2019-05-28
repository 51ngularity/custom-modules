


from collections import deque





#make single value list with .popleft ability
def single_value_list(value_list, length_list):
    list_temp = deque([])
    for x in range(0, length_list):
        list_temp.append(value_list)
    return list_temp

# update list: new element in, last element out
def update_list(list_, value_):
    list_.popleft()
    list_.append(value_)
    return list_











