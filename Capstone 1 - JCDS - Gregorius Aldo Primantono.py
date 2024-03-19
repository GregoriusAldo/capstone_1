from prettytable import PrettyTable

DataPerpus = [
    {'ID Buku' : 'BK001', 'Judul Buku' : 'Taktik dan Strategi Futsal Modern', 'Penulis/Pengarang' : 'Coach Justin', 'Tahun Terbit' : 2011, 'Kategori/Genre' : 'Olahraga', 'Stok' : 3},
    {'ID Buku' : 'BK002', 'Judul Buku' : 'Heavier Than Heaven: A Biography of Kurt Cobain', 'Penulis/Pengarang' : 'Charles R. Cross', 'Tahun Terbit' : 2012, 'Kategori/Genre' : 'Biografi', 'Stok' : 3},
    {'ID Buku' : 'BK003', 'Judul Buku' : 'Dasar-Dasar Pemrograman dengan Python', 'Penulis/Pengarang' : 'Wenty Dwi Yuniarti', 'Tahun Terbit' : 2019, 'Kategori/Genre' : 'Edukasi', 'Stok' : 5},
    {'ID Buku' : 'BK004', 'Judul Buku' : 'The Song of Achilles', 'Penulis/Pengarang' : 'Madeline Miller', 'Tahun Terbit' : 2012, 'Kategori/Genre' : 'Fantasi', 'Stok' : 2},
    {'ID Buku' : 'BK005', 'Judul Buku' : 'Aljabar Linear Elementer', 'Penulis/Pengarang' : 'Ari Andari', 'Tahun Terbit' : 2017, 'Kategori/Genre' : 'Edukasi', 'Stok' : 1}
]

def ShowDisplayDataMenuReadData():
    KolomPerpus = PrettyTable()
    KolomPerpus.field_names = DataPerpus[0].keys()

    for row in DataPerpus:
        KolomPerpus.add_row(row.values())

    print(KolomPerpus)

def MenuUtama():
    while True:
        pilihanMenu = input('''
                    Menu Utama:
                    1. Read Data Perpustakaan
                    2. Create Data Perpustakaan
                    3. Update Data Perpustakaan 
                    4. Delete Data Perpustakaan
                    5. Peminjaman Buku Perpustakaan
                    6. Exit Program Perpustakaan
                    Pilih menu (1/2/3/4/5/6): ''')
        if pilihanMenu == '1':
            ReadDataMenu()
        elif pilihanMenu == '2':
            CreateDataMenu()
        elif pilihanMenu == '3':
            UpdateDataMenu()
        elif pilihanMenu == '4':
            DeleteDataMenu()
        elif pilihanMenu == '5':
            PinjamBukuMenu()
        elif pilihanMenu == '6':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

def ReadDataMenu():
    while True:
        print("Read Menu (Menu A):")
        print("1. Tampilkan Seluruh Data Buku")
        print("2. Cari Berdasarkan ID Buku")
        print("3. Kembali ke Menu Utama")
        
        option = input("Pilih opsi (1/2/3): ")
        
        if option == '1':
            if len(DataPerpus) == 0:
                print("Data tidak ditemukan.")
            else:
                print("Data yang ada:")
                ShowDisplayDataMenuReadData()
                
        elif option == '2':
            if len(DataPerpus) == 0:
                print("Data tidak ditemukan.")
            else:
                id_buku = input("Masukkan ID Buku yang ingin dicari (format: BKxxx, di mana xxx adalah angka.): ")
                if id_buku[:2] == 'BK' and id_buku[2:].isdigit() and len(id_buku) >= 5:
                    found = False
                    for data in DataPerpus:
                        if data['ID Buku'] == id_buku:
                            print("Data yang sesuai:")
                            table = PrettyTable()
                            table.field_names = data.keys()
                            table.add_row(data.values())
                            print(table)
                            found = True
                            break
                    if not found:
                        print("ID Buku tidak ditemukan.")
                else:
                    print("Format ID Buku tidak valid.")
                    
        elif option == '3':
            print("Kembali ke Menu Utama.")
            break
            
        else:
            print("Pilihan tidak valid.")

def CreateDataMenu():
    while True:
        print("Create Data Menu (Menu B):")
        print("1. Tambah Data Buku")
        print("2. Kembali ke Menu Utama")

        option = input("Pilih opsi (1/2): ")

        if option == '1':
            id_buku = input("Masukkan ID Buku (format: BKxxx), di mana xxx adalah angka.: ")
            if not id_buku[:2] == 'BK' or not id_buku[2:].isdigit() or len(id_buku) != 5:
                print("Format ID Buku tidak sesuai. Format yang benar adalah BKxxx, di mana xxx adalah angka.")
                continue
            id_exists = False
            for data in DataPerpus:
                if data['ID Buku'] == id_buku:
                    id_exists = True
                    break
            
            if id_exists:
                print("Data dengan ID Buku tersebut sudah ada.")
                continue
            judul_buku = input("Masukkan Judul Buku: ")
            penulis_pengarang = input("Masukkan Penulis/Pengarang: ")
            tahun_terbit = input("Masukkan Tahun Terbit: ")
            if not tahun_terbit.isdigit() or int(tahun_terbit) < 1900:
                print("Tahun Terbit harus berupa angka dan minimal 1900.")
                continue
            elif len(tahun_terbit) > 4:
                print("Tahun Terbit tidak boleh lebih dari 4 digit.")
                continue
            tahun_terbit = int(tahun_terbit)
            kategori_genre = input("Masukkan Kategori/Genre: ")
            stok = input("Masukkan Stok: ")
            if not stok.isdigit():
                print("Stok harus berupa angka.")
                continue
            stok = int(stok)
            
            while True:
                print("\nApakah Anda yakin ingin menyimpan data ini? (yes/no)")
                save_confirmation = input().lower()
                if save_confirmation == 'yes':
                    DataPerpus.append({'ID Buku': id_buku, 'Judul Buku': judul_buku, 'Penulis/Pengarang': penulis_pengarang,
                                       'Tahun Terbit': tahun_terbit, 'Kategori/Genre': kategori_genre, 'Stok': stok})
                    print("Data berhasil ditambahkan.")
                    break
                elif save_confirmation == 'no':
                    print("Penambahan data dibatalkan.")
                    break
                else:
                    print("Input tidak valid. Silakan masukkan 'yes' atau 'no'.")
            
        elif option == '2':
            print("Kembali ke Menu Utama.")
            break
            
        else:
            print("Pilihan tidak valid.")

def UpdateDataMenu():
    while True:
        print("Update Data:")
        print("1. Update Data Buku")
        print("2. Kembali ke Menu Utama")
        
        choice = input("Pilih opsi (1/2): ")
        
        if choice == '1':
            id_buku = input("Masukkan ID Buku yang ingin diupdate (primary key, format BKxxx, di mana xxx adalah angka.): ")
            while not id_buku[:2] == 'BK' or not id_buku[2:].isdigit() or len(id_buku) != 5:
                print("Format ID Buku harus diawali dengan 'BK' dan diikuti oleh 3 digit angka.")
                id_buku = input("Masukkan ID Buku yang ingin diupdate (primary key, format BKxxx, di mana xxx adalah angka.): ")
                
            found = False
            for i in range(len(DataPerpus)):
                if DataPerpus[i]['ID Buku'] == id_buku:
                    found = True
                    print("Data yang akan diupdate:")
                    table = PrettyTable()
                    table.field_names = DataPerpus[i].keys()
                    table.add_row(DataPerpus[i].values())
                    print(table)
                    
                    confirm = input("Apakah Anda ingin melanjutkan untuk update data (yes/no)? ").lower()
                    if confirm == 'yes':
                        for key in DataPerpus[i].keys():
                            if key == 'ID Buku':
                                new_value = input(f"Masukkan {key} baru (kosongkan jika tidak ingin mengubah atau format ID Buku harus BKxxx, di mana xxx adalah angka.): ")
                                while new_value and (not new_value[:2] == 'BK' or not new_value[2:].isdigit() or len(new_value) != 5 or any(buku['ID Buku'] == new_value for buku in DataPerpus)):
                                    print("Format ID Buku harus diawali dengan 'BK' dan diikuti oleh 3 digit angka. ID Buku harus unik.")
                                    new_value = input(f"Masukkan {key} baru (kosongkan jika tidak ingin mengubah atau format ID Buku harus BKxxx, di mana xxx adalah angka.): ")
                                if new_value:
                                    new_value = new_value
                            elif key == 'Tahun Terbit':
                                new_value = input(f"Masukkan {key} baru (kosongkan jika tidak ingin mengubah atau format tahun terbit harus berupa bilangan bulat): ")
                                while new_value and (not new_value.isdigit() or int(new_value) < 1900 or len(new_value) > 4):
                                    print("Format tahun terbit harus berupa bilangan bulat dan minimal 1900 serta maksimal 4 karakter.")
                                    new_value = input(f"Masukkan {key} baru (kosongkan jika tidak ingin mengubah atau format tahun terbit harus berupa bilangan bulat): ")
                                if new_value:
                                    new_value = int(new_value)
                            elif key == 'Stok':
                                new_value = input(f"Masukkan {key} baru (kosongkan jika tidak ingin mengubah atau format stok harus berupa bilangan bulat): ")
                                while new_value and not new_value.isdigit():
                                    print("Format stok harus berupa bilangan bulat.")
                                    new_value = input(f"Masukkan {key} baru (kosongkan jika tidak ingin mengubah atau format stok harus berupa bilangan bulat): ")
                                if new_value:
                                    new_value = int(new_value)
                            else:
                                new_value = input(f"Masukkan {key} baru (kosongkan jika tidak ingin mengubah): ")
                                
                            if new_value:
                                DataPerpus[i][key] = new_value
                        
                        confirmation = input("Apakah Anda yakin ingin melakukan update data (yes/no)? ").lower()
                        if confirmation == 'yes':
                            print("Data berhasil diupdate.")
                            ShowDisplayDataMenuReadData()
                        elif confirmation == 'no':
                            print("Update data dibatalkan.")
                            break
                        else:
                            print("Input tidak valid. Silakan masukkan 'yes' atau 'no'.")
                            break
                    elif confirm == 'no':
                        print("Update data dibatalkan.")
                        break
                    else:
                        print("Input tidak valid. Silakan masukkan 'yes' atau 'no'.")
                        break
            
            if not found:
                print("Data yang Anda cari tidak tersedia.")
                
        elif choice == '2':
            print("Kembali ke Menu Utama.")
            break
            
        else:
            print("Pilihan tidak valid.")

def DeleteDataMenu():
    while True:
        print("Delete Data Menu:")
        print("1. Delete Data Buku")
        print("2. Kembali ke Menu Utama")
        
        option = input("Pilih opsi (1/2): ")

        if option == '1':
            if not DataPerpus:
                print("Data sudah kosong.")
                break

            print("Delete Data Buku:")
            ShowDisplayDataMenuReadData()
            id_buku = input("Masukkan ID Buku yang ingin dihapus (format BKxxx, di mana xxx adalah angka.): ")

            # Validasi format ID Buku
            if len(id_buku) >= 5 and id_buku[:2] == 'BK' and id_buku[2:].isdigit():
                found = False
                for i, data in enumerate(DataPerpus):
                    if data['ID Buku'] == id_buku:
                        found = True
                        print("Data yang akan dihapus:")
                        table = PrettyTable()
                        table.field_names = data.keys()
                        table.add_row(data.values())
                        print(table)
                        
                        confirmation = input("Apakah Anda yakin ingin menghapus data ini? (yes/no): ").lower()
                        if confirmation == 'yes':
                            DataPerpus.pop(i)
                            print("Data berhasil dihapus.")
                            if not DataPerpus:
                                print("Data kosong.")
                                break
                            ShowDisplayDataMenuReadData()
                            break
                        elif confirmation == 'no':
                            print("Penghapusan data dibatalkan.")
                            break
                        else:
                            print("Input tidak valid. Silakan masukkan 'yes' atau 'no'.")
                        
                if not found:
                    print("Data dengan ID Buku yang dimasukkan tidak ditemukan.")
            else:
                print("Format ID Buku tidak valid. Format yang benar adalah BKxxx, di mana xxx adalah angka.")

        elif option == '2':
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid.")

def PinjamBukuMenu():
    while True:
        print("Menu Peminjaman Buku:")
        print("1. Cari Buku Berdasarkan ID")
        print("2. Cari Buku Berdasarkan Judul")
        print("3. Kembali ke Menu Utama")

        option = input("Pilih opsi (1/2/3): ")     
        
        if option == '1':
            id_buku = input("Masukkan ID Buku yang ingin dipinjam (format: BKxxx, di mana xxx adalah angka.): ")
            if id_buku[:2] == 'BK' and id_buku[2:].isdigit() and len(id_buku) >= 5:
                buku_ditemukan = False
                for buku in DataPerpus:
                    if buku['ID Buku'] == id_buku:
                        buku_ditemukan = True
                        print("Data Buku:")
                        table = PrettyTable()
                        table.field_names = buku.keys()
                        table.add_row(buku.values())
                        print(table)

                        if buku['Stok'] > 0:
                            confirmation = input("Apakah Anda ingin meminjam buku ini? (yes/no): ").lower()
                            if confirmation == 'yes':
                                print("Buku berhasil dipinjam.")
                                buku['Stok'] -= 1
                            elif confirmation == 'no':
                                print("Peminjaman buku dibatalkan.")
                        else:
                            print("Maaf, stok buku habis.")
                        break
                if not buku_ditemukan:
                    print("Buku tidak ditemukan.")
            else:
                print("Format ID Buku tidak valid.")

        elif option == '2':
            judul = input("Masukkan kata kunci judul buku yang ingin dipinjam: ")
            buku_ditemukan = False
            for buku in DataPerpus:
                if judul.lower() in buku['Judul Buku'].lower():
                    buku_ditemukan = True
                    print("Data Buku:")
                    table = PrettyTable()
                    table.field_names = buku.keys()
                    table.add_row(buku.values())
                    print(table)

                    if buku['Stok'] > 0:
                        confirmation = input("Apakah Anda ingin meminjam buku ini? (yes/no): ").lower()
                        if confirmation == 'yes':
                            print("Buku berhasil dipinjam.")
                            buku['Stok'] -= 1
                        elif confirmation == 'no':
                            print("Peminjaman buku dibatalkan.")
                    else:
                        print("Maaf, stok buku habis.")
                    break
            if not buku_ditemukan:
                print("Buku tidak ditemukan.")

        elif option == '3':
            print("Kembali ke Menu Utama.")
            break

        else:
            print("Pilihan tidak valid.")
   
# Panggil menu utama
MenuUtama()






