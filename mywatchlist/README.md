Nama: Naila Azizah
NPM: 2106705814

Link aplikasi html: https://pbp-tugas2-katalog.herokuapp.com/mywatchlist/html/ 
Link aplikasi xml: https://pbp-tugas2-katalog.herokuapp.com/mywatchlist/xml/ 
Link aplikasi json: https://pbp-tugas2-katalog.herokuapp.com/mywatchlist/json/ 

- Jelaskan perbedaan antara JSON, XML, dan HTML!
1. Definisi
   - XML (Extensible Markup Language): bahasa markup untuk menyimpan dan mengangkut data dari satu aplikasi ke aplikasi lain melalui internet.
   - JSON: format yang ditulis dalam JavaScript penyimpanan dan pertukaran data untuk diurai, diakses, serta diorganisir
   - HTML (Hyper Markup Text Language): bahasa yang menggunakan tag untuk menyatakan kode-kode yang harus ditafsirkan oleh browser.

2. Penyimpanan Data
   - XML: disimpan sebagai struktur phon atau tree structure
   - JSON: disimpan sebagai map dengan pasangan key dan value
   - HTML: data disimpan secara lokal menggunakan cookies. HTML memiliki localStorage dan sessionStorage

3. Pengolahan Data
   - XML: permintaan AJAX lambat karena terdaoat banyak bandwidth yang dikonsumsi secara tidak perlu
   - JSON: data diolah secara serial maka lebih cepat prosesnya
   - HTML:

4. Dukungan array
   - XML: tidak mendukung array secara langsung
   - JSON: mendukung array yang bisa diakses
   - HTML: mendukung array yang bisa diakses

5. Kecepatan
   - XML: besar dan lambar dalam transmisi data
   - JSON: ukuran file kecil sehingga mudah transmisi data
   - HTML: lumayan cepat dan error kecil dapat diabaikan

- Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery dalam pengimplementasian sebuah platform untuk memenuhi kebutuhan dalam mengirimkan data dari satu stack ke stack lainnya.
Dengan data delivery, kita dapat mengirimkan data dengan berbagai macam bentuk, seperti HTML, JSON, atau XML.
  

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
: diimplementasikan dengan menjalankan command "python3 manage.py startapp mywatchlist" di terminal
2. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
: diimplementasikan dengan menambahkan path di urls.py yaitu sebagai berikut
"  path('', mywatchlist, name='mywatchlist'),
   path('html/', mywatchlist, name='mywatchlist'),
   path('xml/', show_xml, name='show_xml'),
   path('json/', show_json, name='show_json'),"
3. Membuat sebuah model MyWatchList yang memiliki atribut sebagai berikut:
   - watched untuk mendeskripsikan film tersebut sudah ditonton atau belum
   - title untuk mendeskripsikan judul film
   - rating untuk mendeskripsikan rating film dalam rentang 1 sampai dengan 5
   - release_date untuk mendeskripsikan kapan film dirilis
   - review untuk mendeskripsikan review untuk film tersebut
: diimplentasikan dengan membuat artibut tersebut di models.py dan mengassign tipe text yang akan digunakan
4. Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format:
   - HTML
   - XML
   - JSON
: diimplentasikan dengan membuat fungsi mymovielist, show_xml, dan show_json di views.py yang berisi data yang akan digunakan
5. Membuat routing sehingga data di atas dapat diakses melalui URL:
    http://localhost:8000/mywatchlist/html untuk mengakses mywatchlist dalam format HTML

    http://localhost:8000/mywatchlist/xml untuk mengakses mywatchlist dalam format XML

    http://localhost:8000/mywatchlist/json untuk mengakses mywatchlist dalam format JSON 
   : diimplementasikan dengan menambahkan path, dan menjalankan python2 manage.py runserver
6. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.:
karena pada tugas sebelumnya directory ini sudah di deploy ke heroku, jika file ini di push ke github, heroku akan terupdate
7. Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md

- membuat account PostMan
- mengirimkan url heroku HTML, JSON, dan XML di PostMan
8. Menambahkan unit test pada tests.py untuk menguji bahwa tiga URL di poin 6 dapat mengembalikan respon HTTP 200 OK sebagai berikut;
<img width="1111" alt="Screen Shot 2022-09-21 at 12 44 10" src="https://user-images.githubusercontent.com/101708935/191656510-f170dab![Uploading Screen Shot 2022-09-21 <img width="1111" alt="Screen Shot 2022-09-21 at 12 44 42" src="https://user-images.githubusercontent.com/101708935/191656543-005ad91b-fdeb-4ed5-8b4e-89dee0fd4b52.png">
at 12.44.26.png…]()
0-764c-46e3-9354-36e00418fc4c.png">

   class test_url(TestCase):

   def test_url_html(self):

   response = Client().get('http://localhost:8000/mywatchlist/html/')
   self.assertEqual(response.status_code, 200)


