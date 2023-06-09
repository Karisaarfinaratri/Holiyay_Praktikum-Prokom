def cetak_struk_traveloka(nama_hotel, lokasi_hotel, tanggal_check_in, tanggal_check_out, jumlah_malam, harga_per_malam, jumlah_kamar, total_biaya):
    print("====================================")
    print("          STRUK HOLIYAY             ")
    print("====================================")
    print("Nama Hotel: ", nama_hotel)
    print("Lokasi Hotel: ", lokasi_hotel)
    print("Check-in: ", tanggal_check_in)
    print("Check-out: ", tanggal_check_out)
    print("Jumlah Malam: ", jumlah_malam)
    print("Harga per Malam: ", harga_per_malam)
    print("------------------------------------")
    print("Total Biaya: ", total_biaya)
    print("Terima kasih sudah menggunakan program kami")
    print("====================================")

# Contoh penggunaan
nama_hotel = "Hotel XYZ"
lokasi_hotel = "Jakarta"
tanggal_check_in = "12 Juni 2023"
tanggal_check_out = "15 Juni 2023"
jumlah_malam = 3
harga_per_malam = 500000
jumlah_kamar = 2
total_biaya = jumlah_malam * harga_per_malam * jumlah_kamar

cetak_struk_traveloka(nama_hotel, lokasi_hotel, tanggal_check_in, tanggal_check_out, jumlah_malam, harga_per_malam, jumlah_kamar, total_biaya)
