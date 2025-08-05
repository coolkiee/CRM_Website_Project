from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# Flask uygulamasını oluşturuyoruz. __name__ özel bir Python değişkenidir
# ve Flask'a uygulamanın nerede olduğunu söyler.
app = Flask(__name__)

# Bu, bir URL'nin ("/") nasıl bir fonksiyonla eşleştiğini tanımlar.
# Kullanıcı web sitemizin ana sayfasını ziyaret ettiğinde bu fonksiyon çalışacak.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)

class Musteri(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    sirket_adi = db.Column(db.String(100), nullable=False)
    yetkili_kisi = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True ,nullable=False)
    telefon= db.Column(db.String(20))

    def __repr__(self):
        return f'<Manager {self.sirket_adi}>'
@app.route('/')
def anasayfa():
    return render_template('main_page.html')

# Bu blok, dosyanın doğrudan çalıştırıldığından emin olmamızı sağlar.
# Yani, bu dosyayı çalıştırdığımızda aşağıdaki kodlar devreye girer.
if __name__ == '__main__':
    # Uygulamayı geliştirme modunda (debug=True) başlatır.
    # Bu, kodda değişiklik yaptığınızda sunucunun otomatik olarak
    # yeniden başlayacağı ve hata ayıklamanın kolaylaşacağı anlamına gelir.
    app.run(debug=True)