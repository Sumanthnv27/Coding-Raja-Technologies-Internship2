def add_expenses():
  import ast
  with open("income_amt_file.text","r") as j:
      inc_amt=ast.literal_eval(j.read())
  if len(inc_amt)==0:
    print("plz enter the income value first")
    return 0
  print("enter the expense type")
  exp=input()
  print("Enter the amount")
  amt=int(input())
  from budget_module import budget_calcu
  bal=budget_calcu()
  while bal<amt:
    print("The expenses should less or equal to budget")
    amt=int(input("enter the amount"))
  import ast
  with open("expenses_file.text","r") as j:
      exp_dict=ast.literal_eval(j.read())
  import os
  p=os. path. getsize("expenses_file.text") == 0
  if(p==False): 
    file_li=list(exp_dict)
    if exp not in file_li:
      exp_dict[exp]=amt
    else:
      new_val=exp_dict[exp]
      exp_dict[exp]=new_val+amt
  else:
      exp_dict[exp]=amt
  file1=open("expenses_file.text","w")
  file1.write(str(exp_dict))
file1=open("expenses_file.text","a")
file1.close
import os
p=os. path. getsize("expenses_file.text") == 0
if(p==True):
    dict={}
    file1=open("expenses_file.text","a")
    file1.write(str(dict))
    