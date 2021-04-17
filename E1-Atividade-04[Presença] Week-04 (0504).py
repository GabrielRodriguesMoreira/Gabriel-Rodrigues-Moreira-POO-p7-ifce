print("Tamando do lado A: ") 
a=input()
print("Tamando do lado B: ")
b=input()
print("Tamando do lado C: ") 
c=input()

if b == a :
    iso=True
else: iso=False

if c == b or c == a:
    iso2=True
else : iso2=False

if iso==True and iso2==True:
    print("Triângulo equilátero")
elif iso==True or iso2==True:
    print("Triângulo isósceles")
else: 
    print("Triângulo escaleno")