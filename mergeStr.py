class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       
        res=""
        count=0
        while count< min([len(word1),len(word2)]):
          res+=word1[count]+word2[count]
          count+=1
      


        
        return res+word1[count:]+word2[count:]

        
