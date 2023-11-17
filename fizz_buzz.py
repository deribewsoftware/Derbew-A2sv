class Solution(object):
    def fizzBuzz(self, n):
        res=[]*n
        for i in range(1,n+1):
            if i%3==0 and i %5==0:
                res.insert(i-1,"FizzBuzz")
            elif i%3==0:
                res.insert(i-1,"Fizz")
            elif i%5==0:
                res.insert(i-1,"Buzz")
            else:
                res.insert(i-1,str(i))
        return res


        
            
        """
        :type n: int
        :rtype: List[str]
        """
        
