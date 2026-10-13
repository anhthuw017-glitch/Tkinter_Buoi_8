import tkinter as tk

# Khởi tạo cửa sổ
cua_so = tk.Tk()
cua_so.title("Ung dung Frame & Widget")
cua_so.geometry("400x300")
cua_so.resizable(False, False)  # Khóa kích thước cửa sổ

# Khung trên
khung_tren = tk.Frame(cua_so, bg="lightblue", height=80)
khung_tren.pack(fill="x")

# Khung dưới
khung_duoi = tk.Frame(cua_so, bg="lightyellow")
khung_duoi.pack(fill="both", expand=True)

# Nội dung các khung
tk.Label(khung_tren, text="Khu vuc tieu de", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=15)
tk.Label(khung_duoi, text="Xin chao Tkinter!", font=("Arial", 12), bg="lightyellow").pack(pady=20)

cua_so.mainloop()