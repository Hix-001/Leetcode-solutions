# 27/08/2026
# Easy
# LeetCode 832: Flipping an Image

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        result = []
        for row in image:
            new_row = []
            for i in range(len(row) - 1, -1, -1):
                if row[i] == 1:
                    new_row.append(0)
                else:
                    new_row.append(1)
            result.append(new_row)
        return result