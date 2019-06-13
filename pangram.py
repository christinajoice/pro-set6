import string
str=input()
str=str.lower()
li=list(string.ascii_lowercase[0:26])
flag=1
for i in li:
  if i not in str:
    flag=0
if flag==0:
  print("no")
else:
  print("yes")
