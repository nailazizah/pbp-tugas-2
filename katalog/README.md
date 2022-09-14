TUGAS 2 PBP
-

Nama: Naila Azizah

NPM: 2106705814

Kelas: PBP F

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
!![](../../../../../../Desktop/Bagan Tugas 2 PBP.png)
    Kaitan antara urls.py dengan views.py adalah url berisi hal-hal yang akan ditampilkan (view). Sementara hubungan views dengan model adalah memiliki hubungan balik arah, dimana views.py mengirim respon data dan models.py menirim query.
    Berkas html merupakan isi dari rangkaian dari apa yang akan ditampilkan kepada user lewat web. Maka, hubunga dari keempat aspek tersebut adalah saling berurutan.


2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual Environment adalah tools untuk mengenkapsulasi serta mengatur package atau library pada suatu proyek. Alasan dibalik penggunaan virtual environment adalah untuk mencegah terjadinya issue dependency saat terdapat perbedaan versi maupun update yang berbeda-beda.

Contoh penggunaan dari virtual environment adalah di instansi saat terdapat Project A yang membutuhkan numpy versi 2.0, sedangkan Project B membutuhkan numpy version 1.0. Agar Project A dapat berjalan, kita diharuskan untuk meng-upgrade numpy kita ke versi 2.0. Akan tetapi, updat tersebut juga dapat menyebabkan error-error sehingga Project B tidak lagi bisa dijalankan. Dengan adanya virtual environment, perbedaan ketentuan ini di-handle yaitu dengan menginstall kumpulan library yang dibutuhkan sehingga kedua proyek tetap berjalan.

Oleh karena itu, pada umumnya virtual environment dibutuhkan, terutama untuk mengerjakan dua atau lebih proyek. Tanpa virtual environment, program tidak akan berjalan karena kebutuhan serta ketentuannya tidak terpenuhi.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

    1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
        - implementasi dasar pada views.py sudah disediakan pada template, yaitu seperti fungsi yang menerima parameter request
       
    2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
       - membuka urls.py dan menulis isinya yaitu;
         from django.urls import path
         from katalog.views import show_katalog

         app_name = 'katalog'

         urlpatterns = [path('', show_katalog, name='show_katalog'),]

      - daftarkan aplikasi katalog ke urls.py yand ada dalam project_django engan menambahkan potongan kode berikut pada variabel urlpatterns.
       
    3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
       - menambahkan data pada katalog.html sebagai berikut;
       <b>{{nama}}</b> dan
       <b>{{studentid}}</b> dibawah text nama dan id
       serta

       {% for catalogitem in list_barang %} <tr>
          <th>{{catalogitem.item_name}}</th>
          <th>{{catalogitem.item_price}}</th>
          <th>{{catalogitem.item_stock}}</th>
          <th>{{catalogitem.rating}}</th>
          <th>{{catalogitem.description}}</th>
          <th>{{catalogitem.item_url}}</th>
          </tr>

       {% endfor %}
    4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
       - melakukan git init pada direktori
       - mengecek procfile, pastikan bahwa isinya yaitu web: gunicorn aplikasi_django.wsgi --log-file -
       - menambahkan dan menyimpan variabel repository secret dengan mengakses menambahkan 2 secret di github, satu berisi key nama aplikasi sementara satunya berisi heroku key
