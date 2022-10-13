TUGAS 6 PBP

Nama: Naila Azizah

NPM: 2106705814

Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- 
Synchronous programming:
- proses jalannya yaitu sequential atau berdasarkan antrian eksekusi program
- memblokir klien hingga operasi yang dijalankan selesai
- saat dijalankan, halaman full page di browser akan di refesh jika ada command dari user dan proses lainnya akan di blokir sementara sampai command selesai tereksekusi

Asynchronous programming:
- proses jalannya yaitu dilakukan secara bersamaan
- hasil dari eksekusi tergantung dengan lama suatu proses synchronous
- tidak memblokir klien maupun javascript browser
- saat dijalankan tidak memerlukan refresh karena akan mendapatkan respon dari ajax (Asynchronous JavaScript And XML)  secara langsung

Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
-
Event-based programming adalah saat dimana flow dari program ditentukan oleh event atau event-based.

Event adalah bagian dari data yang dibuat oleh developer serta digunakan oleh user, contoh dari event yaitu button yang dipencet, message passing, atau membaca output

Contoh EDP dalam tugas ini adalah 
```$("#button").click(function(){``` yaitu eksekusi kode dimana berjalannya click pada button untuk menambahkan todo
`

Jelaskan penerapan asynchronous programming pada AJAX.
-
Cara kerja sebagai berikut
  - Terdapat event yang terjadi pada halaman web 
  - Browser membuat JavaScript call yang kemudian akan mengaktifkan XMLHttpRequest.
  - XMLHttpRequest object mengirimkan request ke server
  - Server memproses request tersebut
  - Server mengembalikan response kembali kepada halaman web
  - Response dibaca oleh JavaScript
  - Aksi berikutnya akan dipicu oleh JavaScript sesuai dengan langkah yang dibuat (contohnya memperbarui data di halaman tersebut)


Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- 
Checklist untuk tugas ini adalah sebagai berikut:

- Mengubah tugas 4 yang telah dibuat sebelumnya menjadi menggunakan AJAX.

AJAX GET

- Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.
diimplementasikan dengan membuat view show_json sebagai berikut
```angular2html
model_todo = Task.objects.filter(user = request.user)
  return HttpResponse(serializers.serialize("json", model_todo), content_type="application/json")
```

- Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.

diimplementasikan dengan menambahkan ```path('json/', show_json, name='show_json')``` dan import show_json dari wishlist.views

- Lakukan pengambilan task menggunakan AJAX GET.

diimplementasikan dengan membuat script dibawah resource link ajax sebagai berikut:
```angular2html
<script>
  $(document).ready(function(){
      $.get("/todolist/json", function(data) {
        console.log(data)
        for (i=0; i < data.length; i++){
          $("#mylist").append( // dilanjutkan dengan card display html
```

AJAX POST

- Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.

diimplementasikan dengan menambahkan kode sebagai beriku:
```angular2html
<a href="{% url 'todolist:new_todo' %}"><button class="button-56" role="button">+ New Task</button></a>

<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@mdo">Modal New Task</button>
```
lalu dilanjutkan oleh template modal yang didapatkan dari resource modal dari bootstrap

- Buatlah view baru untuk menambahkan task baru ke dalam database.
  
diimplementasikan dengan membuat view baru yang bernama add_todo dengan return ```return JsonResponse(result)``` 

- Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
  
diimplementasikan dengan menambahkan ```path('add/', add_todo, name='add_todo')``` dan import add_todo dari wishlist.views

- Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add

diimplementasikan dengan menambahkan kode sebagai berikut setelah ada potongan kode event based programming:
```angular2html
$.post("/todolist/add/",{
  title: $('#title').val(),
  description: $('#description').val()}, 
  function (result){
    $(".container").append(
      `<div class="card col-lg-4 col-md-6 col-sm-12" style="width: 18rem;">
          <div class="card-body">
              <h5 class="card-title">${result.fields.title}</h5>
              <p class="card-text">${result.fields.date}</p>
              <p class="card-text">${result.fields.description}</p>
          </div>
      </div>`)
```