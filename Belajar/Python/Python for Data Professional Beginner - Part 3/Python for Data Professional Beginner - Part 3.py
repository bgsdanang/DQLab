#!/usr/bin/env python
# coding: utf-8

# # Object Oriented Programming
# 
# Pemrograman berorientasi objek atau dalam bahasa inggris disebut Object Oriented Programming (OOP) adalah paradigma atau teknik pemrograman di mana semua hal dalam program dimodelkan seperti objek dalam dunia nyata.
# 
# Pada paradigma OOP, struktur dari sebuah program dikemas ke dalam sebuah objek yang memiliki serangkaian properti (properties) dan fungsi (behaviours).
# 
# Misal, kita ingin merepresentasikan seorang karyawan ke dalam sebuah program melalui konsep OOP. Seorang karyawan dapat memiliki serangkaian properti seperti nama, usia, keahlian, dll. Kemudian, seorang karyawan juga dapat memiliki fungsi-fungsi seperti hadir ke kantor, absen, lembur, tugas dinas, dll.

# Dalam bahasa pemrograman Python, terdapat 3 konsep utama OO yaitu:
# 
# * Encapsulation: Menyembunyikan sebagian detail yang dimiliki oleh sebuah objek terhadap objek-objek lainnya.
# * Inheritance: Menurunkan serangkaian fungsi-fungsi yang dimiliki oleh sebuah objek ke sebuah objek baru tanpa mengubah makna dari objek acuan yang digunakan.
# * Polymorphism: Konsep untuk menggunakan fungsi-fungsi dengan nama/ tujuan yang sama dengan cara yang berbeda.

# # Class dan Objek dalam Python - Part 1 & 2
# 
# Setiap objek yang kita representasikan dalam program berbasis OOP merupakan instansi/ bentuk nyata dari sebuah konsep yang disebut dengan class. Oleh karena itu, class dapat disebut sebagai kerangka utama (blueprint) dari objek.
# 
# Dalam sebuah class, terdapat dua jenis atribut yaitu.
# 
# * Class Attribute adalah properti/atribut yang bernilai sama untuk oleh seluruh objek dari sebuah
# * Instance Attribute adalah properti/atribut yang nilainya berbeda-beda untuk setiap objek dari sebuah class.

# # Class dan Objek dalam Python - Part 3
# 
# class Karyawan pada umumnya memiliki beberapa atribut seperti nama, usia, pendapatan serta nama perusahaan di mana karyawan tersebut bekerja.

# In[1]:


# Definisikan class Karyawan
class Karyawan:
    nama_perusahaan = 'ABC'
    
# Inisiasi object yang dinyatakan dalam variabel aksara dan senja
aksara = Karyawan()
senja = Karyawan()

# Cetak nama perusahaan melalui penggunaan keyword __class__
# pada class attribute nama_perusahaan
print(aksara.__class__.nama_perusahaan)

# Ubah nama_perusahaan menjadi 'DEF'
aksara.__class__.nama_perusahaan = 'DEF'

# Cetak nama_perusahaan objek aksara dan senja
print(aksara.__class__.nama_perusahaan)
print(senja.__class__.nama_perusahaan)


# # Class dan Objek dalam Python - Part 4
# 
# Pada bagian sebelumnya adalah contoh deklarasi class Karyawan. Kemudian nama, usia dan pendapatan karyawan adalah contoh dari konsep instance attribute. Hal ini dikarenakan setiap karyawan tentunya dapat memiliki nama, usia dan pendapatan yang berbeda.

# In[2]:


# Definisikan class Karyawan
class Karyawan:
    nama_perusahaan = 'ABC'
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        
# Buat object bernama aksara dan senja
aksara = Karyawan('Aksara', 25, 8500000)
senja = Karyawan('Senja', 28, 12500000)

# Cetak objek bernama aksara
print(aksara.nama + ', Usia: ' + str(aksara.usia) + ', Pendapatan ' + str(aksara.pendapatan))

# Cetak objek bernama senja
print(senja.nama + ', Usia: ' + str(senja.usia) + ', Pendapatan ' + str(senja.pendapatan))


# Dari kode diatas, atribut nama, usia dan pendapatan merupakan contoh dari instance variabel. Kemudian fungsi `__init__()` di dalam class Karyawan secara khusus disebut sebagai constructor. Melalui sebuah constructor, kita dapat meng-assign (menginisialisasi) atribut-atribut milik sebuah objek.
# 
# Setiap fungsi (termasuk constructor) akan menerima dirinya sendiri (self) sebagai parameter pertama dari fungsi. Kemudian, kita dapat menambahkan parameter-parameter lain setelah parameter self sesuai dengan kebutuhan.
# 
# Untuk mengakses instance attribute dalam sebuah class, aku perlu menuliskan sintaks self diikuti dengan tanda titik (.) sebelum nama atribut.

# # Behavior pada Class
# 
# Selain dapat mendefinisikan atribut, dalam sebuah class, kita diperbolehkan untuk mendefinisikan fungsi-fungsi (behavior) dari sebuah class. 
# 
# Dari kode seelumnya, kita dapat menambahkan fungsi-fungsi berkaitan dengan class Karyawan. Sebagai contoh, seorang karyawan mungkin saja memiliki pendapatan tambahan berdasarkan banyaknya kerja lembur dan jumlah proyek yang telah diselesaikan.

# In[3]:


# Definisikan class Karyawan berikut dengan attribut dan fungsinya
class Karyawan:
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
    	self.pendapatan_tambahan += insentif_proyek
    def total_pendapatan(self):
    	return self.pendapatan + self.pendapatan_tambahan
    
# Buat object dari karwayan bernama Aksara dan Senja
aksara = Karyawan('Aksara', 25, 8500000)
senja = Karyawan('Senja', 28, 12500000)

# Aksara melaksanakan lembur
aksara.lembur()

# Senja memiliki proyek tambahan
senja.tambahan_proyek(2500000)

# Cetak pendapatan total Aksara dan Senja
print('Pendapatan Total Aksara: ' + str(aksara.total_pendapatan()))
print('Pendapatan Total Senja: ' +str(senja.total_pendapatan()))


# # Tugas Praktek
# 
# Membuat program yang memuat informasi nama, alamat, nomor telepon, dan daftar karyawan yang bekerja. Kemudian masukkan fungsi untuk mengaktifkan dan menonaktifkan karyawan. 
# 
# Lalu masukan class Karyawan yang berisi nama, usia, pendapatan tetap, tambahan, dan insentif lembur.

# In[4]:


# Definisikan class Karyawan
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur): 
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
    
# Definisikan class Perusahaan
class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon): 
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []
    def aktifkan_karyawan(self, karyawan): 
        self.list_karyawan.append(karyawan)
    def nonaktifkan_karyawan(self, nama_karyawan): 
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan :
            if karyawan.nama == nama_karyawan: 
                karyawan_nonaktif = karyawan
                break
        if karyawan_nonaktif is not None: 
            self.list_karyawan.remove(karyawan_nonaktif)


# # Tugas Praktek

# In[5]:


class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan 

class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon): 
        self.nama = nama
        self.alamat = alamat 
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []
    def aktifkan_karyawan(self, karyawan): 
        self.list_karyawan.append(karyawan)
    def nonaktifkan_karyawan(self, nama_karyawan): 
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan: 
                karyawan_nonaktif = karyawan 
                break
        if karyawan_nonaktif is not None: 
            self.list_karyawan.remove(karyawan_nonaktif)

# Definisikan perusahaan
perusahaan = Perusahaan('ABC', 'Jl. Jendral Sudirman, Blok 11', '(021) 95205XX')

# Definisikan nama-nama karyawan

karyawan_1 = Karyawan('Ani', 25, 8500000, 100000)
karyawan_2 = Karyawan('Budi', 28, 12000000, 150000)
karyawan_3 = Karyawan('Cici', 30, 15000000, 200000)

# Aktifkan karyawan di perusahaan ABC
perusahaan.aktifkan_karyawan(karyawan_1) 
perusahaan.aktifkan_karyawan(karyawan_2) 
perusahaan.aktifkan_karyawan(karyawan_3)


# # Encapsulation pada Python - Part 1
# 
# **Enkapsulasi (Encapsulation)** adalah sebuah teknik dalam OOP yang mengizinkan untuk menyembunyikan detail dari sebuah atribut dalam sebuah class. Pada sebelumnya, setiap atribut dan fungsi yang telah didefinisikan belum menggunakan konsep enkapsulasi, yang mengartikan bahwa setiap atribut dan fungsi dapat diakses di luar class.

# # Encapsulation pada Python - Part 2
# 
# Agar suatu properti ataupun fungsi dari sebuah class tidak dapat diakses secara bebas di luar scope milik suatu class, kita dapat mendefinisikan access modifier (level akses) saat sebuah atribut/fungsi didefinisikan.
# 
# Terdapat 2 macam access modifier dalam Python, yakni.
# 
# * Public access: dapat aku definisikan dengan secara langsung menuliskan nama dari atribut/ fungsi. Dalam sebuah objek, atribut/fungsi yang bersifat public access dapat diakses di luar scope sebuah class
# * Private access: dapat aku definisikan dengan menambahkan double underscore (__) sebelum menuliskan nama dari atribut/fungsi. Dalam sebuah objek, atribut/fungsi yang bersifat private access hanya dapat diakses di dalam scope sebuah class.

# In[6]:


# Definisikan class Karyawan
class Karyawan: 
    nama_perusahaan = 'ABC' 
    __insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.__nama = nama
        self.__usia = usia 
        self.__pendapatan = pendapatan 
        self.__pendapatan_tambahan = 0
    def lembur(self):
        self.__pendapatan_tambahan += self.__insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.__pendapatan_tambahan +=insentif_proyek 
    def total_pendapatan(self):
        return self.__pendapatan + self.__pendapatan_tambahan
    
# Buat objek karyawan bernama Aksara
aksara = Karyawan('Aksara', 25, 8500000)

# Akses ke attribute class Karyawan
print(aksara.__class__.nama_perusahaan)

# Akan menimbulkan error ketika di run
print(aksara.__nama)


# # Inheritance pada Python ??? Part 1
# 
# **Inheritance** adalah salah satu mekanisme di konsep OO yang mengizinkan untuk mendefinisikan sebuah class baru berdasarkan class yang sebelumnya telah dideklarasikan.

# In[7]:


# Definisikan class Karyawan (sebagai base class)
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
    
    
# Buat class turunan (sebagai inherit class) dari class karyawan, 
# yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        
    # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
        
        
# Buat kembali class turunan (sebagai inherit class) dari class karyawan,  
# yaitu class IlmuwanData
class IlmuwanData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        
        # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
        
        
# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())


# Buat objek karyawan yang bekerja sebagai IlmuwanData
senja = IlmuwanData('Senja', 28, 13000000)
senja.tambahan_proyek(2000000)
print(senja.total_pendapatan())


# Dari kode diatas, melalui konsep inheritance class AnalisData dan IlmuwanData akan memiliki setiap atribut dan fungsi yang dimiliki oleh class Karyawan (Hal ini dikarenakan seluruh atribut dan fungsi dari class Karyawan bersifat public).
# 
# Pada konsep inheritance, class AnalisData dan class IlmuwanData disebut sebagai child class dari class Karyawan; sehingga class Karyawan dapat disebut sebagai parent class dari class AnalisData dan IlmuwanData.
# 
# Suatu child class dapat mengakses atribut ataupun fungsi yang dimiliki oleh parent class dengan menggunakan fungsi super(). Pada contoh di atas, fungsi super() digunakan oleh child class (AnalisData dan IlmuwanData) untuk mengakses constructor yang dimiliki oleh parent class (Karyawan).

#  # Inheritance pada Python ??? Part 2
#  
# Pada bagian sebelumnya telah mempelajari bagaimana child class mewarisi fungsi/atribut dari parent class dengan menggunakan fungsi super(). Melalui konsep inheritance, child class dapat memodifikasi atribut/ fungsi yang diwarisi oleh sebuah parent class dengan mendefinisikan ulang atribut/ fungsi menggunakan nama yang sama. 

# In[8]:


# Definisikan class Karyawan (sebagai base class)
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
    
    
# Buat class turunan (sebagai inherit class) dari class karyawan, 
# yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        
    # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
        
        
# Buat kembali class turunan (sebagai inherit class) dari class karyawan,  
# yaitu class IlmuwanData
class IlmuwanData(Karyawan):
    
    # mengubah atribut insentif_lembur yang digunakan pada fungsi lembur()
    insentif_lembur = 500000
    def __init__(self, nama, usia, pendapatan): 
        super().__init__(nama, usia, pendapatan)
        
        
# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())


# Buat objek karyawan yang bekerja sebagai IlmuwanData
senja = IlmuwanData('Senja', 28, 13000000)
senja.lembur()
print(senja.total_pendapatan())


# fungsi lembur pada objek aksara sebagai bagian dari class AnalisData akan menambahkan total_pendapatan milik objek sebesar 250000 mengikuti insentif_lembur milik class Karyawan.
# 
# fungsi lembur pada objek senja sebagai bagian dari class IlmuwanData akan menambahkan total_pendapatan milik objek sebesar 500000 dikarenakan class IlmuwanData telah mendefinisikan kembali nilai insentif lembur menjadi 500000

# # Polymorphism pada Python - Part 1
# 
# Saat mendefinisikan kembali fungsi yang telah diwarisi oleh parent class, secara tidak langsung telah menerapkan salah satu mekanisme yang secara khusus pada paradigma OO disebut dengan istilah **polymorphism**.

# In[9]:


# Definisikan class Karyawan (sebagai base class)
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
    
    
# Buat class turunan (sebagai inherit class) dari class karyawan, 
# yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        
    # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
        
    # menerapkan polymorphism dengan mendefinisikan kembali fungsi 
    # lembur() pada class AnalisData 
    def lembur(self):
        
        # pendapatan tambahan pada class AnalisData sebesar
        # 10 % dari pendapatannya.
        self.pendapatan_tambahan += int(self.pendapatan * 0.1)
        
        
# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())


# # Polymorphism pada Python - Part 2
# 
# Pada konsep **inheritance**, melalui fungsi **super()**, selain dapat mengakses constructor milik **parent class**, **child class** juga dapat mengakses atribut/fungsi yang dimiliki oleh parent class.

# In[10]:


# Definisikan class Karyawan (sebagai base class)
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
    
    
# Buat class turunan (sebagai inherit class) dari class karyawan, 
# yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan): 
        super().__init__ (nama, usia, pendapatan)
        
    # mendefinisikan kembali fungsi lembur() pada class AnalisData 
    def lembur(self):
        
        # memanggil fungsi lembur pada class Karyawan 
        super().lembur()
        
        # pendapatan tambahan pada class AnalisData sebesar
        # 5 % dari pendapatannya.
        self.pendapatan_tambahan += int(self.pendapatan * 0.05)
        
        
# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())


# # Tugas Praktek
# 
# Membuat **class Tenaga Lepas**, berisi nama, usia, dan pendapatan selama bergabung di sebuah proyek. Karyawan lepas dapat insentif dari proyek yang dikerjakan. Kalau hasilnya sukses bisa dapat 1% dari nilai proyek.

# In[11]:


# Definisikan class Karyawan
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self,jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
    
    
# Definisikan class TenagaLepas sebagai child class dari
# class Karyawan
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan, 0)
    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += nilai_proyek * 0.01


# # Tugas Praktek
# 
# Kemudian tambahkan class yang merepresentasikan masing-masing pekerjaan di divisi ini. Di divisi perusahaan tersebut ada empat bidang pekerjaan, mulai dari analisis data, ilmuwan data, pembersih data, dan dokumenter teknis. 
# 
# Setiap peran punya sistem penerimaan fee yang berbeda. Ilmuwan data akan mendapat insentif tambahan sebesar 10% dari proyek yang dikerjakan, dan dokumenter teknis adalah satu-satunya peran yang tidak menerima insentif dari proyek.

# In[12]:


# Definisikan class Karyawan sebagai parent class
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self,jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
    
    
# Definisikan class TenagaLepas sebagai child class dari
# class Karyawan
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan, 0)
    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += nilai_proyek * 0.01
        
        
# Definisikan class AnalisData sebagai child class dari
# class Karyawan
class AnalisData(Karyawan): 
    pass


# Definisikan class IlmuwanData sebagai child class dari
# class Karyawan
class IlmuwanData(Karyawan):
    def tambahan_proyek(self, nilai_proyek): 
        self.pendapatan_tambahan += 0.1 * nilai_proyek
        
        
# Definisikan class PembersihData sebagai child class dari
# class TenagaLepas
class PembersihData(TenagaLepas): 
    pass


# Definisikan class DokumenterTeknis sebagai child class dari
# class TenagaLepas
class DokumenterTeknis(TenagaLepas):
    def tambahan_proyek(self, jumlah_tambahan): 
        return


# # Overloading
# 
# Metode overloading mengizinkan sebuah class untuk memiliki sekumpulan fungsi dengan nama yang sama dan parameter yang berbeda. Berkaitan dengan hal ini, Python tidak mengizinkan pendeklarasian fungsi (baik pada class ataupun tidak) dengan nama yang sama.

# # Tugas Praktek
# 
# Perusahaan ABC memiliki 3 orang karyawan baru, Aku di minta untuk mengisi tabel, dengan detail berikut:
# 
# - Budi berusia = 21 dan pendapatan = 5000000
# - Didi berusia 25 dan pendapatan = 5000000
# - Hadi berusia 21 dan pendapatan = 8000000

# In[13]:


class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    # usia akan di-set nilainya menjadi 21 saat tidak
    # dispesifikasikan dan pendapatan akan di-set nilainya
    # menjadi 5000000 saat tidak dispesifikasikan
    def __init__(self, nama, usia=21, pendapatan=5000000): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
    
# Karyawan baru pertama yang bernama Budi
karyawan_baru1 = Karyawan('Budi')
print(karyawan_baru1.nama)
print(karyawan_baru1.usia)
print(karyawan_baru1.total_pendapatan())

# Karyawan baru ke-2 yang bernama Didi, umur 25
karyawan_baru2 = Karyawan('Didi', 25)
print(karyawan_baru2.nama)
print(karyawan_baru2.usia)
print(karyawan_baru2.total_pendapatan())

# Karyawan baru ke-3 yang bernama Hadi, pendapatan 8000000
karyawan_baru3 = Karyawan('Hadi', pendapatan = 8000000)
print(karyawan_baru3.nama)
print(karyawan_baru3.usia)
print(karyawan_baru3.total_pendapatan())


# # Studi Kasus dari Senja
# 
# Di perusahaan ini, seorang analis data yang masuk umumnya berusia 21, memiliki pendapatan senilai 6.500.000 dan insentif lembur senilai 100.000. Kemudian, untuk seorang ilmuwan data yang masuk umumnya berusia 25, memiliki pendapatan senilai 12.000.000, dan insentif lembur senilai 150.000. Di sisi lain, untuk tenaga lepas, hanya terdapat pendapatan umum senilai 4000000 untuk pembersih data dan 2500000 untuk dokumenter teknis. 
# 
# - Simulasikan dengan program yang telah dibuat.
# - Cetak total pengeluaran yang dimiliki perusahaan untuk menguji fungsionalitas konsep dan teknik polymorphism yang diterapkan.

# In[14]:


# Definisikan class Karyawan sebagai parent class
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self,jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan 

    
# Definisikan class TenagaLepas sebagai child class dari class Karyawan 
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan): 
        super().__init__(nama, usia, pendapatan, 0)
    def tambahan_proyek(self, nilai_proyek): 
        self.pendapatan_tambahan += nilai_proyek  * 0.01

        
# Definisikan class AnalisData sebagai child class dari class Karyawan 
class AnalisData(Karyawan):
    def __init__(self, nama, usia = 21, pendapatan = 6500000,
				 insentif_lembur = 100000):
        super().__init__(nama, usia, pendapatan, insentif_lembur)

        
# Definisikan class IlmuwanData sebagai child class dari class Karyawan
class IlmuwanData(Karyawan):
    def __init__(self, nama, usia = 25, pendapatan = 12000000,
				 insentif_lembur = 150000):
        super().__init__(nama, usia, pendapatan,insentif_lembur)
    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += 0.1 * nilai_proyek

        
# Definisikan class PembersihData sebagai child class dari class TenagaLepas
class PembersihData(TenagaLepas):
    def __init__(self, nama, usia, pendapatan = 4000000):
        super().__init__(nama, usia, pendapatan)

        
# Definisikan class DokumenterTeknis sebagai child class dari class TenagaLepas
class DokumenterTeknis(TenagaLepas):
    def __init__(self, nama, usia, pendapatan = 2500000):
        super().__init__(nama, usia, pendapatan)
        def tambahan_proyek(self, jumlah_tambahan):
            return

        
# Definisikan class Perusahaan 
class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []
    def aktifkan_karyawan(self, karyawan): 
        self.list_karyawan.append(karyawan)
    def nonaktifkan_karyawan(self, nama_karyawan): 
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan: 
                karyawan_nonaktif = karyawan 
                break
        if karyawan_nonaktif is not None: 
            self.list_karyawan.remove(karyawan_nonaktif)
    def total_pengeluaran(self): 
        pengeluaran = 0
        for karyawan in self.list_karyawan:
            pengeluaran += karyawan.total_pendapatan() 
        return pengeluaran
    def cari_karyawan(self, nama_karyawan): 
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan: 
                return karyawan
        return None

    
# Create object karyawan sesuai dengan tugasnya masing-masing
# seperti yang dinyatakan dalam tabel.
ani = PembersihData('Ani', 25)
budi = DokumenterTeknis('Budi', 18)
cici = IlmuwanData('Cici')
didi = IlmuwanData('Didi', 32, 20000000)
efi = AnalisData('Efi')
febi = AnalisData('Febi', 28, 12000000)


# Create object perusahaan
perusahaan = Perusahaan('ABC','Jl. Jendral Sudirman, Blok 11', '(021) 95812XX')


# Aktifkan setiap karyawan yang telah didefinisikan
perusahaan.aktifkan_karyawan(ani)
perusahaan.aktifkan_karyawan(budi)
perusahaan.aktifkan_karyawan(cici)
perusahaan.aktifkan_karyawan(didi)
perusahaan.aktifkan_karyawan(efi)
perusahaan.aktifkan_karyawan(febi)


# Cetak keseluruhan total pengeluaran perusahaan
print(perusahaan.total_pengeluaran())


# In[ ]:




