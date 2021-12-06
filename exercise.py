
nama = input("Masukan Nama Anda: ") # default string
umur = int(input("Masukan umur Anda: "))

print(type(umur))

print("nama saya adalah: " + nama)


# Menghitung luas persegi panjang dan String formating
p = int(input("Masukan panjang: "))
l = int(input("Masukan lebar: "))
L =  p * l
K = (p+l)*2
print("Maka Luas Persegi Panjang adalah {} cm^2 dan Kelilingnya adalah {} cm".format(L, K))


# String operation
x = "Indonesia"
y = "AI"
print(x + " " + y)

a = "Halo, Dunia!"
print(a[3])
print(a[2:8]) # mulai dari 2 sampai 7
print(len(a))
print(a[0] + " " + a[2]) # Menampilkan H dan l

warna = input("Masukan warna: ") # merah muda dan biru
print(warna[-5:])

# Quiz
x = "Indonesia AI"
print(x[2:4]) # karakter 2-3
print(len(x))

x = str(23456789)
print(x[0])

# Boolean (True and False)
print(8 < 9)
print(8 > 9)

# Condition
a = 200
b = 200
if b < a:
   print("a is greater than b")
elif b == a:
   print("a equals b")
else: # b > a
   print("b is greater than a")

nilai = int(input("Masukan nilai Anda: "))
kkm = 70

if nilai > kkm:
   print("Anda lulus")
elif nilai == kkm:
   print("Anda lulus")
else:
   print("Anda mengulang")


b = 200
a = 33
if b > a:
    print("b is greater than a")
if b >= a:
    print("b is greater than or equal to a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")

# List
x = 7
y = [1, 2, 3, 4, 5]
print(y[0]+y[1])

makanan = ["soto", "mie ayam", "sate"]

makanan.append("bakso")
print(makanan[10])


# mengganti minuman
minuman = ["esteh", "es jeruk", "syrup", ]

minuman[0] = input("Minuman pengganti: ")

print(minuman)

# hanya print bilangan genap
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in angka:
   if x % 2 == 0:
      print(x)

# Quiz
c = 3 
a = c
b = c + 1
if b > a:
   print("b is greater than a")
elif c == b:
   print("c is same like b")
else :
   print('other')


tinggi = float(input("masukan tinggi badan: "))
berat = float(input("masukan berat badan: "))

tinggi_normal = 160
berat_normal = 60

if tinggi >= tinggi_normal and berat >= berat_normal:
   print("Anda sehat")
elif tinggi < tinggi_normal and berat >= berat_normal:
   print("Anda kurang tinggi")
elif tinggi >= tinggi_normal and berat < berat_normal:
   print("Anda kurang berat")
else:
   ("Anda kurang sehat")

# Gerbang Logika
print(True and True) #True
print(True and False) #False
print(False and True) # False
print(False and False) # False

print(True or True) #True
print(True or False) #True
print(False or True) # True
print(False or False) # False

