class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if x==0:
            return 0
        return self.helper(x,n)
    def helper(self,x,n):
        if (n)==0:
            return 1.0
        
        y=self.helper(x,int(n/2))
        if n%2==0:
            return y*y
        else:
            if n<0:
                return y*y*(1/x)
            else:
                return y*y*x
                
        
        