from flask import Flask, render_template

# Flask uygulamasını oluşturuyoruz. __name__ özel bir Python değişkenidir
# ve Flask'a uygulamanın nerede olduğunu söyler.
app = Flask(__name__)

# Bu, bir URL'nin ("/") nasıl bir fonksiyonla eşleştiğini tanımlar.
# Kullanıcı web sitemizin ana sayfasını ziyaret ettiğinde bu fonksiyon çalışacak.
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