from csv import writer, reader

def pilih_pemandu():
    print("Selamat datang di program pemilihan pemandu wisata!")
    print("✿ ♡＾▽ ＾♡ ✿")
    print("Disini anda akan diminta memilih salah satu pemandu wisata selama berada di Bali")
    print("Silahkan pilih pemandu Anda:")
    print("Pemandu A")
    print("Pemandu B")
    print("Pemandu C")
    print("Note : cukup masukkan (A,B,atau C)")

    pilihan = input("Masukkan pilihan Anda: ").upper()
#Pemandu Wisata A
    harga=100000
    if pilihan == "A":
            
            print(f'''Berikut Kriteria Pemandu A :
            1. Memiliki kemampuan 2 bahasa asing (bahasa inggris dan bahasa Italia)
            2. Sudah pernah menjelajahi keseluruhan Pulau Bali
            3. Mengetahui tempat kuliner yang enak di Bali
            4. Biaya Tourguide A adalah {harga}''')

            setuju = input("Apakah Anda setuju dengan pemandu A? (ya/tidak): ").lower()

            if setuju == "ya":
                with open("input_pemandu.csv", "a", newline='') as f:
                     tulis = writer(f)
                     tulis.writerow([f" Pemandu A:{100000}"])
                print("Anda memilih pemandu A")
                print("(っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )")
                print("Selamat data Anda telah disimpan.")
            else:
                print("Anda tidak setuju dengan pemandu A. Silahkan pilih pemandu berikutnya.")
                    
#Pemandu Wisata B
    elif pilihan == "B":
            print(f'''Berikut Kriteria Pemandu B :
            1. Fasih dalam berbahasa daerah Bali
            2. Mengetahui sejarah dan adat istiadat Bali
            3. Tahu tempat diving yang bagus di Bali
            4. Biaya Tourguide B adalah {harga}''')
                  
            setuju = input("Apakah Anda setuju dengan pemandu B? (ya/tidak): ").lower()

            if setuju == "ya":
                with open("input_pemandu.csv", "a", newline='') as f:
                     tulis = writer(f)
                     tulis.writerow([f"Pemandu B:{100000}"])
                print("Anda memilih pemandu B")
                print("(っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )")
                print("Selamat data Anda telah disimpan.")
            else:
                print("Anda tidak setuju dengan pemandu B. Silahkan pilih pemandu berikutnya.")
#Pemandu Wisata C 
    elif pilihan == "C":
 
            print(f'''Berikut Kriteria Pemandu C :
            1. Menguasai 3 jenis bahasa asing (bahasa inggris, bahasa chinese, bahasa spanyol)
            2. Sudah kenal dekat dengan beberapa pemiliki wisata di Bali
            3. Tahu tempat berbelanja oleh-oleh di Bali
            4. Biaya Tourguide C adalah {harga}''')
            setuju = input("Apakah Anda setuju dengan pemandu C? (ya/tidak): ").lower()

            if setuju.lower() == 'ya':
                print("Terima kasih telah menggunakan program.")
                with open("input_pemandu.csv", "a", newline='') as f:
                     tulis = writer(f)
                     tulis.writerow([f"Pemandu C:{100000}"])
                print("Anda memilih pemandu C")
                print("(っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )")
                print("Selamat data Anda telah disimpan.")
                exit()

    else:
        print("Pilihan tidak valid. Silahkan pilih antara A, B, atau C.")

        print("Selamat Anda telah berhasil memilih pemandu")


# Menjalankan program
pilih_pemandu()