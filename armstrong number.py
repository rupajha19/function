def num():
    num=int(input("enter any number::"))
    i=num
    sum=0
    while i>0:
        sum=sum+(i%10)*(i%10)*(i%10)
        i=i//10
    if num==sum:
        print("its harshad number")
    else:
        print("its not harshad number")
num()