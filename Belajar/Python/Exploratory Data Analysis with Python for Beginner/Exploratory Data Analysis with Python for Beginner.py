#!/usr/bin/env python
# coding: utf-8

# # Library NumPy
# 
# Numpy berasal dari kata ‘Numerical Python’, sesuai namanya NumPy berfungsi sebagai library untuk melakukan proses komputasi numerik terutama dalam bentuk array multidimensional (1-Dimensi ataupun 2-Dimensi). Array merupakan kumpulan dari variabel yang memiliki tipe data yang sama. NumPy menyimpan data dalam bentuk arrays.

# # Library Pandas
# 
# Pandas merupakan library yang memudahkan dalam melakukan manipulasi, cleansing maupun analisis struktur data. Dengan menggunakan Pandas, dapat memanfaatkan lima fitur utama dalam pemrosesan dan analisis data, yaitu load, prepare, manipulate, modelling, dan analysis data.
# 
# Pandas menggunakan konsep array dari NumPy namun memberikan index kepada array tersebut, sehingga disebut series ataupun data frame. Sehingga bisa dikatakan Pandas menyimpan data dalam dictionary-based NumPy arrays. 1-Dimensi labelled array dinamakan sebagai Series. Sedangkan 2-Dimensi dinamakan sebagai Data Frame.

# # Library SciPy
# 
# Scipy dibangun untuk bekerja dengan array NumPy dan menyediakan banyak komputasi numerik yang ramah pengguna dan efisien seperti rutinitas untuk integrasi, diferensiasi dan optimasi numerik.
# 
# Baik NumPy maupun SciPy berjalan pada semua operating system, cepat untuk diinstall dan gratis. NumPy dan SciPy mudah digunakan, tetapi cukup kuat untuk diandalkan oleh beberapa data scientist dan researcher terkemuka dunia.

# # Library Matplotlib
# 
# Matplotlib merupakan library dari Python yang umum digunakan untuk visualisasi data. Matplotlib memiliki kapabilitas untuk membuat visualisasi data 2-dimensional. Contoh visualisasi yang dapat dibuat dengan menggunakan matplotlib diantaranya adalah
# 
# - Line chart
# - Bar chart
# - Pie chart
# - Box plot chart
# - Violin chart
# - Errorbar chart
# - Scatter chart

# # Memanggil library di Python
# 
# Sebelum dapat digunakan, library tersebut harus terlebih dahulu dipanggil ke dalam lingkungan Python. Command untuk memanggil library di Python menggunakan syntax (menggunakan huruf kecil):
# 
# `
# import library_name as alias
# `
# 
# Alias berfungsi sebagai pengganti nama library, sehingga menghemat komputasi saat function dari library tersebut dipanggil.

# In[1]:


import numpy as np
import pandas as pd


# # Membaca file dari Excel atau CSV sebagai data frame
# 
# Salah satu fungsi Pandas yaitu melakukan load data dari CSV atau Excel file. Syntax yang digunakan untuk melakukan operasi tersebut, yaitu:
# 
# - Membaca  file CSV
# ```
# nama_variabel = pd.read_csv("nama_file.csv")
# ```
# 
# - Membaca file excel
# ```
# nama_variabel = pd.read_excel("nama_file.xlsx")
# ```

# # Tugas Praktek
# 
# Mengimport dataset marketplace ABC dari order.csv dan disimpan ke dalam dataframe bernama order_df.
# 
# Untuk dataset diinput dari link berikut https://storage.googleapis.com/dqlab-dataset/order.csv

# In[2]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")


# # Melihat struktur kolom dan baris dari data frame
# 
# Untuk melihat informasi mengenai berapa size dari dataframe yang akan digunakan termasuk berapa jumlah kolom dan jumlah baris data frame dapat menggunakan fungsi `.shape` pada suatu dataframe. Syntaxnya dinyatakan dengan:
# 
# ```
# print(nama_dataframe.shape)
# ```

# # Tugas Praktek
# 
# Tuliskan syntax Python untuk melihat struktur dari `order_df` dengan menggunakan fungsi `shape`.

# In[3]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.shape)


# # Melihat preview data dari data frame
# 
# Untuk mendapatkan gambaran dari konten dataframe tersebut. Kita dapat menggunakan function head dan tail, dengan syntax:
# 
# ***## Menampilkan konten teratas dari [nama_dataframe]***
# <br> ***## untuk sejumlah bil. bulat [jumlah_data]***
# <br><br>
# `
# print(nama_dataframe.head(jumlah_data))
# `
# 
# ***## Menampilkan konten terbawah dari [nama_dataframe]*** <br>
# ***## untuk sejumlah bil. bulat [jumlah_data]***
# <br><br>
# `
# print(nama_dataframe.tail(jumlah_data))
# `
# 

# <br>
# 
# Jika [jumlah_data] pada function head dan tail dikosongkan maka secara default akan di ditampilkan sebanyak 5 (lima) baris saja. Sehingga bisa ditulis sebagai berikut: 
# 
# ***## DEFAULT: Menampilkan 5 (baris) konten teratas***
# <br> ***## dari [nama_dataframe]***
# <br><br>
# `
# print(nama_dataframe.head())
# `
# 
# 
# ***## DEFAULT: Menampilkan 5 (baris) konten terbawah***
# <br> ***## dari [nama_dataframe]***
# <br><br>
# `
# print(nama_dataframe.tail())
# `

# # Tugas Praktek
# 
# Tampilkan data dari dataframe dengan fungsi `head` dan limit 10 baris!

# In[4]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.head(10))


# # Statistik Deskriptif dari Data Frame - Part 1
# 
# Statistik deskriptif atau summary dalam Python - Pandas, dapat diperoleh dengan menggunakan fungsi `describe()`, yaitu:
# 
# `print(nama_dataframe.describe())`
# 
# Function describe dapat memberikan informasi mengenai nilai rataan, standar deviasi dan IQR (interquartile range).
# 
# Ketentuan umum:
# 
# - Secara umum function **describe()** akan secara otomatis mengabaikan kolom category dan hanya memberikan summary statistik untuk kolom berjenis numerik.
# - Kita perlu menambahkan argument bernama **include = "all"** untuk mendapatkan summary statistik atau statistik deskriptif dari kolom numerik dan karakter.
# 
# yaitu :
# 
# `print(nama_dataframe.describe(include = "all"))`
# 
# Function **describe()** dengan **include="all"** akan memberikan summary statistic dari semua kolom.

# # Statistik Deskriptif dari Data Frame - Part 2
# 
# Jika ingin mendapatkan summary statistik dari kolom yang tidak bernilai angka, maka aku dapat menambahkan command **include=["object"]** pada syntax **describe()**.<br>
# 
# `
# print(nama_dataframe.describe(include = "object"))
# `

# # Statistik Deskriptif dari Data Frame - Part 3
# 
# Untuk mencari rataan dari suatu data dari dataframe. Kita dapat menggunakan syntax mean, median, dan mode dari Pandas.
# 
# `
# print(nama_dataframe.loc[:, "nama_kolom"].mean())
# print(nama_dataframe.loc[:, "nama_kolom"].median())
# print(nama_dataframe.loc[:, "nama_kolom"].mode())
# `

# # Tugas Praktek

# In[5]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# Quick summary  dari segi kuantitas, harga, freight value, dan weight
print(order_df.describe())

# Median dari total pembelian konsumen per transaksi kolom price
print(order_df.loc[:, "price"].median())


# # Mengenal dan Membuat Distribusi Data dengan Histogram
# 
# Histogram merupakan salah satu cara untuk mengidentifikasi sebaran distribusi dari data. Histogram adalah grafik yang berisi ringkasan dari sebaran (dispersi atau variasi) suatu data. 
# 
# Pada histogram, tidak ada jarak antar batang/bar dari grafik. Hal ini dikarenakan bahwa titik data kelas bisa muncul dimana saja di daerah cakupan grafik. Sedangkan ketinggian bar sesuai dengan frekuensi atau frekuensi relatif jumlah data di kelas. Semakin tinggi bar, semakin tinggi frekuensi data. Semakin rendah bar, semakin rendah frekuensi data.
# 
# ***syntax umum:***
# 
# ```
# nama_dataframe[["nama_kolom"]].hist(bins = jumlah_bin, 
#                                     by = nama_kolom, 
#                                     alpha = nilai_alpha, 
#                                     figsize = tuple_ukuran_gambar)
# ```
# <br>
# 
# Beberapa atribut penting dalam histogram pandas:
# 
# - bins = jumlah_bins dalam histogram yang akan digunakan. Jika tidak didefinisikan jumlah_bins, maka function akan secara default menentukan jumlah_bins sebanyak 10.
# - by = nama kolom di DataFrame untuk di group by. (valuenya berupa nama column di dataframe tersebut).
# - alpha = nilai_alpha untuk menentukan opacity dari plot di histogram. (value berupa range 0.0 - 1.0, dimana semakin kecil akan semakin kecil opacity nya)
# - figsize = tuple_ukuran_gambar yang digunakan untuk menentukan ukuran dari plot histogram. Contoh: figsize=(10,12)
# 

# # Tugas Praktek
# 

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# plot histogram kolom: price
order_df[["price"]].hist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()  # Untuk menampilkan histogram plot


# # Standar Deviasi dan Varians pada Pandas
# 
# Varians dan standar deviasi juga merupakan suatu ukuran dispersi atau variasi.
# 
# Syntax dari standar deviasi dan varians pada Pandas:
# 
# ```
# print(nama_dataframe.loc[:, "nama_kolom"].std())
# print(nama_dataframe.loc[:, "nama_kolom"].var())
# ```

# # Tugas Praktek

# In[7]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# Standar variasi kolom product_weight_gram
order_df.loc[:, "product_weight_gram"].std()

# Varians kolom product_weight_gram
order_df.loc[:, "product_weight_gram"].var()


# # Menemukan Outliers Menggunakan Pandas
# 
# **Outliers** merupakan data observasi yang muncul dengan nilai-nilai ekstrim. Yang dimaksud dengan nilai-nilai ekstrim dalam observasi adalah nilai yang jauh atau beda sama sekali dengan sebagian besar nilai lain dalam kelompoknya.
# 
# **Syntax di Python:**
# ```
# Q1 = nama_dataframe.quantile(0.25)
# Q3 = nama_dataframe.quantile(0.75)
# IQR = Q3 - Q1
# print(IQR)
# 
# ```
# 
# 

# In[9]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# Hitung quartile 1
Q1 = order_df[["product_weight_gram"]].quantile(0.25)

# Hitung quartile 3
Q3 = order_df[["product_weight_gram"]].quantile(0.75)

# Hitung inter quartile range dan cetak ke console
IQR = Q3 - Q1
print(IQR)


# # Rename Kolom Data Frame
# 
# Mengganti nama kolom pada Pandas dapat dilakukan dengan 2 cara:
# 
# 1. Menggunakan nama kolom.
# 2. Menggunakan indeks kolom.
# 
# <br>
# 
# ***1. Rename menggunakan nama kolom*** <br>
# syntax : 
# ```
# nama_dataframe.rename(columns={"column_name_before" : "column_name_after"}, inplace = True)
# ```
# 
# <br>
# 
# ***2. Rename menggunakan indeks kolom*** <br>
# syntax : 
# ```
# nama_dataframe.columns.values[no_of_column] = "column_name_after"
# ```

# # Tugas Praktek
# 
# Ubah kolom `freight_value` menjadi `shipping_cost` dalam data frame `order_df`, dengan menggunakan fungsi `rename()`.

# In[10]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={" freight_value" : "shipping_cost "}, inplace=True)
print(order_df)


# # .groupby menggunakan Pandas
# 
# Kegunaan **.groupby** adalah mencari summary dari data frame dengan menggunakan **aggregate** dari kolom tertentu.

# # Tugas Praktek
# 
# Cobalah untuk mencari rata rata dari price per payment_type dari dataset order_df ("https://storage.googleapis.com/dqlab-dataset/order.csv")

# In[11]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# Hitung rata rata dari price per payment_type
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()
print(rata_rata)


# # Sorting Menggunakan Pandas
# 
# **Sorting** adalah sebuah metode mengurutkan data berdasarkan syarat kolom tertentu, dan biasanya digunakan untuk melihat nilai maksimum dan minimum dari dataset. 
# 
# Syntax untuk operasi sorting pada Pandas:
# ```
# nama_dataframe.sort_values(by = "nama_kolom")
# ```
# <br>
# 
# Function tersebut akan secara default mengurutkan secara **ascending** (dimulai dari nilai terkecil), untuk dapat mengurutkan secara **descending** (nilai terbesar lebih dahulu), dapat menggunakan properti tambahan:
# 
# ```
# nama_dataframe.sort_values(by = "nama_kolom", ascending = "False")
# ```

# # Tugas Praktek
# 
# Cari berapa harga maksimum pembelian customer di dataset order_df.

# In[12]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# Hitung harga maksimum pembelian customer
sort_harga = order_df.sort_values(by="price", ascending=False)
print(sort_harga)


# # Tugas dari Andra
# 
# - Median price yang dibayar customer dari masing-masing metode pembayaran.
# - Tentukan metode pembayaran yang memiliki basket size (rataan median price) terbesar.
# - Ubah freight_value menjadi shipping_cost dan cari shipping_cost termahal dari data penjualan tersebut menggunakan sort.
# - Untuk setiap product_category_name, berapa rata-rata weight produk tersebut dan standar deviasi mana yang terkecil dari weight tersebut,
# - Buat histogram quantity penjualan dari dataset tersebut untuk melihat persebaran quantity penjualan tersebut dengan bins = 5 dan figsize= (4,5)

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")


# Median price yang dibayar customer dari masing-masing metode pembayaran. 
median_price = order_df["price"].groupby(order_df["payment_type"]).median()
print(median_price)


# Ubah freight_value menjadi shipping_cost dan cari shipping_cost 
# termahal dari data penjualan tersebut menggunakan sort.
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
sort_value = order_df.sort_values(by="shipping_cost", ascending=0)
print(sort_value)


# Untuk product_category_name, berapa  rata-rata weight produk tersebut 
# dan standar deviasi mana yang terkecil dari weight tersebut, 
mean_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).mean()
print(mean_value.sort_values())
std_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).std()
print(std_value.sort_values())


# Buat histogram quantity penjualan dari dataset tersebutuntuk melihat persebaran quantity 
# penjualan tersebut dengan bins = 5 dan figsize= (4,5)
order_df[["quantity"]].hist(figsize=(4, 5), bins=5)
plt.show()


# In[ ]:




