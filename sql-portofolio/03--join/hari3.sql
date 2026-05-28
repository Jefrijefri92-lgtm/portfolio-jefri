-- Hari 3: INNER JOIN, LEFT JOIN

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
