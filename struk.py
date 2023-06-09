from Holiyay import sign_in
def cetak_struk_traveloka(nama_hotel, , tanggal_check_in, tanggal_check_out, jumlah_malam, harga_per_malam, jumlah_kamar, total_biaya):
    print("====================================")
    print("          STRUK HOLIYAY             ")
    print("====================================")
    print("Username:", username)
    print()
    print("Tempat Wisata: ", tempat_wisata)
    print("Nama Hotel: ", nama_hotel)
    print("Tour Guide: ", tour_guide)
    print("Check-in: ", tanggal_check_in)
    print("Check-out: ", tanggal_check_out)
    print("Jumlah Malam: ", jumlah_hari)
    print("Harga per Malam: ", harga_per_hari)
    print("------------------------------------")
    print("Total Biaya: ", harga_total)
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
