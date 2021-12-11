# for in list

# fruits = [4,2,5]

#for x in fruits : # all
#    print(x)

# for in range

#x = range(6)
#for  n in x:
#    print(n)

#for c in range(1, 4, 0.5):
 #   print(c)

#nama = []
#jumlah = int(input("masukkan jumlah yg dipengenin : "))

#for x in range(jumlah):
#   nama.append(input("masukkan nama ke {} : ".format(x+1)))

#for x in nama:
#   print(x)

#for x in range(1, jumlah+1):
#    print(nama[:x])

i = 1
while i < 6:
    print(i, end=" ")
    i += 0.5
print(" ")
print(" ")

#break
#for x in range(7):
 #  print(x)  
#   if x == 4:
#      break

#for i in range(2):
#   for j in range(3):
#      print("ini baris ke {} dan kolom ke {}".format(i,j))

#for i in range(2):
   #for j in range(3):
  #       print("i:{},j:{}".format(i,j) ,end=" 22")
 #  print("###")

#for x in range(3):
 #  for y in range(3):
#      print(x, y)
#   print("###")

x = [1,2,3,4,5]
y = [2,4,3,5,6]
z = 0

for i in x:
   for j in y:
      if i == j :
         z = z+1

print(z)