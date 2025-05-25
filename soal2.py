data = ('Sandy Rehan Linta', '71241144', 'Yogyakarta, DIY') 

print("Data:", data)
print()

nama = data[0]
nim = data[1]
alamat = data[2]

 
print("NIM :", nim)
print("NAMA :", nama)
print("ALAMAT :", alamat)

nim_tuple = tuple(nim)
print("NIM:", nim_tuple)

nama_depan = nama.split()[0]
nama_depan_tuple = tuple(nama_depan.lower())
print("NAMA DEPAN:", nama_depan_tuple)

nama_terbalik = tuple(nama.split()[::-1])
print("NAMA TERBALIK:", nama_terbalik)
