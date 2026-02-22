import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

d = math.hypot(x1 - x2, y1 - y2)

# If both points are on same side and segment does not go toward circle
# check minimum distance from segment to center

# vector AB
dx = x2 - x1
dy = y2 - y1

# projection parameter
t = -(x1*dx + y1*dy) / (dx*dx + dy*dy)

if 0 <= t <= 1:
    # closest point is inside segment
    px = x1 + t*dx
    py = y1 + t*dy
    h = math.hypot(px, py)
else:
    # closest point is endpoint
    h = min(math.hypot(x1,y1), math.hypot(x2,y2))

if h >= r:
    print(f"{d:.10f}")
else:
    d1 = math.hypot(x1, y1)
    d2 = math.hypot(x2, y2)

    t1 = math.sqrt(d1*d1 - r*r)
    t2 = math.sqrt(d2*d2 - r*r)

    alpha = math.acos(r / d1)
    beta = math.acos(r / d2)

    cos_theta = (x1*x2 + y1*y2) / (d1*d2)
    cos_theta = max(-1, min(1, cos_theta))
    theta = math.acos(cos_theta)

    phi = theta - alpha - beta

    print(f"{t1 + t2 + r*phi:.10f}")