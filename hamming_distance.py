# -*- coding: utf-8 -*-
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dif = 0
        bin_a = bin(x).split('b')[1]
        bin_b = bin(y).split('b')[1]
        # print(bin_a, bin_b)
        if len(bin_a) < len(bin_b):
            bin_a = bin_a.zfill(len(bin_b))
        elif len(bin_a) > len(bin_b):
            bin_b = bin_b.zfill(len(bin_a))
        # print(bin_a, bin_b)

        for a, b in zip(bin_a, bin_b):
            if a != b:
                dif += 1
        return dif


ham_code = Solution()
print (ham_code.hammingDistance(1, 4))
