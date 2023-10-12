def main():
 file=open("income_amt_file.text","a")
 file=open("expenses_file.text","a")
 import os
 p=os. path. getsize("income_amt_file.text") == 0
 if(p==True):
     expenses_dict={}
     income_list=[]
     file=open("income_amt_file.text","w")
     file.write(str(income_list))
     file1=open("expenses_file.text","w")
     file1.write(str(expenses_dict))
     file.close()
     file1.close()
 while True:
    print("Select operation.")
    print("1.add_income")
    print("2.add_expenses")
    print("3.rem_budget")
    print("4.expense_analysis")
    print("5.delete_expense")
    print("6.clear_expense_file")
    choice = input("Enter choice(1/2/3/4/5/6): ")
    if choice in ('1', '2', '3','4','5','6'):
        if choice == '1':
            from income_module import income_Entry
            income_Entry()
        elif choice=="2":
            from expenses_module import add_expenses
            add_expenses()
        elif choice=="3":
            from budget_module import budget_calcu
            print(budget_calcu())
        elif choice=="4":
            from expenses_analysis_module import expense_analysis
            expense_analysis()
        elif choice=="5":
            from delet_expense_module import delete
            delete()
        elif choice=="6":
           from clear_expense_file_mod import delete
           delete()
        next_calculation = input("Do want to stay (yes/no): ")
        while next_calculation not in ["yes","no"]:
           next_calculation = input("plz enter yes or no : ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
main()