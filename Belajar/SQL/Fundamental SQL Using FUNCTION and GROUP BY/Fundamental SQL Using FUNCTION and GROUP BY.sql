-- Fungsi Skalar Matematika - ABS()
SELECT 
StudentID, 
FirstName, 
LastName, 
Semester1, 
Semester2, 
ABS(MarkGrowth) AS MarkGrowth 
FROM students;

-- Fungsi Skalar Matematika - CEILING()
SELECT 
StudentID, 
FirstName, 
LastName, 
CEILING(semester1) AS Semester1, 
CEILING(semester2) AS Semester2, 
MarkGrowth 
FROM students;

-- Fungsi Skalar Matematika - FLOOR()
SELECT 
StudentId, 
FirstName, 
LastName, 
FLOOR(Semester1) as Semester1, 
FLOOR(Semester2) AS Semester2, 
MarkGrowth 
FROM students;

-- Fungsi Skalar Matematika - ROUND()
SELECT 
StudentID, 
FirstName, 
LastName, 
ROUND(Semester1,1) as Semester1, 
ROUND(Semester2,0) as Semester2, 
MarkGrowth 
FROM students;

-- Fungsi Skalar Matematika - SQRT()
SELECT 
StudentID,
FirstName, 
LastName, 
SQRT(Semester1) as Semester1, 
Semester2, 
MarkGrowth 
From students;

-- Tugas Praktek
SELECT 
StudentID, 
FirstName, 
LastName, 
MOD(Semester1,2) AS Semester1, 
Semester2, 
EXP(MarkGrowth) 
FROM students;

-- Fungsi Text - CONCAT()
SELECT 
StudentID, 
CONCAT(FirstName, LastName) as Name,
Semester1, 
Semester2, 
MarkGrowth 
FROM students;

-- Fungsi Text - SUBSTRING_INDEX( )
SELECT 
StudentID, 
SUBSTRING_INDEX(Email,'@',1) AS Name 
FROM students;

-- Fungsi Text - SUBSTR( )
SELECT 
StudentID, 
SUBSTR(FirstName,2,3) as Initial 
From students;

-- Fungsi Text - LENGTH( )
SELECT 
StudentID, 
FirstName, 
LENGTH(FirstName) as Total_Char 
FROM students;

-- Fungsi Text - REPLACE( )
SELECT 
StudentID, 
Email, 
REPLACE(Email,'yahoo','gmail') AS new_Email 
FROM students;

-- Tugas Praktek
SELECT 
StudentID, 
UPPER(FirstName) AS FirstName, 
LOWER(LastName) AS LastName 
FROM students;

-- Fungsi Aggregate - SUM()
SELECT 
SUM(Semester1) as Total_1, 
SUM(Semester2) as total_2 
FROM students;

-- Fungsi Aggregate - COUNT()
SELECT 
COUNT(FirstName) AS Total_student 
From students;

-- Fungsi Aggregate - AVG( )
select 
avg(Semester1) as avg_1,
avg(Semester2) as avg_2 
FROM students;

-- Tugas Praktek
SELECT 
MIN(Semester1) as Min1, 
MAX(Semester1) as Max1, 
MIN(Semester2) as Min2, 
Max(Semester2) as Max2 
FROM students;

-- Group by Single Column
SELECT province,
COUNT(DISTINCT order_id) as total_order,
SUM(item_price) as total_price
FROM sales_retail_2019
GROUP BY province;

-- Group by Multiple Column
SELECT province,
brand,
COUNT(DISTINCT order_id) as total_order,
SUM(item_price) as total_price 
FROM sales_retail_2019
GROUP BY province, brand;

-- Fungsi Aggregate dengan Grouping
SELECT 
province, 
COUNT(DISTINCT order_id) as total_unique_order, 
SUM(item_price) as revenue 
FROM sales_retail_2019 
GROUP BY province;

-- Tugas Praktek
SELECT MONTH(order_date) AS order_month, SUM(item_price) AS total_price, 
CASE  
    WHEN SUM(item_price) >= 30000000000 THEN 'Target Achieved'
    WHEN SUM(item_price) <= 25000000000 THEN 'Less Performed'
	ELSE 'Follow Up'
END as remark
FROM sales_retail_2019
GROUP BY MONTH(order_date);

-- Proyek Pekerjaan - Analisis Penjualan Part 1
-- 1. Total jumlah seluruh penjualan (total/revenue).
SELECT SUM(total) as total 
FROM tr_penjualan;

-- 2. Total quantity seluruh produk yang terjual.
SELECT SUM(qty) as qty 
FROM tr_penjualan;

-- 3. Total quantity dan total revenue untuk setiap kode produk.
SELECT 
kode_produk, 
SUM(qty) as qty, 
SUM(total) as total 
FROM tr_penjualan
GROUP BY kode_produk;

-- Proyek Pekerjaan - Analisis Penjualan Part 2
-- 4. Rata - Rata total belanja per kode pelanggan.
SELECT kode_pelanggan, 
AVG(total) as avg_total 
FROM tr_penjualan
GROUP BY kode_pelanggan;

/* 5. Selain itu,  jangan lupa untuk menambahkan kolom baru 
dengan nama ‘kategori’ yang mengkategorikan total/revenue ke dalam 
3 kategori: High: > 300K; Medium: 100K - 300K; Low: <100K. */
SELECT kode_transaksi,kode_pelanggan,no_urut,kode_produk, nama_produk, qty, total,
CASE  
    WHEN total > 300000 THEN 'High'
    WHEN total < 100000 THEN 'Low'  
    ELSE 'Medium'  
END as kategori 
FROM tr_penjualan;


