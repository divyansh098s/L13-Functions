def add(p,q) :
    return p + q 
def sub(p,q) :
    return p - q
def multi(p,q) :
    return p * q
def divi(p,q) :
    return p / q 

choice = input("Select Operation\n A:Addition \n B:Substraction \n C:Multiplication \n D:Division \n Enter Your Choice : ")
n1 = int(input("Enter Your First Number :"))
n2 = int(input("Enter Your Second Number :"))
if choice == 'A' :
    print(add (n1 , n2))
if choice == 'B' :
    print(sub(n1 , n2))
if choice == 'C' :
    print(multi(n1 , n2))
if choice == 'D' :
    print(divi(n1 , n2))