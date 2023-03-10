def FlagsCoveredArea(n,m,a):
  
  
  n_side_flags=n//a
  m_side_flags=m//a
  return(n_side_flags*m_side_flags)*a

n=int(input("Enter the \'n\' demensions of square:"))
m=int(input("Enter the \'m\' demensions of square:"))
a=int(input("Enter the \'a\' demensions of square:"))
print(FlagsCoveredArea(n,m,a))
 
