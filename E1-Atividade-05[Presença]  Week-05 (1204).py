print("Tamando do lado A: ") 
a=input()
print("Tamando do lado B: ")
b=input()
print("Tamando do lado C: ") 
c=input()

if a==0 or b==0 or c==0:
    print(False)
    breakpoint 

L =[a,b,c]
L.sort()

if int(L[2]) > int(L[1])+int(L[0]):
    print("False")

else: print("True")