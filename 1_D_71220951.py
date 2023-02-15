print("=================== MAKANAN ===================")
print("1. Telur Bakar           : Rp. 7.000")
print("2. Lele Terbang Mas Bhe  : Rp. 10.000")
print("3. Es Coklat Lempu       : Rp. 5.000")
print("4. Es Doger Langensari   : Rp. 13.000")
print("")
print("=================== PESANAN ===================")

telurbakarbrp = int(input("Telur Bakar          : "))
leleterbangbrp = int(input("Lele Terbang         : "))
escoklatbrp = int(input("Es Coklat            : "))
esdogerbrp = int(input("Es Doger             : "))
print("")

totaltelurbakar = 7000*telurbakarbrp
totalleleterbang = 10000*leleterbangbrp
totalescoklat = 5000*escoklatbrp
totalesdoger = 13000*esdogerbrp
totalsemua = totaltelurbakar+totalleleterbang+totalescoklat+totalesdoger

print("==================== TOTAL ====================")
print("TOTAL TELUR BAKAR x", telurbakarbrp, "           : Rp", totaltelurbakar)
print("TOTAL LELE TERBANG x", leleterbangbrp, "          : Rp", totalleleterbang)
print("TOTAL ES COKLAT x", escoklatbrp, "             : Rp", totalescoklat)
print("TOTAL ES DOGER x", esdogerbrp, "              : Rp", totalesdoger)
print("Jumlah total biaya yang harus dibayar adalah Rp", totalsemua)