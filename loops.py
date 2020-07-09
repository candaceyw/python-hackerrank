# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
#
# Example
#
# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.
#
# 0
# 1
# 4
# Input Format
#
# The first and only line contains the integer, .
#
# Constraints
#
#




if __name__ == '__main__':
    n = int(input())
    i = 0

    for i in range(n):
        print(pow(i, 2))