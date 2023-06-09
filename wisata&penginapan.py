import csv
print("===="*20)
def buka_wisata(wisata):
    with open('datakost.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if i[1] == wisata:
                print(f"Nama Tempat Wisata: {i[1]} dengan tiket masuk: {i[0]} memiliki rating: {i[2]}")
            return True
        return False
           