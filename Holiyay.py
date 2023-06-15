import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def sign_up():
    global username
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    file = open("data_base.txt", "a")
    file.write(f"{username}:{password}\n")
    print("Sign up berhasil!")

def sign_in():
    global username
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    file = open("data_base.txt", "r")
    for line in file:
        stored_username, stored_password = line.strip().split(":")
        if username == stored_username and password == stored_password:
            print("Sign in berhasil!")
            return
    print("username atau password salah.")
    sign_in()

def keluar():
     print("Terima Kasih sudah menggunakan Holiyay")
     exit()

def get_filtered_tempat_wisata_dan_hotel(cek_total_harga):
    tempat_wisata_dan_hotel_dict = {}
    tempat_wisata_list = []
    hotel_list = []
    filtered_tempat_wisata_list = []
    filtered_hotel_list = []

    with open("tempat_wisata.txt", "r") as file:
        tempat_wisata_reader = csv.reader(file, delimiter=',')
        next(tempat_wisata_reader)

        for row in tempat_wisata_reader:
            tempat_wisata_list.append(row)

    with open("hotel.txt", "r") as file:
        hotel_reader = csv.reader(file, delimiter=',')
        next(hotel_reader)

        for row in hotel_reader:
            hotel_list.append(row)

    tempat_wisata_list.sort(key=lambda element: int(element[0]))
    hotel_list.sort(key=lambda element: int(element[0]))

    for tempat_wisata in tempat_wisata_list:
        for hotel in hotel_list:
            if cek_total_harga(int(tempat_wisata[0]) + int(hotel[0])):
                if not tempat_wisata in filtered_tempat_wisata_list:
                    filtered_tempat_wisata_list.append(tempat_wisata)
                
                if not hotel in filtered_hotel_list:
                    filtered_hotel_list.append(hotel)
            else:
                if int(hotel[0]) > int(tempat_wisata[0]):
                    if hotel in filtered_hotel_list:
                        filtered_hotel_list.remove(hotel)
                else:
                    if tempat_wisata in filtered_tempat_wisata_list:
                        filtered_tempat_wisata_list.remove(tempat_wisata)

    tempat_wisata_dan_hotel_dict ["tempat_wisata"] = filtered_tempat_wisata_list
    tempat_wisata_dan_hotel_dict ["hotel"] = filtered_hotel_list

    return tempat_wisata_dan_hotel_dict

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


def menu_awal():
    print("Selamat datang di Holiyay!")
    while True:
        try:
            print(
'''Silakan memilih opsi:
1. Sign up
2. Sign in''')
            pilih = input("Masukkan pilihan (1/2): ")
            if pilih == "1":
                sign_up()
            elif pilih == "2":
                sign_in()
                break
            else:
                raise ValueError("\nPilihan yang dimasukkan tidak valid, silakan pilih 1 atau 2.")
            
           
        
        except ValueError as e:
            print("#404 Not Found#", str(e))
            continue
menu_awal()


while True:
    try:
        print(
'''\nSilakan memilih jumlah hari:
2 hari
3 hari
4 hari''')
        hari = int(input("Silakan memilih berapa lama waktu berwisata (2/3/4): "))
        
        if hari not in [2, 3, 4]:
            raise ValueError("\nPilihan jumlah hari yang dimasukkan tidak valid, silakan memilih jumlah hari 2, 3, atau 4.")
        
        # Lanjutkan dengan program selanjutnya
        break
    
    except ValueError as e:
        print("#404 Not Found#", str(e))