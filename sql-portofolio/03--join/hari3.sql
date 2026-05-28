-- Hari 3: INNER JOIN, LEFT JOIN

-- Setup tabel ke-2 produk untuk JOIN
CREATE TABLE produk (
  produk_id INT PRIMARY KEY,
  nama_produk VARCHAR(50),
  harga INT
);

INSERT INTO produk (produk_id, nama_produk, harga) VALUES
(1, 'Kopi Hitam', 15000),
(2, 'Cappuccino', 22000),
(3, 'Latte', 25000),
(4, 'Americano', 18000);

-- Pastikan tabel penjualan juga punya kolom produk_id
ALTER TABLE penjualan ADD COLUMN produk_id INT;
UPDATE penjualan SET produk_id = 1 WHERE produk = 'Kopi Hitam';
UPDATE penjualan SET produk_id = 2 WHERE produk = 'Cappuccino';
UPDATE penjualan SET produk_id = 3 WHERE produk = 'Latte';

-- 1. INNER JOIN: Ambil penjualan + nama produk
SELECT p.tanggal, pr.nama_produk, p.kota, p.jumlah, pr.harga
FROM penjualan p
INNER JOIN produk pr ON p.produk_id = pr.produk_id
ORDER BY p.tanggal DESC;

-- 2. Hitung total revenue per produk pakai JOIN
SELECT pr.nama_produk, SUM(p.jumlah * pr.harga) AS total_revenue
FROM penjualan p
INNER JOIN produk pr ON p.produk_id = pr.produk_id
GROUP BY pr.nama_produk
ORDER BY total_revenue DESC;

-- 3. LEFT JOIN: Lihat semua produk, walau belum pernah terjual
SELECT pr.nama_produk, COUNT(p.id) AS jumlah_terjual
FROM produk pr
LEFT JOIN penjualan p ON p.produk_id = pr.produk_id
GROUP BY pr.nama_produk;
