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
    main()

ind_hotel = [ele[0] for ele in daftar_hotel]
for ele in daftar_hotel:
    # print(ele)

    # while True:
        try:
            pilihan = input("Input hotel pilihan ")
            assert pilihan in ind_hotel, "Hotel tidak ada pada filter"
            break
        except AssertionError as er:
            print(er)

print("Hotel terpilih")
print(daftar_hotel[int(pilihan)-1])
    

# def wisata():
#     global daftar_wisata
print(
    '''Silakan memilih jumlah tempat wisata:
    1. 1 tempat
    2. 2 tempat
    3. 3 tempat
    4. 4 tempat''')
jumlah=input("jumlah tempat (1/2/..): ")
with open("D:\Matkul Prokom\TUBES PROKOM\Holiyay_Praktikum-Prokom\List_Tempat_Wisata.txt") as csv_file2:
        csv_reader2 = csv.reader(csv_file2, delimiter=',')

        if jumlah =="1":
            daftar_wisata=[]
            for j in csv_reader2:
                        daftar_wisata.append(j)
                        print(f'''
{j[0]}. Nama Hotel: {j[2]}
    Harga/malam: {j[1]}
    Rating: {j[3]}''')  
                        
            pilih1=input("silakan memilih tempat pertama: ")

        elif jumlah =="2":
            daftar_wisata=[]
            for j in csv_reader2:
                        daftar_wisata.append(j)
                        print(f'''
{j[0]}. Nama Hotel: {j[2]}
    Harga/malam: {j[1]}
    Rating: {j[3]}''')  
            pilih1=input("silakan memilih tempat pertama: ")
            pilih2=input("silakan memilih tempat kedua: ")

        elif jumlah =="3":
            daftar_wisata=[]
            for j in csv_reader2:
                        daftar_wisata.append(j)
                        print(f'''
{j[0]}. Nama Hotel: {j[2]}
    Harga/malam: {j[1]}
    Rating: {j[3]}''')  
            pilih1=input("silakan memilih tempat pertama: ")
            pilih2=input("silakan memilih tempat kedua: ")
            pilih3=input("silakan memilih tempat ketiga: ")

        elif jumlah =="4":
            daftar_wisata=[]
            for j in csv_reader2:
                        daftar_wisata.append(j)
                        print(f'''
{j[0]}. Nama Hotel: {j[2]}
    Harga/malam: {j[1]}
    Rating: {j[3]}''')  
            pilih1=input("silakan memilih tempat pertama: ")
            pilih2=input("silakan memilih tempat kedua: ")
            pilih3=input("silakan memilih tempat ketiga: ")
            pilih4=input("silakan memilih tempat keempat: ")
                   
# if __name__ == "__main__":
    # main()
