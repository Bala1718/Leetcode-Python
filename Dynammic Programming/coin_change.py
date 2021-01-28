import sys
def coinchange(coins,m,v):
    dp_table = [0 for i in range(V+1)]

    dp_table[0]=0

    for i in range(1,V+1):
        dp_table[i]= sys.maxsize

    for i in range(1, V+1):
        for j in range(m):
            if (coins[j] <= i):
                sub_res = dp_table[i-coins[j]]
                if(sub_res!=sys.maxsize and sub_res+1<dp_table[i]):
                    dp_table[i] = sub_res + 1
    return dp_table[V]