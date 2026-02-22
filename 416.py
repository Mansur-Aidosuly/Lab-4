from datetime import datetime, timedelta, timezone

def parse_time(s):
    #Split datetime and timezone
    dt_part = s[:19]
    tz_part = s[20:]

    #Create timezone object
    sign = 1 if tz_part[3] == "+" else -1
    hours = int(tz_part[4:6])
    minutes = int(tz_part[7:9])
    tz = timezone(timedelta(hours = sign*hours, minutes = sign*minutes))

    #Parse datetime and attach timezone
    dt = datetime.strptime(dt_part, "%Y-%m-%d %H:%M:%S")
    return dt.replace(tzinfo = tz)

start = parse_time(input().strip())
end = parse_time(input().strip())

# Convert to UTC
start_utc = start.astimezone(timezone.utc)
end_utc = end.astimezone(timezone.utc)

# Compute duration in seconds
duration_seconds = int((end_utc - start_utc).total_seconds())
print(duration_seconds)