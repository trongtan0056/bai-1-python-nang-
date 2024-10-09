import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu, messagebox as msg

# Tạo cửa sổ chính (Main Window)
win = tk.Tk()
win.title("emtan666")
win.resizable(True, True)

# Tạo thanh menu
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Tạo menu File và Help
file_menu = Menu(menu_bar)
file_menu.add_command(label="new")
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="about", command=lambda: show_msg_box())
menu_bar.add_cascade(label="Help", menu=help_menu)

# Tạo frame chứa các thành phần giao diện chính
mighty = ttk.LabelFrame(win, text='Mighty Python')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Label và hộp nhập liệu cho tên
a_label = ttk.Label(win, text="enter a name:")
a_label.grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()

# Label và combobox để chọn số
ttk.Label(win, text="choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Nút bấm chính
button = ttk.Button(win, text="Nhấn vào đây", command=lambda: click_me(name.get(), number_chosen.get()))
button.grid(column=2, row=1)

# Tạo các hộp kiểm (Checkbuttons)
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Tạo các Radiobuttons để thay đổi màu nền
COLOR1 = "Blue"
COLOR2 = "GOLD"
COLOR3 = "RED"

radVar = tk.IntVar()
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=lambda: radCall(radVar.get()))
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=lambda: radCall(radVar.get()))
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=lambda: radCall(radVar.get()))
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

# Tạo hộp văn bản có khả năng cuộn (ScrolledText)
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Tạo một frame chứa các nhãn
buttons_frame = ttk.LabelFrame(win, text='bang label')
buttons_frame.grid(column=1, row=7)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

# Hiển thị hộp thoại thông báo
def show_msg_box():
    msg.showinfo('python message info box', 'cham thang xanh')

# Hàm xử lý khi nhấn vào nút
def click_me(name, number):
    button.configure(text=f'hello {name} {number}')
    a_label.configure(foreground='red')
    a_label.configure(text='A red label')

# Hàm thay đổi màu nền dựa trên radiobutton được chọn
def radCall(radSel):
    if radSel == 1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3: win.configure(background=COLOR3)


# Khởi chạy vòng lặp chính
win.mainloop()
