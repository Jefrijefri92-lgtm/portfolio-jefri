filter kota saja
SELECT * FROM penjualan WHERE kota = 'Jakarta';

menampilkan kopi hitam dengan jumlah lebih dari 30
SELECT * FROM penjualan 
WHERE produk = 'Kopi Hitam' AND jumlah > 30;

Urutkan dari harga termahal
SELECT * FROM penjualan 
ORDER BY harga DESC;

Ambil 2 transaksi terakhir
SELECT * FROM penjualan 
ORDER BY tanggal DESC 
LIMIT 2;
