from datetime import datetime, timedelta, timezone

def parse_time(line):
    date_time, utc_part = line.split()
    year, month, day = map(int, date_time.split("-"))

    sign = 1 if "+" in utc_part else -1
    hours, minutes = map(int, utc_part[4:].split(":"))

    offset = timezone(sign * timedelta(hours = hours, minutes = minutes))

    return datetime(year, month, day, tzinfo = offset)

d1 = parse_time(input().strip())
d2 = parse_time(input().strip())

dt1_utc = d1.astimezone(timezone.utc)
dt2_utc = d2.astimezone(timezone.utc)

seconds = abs((d2 - d1).total_seconds())
days = int(seconds // 86400)

print(days)