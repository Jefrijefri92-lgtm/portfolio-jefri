--Setup Data Baru
CREATE TABLE penjualan (
    bulan VARCHAR(10),
    total INT
);

INSERT INTO penjualan VALUES
('Jan', 5000000),
('Feb', 7000000),
('Mar', 6500000),
('Apr', 8000000),
('May', 7200000);

Bandingin vs Bulan Lalu
SELECT 
    bulan,
    total AS penjualan_bulan_ini,
    LAG(total) OVER(ORDER BY bulan) AS penjualan_bulan_lalu,
    total - LAG(total) OVER(ORDER BY bulan) AS selisih
FROM penjualan
ORDER BY bulan;

1. LAG(total) = "Ambil nilai total dari 1 baris SEBELUMNYA"
2. OVER(ORDER BY bulan) = Urutannya pake kolom bulan. Kalo ga di-ORDER BY, ngawur hasilnya
3. LEAD(total) = Kebalikannya LAG, ngambil dari 1 baris SETELAHNYA

MENAMPILKAN PRESENTASE PERBANDINGAN
SELECT 
    bulan,
    total AS penjualan_bulan_ini,
    LAG(total) OVER(ORDER BY bulan) AS penjualan_bulan_lalu,
    total - LAG(total) OVER(ORDER BY bulan) AS selisih,
    ROUND(
        (total - LAG(total) OVER(ORDER BY bulan)) * 100.0 / 
        LAG(total) OVER(ORDER BY bulan), 
    2) AS persen_tumbuh
FROM penjualan
ORDER BY bulan;

   hasilnya ada di my SQL: https://dbfiddle.uk/nrBp06Xe
