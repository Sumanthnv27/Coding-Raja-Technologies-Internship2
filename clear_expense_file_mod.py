def delete():
     expenses_dict={}
     income_list=[]
     file=open("income_amt_file.text","w")
     file.write(str(income_list))
     file1=open("expenses_file.text","w")
     file1.write(str(expenses_dict))
     file.close()
     file1.close()