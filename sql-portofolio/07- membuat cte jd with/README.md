Pake CTE jadi gini
WITH rata_penjualan AS (
    SELECT AVG(total) AS avg_total 
    FROM penjualan
)
SELECT 
    p.bulan, 
    p.total,
    r.avg_total,
    p.total - r.avg_total AS selisih_dari_avg
FROM penjualan p
CROSS JOIN rata_penjualan r
WHERE p.total > r.avg_total
ORDER BY p.total DESC;

Bedahnya:
1. WITH rata_penjualan AS (...) = Kita bikin "tabel sementara" namanya rata_penjualan isinya rata-rata doang
2. FROM penjualan p CROSS JOIN rata_penjualan r = Tempel rata-ratanya ke tiap baris
3. Baru deh WHERE p.total > r.avg_total = Filter yg di atas rata-rata

Keuntungan CTE:
1. Baca dari atas ke bawah = alur logika jelas. "Pertama itung rata2, terus bandingin"
2. Bisa dipake berulang = rata_penjualan bisa di-JOIN 5x kalo mau
3. Bisa bikin CTE bertingkat = WITH a AS (...), b AS (...), c AS (...)

DROP TABLE IF EXISTS penjualan;
CREATE TABLE penjualan (
    id INT, -- buat urutan
    bulan VARCHAR(10), 
    total INT
);

INSERT INTO penjualan VALUES
(1, 'Jan', 5000000),
(2, 'Feb', 7000000),
(3, 'Mar', 6500000),
(4, 'Apr', 8000000),
(5, 'May', 7200000);

WITH penjualan_banding AS (
    SELECT
        bulan,
        total AS penjualan_bulan_ini,
        LAG(total) OVER(ORDER BY id) AS penjualan_bulan_lalu, -- Ganti ke id
        total - LAG(total) OVER(ORDER BY id) AS selisih,
        ROUND(
            (total - LAG(total) OVER(ORDER BY id)) * 100.0 / 
            LAG(total) OVER(ORDER BY id),
        2) AS persen_tumbuh
    FROM penjualan
)
SELECT * 
FROM penjualan_banding 
WHERE persen_tumbuh > 10
ORDER BY persen_tumbuh DESC;
hasil Mysql:https://dbfiddle.uk/rufr0Ulu
