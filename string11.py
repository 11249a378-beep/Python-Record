str="apple mango apple orange apple orange mango"
str=str.split()
str1=[]
for i in str:
    if i not in str1:
        str1.append(i)
for i in range(0,len(str1)):
    print("frequency of",str1[i],'is:' ,str.count(str1[i]))


