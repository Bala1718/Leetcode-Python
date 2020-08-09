class Solution(object):
    def xorOperation(self, n, start):
        xor_arr = 0
        arr = []
        for i in range(n):
            arr.append(start+2*i)
            xor_arr = xor_arr ^ arr[i]
        return xor_arr