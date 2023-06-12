import csv

def main():
    global daftar_hotel
    print(
    '''Silakan memilih jumlah hari:
    1. 2 hari
    2. 3 hari
    3. 4 hari''')
    hari=input("hari (1/2/3): ")
    with open("D:/Matkul Prokom/TUBES PROKOM/Holiyay_Praktikum-Prokom/List_Hotel.txt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        if hari == "1":
            daftar_hotel=[]
            print('''silakan memilih rentang budget anda: 
            1. < Rp 600.000,-
            2. > RP 600.000,-''')
            budget=input("budget (1/2): ")
            if budget == "1":
                for i in csv_reader:
                        if int(i[1]) <= 220000  :
                            daftar_hotel.append(i)
                            print(f'''
{i[0]}. Nama Hotel: {i[2]}
    Harga/malam: {i[1]}
    Rating: {i[3]}''')      

            elif budget == "2":
                 for i in csv_reader:
                        if int(i[1]) >= 230000  :
                            daftar_hotel.append(i)
                            print(f'''
{i[0]}. Nama Hotel: {i[2]}
    Harga/malam: {i[1]}
    Rating: {i[3]}''')   
                            
        elif hari == "2":
            daftar_hotel=[]
            print('''silakan memilih rentang budget anda: 
            1. < Rp 800.000,-
            2. > RP 800.000,-''')
            budget=input("budget (1/2): ")
            if budget == "1":
                for i in csv_reader:
                        if int(i[1]) <= 220000  :
                            daftar_hotel.append(i)
                            print(f'''
{i[0]}. Nama Hotel: {i[2]}
    Harga/malam: {i[1]}
    Rating: {i[3]}''')                            
            elif budget == "2":
                 for i in csv_reader:
                        if int(i[1]) >= 220000  :
                            daftar_hotel.append(i)
                            print(f'''
{i[0]}. Nama Hotel: {i[2]}
    Harga/malam: {i[1]}
    Rating: {i[3]}''')
         
        elif hari == "3":
            daftar_hotel=[]
            print('''silakan memilih rentang budget anda: 
            1. < Rp 1.000.000,-
            2. > RP 1.000.000,-''')
            budget=input("budget (1/2): ")
            if budget == "1":
                for i in csv_reader:
                        if int(i[1]) <= 220000  :
                            daftar_hotel.append(i)
                            print(f'''
{i[0]}. Nama Hotel: {i[2]}
    Harga/malam: {i[1]}
    Rating: {i[3]}''')   
            elif budget == "2":
                 for i in csv_reader:
                        if int(i[1]) >= 220000  :
                            daftar_hotel.append(i)
                            print(f'''
{i[0]}. Nama Hotel: {i[2]}
    Harga/malam: {i[1]}
    Rating: {i[3]}''')   
        
if __name__ == "__main__":
#     main()
#     pilihan=[]
#     pilihan = input("\nSilakan memilih tempat wisata berdasarkan nomor (1/2..16/18..): ")

    main()
ind_hotel = [ele[0] for ele in daftar_hotel]
for ele in daftar_hotel:
    # print(ele)

    while True:
        try:
            pilihan = input("Input hotel pilihan ")
            assert pilihan in ind_hotel, "Hotel tidak ada pada filter"
            break
        except AssertionError as er:
            print(er)

    print("Hotel terpilih")
    print(daftar_hotel[int(pilihan)-1])
    break

