def pilih_pemandu():
    print("Selamat datang di program pemilihan pemandu wisata!")
    print("✿ ♡＾▽ ＾♡ ✿")
    print("Disini anda akan diminta memilih salah satu pemandu wisata selama berada di Bali")
    print("Silahkan pilih pemandu Anda:")
    print("Pemandu A")
    print("Pemandu B")
    print("Pemandu C")

    pemandu_terpilih = None

    while pemandu_terpilih is None:
        pilihan = input("Masukkan pilihan Anda: ").upper()

        if pilihan == "A":
            print("Anda memilih pemandu A.")
            setuju = input("Apakah Anda setuju dengan pemandu A? (ya/tidak): ").lower()

            if setuju == "ya":
                pemandu_terpilih = "A"
            else:
                print("Anda tidak setuju dengan pemandu A. Silakan pilih pemandu berikutnya.")

        elif pilihan == "B":
            print("Anda memilih pemandu B.")
            setuju = input("Apakah Anda setuju dengan pemandu B? (ya/tidak): ").lower()

            if setuju == "ya":
                pemandu_terpilih = "B"
            else:
                print("Anda tidak setuju dengan pemandu B. Silakan pilih pemandu berikutnya.")

        elif pilihan == "C":
            print("Anda memilih pemandu C.")
            setuju = input("Apakah Anda setuju dengan pemandu C? (ya/tidak): ").lower()

            if setuju == "ya":
                pemandu_terpilih = "C"
            else:
                print("Maaf tidak ada Pemandu Wisata  yang cocok dengan anda")
        else:
            print("Pilihan tidak valid. Silakan pilih antara A, B, atau C.")

    print("Selamat Anda telah berhasil memilih pemandu", pemandu_terpilih)

# Menjalankan program
pilih_pemandu()
