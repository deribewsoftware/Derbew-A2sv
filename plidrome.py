class Solution:
    def isPalindrome(self, x: int) -> bool:
        res=""
        newStr=str(x)
        for i in range(len(newStr)-1,-1,-1):
            res+= newStr[i]
        intnum=int(res)
        if intnum==x:
            return True
        else:
            return False

        
