def start_spring(**kwargs):
    result = ''
    spring_objects = {}
    for key, value in kwargs.items():
        if value not in spring_objects:
            spring_objects[value] = []
        spring_objects[value].append(key)

    sorted_collections_and_objects = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple_ in sorted_collections_and_objects:
        type_object = tuple_[0]
        list_of_objects = tuple_[1]
        sorted_list_of_objects = sorted(list_of_objects)
        result += f"{type_object}:\n"
        for obj in sorted_list_of_objects:
            result += f"-{obj}\n"
    return result.strip()


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))


# def start_spring(**kwargs):
#     exit = ''
#     my_dict = {}
#     for key, value in kwargs.items():
#         if value not in my_dict:
#             my_dict[value] = [key]
#         else:
#             my_dict[value] += [key]
#     my_dict_sorted = sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0]))
#     for names in my_dict_sorted:
#         name = names[0]
#         kind = names[1]
#         sorted_kind = sorted(kind)
#         exit += f'{name}:\n'
#         for type in sorted_kind:
#             exit += f'-{type}\n'
#
#     return exit
# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
#
# print(start_spring(**example_objects))