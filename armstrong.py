n=input('enter the number')
ln=len(n)
s=0
for i in n:
    s+=int(i)**ln
if int(n)==s:
    print("armstrong number")
else:
    print("its not a armstrong number")
