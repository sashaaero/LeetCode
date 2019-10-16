class Solution:
    def countPrimes(self, n: int) -> int:
        lstPrime = []

        def prime(a):
            if a<=1:
                return 0
            if a==2:
                return 1
            else:
                for i in range(2,a):
                    if(a%i)==0:
                        return 0
                return 1

        pr = n - 1

        while pr > 1:
            y=prime(pr)
            if y==1:
                lstPrime.append(pr)
            pr = pr - 1
            
        return(len(lstPrime))
