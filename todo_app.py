import os

NAMA_FILE = "todo.txt"

def muat_tugas():
    tugas = []
    if os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "r") as file:
            for baris in file:
                bagian = baris.strip().split("|")
                if len(bagian) == 2:
                    deskripsi, status = bagian
                    tugas.append({
                        "deskripsi": deskripsi,
                        "selesai": status == "selesai"
                    })
    return tugas

def simpan_tugas(tugas):
    with open(NAMA_FILE, "w") as file:
        for t in tugas:
            status = "selesai" if t["selesai"] else "belum"
            file.write(f"{t['deskripsi']}|{status}\n")

def tampilkan_menu():
    print("\n=== APLIKASI TO-DO LIST ===")
    print("1. Lihat daftar tugas")
    print("2. Tambah tugas baru")
    print("3. Tandai tugas sebagai selesai")
    print("4. Hapus tugas")
    print("5. Keluar")

def tampilkan_tugas(tugas):
    if not tugas:
        print("Daftar tugas kosong.")
    else:
        print("\n--- Daftar Tugas ---")
        for idx, t in enumerate(tugas, 1):
            status = "✅" if t["selesai"] else "❌"
            print(f"{idx}. {t['deskripsi']} {status}")
        print("--------------------")

def tambah_tugas(tugas):
    deskripsi = input("Masukkan deskripsi tugas: ").strip()
    if deskripsi:
        tugas.append({"deskripsi": deskripsi, "selesai": False})
        print("Tugas berhasil ditambahkan!")
    else:
        print("Deskripsi tidak boleh kosong.")

def tandai_selesai(tugas):
    tampilkan_tugas(tugas)
    try:
        nomor = int(input("Masukkan nomor tugas yang selesai: "))
        if 1 <= nomor <= len(tugas):
            tugas[nomor - 1]["selesai"] = True
            print("Tugas ditandai sebagai selesai.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

def hapus_tugas(tugas):
    tampilkan_tugas(tugas)
    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor <= len(tugas):
            tugas.pop(nomor - 1)
            print("Tugas berhasil dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

def main():
    tugas = muat_tugas()
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tampilkan_tugas(tugas)
        elif pilihan == "2":
            tambah_tugas(tugas)
        elif pilihan == "3":
            tandai_selesai(tugas)
        elif pilihan == "4":
            hapus_tugas(tugas)
        elif pilihan == "5":
            simpan_tugas(tugas)
            print("Tugas disimpan. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1-5.")

if __name__ == "__main__":
    main()