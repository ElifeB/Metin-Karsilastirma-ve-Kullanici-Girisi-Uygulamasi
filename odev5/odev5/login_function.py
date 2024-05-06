# ------------------------------------------------------------------------------------------------------------------------
# Kütüphaneler
# ------------------------------------------------------------------------------------------------------------------------
import sqlite3
from tkinter import messagebox

# ------------------------------------------------------------------------------------------------------------------------
# Kullanıcı İşlemleri
# ------------------------------------------------------------------------------------------------------------------------
# -> Tablo Oluşturma Fonksiyonu
def createTable():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.commit()
    conn.close()

# -> Tablo Oluşturulmuş mu Kontrolü
def isTableCreated():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table = c.fetchone()
    conn.close()
    return table

# -> Kullanıcı Kayıt Fonksiyonu
def registerUser(username: str, password: str):
    isTableCreatedResponse=isTableCreated()
    if not isTableCreatedResponse:
        createTable()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = c.fetchone()
    if existing_user:
        messagebox.showerror("Hata", "Bu kullanıcı adı zaten var!")
    else:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Başarılı", "Kayıt başarıyla tamamlandı.")
    conn.close()

# -> Kullanıcı Kontrol Fonksiyonu
def userChecker(username: str, password: str):
    isTableCreatedResponse=isTableCreated()
    if not isTableCreatedResponse:
        createTable()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

# -> Şifre Değiştirme Fonksiyonu
def changePassword(username: str, current_password: str, new_password: str):
    isTableCreatedResponse=isTableCreated()
    if not isTableCreatedResponse:
        createTable()
    # Mevcut şifre veritabanında doğru mu kontrol et
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, current_password))
    user = c.fetchone()
    if user:
        # Şifreyi güncelle
        c.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
        conn.commit()
        messagebox.showinfo("Başarılı", "Şifre başarıyla değiştirildi.")
        password_window.destroy()  # Pencereyi kapat
    else:
        messagebox.showerror("Hata", "Mevcut şifre yanlış!")
    conn.close()