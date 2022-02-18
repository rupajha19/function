# def add_numbers(num1,num2):
#     print(num1+num2)
# add_numbers(56,12)




# add_numbers_list naam ka function likhiye jo do integers ki 2 lists leta ho aur fir same position wale 
# integers ka sum print karta ho. Same position waale 2 integers ka sum karne ke liye Part 1 mein di gayi
#  add_numbers waale function ka use karo. Jaise agar hum iss function ko [50, 60, 10] aur [10, 20, 13] 
#  denge ko woh yeh print karega

def add_numbers(list1,list2):
    i=0
    k=[]
    sum=0
    while i<len(list1):
        j=0
        while j<len(list2):
            if i==j:
                k.append(list1[i]+list2[i])
            j+=1
        i+=1
    print(k)

                

add_numbers([50,60,10],[10,20,13])

