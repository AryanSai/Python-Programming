hex = input("Enter the Hexadecimal string: ")

binary = "{0:b}".format(int(hex, 16)).zfill(len(hex)*4)

print ("The Binary string is: ",binary)

n,i,x,b,p,e=binary[6],binary[7],binary[8],binary[9],binary[10],binary[11]

print("n=%s i=%s x=%s b=%s p=%s e=%s" %(n,i,x,b,p,e))

if b == "1":
  print("Base Relative Addressing")
if p == "1":
  print("PC Relative Addressing")
if p == "0" and b == "0":
  print("Direct Addressing")
if x == "1":
  print("Indexed Addressing")

if e == "0":
  print("Format 3")
else:
  print("Format 4") 

if n == "0" and i == "1":
  print("Immediate Addressing")
elif n == "1" and i == "0":
  print("Indirect Addressing") 
  