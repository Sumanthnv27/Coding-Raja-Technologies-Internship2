def income_Entry():
  print("Enter the income amount")
  inamt=int(input())
  import ast
  with open("income_amt_file.text","r") as j:
      inc_amt=ast.literal_eval(j.read())
#   import os
#   p=os. path. getsize("income_amt_file.text") == 0
  p=len(inc_amt)
  if(p!=0): 
    new_amt=inc_amt[0]+inamt
    inc_amt.append(new_amt)
    print(f"The avalable balance is {new_amt}")
  else:
     inc_amt.append(inamt) 
     print(f"The avalable balance is {inamt}")
  file1=open("income_amt_file.text","w")
  file1.write(str(inc_amt))
file1=open("income_amt_file.text","a")
file1.close
import os
p=os. path. getsize("income_amt_file.text") == 0
if(p==True):
    lst=[]
    file1=open("income_amt_file.text","a")
    file1.write(str(lst))