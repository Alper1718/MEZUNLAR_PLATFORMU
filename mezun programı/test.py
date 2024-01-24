import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd

max_entries = 5000

def show_menu():
    frame_menu.pack()


class Graduate:
    def __init__(self):
        self.name = ''
        self.phone = ''
        self.email = ''
        self.address = ''
        self.university = ''
        self.graduation_year = 0
        self.profession = ''
        self.workplace = ''

num = 0
graduates = [Graduate() for _ in range(max_entries)]

def insert():
    global num, graduates

    if num < max_entries:
        i = num
        num += 1

        graduates[i].name = entry_name.get()
        graduates[i].phone = entry_phone.get()
        graduates[i].email = entry_email.get()
        graduates[i].address = entry_address.get()
        graduates[i].university = entry_university.get()
        graduates[i].graduation_year = int(entry_graduation_year.get())
        graduates[i].profession = entry_profession.get()
        graduates[i].workplace = entry_workplace.get()

        save_to_excel()  # Mezun bilgilerini Excel'e kaydet

    else:
        messagebox.showerror("Hata", "Maksimum mezun sayısına ulaşıldı")



def delete_index(i):
    global num, graduates

    for j in range(i, num - 1):
        graduates[j].name = graduates[j + 1].name
        graduates[j].phone = graduates[j + 1].phone
        graduates[j].email = graduates[j + 1].email
        graduates[j].address = graduates[j + 1].address
        graduates[j].university = graduates[j + 1].university
        graduates[j].graduation_year = graduates[j + 1].graduation_year
        graduates[j].profession = graduates[j + 1].profession
        graduates[j].workplace = graduates[j + 1].workplace

    save_to_excel()  # Mezun bilgilerini Excel'e kaydet

def delete_record():
    global num, graduates

    name = entry_name.get()

    for i in range(num):
        if graduates[i].name == name:
            delete_index(i)
            num -= 1
            break



def search_record():
    global num, graduates

    search_name = entry_name.get().lower()

    for i in range(num):
        if graduates[i].name.lower() == search_name:
            result_label.config(text=f"Mezun Adı Soyadı: {graduates[i].name}\nTelefon: {graduates[i].phone}\nMail: {graduates[i].email}\nAdres: {graduates[i].address}\nMezun Olduğu Üniversite: {graduates[i].university}\nMezuniyet Yılı: {graduates[i].graduation_year}\nMeslek: {graduates[i].profession}\nÇalıştığı Kurum: {graduates[i].workplace}")
            break
    else:
        result_label.config(text="Mezun bulunamadı")

def search_by_year():
    global num, graduates

    search_year = int(entry_graduation_year.get())

    matching_names = [graduate.name for graduate in graduates if graduate.graduation_year == search_year]

    if matching_names:
        result_label.config(text=f"Mezunlar ({search_year} yılı): {', '.join(matching_names)}")
    else:
        result_label.config(text=f"{search_year} yılında mezun olan kimse bulunamadı")

def save_to_excel():
    global graduates

    data = {
        'Name': [graduate.name for graduate in graduates],
        'Phone': [graduate.phone for graduate in graduates],
        'Email': [graduate.email for graduate in graduates],
        'Address': [graduate.address for graduate in graduates],
        'University': [graduate.university for graduate in graduates],
        'Graduation Year': [graduate.graduation_year for graduate in graduates],
        'Profession': [graduate.profession for graduate in graduates],
        'Workplace': [graduate.workplace for graduate in graduates],
    }

    df = pd.DataFrame(data)
    df.to_excel('bilgi.xlsx', index=False)

# Resim eklemek için
def load_image(path, size):
    image = Image.open(path)
    image = image.resize((150, 150))
    return ImageTk.PhotoImage(image)
# GUI
root = tk.Tk()
root.title("Mezunlar Platformu")
root.geometry("800x600")

frame_menu = tk.Frame(root)

label_name = tk.Label(frame_menu, text="Mezun Adı Soyadı:")
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_name = tk.Entry(frame_menu, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10, sticky="w")

label_phone = tk.Label(frame_menu, text="Telefon:")
label_phone.grid(row=0, column=2, padx=10, pady=10, sticky="e")

entry_phone = tk.Entry(frame_menu, width=15)
entry_phone.grid(row=0, column=3, padx=10, pady=10, sticky="w")

label_email = tk.Label(frame_menu, text="Mail:")
label_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_email = tk.Entry(frame_menu, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=10, sticky="w")

label_address = tk.Label(frame_menu, text="Adres:")
label_address.grid(row=1, column=2, padx=10, pady=10, sticky="e")

entry_address = tk.Entry(frame_menu, width=30)
entry_address.grid(row=1, column=3, padx=10, pady=10, sticky="w")

label_university = tk.Label(frame_menu, text="Mezun Olduğu Üniversite:")
label_university.grid(row=2, column=0, padx=10, pady=10, sticky="e")

entry_university = tk.Entry(frame_menu, width=30)
entry_university.grid(row=2, column=1, padx=10, pady=10, sticky="w")

label_graduation_year = tk.Label(frame_menu, text="Mezuniyet Yılı:")
label_graduation_year.grid(row=2, column=2, padx=10, pady=10, sticky="e")

entry_graduation_year = tk.Entry(frame_menu, width=10)
entry_graduation_year.grid(row=2, column=3, padx=10, pady=10, sticky="w")



label_profession = tk.Label(frame_menu, text="Meslek:")
label_profession.grid(row=3, column=2, padx=10, pady=10, sticky="e")

entry_profession = tk.Entry(frame_menu, width=20)
entry_profession.grid(row=3, column=3, padx=10, pady=10, sticky="w", columnspan=3)

label_workplace = tk.Label(frame_menu, text="Çalıştığı Kurum:")
label_workplace.grid(row=3, column=0, padx=10, pady=10, sticky="e")

entry_workplace = tk.Entry(frame_menu, width=30)
entry_workplace.grid(row=3, column=1, padx=10, pady=10, sticky="w", columnspan=5)

btn_insert = tk.Button(frame_menu, text="Yeni mezun ekle", command=insert, height=2, width=20)
btn_insert.grid(row=5, column=0, columnspan=2, pady=10)

image_insert = Image.open("alis.png")
image_insert = image_insert.resize((100, 100))
photo_insert = ImageTk.PhotoImage(image_insert)
label_insert = tk.Label(frame_menu, image=photo_insert)
label_insert.image = photo_insert
label_insert.grid(row=6, column=0, columnspan=2)

btn_delete = tk.Button(frame_menu, text="Mezunu sil", command=delete_record, height=2, width=20)
btn_delete.grid(row=5, column=2, columnspan=5, pady=10)

image_delete = Image.open("hawks.png")
image_delete = image_delete.resize((160, 110))
photo_delete = ImageTk.PhotoImage(image_delete)
label_delete = tk.Label(frame_menu, image=photo_delete)
label_delete.image = photo_delete
label_delete.grid(row=6, column=2, columnspan=5)
btn_search = tk.Button(frame_menu, text="Mezun ara", command=search_record, height=2, width=20)
btn_search.grid(row=6, column=0, columnspan=6, pady=10)

btn_search_year = tk.Button(frame_menu, text="Mezun yıla göre ara", command=search_by_year, height=2, width=20)
btn_search_year.grid(row=7, column=0, columnspan=6, pady=10)

result_label = tk.Label(frame_menu, text="")
result_label.grid(row=8, column=0, columnspan=6, pady=10)

show_menu()

root.mainloop()
