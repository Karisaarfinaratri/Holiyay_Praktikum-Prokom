# membuat fungsi sign up
def sign_up():
    global username
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # membuka file txt dengan mode "a" dan menambahkan data yang diinputkan oleh user
    file = open("data_base.txt", "a")
    file.write(f"{username}:{password}\n")
    print("Sign up berhasil!")

# membuat fungsi sign in
def sign_in():
    global username
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # membuka file txt dalam mode "r" dan mengecek kesamaan data input user dan di data_base
    file = open("data_base.txt", "r")
    for line in file:
        stored_username, stored_password = line.strip().split(":")
        if username == stored_username and password == stored_password:
            print("Sign in berhasil!")
            return
    print("username atau password salah.")
    sign_in()