ll = [None, None, None, None]


def get_index(value):
    return hash(value) % len(ll)


def add(value):
    index = get_index(value)
    if ll[index] is None:
        ll[index] = []
    ll[index].append(value)