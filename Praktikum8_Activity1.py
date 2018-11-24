#Kegiatan 1
x={"Nama":"Indraswari Wahyu Pertiwi",
   "NIM":"L200183076",
   "Fakultas":"Komunikasi dan Informatika",
   "Prodi":"Teknik Informatika Double Degree",
   "Asal":"Banjarmasin",
   "TTL":"Banjarbaru,15 Oktober 2000",
   "Email":"indraswariwp722@gmail.com"}

def a():
    print("Nama :",x["Nama"])
def b():
    print("NIM :",x["NIM"])
def c():
    print("Fakultas :",x["Fakultas"])
def d():
    print("Prodi :",x["Prodi"])
def e():
    print("Asal :",x["Asal"])
def f():
    print("Tempat Tanggal Lahir :",x["TTL"])
def g():
    print("Email :",x["Email"])

    
h="""
Pilihan yang tersedia :
a untuk menampilkan Nama
b untuk menampilkan NIM
c untuk menampilkan Fakultas
d untuk menampilkan Prodi
e untuk menampilkan Asal
f untuk menampilkan Tempat Tanggal Lahir
g untuk menampilkan Email
0 untuk bantuan
x untuk keluar
"""

print (h)
while True:
    k=input("pilihan saudara : ")
    if k=="a":
         a()
    elif k=="b":
         b()
    elif k=="c":
         c()
    elif k=="d":
         d()
    elif k=="e":
        
         e()
    elif k=="f":
         f()
    elif k=="g":
         g()
    elif k=="o":
         h()
    elif k=="x":
        print ("Terima Kasih")
        break
    else:
        print("Pilihan Tidak Ada, Silahkan Coba Lagi",k)
