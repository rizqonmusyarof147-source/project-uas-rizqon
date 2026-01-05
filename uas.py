import tkinter as tk
from tkinter import messagebox

def konversi_nilai():
    try:
        nilai = float(entry_nilai.get())

        if nilai < 0 or nilai > 100:
            messagebox.showerror("Error", "Nilai harus antara 0 - 100")
            return
        if nilai >= 99:
            huruf = "A - keren bet luu"
        elif nilai >= 90:
            huruf = "B - cukup keren"
        elif nilai >= 80:
            huruf = "C - lumayan oke lahh"
        elif nilai >= 70:
            huruf = "D - belajar lagi deck"
        elif nilai >= 60:
            huruf = "E - nilai apaan inii"
        else:
            huruf = "F - dongoo"

        nama = entry_nama.get()
        label_hasil.config(text=f" Nama :{nama} - Kategori Nilai : {huruf}")


    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid")

data_nilai = []


root = tk.Tk()
root.title("Aplikasi sederhana By Rizqon(251301003)")
root.geometry("400x600")

label_judul = tk.Label(root, text="Konversi Nilai ", font=("Arial", 12, "bold"))
label_judul.pack(pady=10)

label_nilai = tk.Label(root, text="Masukkan Nilainya broo:")
label_nilai.pack()

entry_nilai = tk.Entry(root)
entry_nilai.pack()

label_nama = tk.Label(root, text="Masukkan Namanya oii:")
label_nama.pack()

entry_nama = tk.Entry(root)
entry_nama.pack()



def save_data():
    if label_hasil.cget("text") == "Nilai : -":
        messagebox.showwarning("Peringatan", "Belum ada data untuk disimpan!")
        return

    data = {
        "nama": entry_nama.get(),
        "nilai": entry_nilai.get(),
        "hasil": label_hasil.cget("text")
    }

    data_nilai.append(data)
    messagebox.showinfo("Info", "Data berhasil disimpan di program")

    
btn_proses = tk.Button(root, text="Proses", command=konversi_nilai)
btn_proses.pack(pady=10)

def reset_fields():
    entry_nama.delete(0, tk.END)
    entry_nilai.delete(0, tk.END)
    label_hasil.config(text="Nilai Huruf: -")


btn_reset = tk.Button(root, text="Reset", command=reset_fields)
btn_reset.pack(pady=5)

btn_save = tk.Button(root, text="Simpan data", command=save_data)
btn_save.pack(pady=5)


def lihat_data():
    if not data_nilai:
        messagebox.showinfo("Info", "Belum ada data tersimpan")
        return

    teks = ""
    for i, d in enumerate(data_nilai, 1):
        teks += f"{i}. {d['hasil']}\n\n"

    messagebox.showinfo("Data Tersimpan", teks)

btn_lihat = tk.Button(root, text="Lihat Data", command=lihat_data)
btn_lihat.pack(pady=5)


label_hasil = tk.Label(root, text="Kategori Nilai : -", font=("Arial", 10))
label_hasil.pack()


root.mainloop()
