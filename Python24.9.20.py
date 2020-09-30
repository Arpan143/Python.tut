"""simple sorting and all"""
A = [5522 , 4 , 2 , 1 , 21 , 56]
A.sort()
A.reverse()
B = [2 , 6, 4]
B.sort()
print(A)
print(B)
print(A,B)
A, B = B, A
print(A,B)
# """New"""
# C = (5522 , 4 , 2 , 1 , 21 , 56)
# """C.sort()"""
# """C.reverse()"""
# D = [2 , 6, 4]
# D.sort()
# print(C)
# print(D)
# print(C,D)
# C, D = D, C
# print(C,D)
""" Dictionary """
# d1={}
# print(type(d1))
# print("enter word")
# A=input()
# D1={"Permaculture":" combine two words to make a new one",
# "Freegan":"a person who believes it is wrong to throw away food",
# "Hothouse":"greenhouse ", "Hellacious":" awful experience"}
# if A in D1:
#     print("The meaning of the word is", D1.get(A))
# else:
#     print("meaning Not available.")
"""  Greater than less than """
# print("enter number 1")
# var1=input()
# print("enter number ")
# var2=input()
# # print("enter number 3")
# # var3=input()
# if var1>var2:
#     print("var 1 is greater")
# if var1== var2:
#     print(var2,"is equal to", var2)
# else:
#     print(var1, "is lesser then", var2)
"""Else If Age"""
# print("enter your age")
# Age=int(input())
# if 101>Age>18:
#     print("Eligible for driving")
# elif Age==18:
#     print("physical presence required")
# elif Age>101:
#     print("physical presence required")
# else:
#     print("not eligible.")
""" Faulty calculator """
# Num1=int(input("enter number 1:"))
# Num2=int(input("enter number 2:"))
# Op=input("enter operator")
# if Op=="+":
#     if Num1==56 and Num2==9:
#         print("77")
#     elif Num2==56 and Num1==9:
#         print("77")
#     else:
#         print(Num1+Num2)
# if Op=="*":
#     if Num1==45 and Num2==3:
#         print("555")
#     elif Num2==45 and Num1==3:
#         print("555")
#     else:
#         print(Num1*Num2)
# if Op=="-":
#     print(Num1-Num2)
# if Op=="/":
#     if Num1==56 and Num2==6:
#         print("4")
#     else:
#         print(Num1/Num2)
"""  For loop  """
# listA = [ ["Arpan",18],
#           ["Shivam",19],
#           ["Goyal",17],
#           ["Vishal",20]
#         ]
# dictA=dict(listA)
# print(dictA)
# for item, age in dictA.items():
#     print(age)
# listN = [ "Ar", 2, 23, 44, "KK", "LM", "hss", 223, 6
#          ]
# for item in listN:
#     if str(item).isnumeric():
#         if item>6:
#             print(int(item))
#         else:
    #         print("error")
    # else:
    #     print("error")
"""While loop"""

# i = 0
# while(True):
#     if i<5:
#         i=i+1
#         continue
#     i=i+1
#     print(i+1) 
#     if i>= 45:
#         break
"""Exercise-3"""

# A=int(input("enter number "))
# while(True) :
#     A=int(input("enter number "))
#     if A<100:
#         continue
#     elif A==100:
#         print("congratulations number is equal to 100")
#     else:
#         print("congratulations number is greater than 100")
#     break
"""Exercise-4"""

# True_Number=22
# Chances=5
# i=0
# while(True):
#     print("Number of guesses left =", Chances-i )
#     A=int(input("guess a number ="))
#     i=i+1
#     if i<Chances:
#         if A>True_Number:
#             print("number is greater than true number")
#         elif A==True_Number:
#             print("True guess", "Winner winner")
#             print("number of guesses used = ", i)
#             break
#         else:
#             print("number is smaller than true number")
#         continue    
#     elif i>=Chances:
#         print("Game over, no more chances left")
#         break
***while(True):
    N = int(input("number"))
    if N<=100:
        continue
    print(N )***
  


    
