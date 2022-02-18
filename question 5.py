# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain" agar dono 
# numbers even (2 se divide hote hain) nahi toh print kare "Dono numbers even nahi hai"

# 
# def  check_numbers(num1,num2):
#     i=0
#     while i<len(num1):
#         j=0
#         while j<len(num2):
#             if i==j:
#                 if num1[i]%2==0 and num2[j]%2==0:
#                     print("even")
#                 else:
#                     print("not even")
#                 j=j+1
#             i=i+1
# num1=[2,4,8]
# num2=[6,8,4]
# check_numbers(num1,num2)

# (ii)# def  check_numbers(num1,num2):
#     if num1%2==0 and num2%2==0:
#         print("even")
#     else:
#         print("not even")
# check_numbers(5,3)



# Question (Part 2)
# Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko arguments ki tarah le aur fir 
# check kare ki same index waale dono integers even hain ya nahi. Yeh check karne ke liye pichle Part 1 
# mein likhe check_numbers function ka use karo. Agar aapne apne function ko [2, 6, 18, 10, 3, 75] aur 
# [6, 19, 24, 12, 3, 87] Toh usko yeh output deni chaiye:

# (i) list1=[2, 6, 18, 10, 3, 75]
# list2=[6, 19, 24, 12, 3, 87]
# def check_number_list(list1,list2):
#     i=0
#     while i <len(list1):
#             if list1[i]%2==0 and list2[i]%2==0:
#                 print("dono even")
#             else: #list1[i]%2!=0 and list2[i]%2!=0:
#                 print("not odd")
#             i+=1
# check_number_list(list1,list2)


# (ii) method

def check_number_list(num1,num2):
    i=0
    while i<len(num1):
        if num1[i]%2==0 and num2[i]%2==0:
            print("dono even hai")
        else:
            print("dono odd hai")
        i=i+1
check_number_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])
