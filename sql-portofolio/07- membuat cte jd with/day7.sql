--Pake CTE jadi gini

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

Gabungin Day 6 + Day 7. Pake CTE buat nyimpen hasil LAG(),
terus dari situ filter cuma bulan yg persen_tumbuh > 10%
    
WITH penjualan_banding AS (
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
    -- ORDER BY dan ; dihapus dari sini
)
SELECT * 
FROM penjualan_banding 
WHERE persen_tumbuh > 10
ORDER BY persen_tumbuh DESC; -- ORDER BY pindah ke sini
