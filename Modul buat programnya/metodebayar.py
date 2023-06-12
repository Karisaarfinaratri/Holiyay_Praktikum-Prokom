# input jenis pembayaran
while True:
    print(
        '''\nSilahkan memilih jenis pembayaran:
        1. Bank BRI
        2. Bank BCA
        3. Bank Mandiri''')
    jenis_pembayaran = int(input("Masukkan jenis pembayaran: "))
    input_biaya = int(input("Masukkan biaya sesuai total: "))

    konfirmasi_pembayaran = input("Apakah Anda setuju dengan pembayaran tersebut? (ya/tidak) ")