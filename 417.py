import math

# Radius
R = float(input())

# Points
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# Direction vector
dx = x2 - x1
dy = y2 - y1

# Quadratic coefficients
a = dx*dx + dy*dy
b = 2 * (x1*dx + y1*dy)
c = x1*x1 + y1*y1 - R*R

discriminant = b*b - 4*a*c

if discriminant < 0:
    print("0.0000000000")
else:
    sqrt_d = math.sqrt(discriminant)
    t1 = (-b - sqrt_d) / (2*a)
    t2 = (-b + sqrt_d) / (2*a)

    t_low = max(0, min(t1, t2))
    t_high = min(1, max(t1, t2))

    if t_low > t_high:
        print("0.0000000000")
    else:
        length = math.sqrt(a) * (t_high - t_low)
        print(f"{length:.10f}")