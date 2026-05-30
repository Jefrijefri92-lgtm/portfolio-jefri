## Day 4 - CTE & Subquery: Bandingin ke Rata-rata Kategori

**Tujuan**: Nampilin produk yg harganya di atas rata-rata kategorinya sendiri.

**Konsep**: 
1. `GROUP BY + AVG()` → hitung rata-rata per kategori
2. Subquery/CTE → simpen hasil rata-rata sementara
3. `JOIN` → tempelin rata-rata ke tiap produk
4. `WHERE` → filter produk yg > rata-rata

**Query:**
```sql
SELECT 
    p.nama_produk,
    p.kategori,
    p.harga,
    ROUND(a.rata_rata_harga, 0) AS rata_kategori
FROM produk p
JOIN (
    SELECT 
        kategori,
        AVG(harga) AS rata_rata_harga
    FROM produk
    GROUP BY kategori
) a ON p.kategori = a.kategori
WHERE p.harga > a.rata_rata_harga
ORDER BY p.kategori, p.harga DESC;


link my sql :https://dbfiddle.uk/K--bX9V1
