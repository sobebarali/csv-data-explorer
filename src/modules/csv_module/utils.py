from datetime import datetime
from typing import Optional
from modules.csv_module.constants import DATE_FORMATS


def parse_date(date_str: str) -> Optional[datetime.date]:
    """Parse a date string into a datetime.date object."""
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None