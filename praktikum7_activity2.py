coba=0
kode="indras"
while coba<3:
    x=str(input("masukan password :"))
    if x==kode:
        print("anda berhasil login")
        break
    elif coba==2:
        print("anda salah memasukan password 3 kali, akses anda ditolak")
    else:
        print("password yang anda masukan salah,silahkan coba lagi")
    coba+=1
