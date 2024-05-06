# ------------------------------------------------------------------------------------------------------------------------
# Kütüphaneler
# ------------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox
import sqlite3
import odev4
import login_function
import othercompare_function

# ------------------------------------------------------------------------------------------------------------------------
# Global değişkenler
# ------------------------------------------------------------------------------------------------------------------------
change_password_user = None
text1_entry = None
text2_entry = None
root = None
login_frame = None
menu_frame = None

# ------------------------------------------------------------------------------------------------------------------------
# Menü Fonksiyonları
# ------------------------------------------------------------------------------------------------------------------------
# -> Giriş Fonksiyonu
def loginFunction():
    user = login_function.userChecker(username_entry.get(), password_entry.get())
    if user:
        showOtherMenu()
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

# -> Kayıt Fonksiyonu
def registerUserFunction():
    login_function.registerUser(username_entry.get(), password_entry.get())

# -> Şifre Değiştirme Fonksiyonu
def changePasswordFunction():
    if change_password_user:  # Değişken tanımlıysa devam et
        login_function.changePassword(change_password_user.get(), current_password_entry.get(), new_password_entry.get())
    else:
        messagebox.showerror("Hata", "Kullanıcı adı giriniz.")

# -> Metin Karşılaştırma Fonksiyonu
def compareTextFunctionJaccardFunction():
    global text1_entry, text2_entry
    response = odev4.odev4Main(text1_entry.get(), text2_entry.get())
    messagebox.showinfo("Benzerlik Oranı", "Benzerlik Oranınız: " + response)

def compareTextFunctionLevenshteinFunction():
    global text1_entry, text2_entry
    response = othercompare_function.levenshteinCompare(text1_entry.get(), text2_entry.get())
    messagebox.showinfo("Benzerlik Oranı", "Benzerlik Oranınız: " + response)

# ------------------------------------------------------------------------------------------------------------------------
# Menü Ekranları
# ------------------------------------------------------------------------------------------------------------------------
# -> Diğer Menü Ekranı
def showOtherMenu():
    global login_frame, menu_frame
    login_frame.pack_forget()
    otherMenu()
    menu_frame.pack()

# -> Şifre Değiştirme Menü Ekranı
def changePasswordMenu():
    global change_password_user, current_password_entry, new_password_entry
    # Yeni bir pencere oluştur
    password_window = tk.Toplevel(root)
    password_window.title("Şifre Değiştir")

    # Kullanıcı adı, mevcut şifre ve yeni şifre giriş alanları
    tk.Label(password_window, text="Kullanıcı Adı:").grid(row=0, column=0)
    tk.Label(password_window, text="Mevcut Şifre:").grid(row=1, column=0)
    tk.Label(password_window, text="Yeni Şifre:").grid(row=2, column=0)

    # Entry widget'ları oluştur
    change_password_user = tk.Entry(password_window)
    current_password_entry = tk.Entry(password_window, show="*")
    new_password_entry = tk.Entry(password_window, show="*")

    # Entry widget'larını grid'e yerleştir
    change_password_user.grid(row=0, column=1)
    current_password_entry.grid(row=1, column=1)
    new_password_entry.grid(row=2, column=1)

    # Şifre değiştirme butonu
    change_button = tk.Button(password_window, text="Değiştir", command=changePasswordFunction)
    change_button.grid(row=3, columnspan=2, pady=5)

# -> Metin Karşılaştırma Menü Ekranı
def compareTextMenu():
    global text1_entry, text2_entry
    text_window = tk.Toplevel(root)
    text_window.title("Metin Karşılaştırma")

    # Metin giriş alanları
    tk.Label(text_window, text="Metin 1:").grid(row=0, column=0)
    tk.Label(text_window, text="Metin 2:").grid(row=1, column=0)
    text1_entry = tk.Entry(text_window)
    text2_entry = tk.Entry(text_window)
    text1_entry.grid(row=0, column=1)
    text2_entry.grid(row=1, column=1)

    # Karşılaştırma butonları
    compare_button_jaccard = tk.Button(text_window, text="Jaccard Karşılaştır", command=compareTextFunctionJaccardFunction)
    compare_button_jaccard.grid(row=2, columnspan=2, pady=5)
    compare_button_levenshtein = tk.Button(text_window, text="Levenshtein Karşılaştır", command=compareTextFunctionLevenshteinFunction)
    compare_button_levenshtein.grid(row=3, columnspan=2, pady=5)


# -> Giriş Menü Ekranı
def loginMenu():
    global root, username_entry, password_entry, login_frame
    login_frame = tk.Frame(root)
    tk.Label(login_frame, text="Kullanıcı Adı:").grid(row=0, column=0)
    tk.Label(login_frame, text="Şifre:").grid(row=1, column=0)
    username_entry = tk.Entry(login_frame)
    password_entry = tk.Entry(login_frame, show="*")
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)
    login_button = tk.Button(login_frame, text="Giriş Yap", command=loginFunction)
    register_button = tk.Button(login_frame, text="Kayıt Ol", command=registerUserFunction)
    login_button.grid(row=2, column=0, columnspan=2, pady=5)
    register_button.grid(row=3, column=0, columnspan=2)
    login_frame.pack(padx=20, pady=20)
    return username_entry, password_entry

# -> Diğer Menü Ekranı
def otherMenu():
    global root, menu_frame
    menu_frame = tk.Frame(root)
    tk.Button(menu_frame, text="Karşılaştır", command=compareTextMenu).pack()
    tk.Button(menu_frame, text="İşlemler", command=changePasswordMenu).pack()
    tk.Button(menu_frame, text="Çıkış", command=root.quit).pack()
    menu_frame.pack(padx=20, pady=20)

def createGui():
    # Tkinter penceresi oluşturma
    global root
    root = tk.Tk()
    root.title("Ödev 5")
    loginMenu()
    root.mainloop()

# ------------------------------------------------------------------------------------------------------------------------
# Ana Fonksiyon
# ------------------------------------------------------------------------------------------------------------------------
# -> Ana Fonksiyon
def main():
    # GUI oluşturma fonksiyonunu çağır
    createGui()

# -> Ana Fonksiyon Çağrısı
if __name__ == "__main__":
    main()