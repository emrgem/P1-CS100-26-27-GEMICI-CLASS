"""Lesson 6B Sandbox
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: the third number ----------
# Run each one. Write down what you get.

# for i in range(0, 10, 2):
#     print(i)
# for i in range(0, 10, -2): # wont work
#     print(i)
# for i in range(10, 0, -2): # will work
#     print(i)
# for i in range(5,0): # wont work
#     print(i)
# for i in range(5,0,-1): # works
#     print(i)
# for i in range(5,-1,-1): # works
#     print(i)

# What changed? ______________________________


# Now make it count DOWN from 5 to 1.
# Hint: the third number can be negative.


# ---------- Quick Try 2: the accumulator ----------
# Add up 1 + 2 + 3 + 4 using a loop.
#
# You need a variable that survives BETWEEN runs of the loop.
# Think about where it has to be created.

total = 0          # <- outside

# for i in range(1, 5):
#     total = 0
#     # total = total + 1
#     # total += 1
#     total += i
# print(total)       # <- use it here. Should print 10.
for i in range(1, 5):
    print(total)       # <- use it here. Should print 10.
    total = 0
    # total = total + 1
    # total += 1
    total += i


# ---------- Quick Try 3: break it on purpose ----------
# Move the `total = 0` line INSIDE the loop (indent it).
# Run it again. What does it print now, and why?
