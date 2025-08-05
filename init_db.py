import sqlite3

connection = sqlite3.connect('instance/crm.db')#dosya var mı diye kontrol eder
# |eğer yoksa yeniden oluşturur

cursor = connection.cursor() #sql komutlarını çalıştırmak için cursor nesnesi oluşturur

cursor.execute('''
CREATE TABLE IF NOT EXISTS musteriler(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sirket_adi TEXT NOT NULL,
    yetkili_kisi TEXT,
    email TEXT NOT NULL UNIQUE,
    telefon TEXT NOT NULL);
''')
#cursor.execute = sql komutlarını çalıştırır
# CREATE TABLE IF NOT EXISTS musteriler =tablo henüz yoksa, bu komutla yeni bir tablo oluşturulur
# UNIQUE: Bu alana girilen verinin başka bir kayıtta daha olamayacağını belirtir. (İki müşteri aynı e-postaya sahip olamaz)
# PRIMARY KEY AUTOINCREMENT: Her kayda otomatik olarak artan, benzersiz bir numara (ID) verir.

connection.commit() #Değişiklikleri veritabanına kaydediyor

connection.close() #bağlantıyı kapatıyor
