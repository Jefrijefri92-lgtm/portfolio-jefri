## Day 5 - Window Function: ROW_NUMBER() Ranking
**Tujuan**: Kasih ranking produk termahal per kategori

**Query Juara 1 Tiap Kategori:**
```sql
SELECT nama_produk, kategori, harga
FROM (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY kategori ORDER BY harga DESC) AS ranking
    FROM produk
) ranked
WHERE ranking = 1;

LINK MYSQL:https://dbfiddle.uk/tkx_7yZ7
