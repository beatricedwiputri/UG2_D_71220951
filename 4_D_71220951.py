print("!! Selamat datang di H+ GYM !!")

daftarmember = {}

while True:
    print("Silahkan pilih menu dibawah ini:")
    print("1. Menambah data")
    print("2. Menampilkan data")
    print("3. Keluar")
    pilihan = input("Silahkan masukkan pilihan yang Anda inginkan: ")
    if(pilihan=="1"):
        namakamu = input("Masukkan nama pelanggan: ")
        memberkamu = input("Masukkan jenis member: ").lower()
        if(namakamu in daftarmember):
            print("Data yang Anda isi sudah ada di dalam daftar data!")
            print("")
        else:
            daftarmember[namakamu] = memberkamu
            print("Data sudah berhasil ditambahkan!")
            print("")
    elif(pilihan=="2"):
        print("---------------------------------")
        print("Pelanggan  Member:")
        for i, (namakamu, memberkamu) in enumerate(daftarmember.items(),1):
            print(f"{i}.{namakamu}  {memberkamu}")
        print("")
    elif(pilihan=="3"):
        print("")
        print("Sistem Berhenti..")
        break
    else:
        print("Input tidak valid! Silahkan masukan input yang benar!")
