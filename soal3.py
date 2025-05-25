nama_file = input("Masukan nama file:")

try:
    file = open(nama_file)
except:
    print("file tidak ditemukan.")
    quit()

jumlah_per_jam = {}

for baris in file:
    if baris.startswith("From "):
        kata = baris.split()
        waktu = kata[5]
        jam = waktu[:2]

        if jam in jumalah_per_jam:
            jumlah_per_jam[jam] += 1
        else:
            jumlah_per_[jam] = 1

hasil_urut = sorted(jumlah_per_jam.items())
for jam, jumlah in hasil_urut:
    print(jam, jumlah)
