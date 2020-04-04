# https://gist.github.com/andrewblum/4b47fdf20c9e9db913f574a687a549d7
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input: [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0],[0,0,0,0,0]]
#
# Output: 1
#
# Example 2:
#
# Input: [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]
#
# Output: 3


def count_islands(map):
    """ingest an array of arrays and count the number of 'islands'"""

    island_count = 0
    contiguous = False
    for lat in range(len(map)):
        line = map[lat]
        for coord in range(len(line)):
            if line[coord] == 1:
                if (coord < (len(line) - 1) and line[coord + 1] == 1) or (lat < (len(map) - 1) and map[lat + 1][coord] == 1):
                    if contiguous:
                        continue
                    else:
                        contiguous = True
                        island_count += 1
                elif contiguous:
                    continue
                elif not contiguous:
                    island_count += 1
                elif (coord < (len(line) - 1) and line[coord + 1] == 0) or (lat < (len(map) - 1) and map[lat + 1][coord] == 0):
                    continguous = False
            elif line[coord] == 0:
                continue
    return island_count


# notes on recursion: it would have to go in several directions?
# start with a point. If it's a 1, then check the surrounding points -- so in the case of 0, 0 index, check 1 and index 0 of row 1
# that's the base case and then you back out, but like... how. Is this a tree hting? It feels TREEISH.
# you need to track how many islands you have, and also whether or not you are still in one contiguous
# so maybe you recurse through, moving to the next spot both horizontally and vertically until you run out of "movement"
# increment the counter, then move to the next land spot that you haven't "touched"
# recursion SHOULD address the issue of checking all four coordinates for each land--you only need to check "forward" and "above"
# because you've come from a spot that is already identified as contiguous, so you don't need to re-confirm
