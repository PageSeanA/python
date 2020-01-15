#Middle
#1
# print("Total bill amount?")
# bill = float(input())
# print("Level of service? Good, Fiar or Bad")
# service = input()
# # % tipped for good 0.20, fiar 0.15, bad 0.10
# if service == "good":
#     total = bill + float(bill) * float(0.20)
# elif service == "fair":
#     total = bill + float(bill) * float(0.15)
# else:
#     total = bill + float(bill) * float(0.10)
# print(total)

#2

# print("Total bill amount?")
# bill = float(input())
# print("Level of service? Good, Fiar or Bad")
# service = input()
# # % tipped for good 0.20, fiar 0.15, bad 0.10
# if service == "good":
#     total = bill + float(bill) * float(0.20)
# elif service == "fair":
#     total = bill + float(bill) * float(0.15)
# else:
#     total = bill + float(bill) * float(0.10)
# print(total)
# print("Split how many ways?")
# split = total / float(input())
# print(split)

#3
# print("You have 0 coins. Do you want another, yes or no?")
# answer = input("")
# count = 0
# while answer == "yes":
#     count += 1
#     print("You have", count)
#     answer = input("Do you want another? ")
# print("Bye")


#4
# side = int(input("Please Enter any Side of a Square  : "))

# print("Hollow Square Star Pattern") 
# for i in range(side):
#     for j in range(side):
#         if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
#             print('*', end = '  ')
#         else:
#             print(' ', end = '  ')
#     print()


#5

# n = 7
# for i in range(n):
#     print(' '*n, end= "")
#     print('* '*(i))
#     n-=1

#6
for i in range (1,11):
    for n in range (1,11):
        result = 1 * n
        print(str(i) + " " + "X  "+str(n) + " = " + str(result))
