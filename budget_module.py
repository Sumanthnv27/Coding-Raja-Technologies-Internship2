def budget_calcu():
   import ast
   with open("income_amt_file.text","r") as j:
      inc_amt=ast.literal_eval(j.read())
   with open("expenses_file.text","r") as j:
      exp_dict=ast.literal_eval(j.read())
   if len(inc_amt)==0 and len(exp_dict)==0:
    print("plz enter the income value and expenses first")
    return 0
   with open("income_amt_file.text","r") as j:
      inc_amt=ast.literal_eval(j.read())
   with open("expenses_file.text","r") as j:
      exp_dict=ast.literal_eval(j.read())
   p=0
   lst=list(exp_dict.values())
   for x in lst:
       p=p+x
   rem_budget=inc_amt[0]-p
   return rem_budget