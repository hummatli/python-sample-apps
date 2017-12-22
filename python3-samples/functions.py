def func4(arg1, arg2 = 3):
   print(arg1, '_ ', arg2)
#call
func4(2) # prints 2_3
func4(2, 5) # prints 2_5
#Argumentlerin adi ile muracet etmek
func4(arg2=2, arg1=5) # prints 5_2 