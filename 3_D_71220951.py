brand = input("Masukkan brand apa saja yang hendak dibeli (pisahkan dengan koma): ")
brand = [hargabarang.strip() for hargabarang in brand.split(",")]
harganya = []
for hargabarang in brand:
    hargaitu = float(input(f"Berapa harga barang {hargabarang} ? :"))
    harganya.append(hargaitu)

totaldiskon = 0
for i in range(len(brand)):
    harga = harganya[i]
    diskon = 0
    if(hargaitu>=25000000):
        diskon = 0.25*hargaitu
    elif(hargaitu>=10000000):
        diskon = 0.1*hargaitu
    totaldiskon += diskon
    print(f"Diskon Rp. {brand[i]} Rp.{diskon:.1f} Harga {brand[i]} Rp. {hargaitu-diskon:.1f}")

totalharga = sum(harganya)-totaldiskon

print(f"Total diskon yang anda dapatkan adalah sebesar: Rp.{totaldiskon:.1f}")
print(f"Total uang yang harus anda bayarkan adalah: Rp. {totalharga:.1f}")
