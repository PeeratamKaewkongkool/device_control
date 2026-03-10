import tkinter as tk
from tkinter import messagebox
import sqlite3

# สร้างฐานข้อมูล
conn = sqlite3.connect("exercise.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS exercise(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    name TEXT,
    time TEXT
)""")

conn.commit()


def add_data():
    d = date_entry.get()
    n = name_entry.get()
    t = time_entry.get()

    if d == "" or n == "" or t == "":
        messagebox.showwarning("แจ้งเตือน", "กรอกข้อมูลให้ครบ")
        return

    c.execute("INSERT INTO exercise(date,name,time) VALUES(?,?,?)",(d,n,t))
    conn.commit()

    messagebox.showinfo("สำเร็จ","บันทึกข้อมูลแล้ว")

    date_entry.delete(0,tk.END)
    name_entry.delete(0,tk.END)
    time_entry.delete(0,tk.END)

    show_data()


def show_data():
    listbox.delete(0,tk.END)

    c.execute("SELECT * FROM exercise")
    rows = c.fetchall()

    for r in rows:
        listbox.insert(tk.END,f"{r[1]} | {r[2]} | {r[3]} นาที")


# UI
root = tk.Tk()
root.title("Exercise Record")
root.geometry("400x400")

tk.Label(root,text="วันที่").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root,text="ประเภทการออกกำลังกาย").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root,text="เวลา (นาที)").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Button(root,text="บันทึกข้อมูล",command=add_data).pack(pady=10)

listbox = tk.Listbox(root,width=50)
listbox.pack()

tk.Button(root,text="แสดงข้อมูล",command=show_data).pack(pady=5)

root.mainloop()