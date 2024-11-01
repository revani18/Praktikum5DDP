# 2. Buat program python dengan match case untuk 
# mengitung luas bangun datar :
# jika pilih 1, maka menghitung luas persegi  
# jika pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga 
# selain pilihan di atas, maka keterangan : salah pilih angka
# Match Case - Perhitungan Luas - Luas Persegi, Luas Lingkaran, Luas Segitiga

hitung_luas = int(input("""Pilih Salah Satu:
1. Hitung Luas Persegi
2. Hitung Luas Lingkaran
3. Hitung Luas Segitiga
Masukkan Pilihan (1/2/3) : 
"""))

match hitung_luas :
    case 1 :
        print('Menghitung Luas Persegi')
        sisi = int(input('Masukkan Nilai Sisi : '))
        hitung_luas_persegi = sisi**2
        print(f'Jadi Luas Persegi dengan sisi {sisi} cm adalah {hitung_luas_persegi} cm^2' )
    case 2 :
        print('Menghitung Luas Lingkaran')
        phi = 3.14
        r = int(input('Masukkan Nilai jari-jari : '))
        hitung_luas_lingkaran = phi*r*r
        print(f'Jadi Luas Lingkaran dengan jari-jari {r} cm adalah {hitung_luas_lingkaran} cm^2')
    case 3 :
        print('Menghitung Luas Segitiga')
        alas = int(input('Masukkan Panjang Alas Segitiga : '))
        tinggi = int(input('Masukkan Tinggi Segitiga : '))
        hitung_luas_segitiga = 1/2*alas*tinggi
        print(f'Jadi Luas Segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah {hitung_luas_segitiga} cm^2')
    case _ :
        print('Pilihan Tidak Valid')