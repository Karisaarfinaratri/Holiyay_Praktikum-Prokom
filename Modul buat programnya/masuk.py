def sign_up():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    file = open("data_base.txt", "a")
    file.write(f"{username}:{password}\n")
    print("Sign up berhasil!")

def sign_in():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    file = open("data_base.txt", "r")
    for line in file:
        stored_username, stored_password = line.strip().split(":")
        if username == stored_username and password  == stored_password:
            print("Sign in berhasil!")
            return
    print("username atau password salah.")

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
        break
    else:
        print("Pilihan tidak valid. Silahkan coba lagi.")