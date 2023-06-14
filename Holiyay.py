# membuat fungsi sign up
def sign_up():
    global username
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # membuka file txt dengan mode "a" dan menambahkan data yang diinputkan oleh user
    file = open("data_base.txt", "a")
    file.write(f"{username}:{password}\n")
    print("Sign up berhasil!")

# membuat fungsi sign in
def sign_in():
    global username
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # membuka file txt dalam mode "r" dan mengecek kesamaan data input user dan di data_base
    file = open("data_base.txt", "r")
    for line in file:
        stored_username, stored_password = line.strip().split(":")
        if username == stored_username and password == stored_password:
            print("Sign in berhasil!")
            return
    print("username atau password salah.")
    sign_in()

#Memilih Pemandu wisata
def pilih_pemandu():
    print('''
    Selamat datang di program pemilihan pemandu wisata!
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

#Mencentak Struk Pembayaran

def cetak_struk_holiyay(
        username, tempat_wisata, harga_tempat_wisata, hotel_pilihan, harga_per_malam, tour_guide, harga_pemandu, hari, harga_total, input_biaya
    ):
    print("="*35)
    print("          STRUK HOLIYAY             ")
    print("="*35)
    print("Username           :", username)
    print("Tempat Wisata      : ", tempat_wisata)
    print("Harga Tempat Wisata: ", harga_tempat_wisata)
    print("Nama Hotel         : ", hotel_pilihan)
    print("Harga per Malam    : ", harga_per_malam)
    print("Jumlah hari        : ", tour_guide)
    print("Tour Guide         : ", harga_pemandu)
    print("Harga Tour Guide   : ", hari)
    print("-"*35)
    print("Total Biaya        : ", harga_total)
    print("Biaya yang dibayar : ", input_biaya)
    print("="*35)
    print("\nTerima kasih sudah menggunakan program kami")
