"""Lesson 8B SANDBOX
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: a number triangle ----------
# Print this. Each row counts from 1 up to the row number.

for row in range(4):
    for col in range(row + 1):
        print("*", end="")
    print()

#
#   1
#   1 2
#   1 2 3
#   1 2 3 4
# for row in range(1,5):
#     for col in range(1, row + 1):
#         print(col, end=" ")
#     print()
for row in range(4):
    for col in range( row + 1):
        print(col+1, end=" ")
    print()


#break leaves only the inner loop
for row in range(3):
    for col in range(5):
        if col == 2:
            break
        print(row,col)



# ---------- Quick Try 2: upside down ----------
# Print a triangle that SHRINKS, starting with 5 stars.
#
#   *****
#   ****
#   ***
#   **
#   *
