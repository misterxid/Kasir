def menu ():
print (“—– MENU —–“)
print (“1. KASIR”)
print (“2. KALKULATOR”)
print (“—————-“)
pilih = input(“Pilih menu : “)
if pilih == “1”:
kasir()
elif pilih == “2”:
kalkulator()
else:
exit
tanya()

def kasir():
nm_brng=input(“Masukan Nama Barang = “)
harga=int(input(“Masukan Harga Barang = “))
jmlbeli=int(input(“Masukan Jumlah Beli = “))
total=harga*jmlbeli
print(“Total Harga”, nm_brng, “Adalah Rp.”,total)
cast=int(input(“masukan pembayaran = “))
hu=total-cast
kmbl=cast-total
if(cast>total):
print(“Jumlah Kembalian anda adalah Rp.”,kmbl)

print(“Rincian kembalian adalah “)
d = [100000, 50000, 20000, 10000, 5000, 1000, 500, 200, 100, 50]
for x in range (0, 10):
i=0 
while kmbl >= d[x]:
kmbl = kmbl – d[x]
i = i+1
if (i>0):
print (“Uang Rp. %d sebanyak %d lembar” %(d[x], i))
else:
print (“Selesai”)
tanya()

else:
print(“Anda memiliki Hutang sebesar Rp.”,hu)

tanya()

def kalkulator():
print (“— KALKULATOR —“)
print (“1. (+) 3. (*)”)
print (“2. (-) 4. (/)”)
print (“5. (%) 6. (**)”)
print (“——————“)
operasi = input(“Pilih operasi : “)
a = int(input(“a : “))
b = int(input(“b : “))
if operasi == “1”:
print (“Hasil = “,a+b)
elif operasi == “2”:
print (“Hasil = “,a-b)
elif operasi == “3”:
print (“Hasil = “,a*b)
elif operasi == “4”:
print (“Hasil = “,a/b)
elif operasi == “5”:
print (“Hasil = “,a%b)
elif operasi == “6”:
print (“Hasil = “,a**b)
else:
print (“ERROR”)
tanya()

def tanya():
tanya = input(“Kembali ke menu (y/t)? “)
if tanya == “y”:
menu()
elif tanya == “t”:
exit
else:
print (“Salah input”)

username = input(“Username : “)
password = input(“Password : “)
if username == “mahend” and password == “12131415”:
menu()
else:
print (“LOGIN GAGAL”)
