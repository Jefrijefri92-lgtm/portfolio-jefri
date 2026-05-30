SELECT 
    nama_produk,
    kategori,
    harga,
    ROW_NUMBER() OVER(PARTITION BY kategori ORDER BY harga DESC) AS ranking
FROM produk
ORDER BY kategori, ranking;

LINK MYSQL:
