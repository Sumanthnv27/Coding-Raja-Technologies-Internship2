def delete():
  import ast
  with open("expenses_file.text","r") as j:
      exp_dict=ast.literal_eval(j.read())
  explist=list(exp_dict)
  print(f"the available expenditures are {exp_dict}")
  print("Enter the expense type to delete")
  delexp=input()
  while delexp not in explist:
     delexp=input("Not found!\n plz enter the valid expense type:")
  val=exp_dict[delexp]
  del  exp_dict[delexp]
  import ast
  with open("income_amt_file.text","r") as j:
      inc_amt=ast.literal_eval(j.read())
  inc_amt[0]=inc_amt[0]+val
  file1=open("expenses_file.text","w")
  file1.write(str(exp_dict))
  file1=open("income_amt_file.text","w")
  file1.write(str(inc_amt))