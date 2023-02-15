nomorteleponkamubrp = input("Masukkan Nomor Telepon: ")

if(len(nomorteleponkamubrp!=12)):
    print("Tidak valid, nomor telepon Anda tidak 12 digit")
else:
    if(nomorteleponkamubrp.startswith("0816")):
        print("")
        print("Anda menggunakan operator Indosat")
    elif(nomorteleponkamubrp.startswith("0814")):
        print("")
        print("Anda menggunakan operator Telkomsel")
    else:
        print("")
        print("Operator anda tidak diketahui")

angkapalingakhir = int(nomorteleponkamubrp[-1])
if(angkapalingakhir%2==0):
    print("Nomor anda berakhiran genap")
else:
    print("Nomor anda berakhiran ganjil")

