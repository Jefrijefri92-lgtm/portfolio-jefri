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
