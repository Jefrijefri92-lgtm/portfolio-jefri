--Bandingin vs Bulan Lalu
  
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

--sql Bandingin vs Bulan Lalu
SELECT 
    bulan,
    total AS penjualan_bulan_ini,
    LAG(total) OVER(ORDER BY bulan) AS penjualan_bulan_lalu,
    total - LAG(total) OVER(ORDER BY bulan) AS selisih
FROM penjualan
ORDER BY bulan;
