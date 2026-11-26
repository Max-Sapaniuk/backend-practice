def add_slot(slots, slot):
    return sorted([*slots, slot])


def paginate(items, page, size):
    if page < 1 or size < 1:
        return []
    start = (page - 1) * size
    return items[start : start + size]


def last_n(items, n):
    if n <= 0:
        return []
    return items[-n:]


def week_template(day_slots):
    return [list(day_slots) for _ in range(7)]
