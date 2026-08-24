n = 3
import string

l = string.ascii_lowercase[:n]
o = []
for i in range(n):
    o.append('-'.join(l[::-1][:i+1] + l[n-i:]).center((4*n-3), '-'))

print(*o, *o[::-1][1:], sep = '\n')


# 2n-1 rows

# 1, 5, 9, 13, 17
# 1x+b = 1
# 2x+b = 5
# x = 4; b = -3
# 4n-3 columns

# a

# --b--
# b-a-b
# --b--

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# ------d------
# ----d-c-d----
# --d-c-b-c-d--
# d-c-b-a-b-c-d
# --d-c-b-c-d--
# ----d-c-d----
# ------d------

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------