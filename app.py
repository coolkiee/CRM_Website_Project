from flask import Flask, render_template,request,redirect,url_for
import sqlite3


app = Flask(__name__) #flask web örneği oluşturur

def get_db_connection():
    conn=sqlite3.connect('instance/crm.db')
    conn.row_factory = sqlite3.Row #database den gelen sonuçları hem (satır[0]) hemde  (satır['sirket_adı']) olarak tutar
    return conn

# Veritabanı şemasını kontrol eden ve güncelleyen fonksiyon
def check_and_update_schema():
    conn = get_db_connection()
    cursor = conn.execute("PRAGMA table_info(musteriler)")
    columns = [row['name'] for row in cursor.fetchall()]
    schema_changed = False
    
    # 'yetkili_kisi' sütunu eksikse, tabloya ekle
    if 'yetkili_kisi' not in columns:
        print("Veritabanı şeması güncelleniyor: 'musteriler' tablosuna 'yetkili_kisi' sütunu ekleniyor.")
        conn.execute('ALTER TABLE musteriler ADD COLUMN yetkili_kisi TEXT')
        schema_changed = True

    # Eğer şemada bir değişiklik yapıldıysa, veritabanına kaydet
    if schema_changed:
        conn.commit()
        
    conn.close()

check_and_update_schema()

#mainpage
@app.route('/')
def index():
    return render_template('main_page.html')

@app.route('/musteri/ekle' , methods=['GET','POST']) #URL nin 2 tür isteği kabul edeceğini belirtir
def musteri_ekle():
    if request.method == 'POST':
        sirket_adi = request.form['sirket_adi']
        yetkili_kisi = request.form['yetkili_kisi']
        email = request.form['email']
        telefon = request.form['telefon']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO musteriler (sirket_adi, yetkili_kisi, email, telefon) VALUES (?, ?, ?, ?)',
            (sirket_adi, yetkili_kisi, email, telefon)
        ) # INSERT INTO = SQL komutuyla bu dataları database e yeri bir müşteri ekler
          #VALUES bölümünde ? ,? ,? ,? bölümü sql enjeksiyonunu engellemeye yarar
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('musteri_ekle.html')

if __name__=='__main__':
    app.run(debug=True)