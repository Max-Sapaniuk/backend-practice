from slots import add_slot, last_n, paginate, week_template

day = [(600, 660), (540, 600)]
result = add_slot(day, (480, 540))
assert result == [(480, 540), (540, 600), (600, 660)]
assert day == [(600, 660), (540, 600)], "add_slot must not mutate the input"
assert result is not day

items = list(range(1, 11))
assert paginate(items, 1, 4) == [1, 2, 3, 4]
assert paginate(items, 3, 4) == [9, 10]
assert paginate(items, 4, 4) == []

assert last_n(items, 3) == [8, 9, 10]
assert last_n(items, 0) == []
assert last_n(items, 20) == items

week = week_template(day)
assert len(week) == 7
assert all(d == day for d in week)
week[0].append((900, 960))
assert week[1] == day, "days must not share one list"
assert day == [(600, 660), (540, 600)], "week_template must not mutate the input"

print("✅ all checks passed")
