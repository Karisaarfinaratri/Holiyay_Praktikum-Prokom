import csv
print("===="*20)
def buka_wisata(hotel):
    with open("List_hotel.txt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if i[0] == hotel:
                print(f'''Nama Hotel: {i[1]}, dengan Harga/malam: {i[0]}, memiliki rating: {i[2]}''')
            return True
        return False

def main():
    hari=input("hari: ")
    print('''silakan memilih rentang budget anda: 
            1. < Rp 600.000,-
            2. > RP 600.000,-''')
    budget=input("budget (1/2): ")
    with open("List_hotel.txt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        daftar_hotel=[]

        if hari == 2:
            if budget == 1:
                for i in csv_reader:
                        if int(i[0]) < 250000  :
                            daftar_hotel.append(i)
                            print(f'{i[0]}. {i[1]}')

if __name__ == "__main__":
    main()
