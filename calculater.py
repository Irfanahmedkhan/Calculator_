print("welcome to my first python program for Calculation ", end="\n\n")
print("+ (add), - (subtract), * (multiply), and / (divide)", end="\n\n")

opr = input("Chose operator from the above  :  ",)
print()

f_num = int(input("thanks, now Kindly Enter your First Number  :  "))
s_num = int(input("Enter your Second Number  :  "))
print()

if opr == "+":
    print("First & Second Number Addition is  :  ", f_num+s_num, end="\n\n")
elif opr == " - ":
    print("First & Second Numbers subtraction is  :  ", f_num-s_num, end="\n\n")
elif opr == "*":
    print("First & Second Numbers Multiplication is  :  ", f_num*s_num, end="\n\n")
elif opr == "/":
    print("First & Second Numbers division is  :  ", f_num/s_num, end="\n\n")

print("Thanks for your Intrest : Have A nice day")
