#this function add two numbers 
def add(a,b):
    return a+b

#this function substract two nubers
def substract(a,b):
     return a-b

#this function multiplies two numbers
def multiplies(a,b):
     return a*b

#this function divides two numbes
def divide(a,b):
    return a/b 

print("choose operator")
print("1.Addition")
print("2.substraction")
print("3.multiply")
print("4.division")

while True:
       # take input from user
    choice =input("enter choice(1/2/3/4): ")

       #check choice is one of the four option
    if choice in ('1','2','3','4'):
        try:
                num1=float(input("Enter first number:"))
                num2=float(input("Enter second number:"))

        except ValueError:
                print("invalid input")
                


        if choice=='1':
                    print(num1,"+",num2,"=",add(num1,num2))

        elif choice=='2':
                    print(num1,"-",num2,"=",substract(num1,num2))
                
        elif choice=='3':
                    print(num1,"*",num2,"=",multiplies(num1,num2))

        elif choice=='4':
                    print(num1,"/",num2,"=",divide(num1,num2))

         #check if user want to contineu their calculation 
        #break while loop if answer is no

        another_calculation=input("want contineu another calculation?(yes/no):")

        if another_calculation =="no":
             break
           
    else:
       print("invalid input")