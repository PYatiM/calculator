import calendar as cal
import time as ti 

while True:
     print("WHAT DO YOU WANT TO DO TODAY \N{smiling face with smiling eyes}: \n")
     print("1. CALENDER \N{calendar} \n")
     print("2: CALCULATOR \N{abacus}\n")
     print("3: TIME \N{alarm clock}\n")
     print("4: EXIT \N{cross mark}\n")

     a = int(input("ENTER THE CHOICE : "))
     print("\n")
     if a == 2:
          print("CALCULATOR \n")
          def calc(x,y):
               while True:
                    print("THE OPTIONS FOR CALCULATOR : \n1. ADDITION \n2. SUBTRACTION \n3. DIVISION \n4. MULTIPYING \n5. SQUARE ROOT \n6. POWER \n7. EXIT")
                    print("\n")
                    c = int(input("ENTER THE OPTION U WANNA CHOOSE : ")) 
                    print("\n")
                    if c == 1:
                         print(f"{x}+{y} = {x+y}")
                         print("\n")
                    elif c == 2:
                         print(f"{x}-{y} = {x-y}")
                         print("\n")
                    elif c == 3:
                         print(f"{x}/{y} = {x/y}")
                         print("\n")
                    elif c == 4:
                         print(f"{x}*{y} = {x*y}")
                         print("\n")
                    elif c == 5:
                         print(f"{x}^0.5 = {x**0.5}")
                         print("\n")
                    elif c == 6:
                         print(f"{x}^{y} = {x**y}")
                         print("\n")
                    elif c == 7:
                         print("THANK YOU FOR USING THE CALCULATOR")
                         break
                    elif c>6 or c<1:
                         print("INVALID OPTION \N{loudly crying face}")
                         print("\n")

          a, b = map(int, input("ENTER THE TWO VALUES OF A AND B : ").split())
          calc(a,b)
     elif a == 1:
          def calen(m,y):
               print("\n")
               print(f"THE CALENDER FOR THE MONTH OF {m} and year {y} IS : ")
               m = m.lower()
               match (m):
                   case "january":
                       print(cal.month(y,1))
                       print("\n")
                       
                   case "february":
                       print(cal.month(y,2))
                       print("\n")
                       
                   case "march":
                       print(cal.month(y,3))
                       print("\n")
                       
                   case "april":
                       print(cal.month(y,4))
                       print("\n")
                       
                   case "may":
                       print(cal.month(y,5))
                       print("\n")
                       
                   case "june":
                       print(cal.month(y,6))
                       print("\n")
                       
                   case "july":
                       print(cal.month(y,7))
                       print("\n")
                       
                   case "august":
                       print(cal.month(y,8))
                       print("\n")
                       
                   case "september":
                       print(cal.month(y,9))
                       print("\n")
                       
                   case "october":
                       print(cal.month(y,10))
                       print("\n")
                       
                   case "november":
                       print(cal.month(y,11))
                       print("\n")
                       
                   case "december":
                       print(cal.month(y,12))
                       print("\n")
                       
                   case _:
                       print("INVALID MONTH \N{loudly crying face}")         
                       print("\n")
                       print("\n")
          b = input("Enter the month : ")
          e = b.lower()
          c = int(input("ENTER THE YEAR : "))
          calen(e,c)
     elif a == 3:
          print("\n")
          print("The current time is :")
          print("\n")
          print(ti.strftime("%H:%M"))
          print("\n")
          break
     elif a == 4:
          print("THANK YOU \N{saluting face}")
          
     else:
          print("INVALID CHOICE \N{loudly crying face}")
