-- Hari 2: GROUP BY, SUM, COUNT, AVG, HAVING
-- Dataset: Penjualan Kopi Jan 2024

-- 1. Total penjualan per kota
SELECT kota, SUM(jumlah) AS total_cup
FROM penjualan
GROUP BY kota
ORDER BY total_cup DESC;

-- 2. Rata-rata harga per produk
SELECT produk, AVG(harga) AS rata_rata_harga, COUNT(*) AS jumlah_transaksi
FROM penjualan
GROUP BY produk;

-- 3. Kota dengan total penjualan > 50 cup
SELECT kota, SUM(jumlah) AS total_cup
FROM penjualan
GROUP BY kota
HAVING SUM(jumlah) > 50;

-- 4. Jumlah transaksi per tanggal
SELECT tanggal, COUNT(*) AS jumlah_transaksi
FROM penjualan
GROUP BY tanggal
ORDER BY tanggal;
