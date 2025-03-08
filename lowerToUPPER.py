s = input("Enter a string:")
os = ''
for i in s:
    if i.isupper():
        o = i.lower()
    elif i.islower():
        o = i.upper()
    else:
        o = i
    os += o
    
print(os)
