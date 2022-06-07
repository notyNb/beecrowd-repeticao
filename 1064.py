n = 0

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

mediaA = 0
mediaB = 0
mediaC = 0
mediaD = 0
mediaE = 0
mediaF = 0


if a > 0.0:
    n += 1
    mediaA = a
else:
    mediaA = 0

if b > 0.0:
    n += 1
    mediaB = b
else:
    mediaB = 0

if c > 0.0:
    n += 1
    mediaC = c
else:
    mediaC = 0

if d > 0.0:
    n += 1
    mediaD = d
else:
    mediaD = 0

if e > 0.0:
    n += 1
    mediaE = e
else:
    mediaE = 0
    
if f > 0.0:
    n += 1
    mediaF = f
else:
    mediaF = 0

mediafinal = ((mediaA + mediaB + mediaC + mediaD + mediaE + mediaF) /n)

print(f"{n} valores positivos")
print(f"{mediafinal:.1f}")
