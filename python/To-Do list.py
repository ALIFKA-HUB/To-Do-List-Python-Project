import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menambahkan tugas
def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)  # Hapus input setelah ditambahkan
    else:
        messagebox.showwarning("Input Error", "Masukkan tugas yang ingin ditambahkan.")

# Fungsi untuk menghapus tugas yang dipilih
def delete_task():
    try:
        selected_task_index = listbox.curselection()
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Pilih tugas yang ingin dihapus.")

# Fungsi untuk menandai tugas sebagai selesai
def mark_done():
    try:
        selected_task_index = listbox.curselection()
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, f"{task} (Selesai)")
        listbox.itemconfig(selected_task_index, {'bg':'lightgreen'})
    except IndexError:
        messagebox.showwarning("Selection Error", "Pilih tugas yang ingin ditandai sebagai selesai.")

# Fungsi untuk menyimpan daftar tugas ke file
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Fungsi untuk memuat daftar tugas dari file
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass  # Jika file tidak ditemukan, tidak ada tugas yang dimuat

# Setup GUI
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Entry untuk menambahkan tugas
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

# Tombol untuk menambahkan tugas
add_button = tk.Button(root, text="Tambah Tugas", width=15, command=add_task)
add_button.pack(pady=5)

# Listbox untuk menampilkan tugas
listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Tombol untuk menghapus tugas
delete_button = tk.Button(root, text="Hapus Tugas", width=15, command=delete_task)
delete_button.pack(pady=5)

# Tombol untuk menandai tugas sebagai selesai
done_button = tk.Button(root, text="Tandai Selesai", width=15, command=mark_done)
done_button.pack(pady=5)

# Tombol untuk menyimpan tugas
save_button = tk.Button(root, text="Simpan Tugas", width=15, command=save_tasks)
save_button.pack(pady=5)

# Memuat tugas dari file saat aplikasi dibuka
load_tasks()

# Menjalankan aplikasi
root.mainloop()

