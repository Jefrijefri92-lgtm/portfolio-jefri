
1. Tampilkan semua data
```sql
  CREATE TABLE penjualan (
    id INT,
    tanggal DATE,
    kota VARCHAR(20),
    produk VARCHAR(20),
    jumlah INT,
    harga INT
);

INSERT INTO penjualan VALUES
(1, '2024-01-05', 'Jakarta', 'Kopi Hitam', 50, 15000),
(2, '2024-01-06', 'Bandung', 'Latte', 30, 25000),
(3, '2024-01-07', 'Jakarta', 'Cappuccino', 40, 22000),
(4, '2024-01-08', 'Surabaya', 'Kopi Hitam', 60, 15000),
(5, '2024-01-09', 'Bandung', 'Kopi Hitam', 25, 15000),
(6, '2024-01-10', 'Jakarta', 'Latte', 35, 25000);
    
2. filter kota saja  
SELECT * FROM penjualan;
SELECT * FROM penjualan WHERE kota = 'Jakarta';

3. menampilkan kopi hitam dengan jumlah lebih dari 30
SELECT * FROM penjualan 
WHERE produk = 'Kopi Hitam' AND jumlah > 30;

4. Urutkan dari harga termahal
SELECT * FROM penjualan 
ORDER BY harga DESC;

5. Ambil 2 transaksi terakhir
SELECT * FROM penjualan 
ORDER BY tanggal DESC 
LIMIT 2;
