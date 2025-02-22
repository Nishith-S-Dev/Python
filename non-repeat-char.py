# the problem statement is to find the one char which is not reapeatable
str = "Nishith"


for char in str:
   if str.count(char)==1 :
     print("the given first char :",char )
     break
