import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import sqlite3

# สร้างฐานข้อมูล
conn = sqlite3.connect("exercise.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS exercise(
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
name TEXT,
time TEXT
)
""")

conn.commit()


def เพิ่มข้อมูล():
    d = ช่องวันที่.get()
    n = ช่องออกกำลังกาย.get()
    t = ช่องเวลา.get()

    if d == "" or n == "" or t == "":
        messagebox.showwarning("แจ้งเตือน","กรอกข้อมูลให้ครบ")
        return

    c.execute("INSERT INTO exercise(date,name,time) VALUES(?,?,?)",(d,n,t))
    conn.commit()

    แสดงข้อมูล()
    ล้างช่อง()


def ลบข้อมูล():
    selected = ตาราง.focus()

    if selected == "":
        messagebox.showwarning("แจ้งเตือน","เลือกข้อมูลก่อนลบ")
        return

    data = ตาราง.item(selected)
    record_id = data["values"][0]

    c.execute("DELETE FROM exercise WHERE id=?",(record_id,))
    conn.commit()

    แสดงข้อมูล()


def แก้ไขข้อมูล():
    selected = ตาราง.focus()

    if selected == "":
        messagebox.showwarning("แจ้งเตือน","เลือกข้อมูลก่อนแก้ไข")
        return

    data = ตาราง.item(selected)
    record_id = data["values"][0]

    d = ช่องวันที่.get()
    n = ช่องออกกำลังกาย.get()
    t = ช่องเวลา.get()

    c.execute("UPDATE exercise SET date=?,name=?,time=? WHERE id=?",(d,n,t,record_id))
    conn.commit()

    แสดงข้อมูล()
    ล้างช่อง()


def ค้นหาข้อมูล():
    keyword = ช่องค้นหา.get()

    for row in ตาราง.get_children():
        ตาราง.delete(row)

    c.execute("SELECT * FROM exercise WHERE name LIKE ?",('%'+keyword+'%',))
    rows = c.fetchall()

    for r in rows:
        ตาราง.insert("",tk.END,values=r)


def แสดงข้อมูล():
    for row in ตาราง.get_children():
        ตาราง.delete(row)

    c.execute("SELECT * FROM exercise")
    rows = c.fetchall()

    for r in rows:
        ตาราง.insert("",tk.END,values=r)


def ล้างช่อง():
    ช่องออกกำลังกาย.delete(0,tk.END)
    ช่องเวลา.delete(0,tk.END)


def เลือกข้อมูล(event):
    selected = ตาราง.focus()
    data = ตาราง.item(selected)

    if data["values"]:
        row = data["values"]

        ช่องวันที่.set_date(row[1])
        ช่องออกกำลังกาย.delete(0,tk.END)
        ช่องเวลา.delete(0,tk.END)

        ช่องออกกำลังกาย.insert(0,row[2])
        ช่องเวลา.insert(0,row[3])


# UI
root = tk.Tk()
root.title("โปรแกรมบันทึกการออกกำลังกาย")
root.geometry("900x650")
root.configure(bg="#1abc9c")


หัวข้อ = tk.Label(root,
text="โปรแกรมบันทึกการออกกำลังกาย",
font=("Arial",28,"bold"),
bg="#1abc9c",
fg="white")

หัวข้อ.pack(pady=10)


เครดิต = tk.Label(root,
text="ผู้สร้าง : Peeratam Kaewkongkool 684245022",
font=("Arial",14),
bg="#1abc9c",
fg="white")

เครดิต.pack(pady=5)


frame = tk.Frame(root,bg="#1abc9c")
frame.pack(pady=10)


tk.Label(frame,text="วันที่",font=("Arial",14),bg="#1abc9c",fg="white").grid(row=0,column=0,pady=10)

ช่องวันที่ = DateEntry(frame,
width=33,
font=("Arial",14),
background="darkblue",
foreground="white",
borderwidth=2,
date_pattern="dd/mm/yyyy")

ช่องวันที่.grid(row=0,column=1,pady=10)


tk.Label(frame,text="ประเภทการออกกำลังกาย",font=("Arial",14),bg="#1abc9c",fg="white").grid(row=1,column=0,pady=10)

ช่องออกกำลังกาย = tk.Entry(frame,font=("Arial",14),width=35)
ช่องออกกำลังกาย.grid(row=1,column=1,pady=10)


tk.Label(frame,text="เวลา (นาที)",font=("Arial",14),bg="#1abc9c",fg="white").grid(row=2,column=0,pady=10)

ช่องเวลา = tk.Entry(frame,font=("Arial",14),width=35)
ช่องเวลา.grid(row=2,column=1,pady=10)


# ปุ่ม
frameปุ่ม = tk.Frame(root,bg="#1abc9c")
frameปุ่ม.pack(pady=20)

tk.Button(frameปุ่ม,text="เพิ่มข้อมูล",
font=("Arial",14,"bold"),
bg="#2ecc71",
fg="white",
width=12,
height=2,
command=เพิ่มข้อมูล).grid(row=0,column=0,padx=10)

tk.Button(frameปุ่ม,text="แก้ไขข้อมูล",
font=("Arial",14,"bold"),
bg="#f1c40f",
width=12,
height=2,
command=แก้ไขข้อมูล).grid(row=0,column=1,padx=10)

tk.Button(frameปุ่ม,text="ลบข้อมูล",
font=("Arial",14,"bold"),
bg="#e74c3c",
fg="white",
width=12,
height=2,
command=ลบข้อมูล).grid(row=0,column=2,padx=10)

tk.Button(frameปุ่ม,text="แสดงทั้งหมด",
font=("Arial",14,"bold"),
bg="#3498db",
fg="white",
width=12,
height=2,
command=แสดงข้อมูล).grid(row=0,column=3,padx=10)


# ค้นหา
frameค้นหา = tk.Frame(root,bg="#1abc9c")
frameค้นหา.pack(pady=10)

ช่องค้นหา = tk.Entry(frameค้นหา,font=("Arial",14),width=30)
ช่องค้นหา.grid(row=0,column=0,padx=10)

tk.Button(frameค้นหา,text="ค้นหา",
font=("Arial",12,"bold"),
bg="#9b59b6",
fg="white",
width=10,
command=ค้นหาข้อมูล).grid(row=0,column=1)


# ตาราง
style = ttk.Style()
style.configure("Treeview",font=("Arial",12),rowheight=30)
style.configure("Treeview.Heading",font=("Arial",13,"bold"))

ตาราง = ttk.Treeview(root,
columns=("ID","Date","Exercise","Time"),
show="headings")

ตาราง.pack(fill="both",expand=True,padx=20,pady=20)

ตาราง.heading("ID",text="ID")
ตาราง.heading("Date",text="วันที่")
ตาราง.heading("Exercise",text="การออกกำลังกาย")
ตาราง.heading("Time",text="เวลา")

ตาราง.bind("<ButtonRelease-1>",เลือกข้อมูล)


footer = tk.Label(root,
text="Mini Project - Exercise Record Program | Peeratam Kaewkongkool 684245022",
font=("Arial",10),
bg="#1abc9c",
fg="white")

footer.pack(pady=5)


แสดงข้อมูล()

root.mainloop()