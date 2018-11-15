waktu=("pagi","siang","sore","petang","malam")
nama=str(input("masukan nama anda : "))
x=float(input("pukul berapa sekarang? "))
if x<=11.30:
    w=0
elif x<=15.30:
    w=1
elif x<=17.30:
    w=2
elif x<=19.30:
    w=3
elif x<=24.00:
    w=4
print("selamat",waktu[w],nama)
