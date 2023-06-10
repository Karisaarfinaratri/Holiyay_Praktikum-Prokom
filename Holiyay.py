

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
        '''Silahkan memilih rentang budget:
        1. Kurang dari Rp 400.000,-
        2. Lebih dari Rp 400.000,-''')
        uang=int(input("masukkan jumlah nominal budget anda: "))
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
        uang=int(input("masukkan jumlah nominal: "))
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
    # jika user memilih 4 hari untuk berlibur
    elif hari =="4":
        uang=int(input("masukkan jumlah nominal: "))
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