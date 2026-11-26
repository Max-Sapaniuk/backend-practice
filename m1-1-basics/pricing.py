from decimal import ROUND_HALF_UP, Decimal


def calc_total(price, qty, discount_percent=None):
    total = Decimal(price) * qty
    if discount_percent is not None:
        total *= 1 - Decimal(str(discount_percent)) / 100
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def format_line(name, qty, total, discount_percent=None):
    line = f"{name:<20} x{qty:<3}{total:>12,.2f} UAH"
    if discount_percent is not None:
        line += f" (-{discount_percent}%)"
    return line


def normalize_comment(comment):
    if comment is None:
        return None
    comment = comment.strip()
    return comment or None
