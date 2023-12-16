A=5

My_Name="Kenna"

B=0.5

print(A)

print(My_Name)

print(B)

C=5
D=10
print(C+D)
print(C*D)
print(C/D)
if C==D:
    print("C=D")
else:
        print("C!=D")
X=5
Y=3
print(X%Y)

is_raining=True
is_cold=True
if is_raining and is_cold:
    print("Today is raining and also is cold.")
else:
    print("Today is sunny and warm.")
    
is_messy=True
is_dirty=False
if is_messy or is_dirty:
    print("The room need to be cleaned.")
else:
    print("The room don't need to be cleaned.")

is_close=True
if not is_close:
    print("The destination is not close.")
else:
    print("The destination is close.")

Z=2
Q=8
if Z==Q:
    print("Z is equal to Q.")
elif Z>Q:
    print("Z is greater than Q.")
else:
    print("Z is less than Q.")

count=1
while count<8:
    print("Number is less than 8.")
    count+=3

Vegetables=["Cucumber","Carrot","Tomato"]
for vegetable in Vegetables:
    print(vegetable +"is good for your health.")

Colors=("green","purple","light blue","white")
for Color in Colors:
    print("We have different colors on this dress,such as:"+ Color+".")

def make_coffee():
    coffee="You delicious coffee is ready."
    print("Hi Miss."+coffee)

make_coffee()
    


        
    
