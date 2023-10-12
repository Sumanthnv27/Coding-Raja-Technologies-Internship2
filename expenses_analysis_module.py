def expense_analysis():
  import ast
  with open("income_amt_file.text","r") as j:
      inc_amt=ast.literal_eval(j.read())
  with open("expenses_file.text","r") as j:
      exp_dict=ast.literal_eval(j.read())
  if len(inc_amt)==0 and len(exp_dict)==0:
    print("plz enter the income value and expenses first")
    return 0
  with open("expenses_file.text","r") as j:
      exp_dict=ast.literal_eval(j.read())
  keylist=list(exp_dict)
  val_list=list(exp_dict.values())
  length=len(val_list)
  print("Catagories               |   Spending_trend")
  for x in range(length):
    
    print(f"{keylist[x]}                       {val_list[x]}")
