# from csv import writer, reader

# def A():
#     print(f'''Berikut Kriteria Pemandu A :
#             1. Memiliki kemampuan 2 bahasa asing (bahasa inggris dan bahasa Italia)
#             2. Sudah pernah menjelajahi keseluruhan Pulau Bali
#             3. Mengetahui tempat kuliner yang enak di Bali
#             4. Biaya Tourguide A adalah Rp 100.000,-''')
     
# def B():
#     print(f'''Berikut Kriteria Pemandu B :
#             1. Fasih dalam berbahasa daerah Bali
#             2. Mengetahui sejarah dan adat istiadat Bali
#             3. Tahu tempat diving yang bagus di Bali
#             4. Biaya Tourguide B adalah Rp 90.000,-''')
    
# def C():
#      print(f'''Berikut Kriteria Pemandu C :
#             1. Menguasai 3 jenis bahasa asing (bahasa inggris, bahasa chinese, bahasa spanyol)
#             2. Sudah kenal dekat dengan beberapa pemiliki wisata di Bali
#             3. Tahu tempat berbelanja oleh-oleh di Bali
#             4. Biaya Tourguide C adalah Rp 120.000,-''')
     

# def pilih_pemandu():
#     print('''
#     Selamat datang di program pemilihan pemandu wisata!
#     ✿ ♡＾▽ ＾♡ ✿
#     Disini anda akan diminta memilih salah satu pemandu wisata selama berada di Bali
#     Apakah anda ingin melihat detail kriteria pemandu :
#     1. Ya
#     2. Tidak
#     Note : cukup masukkan (1/2)''')
#     kriteria = input("Masukkan pilihan Anda: ")
# #Pemandu Wisata A
#     if kriteria == "1":
#         A()
#         print('''
#         1. Ya
#         2. Tidak''')
#         setuju = input("Apakah Anda setuju dengan pemandu A? (1/2): ")

#         if setuju == "1":
#                 print("Anda memilih pemandu A")
#                 print("(っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )")
#         elif setuju == "2":
#                 print("Anda tidak setuju dengan pemandu A. Silahkan pilih pemandu berikutnya.")
                    
# #Pemandu Wisata B
#     elif kriteria == "2":
#         print('''
#         1. Ya
#         2. Tidak''')
#         setuju = input("Apakah Anda setuju dengan pemandu A? (1/2): ")    
#         B()        
            

#         if setuju == "1":
#                 print("Anda memilih pemandu B")
#                 print("(っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )")
#                 print("Selamat data Anda telah disimpan.")
#         else:
#                 print("Anda tidak setuju dengan pemandu B. Silahkan pilih pemandu berikutnya.")
# #Pemandu Wisata C 
#     elif kriteria == "3":
#         C()
#         print('''
#         1. Ya
#         2. Tidak''')
#         setuju = input("Apakah Anda setuju dengan pemandu A? (1/2): ")
            
            

#         if setuju == '1':
#                 print("Anda memilih pemandu C")
#                 print("(っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )")
#                 print("Selamat data Anda telah disimpan.")
#                 exit()

#     else:
#         print("Pilihan tidak valid. Silahkan pilih antara A, B, atau C.")

#         print("Selamat Anda telah berhasil memilih pemandu")


# # Menjalankan program
# pilih_pemandu()

# def pilih_pemandu():
#     print("Selamat datang di program pemilihan pemandu wisata!")
#     print("✿ ♡＾▽ ＾♡ ✿")
#     print("Disini anda akan diminta memilih salah satu pemandu wisata selama berada di Bali")
#     print("Silahkan pilih pemandu Anda:")
#     print("Pemandu A (100000)")
#     print("Pemandu B (100000)")
#     print("Pemandu C (150000)")

#     pemandu_dict = {}
#     pemandu_terpilih = None
#     harga_pemandu = None

#     while pemandu_terpilih is None:
#         pilihan = input("Masukkan pilihan Anda: ").upper()

#         if pilihan == "A":
#             print("Anda memilih pemandu A.")
#             setuju = input("Apakah Anda setuju dengan pemandu A? (ya/tidak): ").lower()

#             if setuju == "ya":
#                 pemandu_terpilih = "A"
#                 harga_pemandu = 100000
#             else:
#                 print("Anda tidak setuju dengan pemandu A. Silakan pilih pemandu berikutnya.")

#         elif pilihan == "B":
#             print("Anda memilih pemandu B.")
#             setuju = input("Apakah Anda setuju dengan pemandu B? (ya/tidak): ").lower()

#             if setuju == "ya":
#                 pemandu_terpilih = "B"
#                 harga_pemandu = 100000
#             else:
#                 print("Anda tidak setuju dengan pemandu B. Silakan pilih pemandu berikutnya.")

#         elif pilihan == "C":
#             print("Anda memilih pemandu C.")
#             setuju = input("Apakah Anda setuju dengan pemandu C? (ya/tidak): ").lower()

#             if setuju == "ya":
#                 pemandu_terpilih = "C"
#                 harga_pemandu = 100000
#             else:
#                 print("Maaf tidak ada Pemandu Wisata  yang cocok dengan anda")
#         else:
#             print("Pilihan tidak valid. Silakan pilih antara A, B, atau C.")

#     print("Selamat Anda telah berhasil memilih pemandu", pemandu_terpilih)

#     pemandu_dict["pemandu_terpilih"] = pemandu_terpilih
#     pemandu_dict["harga_pemandu"] = harga_pemandu

#     return pemandu_dict

def pilih_pemandu():
    print('''Selamat datang di program pemilihan pemandu wisata!
    ✿ ♡＾▽ ＾♡ ✿
    Disini anda akan diminta memilih salah satu pemandu wisata selama berada di Bali
    Silahkan pilih pemandu Anda:
    1. Pemandu A
       Berikut Kriteria Pemandu A :
        1. Memiliki kemampuan 2 bahasa asing (bahasa inggris dan bahasa Italia)
        2. Sudah pernah menjelajahi keseluruhan Pulau Bali
        3. Mengetahui tempat kuliner yang enak di Bali
        4. Biaya Tourguide A adalah Rp 100.000,-
    2. Pemandu B
       Berikut Kriteria Pemandu B :
        1. Fasih dalam berbahasa daerah Bali
        2. Mengetahui sejarah dan adat istiadat Bali
        3. Tahu tempat diving yang bagus di Bali
        4. Biaya Tourguide B adalah Rp 80.000,-
    3. Pemandu C
       Berikut Kriteria Pemandu C :
            1. Menguasai 3 jenis bahasa asing (bahasa inggris, bahasa chinese, bahasa spanyol)
            2. Sudah kenal dekat dengan beberapa pemiliki wisata di Bali
            3. Tahu tempat berbelanja oleh-oleh di Bali
            4. Biaya Tourguide C adalah Rp 120.000,-''')

    pemandu_dict = {}
    pemandu_terpilih = None
    harga_pemandu = None

    while pemandu_terpilih is None:
        pilihan = input("Masukkan pilihan Anda (1/2/3): ")

        if pilihan == "1":
            print("Anda memilih pemandu A.")
            pemandu_terpilih = "A"
            harga_pemandu = 100000

        elif pilihan == "2":
            print("Anda memilih pemandu B.")
            pemandu_terpilih = "B"
            harga_pemandu = 800000
            
        elif pilihan == "3":
            print("Anda memilih pemandu C.")
            pemandu_terpilih = "C"
            harga_pemandu = 120000
           
        else:
            print("Pilihan tidak valid. Silakan pilih antara A, B, atau C.")

    print("Selamat Anda telah berhasil memilih pemandu", pemandu_terpilih)

    pemandu_dict["pemandu_terpilih"] = pemandu_terpilih
    pemandu_dict["harga_pemandu"] = harga_pemandu

    return pemandu_dict

