from typing import List


def sNumber(z: List[int]) -> int:
        for i in z:
            if(z.count(i) == 1):
                return(i)

z = [4,1,2,1,2]
z1 = [2,2,1]
print(sNumber(z1))