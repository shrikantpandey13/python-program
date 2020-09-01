ch = input(“Enter any character: “);

if((ch>=’a’ and ch<=’z’) or (ch>=’A’ and ch<=’Z’)):
    print(ch,end = ” “)
    print(“is an alphabet”)
else:
    print(ch,end = ” “)
    print(“is not an alphabet”)
    
    
    
    
ch = input(“Enter any character: “);

if((ord(ch)>=97 and ord(ch)<=122) or (ord(ch)>=65 and ord(ch)<=90)):
print(ch,end = ” “)
print(“is an alphabet”)
else:
print(ch,end = ” “)
print(“is not an alphabet”)
