

a=["n","i","t","i","n"]
# a=["m","a","m","a"]
# a=["2","3","2"]
# a=["2","3","4"]
i=0
b=""
while i<len(a):
    b+=a[i]
    i+=1
print(b)
c=b[::-1]
if b==c:
    print("palendrom")
else:
    print("not palendrom")




# #                ### NUMBER PALENDROM  ###
# a=int(input("enter no"))
# b=a
# reverse=0
# while a>0:
#     reverse=(reverse*10)+(a%10)
#     a=a//10
# if reverse==b:
#         print("its palendron",b)
# else:
#         print("its not a palendron",b)
