daftar_nilai = (40, 40, 40, 40)

nilai_awal = daftar_nilai[0]

semua_sama = True

for elemen in  daftar_nilai:
    if elemen != nilai_awal:
        semua_sama = False
        break   

print("Hasil elemen:", semua_sama)
