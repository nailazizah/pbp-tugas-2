TUGAS 5 PBP
-

Nama: Naila Azizah

NPM: 2106705814


Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
- 
1. Internal CSS
- diletakkan di dalam bagian atas atau ```<head></head>``` pada html.
- mensupport style yang beda pada tiap halaman
- CSS internal diletakkan di dalam tag ```<style></style>```
- kekurangannya yaitu tidak bisa diaplikasikan di file lainnya

2. Inline CSS
- digunakan untuk tag HTML tertentu
- ditulis langsung pada atribut elemen HTML
- digunakan jika ingin merubah suatu eleemn spesifik saja
- memiliki kekurangan yaitu kurang efisien karena harus memberikan style ke tiap tag-tag HTML 

3. Eksternal CSS
- ditulis terpisah dengan file HTML
- ditulis pada file baru dengan extention .css
- kelebihannya adalah file HTML akan lebih ringkas karena terpisah dari CSS
- website akan memiliki loading time yang lebih singkat 
- kekurangannya adalah susah di debug saat terjadi error karena terpisah


Jelaskan tag HTML5 yang kamu ketahui.
-
```<a>``` : tag untuk mendefinisikan suatu hyperlink

```<b``` : mendisplay text dengan style bold

```<body>```: mendefinisikan body dari HTML

```<style>```: informasi style atau penampilan pada dokumen

```<div>```: untuk spesifikasi suatu divisi atau section dari dokumen

```<input>```: mendefinisikan suatu input

```<label>```: mendefinisikan label untuk ```<input>```

```<link>```: menghubungkan dokumen dengan suatu sumber eksternal (ke halaman lainnya)

```<h1> -- <h6>```: mendefinisikan headings 

```<hr>```: mendisplay garis horizontal

```img```: merepresentasikan suatu gambar img

Jelaskan tipe-tipe CSS selector yang kamu ketahui.
-

1. Id selectors: menggunakan atribut id dari HTML untuk memilih suatu elemen dari HTML

Contoh:
    ```#div-container{ color: pink; background-color: white;```
   Output yang dihasilkan adalah pada div-container, teks akan berwarna pink dengan warna background putih
    
3. Class Selectors: mengimplementasikan kode ke suatu atribut class

Contoh:
    ```.paragraph-class { ...```

3. Element selectors: mengimplementasikan kode berdasarkan tag yang ada
    
Contoh:
    ```h1 { atau p {```
   
4. Group selectors: mengimplementasikan kode ke banyak selectors lainnya dalam satu baris kode yaitu dengan menambahkan koma

Contoh:
    ```h1, .paragraph-class {```


Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
-
1. Kustomisasi templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
2. Kustomisasi templat untuk halaman login, register, dan create-task semenarik mungkin.
Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).
Membuat keempat halaman yang dikustomisasi menjadi responsive.

Diimplementasikan dengan menambahkan bootstrap ke tiap halaman html
```<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">```
di bawah title

```<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>```
di bawah header

Untuk konstumisasi, dilakukan dengan menambahkan tag ```<style> </style``` berserta dengan selector-selectornya

Untuk membuat card,
<img width="560" alt="Screen Shot 2022-10-06 at 11 35 28" src="https://user-images.githubusercontent.com/101708935/194215037-db5a8329-2aee-4b68-a058-6456b72eac0f.png">
Lanjutkan dengan potongan kode yang sudah dibuat

Untuk hover, tambahkan selector sebagai berikut di tag style
<img width="546" alt="Screen Shot 2022-10-06 at 11 35 07" src="https://user-images.githubusercontent.com/101708935/194215060-fe25d398-3e6f-40ae-9e66-5d37e05dfec4.png">



