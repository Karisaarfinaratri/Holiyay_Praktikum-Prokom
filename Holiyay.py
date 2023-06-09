# membuat fungsi sign up
def sign_up():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # membuka file txt dengna mode "a" dan menambahkan data yang diinputkan oleh user 
    file = open("data_base.txt", "a")
    file.write(f"{username}:{password}\n")
    print("Sign up berhasil!")

# membuat fungsi sign
def sign_in():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # membuka file txt dalam mode "r" dan mengecek kesamaan data input user dan di data_base
    file = open("data_base.txt", "r")
    for line in file:
        stored_username, stored_password = line.strip().split(":")
        if username == stored_username and password  == stored_password:
            print("Sign in berhasil!")
            return
    print("username atau password salah.")

# Test fungsi sign-up dan sign-in 
print("Selamat datang!")
while True:
    print(
    '''Silakan memilih opsi:
    1. Sign up
    2. sign in''')
    pilih = input("Masukkan pilihan (1/2): ")
    if pilih == "1":
        sign_up()
    elif pilih == "2":
        sign_in()
        # Jika login berhasil, keluar dari loop dan lanjutkan ke program selanjutnya
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

#memilih kategori dan lama wisata
print(
'''Silakan memilih kategori:
1. Budget
2. Rating''')
kategori=input("Silakan memilih kategori wisata (1/2): ")
hari=input("silakan memilih berapa lama waktu berwisata (2 hari sampai dengan 4 hari): ")

# jika user memilih kategori budget
if kategori == "1":
    # jika user memilih 2 hari untuk berlibur
    if hari == "2":
        print(
        '''Silakan memilih rentang budget:
        1. Kurang dari Rp 400.000,-
        2. Lebih dari Rp 400.000,-''')
        uang=int(input("masukkan jumlah nomimal budget anda: "))
        #kurang dari Rp 400.000,-
        if uang==1:
            print("berikut tempat wisata yang dapat anda pilih" )
            a = open("tempat_wisata.txt", "r")
            isi_a = a.read()
            print(isi_a)
            a.close()
            print("\nberikut tempat penginapan yang dapat anda pilih")
            # open()
            # while True:
            murah2wisata=input("silahkan memilih tempat wisata: ")
            murah2hotel=input("silahkan memilih tepat penginapan: ")
        #lebih dari Rp400.000,-
        elif uang==2:
            print("berikut tempat wisata yang dapat anda pilih" )
            print(data["wisata"])
            print()
            print("berikut tempat penginapan yang dapat anda pilih")
            print(data["hotel_harga"]["hotel_menengah"])
            menengah2wisata=input("silahkan memilih tempat wisata: ")
            menengah2hotel=input("silahkan memilih tepat penginapan: ")
    # jika user memilih 3 hari untuk berlibur
    elif hari == "3":
        uang=int(input("masukkan jumlah nomimal: "))
        if uang<=600000:
            print("berikut tempat wisata yang dapat anda pilih" )
            print(data["wisata"])
            print()
            print("berikut tempat penginapan yang dapat anda pilih")
            print(data["hotel_harga"]["hotel_murah"])
            murah3wisata=input("silahkan memilih tempat wisata: ")
            murah3hotel=input("silahkan memilih tepat penginapan: ")
        elif uang<=800000:
            print("berikut tempat wisata yang dapat anda pilih" )
            print(data["wisata"])
            print()
            print("berikut tempat penginapan yang dapat anda pilih")
            print(data["hotel_harga"]["hotel_menengah"])
            menengah2wisata=input("silahkan memilih tempat wisata: ")
            menengah2hotel=input("silahkan memilih tepat penginapan: ")
        else:
            print("berikut tempat wisata yang dapat anda pilih" )
            print(data["wisata"])
            print()
            print("berikut tempat penginapan yang dapat anda pilih")
            print(data["hotel_harga"]["hotel_mahal"])
            mahal2wisata=input("silahkan memilih tempat wisata: ")
            mahal2hotel=input("silahkan memilih tepat penginapan: ")
    # jika user memilih 4 hai untuk berlibur
    elif hari =="4":
        uang=int(input("masukkan jumlah nomimal: "))
        if uang<=700000:
            murah4=input("silahkan memilih tempat wisata: ")
        elif uang<=900000:
            menengah4=input("silahkan memilih tempat wisata: ")
        else:
            mahal4=input("silahkan memilih tempat wisata: ")

# jika user memilih kategori berdasarkan rating
elif kategori == "2":
    print(
    '''Silakan memilih rating:
    1. Di atas 4,5
    2. Di atas 4''')
    rating=input("masukkan kategori rating yang anda inginkan (1/2): ")
    #jika user memilih rating di atas 4,5
    if rating == "1":
        if hari == "2":
            a = open("tempat_wisata.txt", "r")
            isi_a = a.read()
            print(isi_a)
            a.close() 
        elif hari == "3":
            a = open("tempat_wisata.txt", "r")
            isi_a = a.read()
            print(isi_a)
            a.close() 
        elif hari == "4":
            a = open("tempat_wisata.txt", "r")
            isi_a = a.read()
            print(isi_a)
            a.close()
    #jika user memilih rating di atas 4 
    elif rating == "2":
        if hari == "2":
            a = open("tempat_wisata.txt", "r")
            isi_a = a.read()
            print(isi_a)
            a.close() 
        elif hari == "3":
            a = open("tempat_wisata.txt", "r")
            isi_a = a.read()
            print(isi_a)
            a.close()
        elif hari == "4":
            a = open("tempat_wisata.txt", "r")
            isi_a = a.read()
            print(isi_a)
            a.close() 