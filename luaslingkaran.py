def hitung_luas_lingkaran():
    print ("_______________________________________________________")
    print ("program ini sangat membantu untuk hitung menghitung")
    print ("gunakan program dengan bijak")
    print ("Terimakasih")
    print ("_______________________________________________________") 
    print ("Menghitung luas lingkaran")
    radius = int(input("jari-jari = "))
    luas = 22/7 * radius * radius
    print (("Luas= "), luas)

def hitung_luas_persegi_panjang():
    print ("Menghitung Luas Persegi Panjang")
    panjang = int(input("panjang= "))
    lebar = int(input("lebar= "))
   
    luas = panjang*lebar
    print (("Luas="), luas)
   


#Program Utama
print ("Menghitung luas")
print ("1. Lingkaran")
print ("2. Persegi panjang")

pilihan = int(input("pilihan(1 atau 2): "))
if pilihan == 1:
    hitung_luas_lingkaran()
elif pilihan == 2:
    hitung_luas_persegi_panjang()
else:
        print ("Pilihan salah")