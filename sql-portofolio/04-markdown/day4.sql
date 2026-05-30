
### 2. Isi file `day4.sql`
Langsung copy semua biar bisa di-run:
```sql
-- Day 4: Produk di atas rata-rata kategori
-- 1. Bikin tabel
CREATE TABLE produk (
    id INT PRIMARY KEY,
    nama_produk VARCHAR(50),
    kategori VARCHAR(20),
    harga INT
);

-- 2. Isi data
INSERT INTO produk VALUES
(1, 'iPhone 15', 'Elektronik', 15000000),
(2, 'Samsung S24', 'Elektronik', 12000000),
(3, 'Earphone 50rb', 'Elektronik', 50000),
(4, 'Kaos Uniqlo', 'Pakaian', 300000),
(5, 'Jaket Gore-Tex', 'Pakaian', 2500000),
(6, 'Kaos Oblong', 'Pakaian', 80000),
(7, 'Beras 5kg', 'Sembako', 70000),
(8, 'Minyak 2L', 'Sembako', 35000);

-- 3. Query utama
SELECT 
    p.nama_produk,
    p.kategori,
    p.harga,
    ROUND(a.rata_rata_harga, 0) AS rata_kategori
FROM produk p
JOIN (
    SELECT kategori, AVG(harga) AS rata_rata_harga
    FROM produk
    GROUP BY kategori
) a ON p.kategori = a.kategori
WHERE p.harga > a.rata_rata_harga
ORDER BY p.kategori;
