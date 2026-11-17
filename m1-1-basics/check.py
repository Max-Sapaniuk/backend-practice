from decimal import Decimal

from pricing import calc_total, format_line, normalize_comment

assert calc_total("350.50", 3) == Decimal("1051.50")
assert calc_total("0.10", 3) == Decimal("0.30")
assert calc_total("199.99", 1, discount_percent=15) == Decimal("169.99")
assert calc_total("10.05", 1, discount_percent=50) == Decimal("5.03")
assert str(calc_total("100", 2, discount_percent=0)) == "200.00"
assert isinstance(calc_total("1", 1), Decimal)

assert format_line("Haircut", 3, Decimal("1051.50")) == "Haircut              x3      1,051.50 UAH"
assert (
    format_line("Beard trim", 1, Decimal("5.03"), 50)
    == "Beard trim           x1          5.03 UAH (-50%)"
)
assert (
    format_line("Consultation", 2, Decimal("200.00"), 0)
    == "Consultation         x2        200.00 UAH (-0%)"
)

assert normalize_comment(None) is None
assert normalize_comment("") is None
assert normalize_comment("   ") is None
assert normalize_comment("  call me before  ") == "call me before"

print("✅ all checks passed")
