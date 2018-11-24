def konversi_suhu():
    x=int(input('pilih konversi :'))
    if (x==1):
        f=int(input('masukan suhu celcius :'))
        c=32+9.0/5*f
        print(c)
    if (x==2):
        a=int(input('masukan suhu farenheit :'))
        b=(a-32)*5.0/9
        print (b)
print('konversi suhu')
print('1.celcius ke fahrenheit')
print('2. fahrenheith ke celcius')
konversi_suhu()