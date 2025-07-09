import tkinter as tk
from tkinter import messagebox

# الحروف المستخدمة في التشفير
LETTERS = 'abcdefghijklmnopqrstuvwxyz!?'
الحروف='ابتثجحخدذرزسشصضطظعغفقلمنهوي'
# داله التشفير
def encrypt():
    text = input_Entry.get().lower()
    key = key_Entry.get()

    if not key.isdigit() or not (1 <= int(key) <= 28):
        messagebox.showerror("خطأ", "يجب أن يكون المفتاح رقمًا بين 1 و 28")
        return

    cipher = ''
    for char in text:
        if char in LETTERS:
            idx = (LETTERS.find(char) + int(key)) % 28
            cipher += LETTERS[idx]
        elif char in الحروف:
            idx = (الحروف.find(char) + int(key)) % 28
            cipher += الحروف[idx]
        else:
            cipher += char  #اي شيء غير الحروف يتم ارجاعه كماهو بدون تشفير
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, cipher)

# دالة فك التشفير
def decrypt():
    text = input_Entry.get().lower()
    key = key_Entry.get()

    if not key.isdigit() or not (1 <= int(key) <= 28):
        messagebox.showerror("خطأ", "يجب أن يكون المفتاح رقمًا بين 1 و 28")
        return

    plain = ''
    for char in text:
        if char in LETTERS:
            idx = (LETTERS.find(char) - int(key)) % 28
            plain += LETTERS[idx]
        elif char in الحروف:
            idx = (الحروف.find(char) - int(key)) % 28
            plain += الحروف[idx]
        else:
            plain += char #اي شيء غير الحروف يتم ارجاعه كماهو بدون تشفير

    output_text.delete(1.0, tk.END) # عشلن في كل مره يتم التاكد ان خانه العرض فارغه
    output_text.insert(tk.END, plain)

# دالة الخروج
def exit_app():
    screen.destroy()


# انشاء الواجهة
screen = tk.Tk()
screen.title("Caesar Cipher Tool - أداة تشفير قيصر")
screen.geometry("750x400")
screen.iconbitmap("ghost.ico")
screen.configure(bg="#002c3e")

# العنوان
toolbar = tk.Label(
    screen,
    text="أداة تشفير وفك تشفير باستخدام خوارزمية قيصر",
    bg="#ffffff",
    fg="#00334e",
    font=("Arial", 14, "bold")
)
toolbar.pack(fill=tk.X, padx=20, pady=20)


input_frame = tk.Frame(screen, bg="#002c3e")
input_frame.pack(pady=10, padx=20, fill=tk.X)

# إدخال النص
tk.Label(input_frame, text="النص:", fg="white", bg="#002c3e", font=('Arial', 12)).grid(row=0, column=0, sticky='ew' ,)
# input_Entry = tk.Entry(input_frame, fg="black", bg='#cce7e8', font=('Arial', 12), width=60) هنا استخدمنا عرض محدد  وهو ليس مرن مع الشاششه
input_Entry = tk.Entry(input_frame, fg="black", bg='#cce7e8', font=('Arial', 12)) # نحذف العرض المحدد ونستخدم بدله sticky east and west
input_Entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
# input_Entry.grid(row=0, column=1, padx=10, pady=5)


# اجعل العمود الثاني يتمدد تلقائيًا
input_frame.columnconfigure(1, weight=1)

# إدخال المفتاح
tk.Label(input_frame, text="المفتاح (1-28):", fg="white", bg="#002c3e", font=('Arial', 12)).grid(row=1, column=0, sticky='ewnw')
key_Entry = tk.Entry(input_frame, fg="black", bg='#cce7e8', font=('Arial', 12),height=10)
key_Entry.grid(row=1, column=1, padx=10, pady=5,sticky="ew")

# أزرار التشفير، فك التشفير، والخروج
button_frame = tk.Frame(screen, bg="#002c3e")
button_frame.pack(pady=10)

tk.Button(button_frame, text='تشفير', fg='white', bg='#1d7ea4', font=('Arial', 12, 'bold'), width=12, command=encrypt).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text='فك التشفير', fg='white', bg='#1d7ea4', font=('Arial', 12, 'bold'), width=12, command=decrypt).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text='خروج', fg='white', bg='#ff5c5c', font=('Arial', 12, 'bold'), width=12, command=exit_app).grid(row=0, column=2, padx=10)

# منطقة الإخراج
output_text = tk.Text(screen, height=5, font=('Arial', 12), bg='#f0f0f0', fg='#00334e')
output_text.pack(padx=20, pady=20, fill=tk.X)

# بدء التطبيق
screen.mainloop()
