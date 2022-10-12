TUGAS 4 PBP
-
Nama: Naila Azizah

NPM: 2106705814

Kelas: PBP F

link aplikasi todolist: https://pbp-tugas2-katalog.herokuapp.com/todolist/login/?next=/todolist/ 

1. Apa kegunaan {% csrf_token %} pada elemen <form>? 
Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

CSRF yaitu Cross-Site Request Forgery. Kegunaan dari token ini adalah untuk menghindari csrf attack tindakan kejahatan pada aplikasi. Token ini memastikan keamanan dari post requests dari user.
   Jika tidak ada potongan kode tersebut, 
   Cara kerja dari potongan tersebut adalah csrf_token akan membuat token di server saat page dirender, 

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? 
Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Ya, kita dapat membuat elemen <form> secara manual. Salah satu cara lain untuk membuat form dalam aplikasi adalah dengan cara manual, sebagai berikut;
   <img width="598" alt="Screen Shot 2022-09-29 at 09 05 07" src="https://user-images.githubusercontent.com/101708935/192922091-5242ffd3-afe8-4988-893b-a21866b2243a.png">

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, 
penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
- Pertama, browser akan display HTML layout berupa form ke user
- Saat data disubmit oleh user lewat button submit, data akan diakses dengan potongan kode request.POST.get()
- Berdasarkan data HTML form yang didapatka, browser akan generate HTTP request, method, dan arguments ke tujuan url
- Server akan menerima request tersebut dan menyesuaikan request dengan page views.py selanjutnya yang ingin ditampilkan
- Server akan generate HTML file dan kemudian didisplay ke user.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.

: diimplementasikan dengan menjalankan command "python3 manage.py startapp todolist" di terminal directory pbp-tugas-2


- Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
: diimplementasikan dengan menambahkan path di urls.py yaitu sebagai berikut
"  path('', todolist, name='todolist'),"

- Membuat sebuah model Task yang memiliki atribut user, date, title, description
  : diimplentasikan dengan membuat artibut tersebut di models.py dan mengassign tipe text yang akan digunakan
  - user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  - date = models.DateField() 
  - title = models.TextField()
  - description = models.TextField()

- Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
: diimplementasikan dengan
  - membuat fungsi register, login, dan logout di views.py
  - menambahkan import redirect, UserCreation, dan messages
  - import fungsi register, login, dan logout di urls.py
  - mengisi fungsi dengan kode masing-masing
    - register: berisi potongan kode membuat form
    - login: berisi potongan kode authenticate user
    - logout: berisi potongan kode untuk redirect ke halaman utama
  - menambahkan path ur; ke urlpatterns seperti berikut: path('register/', register, name='register'),
  - membuat file register.html, login.html, logout.html di templates, masing-masing sesaui yang diinginkan dan memiliki textfield atau button yang diperlukan

- Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
: diimplementasikan dengan membuat todolist.html di folder templates

- Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
: diimplementasikan dengan
  - membuat fungsi baru di views.py yaitu add_todo
  - membuat variable untuk title dan description serta membuat form
  - context sebagai berikut:
  context = {
  'title': title,
  'description': description,
  'form': form}

- Membuat routing sehingga beberapa fungsi dapat diakses melalui URL
: diimplementasikan dengan menambahkan path, dan menjalankan python2 manage.py runserver

- Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
: karena pada tugas sebelumnya directory ini sudah di deploy ke heroku, jika file ini di push ke github, heroku akan terupdate dengan aplikasi todolist

