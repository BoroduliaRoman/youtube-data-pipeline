from datetime import timedelta, datetime


SHORTS_MAX_DURATION_SECONDS = 60

def parse_duration(duration_str: str) -> timedelta:
    """Convert an ISO 8601 duration string to timedelta."""
    duration_str = duration_str.replace("P", "").replace("T", "")

    components = ['D', 'H', 'M', 'S']
    values = {'D': 0, 'H': 0, 'M': 0, 'S': 0}

    for component in components:
        if component in duration_str:
            value, duration_str = duration_str.split(component)

            values[component] = int(value)

    total_duration = timedelta(
        days= values['D'], hours=values['H'], minutes=values['M'], seconds=values['S']
    )
    return total_duration

def transform_data(row: dict) -> dict:
    duration_td = parse_duration(row['Duration'])

    row['Duration'] = (datetime.min + duration_td).time()
    row['Video_Type'] = 'Shorts' if duration_td.total_seconds() \
        <= SHORTS_MAX_DURATION_SECONDS else 'Normal'

    return row