import re

def capital_text(s):
    return re.sub(r"(?:^|[.!?])\s*(.)", lambda m: m.group(0).upper(), s)