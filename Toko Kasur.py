

print (20*"=")
print("Welcome To Toko Kasur")
print(20*"=" + "\n")

class TokoKasur:
    def __init__(self):
        self.kasur = []
    
    def menu_admin(self):
        print("Menu Admin: ")
        print("1. Tambah Daftar Kasur")
        print("2. Lihat Daftar Kasur")
        print("3. Ubah Kasur")
        print("4. Hapus Kasur")
        print("5. Keluar")
    
    def menu_pembeli(self):
        print("Menu Pembeli: ")
        print("1. Transaksi")
        print("2. Keluar")
    
    def tambah_kasur(self):
        print("Tambah daftar kasur")
        nama_kasur = input("Masukkan nama kasur: ")
        harga_kasur = int(input("Masukkan harga kasur: "))
        self.kasur.append({"nama": nama_kasur, "harga": harga_kasur})
        print("Kasur berhasil ditambahkan")
    
    def lihat_daftar_kasur(self):
        print("Daftar Kasur:")
        for idx, kasur in enumerate(self.kasur, start=1):
            print(f"{idx}. Nama: {kasur['nama']}, Harga: {kasur['harga']}")
    
    def ubah_kasur(self):
        self.lihat_daftar_kasur()
        idx = int(input("Pilih nomor kasur yang ingin diubah: ")) - 1
        if 0 <= idx < len(self.kasur):
            nama_kasur = input("Masukkan nama kasur baru: ")
            harga_kasur = int(input("Masukkan harga kasur baru: "))
            self.kasur[idx] = {"nama": nama_kasur, "harga": harga_kasur}
            print("Kasur berhasil diubah!")
        else:
            print("Nomor kasur tidak valid.")
    
    def hapus_kasur(self):
        self.lihat_daftar_kasur()
        idx = int(input("Pilih nomor kasur yang ingin dihapus: ")) - 1
        if 0 <= idx < len(self.kasur):
            del self.kasur[idx]
            print("Kasur berhasil dihapus!")
        else:
            print("Nomor kasur tidak valid.")

    def transaksi(self):
        self.lihat_daftar_kasur()
        idx = int(input("Pilih nomor kasur untuk transaksi: ")) - 1
        if 0 <= idx < len(self.kasur):
            print(f"Anda telah melakukan transaksi dengan membeli kasur {self.kasur[idx]['nama']} seharga {self.kasur[idx]['harga']}.")
        else:
            print("Nomor kasur tidak valid.")


def main():
    toko_kasur = TokoKasur()

    while True:
        print("1. Login sebagai Admin")
        print("2. Login sebagai Pembeli")
        role = input("Pilihan: ")

        if role == "1":
            while True:
                toko_kasur.menu_admin()
                pilihan = input("Pilih menu: ")

                if pilihan == "1":
                    toko_kasur.tambah_kasur()
                elif pilihan == "2":
                    toko_kasur.lihat_daftar_kasur()
                elif pilihan == "3":
                    toko_kasur.ubah_kasur()
                elif pilihan == "4":
                    toko_kasur.hapus_kasur()
                elif pilihan == "5":
                    break
                else:
                    print("Menu tidak valid, silahkan coba lagi.")

        elif role == "2":
            while True:
                toko_kasur.menu_pembeli()
                pilihan= input("Pilih menu: ")

                if pilihan == "1":
                    toko_kasur.transaksi()
                elif pilihan == "2":
                    break
                else:
                    print("Menu tidak valid.")


if __name__ == "__main__":
    main()
