from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jefri Design - Jasa Logo Profesional</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif; }
        body { background: #f5f5f5; color: #333; line-height: 1.6; }
        header { background: #1e40af; color: white; padding: 60px 20px; text-align: center; }
        header h1 { font-size: 2.5rem; margin-bottom: 10px; }
        header p { font-size: 1.2rem; opacity: 0.9; }
        .btn { display: inline-block; background: #fbbf24; color: #1e3a8a; padding: 12px 30px; 
               margin-top: 20px; border-radius: 50px; text-decoration: none; font-weight: bold; }
        .btn:hover { background: #f59e0b; }
        section { padding: 60px 20px; max-width: 1000px; margin: auto; }
        .portfolio { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 30px; }
        .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
        .card img { width: 100%; height: 200px; object-fit: cover; border-radius: 8px; background: #ddd; }
        .card h3 { margin: 15px 0 5px 0; }
        footer { background: #1e3a8a; color: white; text-align: center; padding: 30px 20px; margin-top: 40px; }
        @media(max-width:600px){ header h1{font-size: 2rem;} }
                /* CSS Lightbox */
        .lightbox { 
            display: none; 
            position: fixed; 
            z-index: 999;
            top: 0; left: 0; 
            width: 100%; height: 100%; 
            background: rgba(0,0,0,0.9);
        }
        .lightbox:target { 
            display: flex; 
            justify-content: center; 
            align-items: center; 
        }
        .lightbox img { 
            max-width: 90%; 
            max-height: 90%; 
            border: 4px solid white;
            border-radius: 8px;
        }
        .close { 
            position: absolute; 
            top: 20px; 
            right: 40px; 
            color: white; 
            font-size: 50px; 
            font-weight: bold;
            text-decoration: none;
        }
        .close:hover { color: #fbbf24; }
        .card img { cursor: zoom-in; }
        
        /* Responsive buat HP */
.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
}
@media (max-width: 768px) {
    body {
        padding: 20px;
    }
    .container {
        flex-direction: column;
        align-items: center;
    }
    .card {
        width: 90%;
        max-width: 350px;
    }
    h1 {
        font-size: 2rem;
    }
    .lightbox img {
        max-width: 95%;
    }
}
    </style>
</head>
<body>

    <header>
        <h1>JEFRI DESIGN</h1>
        <p>Bikin Logo Keren, Brand Makin Kenceng</p>
        <a href="https://wa.me/6285602956092" class="btn">Chat WA Sekarang</a>
    </header>

    <section>
        <h2 style="text-align:center; font-size:2rem; margin-bottom:10px;">Hasil Karya</h2>
        <p style="text-align:center; margin-bottom:20px;">Contoh logo yang dibikin pake CorelDRAW X7</p>
        
        <div class="portfolio">
            <div class="card">
            <a href="#logo1">
                <img src="/static/logo.png" alt="logo kopi senja.png">
            </a>
                <h3>Logo Kopi Senja</h3>
                <p>Style minimalis, warna coklat</p>
            </div>
            <div class="card">
               <a href="#logo2">
                <img src="/static/logo2.png" alt="logo toko kue.png">
            </a>
                <h3>Logo Toko Kue</h3>
                <p>Style playful, warna cerah</p>
            </div>
            <div class="card">
                <a href="#logo3">
                <img src="/static/logo3.jpg" alt="logo bengkel.jpg">
            </a>
                <h3>Logo Bengkel</h3>
                <p>Style tegas, maskulin</p>
            </div>
        </div>
    </section>

    <section style="background:white;">
        <h2 style="text-align:center; font-size:2rem; margin-bottom:30px;">Kenapa Pilih Saya?</h2>
        <div class="portfolio">
            <div class="card">
                <h3>⚡ Cepat</h3>
                <p>Jadi 1-2 hari. Revisi 3x gratis.</p>
            </div>
            <div class="card">
                <h3>💎 File Lengkap</h3>
                <p>Dapat PNG, JPG, SVG, CDR. Siap cetak.</p>
            </div>
            <div class="card">
                <h3>💰 Harga Teman</h3>
                <p>Mulai 150rb aja. Kualitas premium.</p>
            </div>
        </div>
    </section>

    <footer>
        <p>© 2026 Jefri Design | Cilacap, Jawa Tengah</p>
        <p>WA: 0856-0295-6092 | IG: @jefri.design</p>
    </footer>
    <!-- pop-up gambar logo 1 ---->
    <div id="logo1" class="lightbox">
        <a href="#" class="close">&times;</a>
         <img src="/static/logo.png">
    </div>
    
     <div id="logo2" class="lightbox">
        <a href="#" class="close">&times;</a>
         <img src="/static/logo2.png">
    </div>
    
     <div id="logo3" class="lightbox">
        <a href="#" class="close">&times;</a>
         <img src="/static/logo3.jpg">
    </div>
    <section style="padding: 60px 20px; background: #f9fafb;">
    <h2 style="text-align: center; margin-bottom: 40px; font-size: 2rem;">Apa Kata Client</h2>
    <h2 style="text-align: center; margin-bottom: 40px; font-size: 2rem;">Apa Kata Mereka</h2>
    
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px; max-width: 1000px; margin: auto;">
        
        <!-- Testimoni 1 -->
        <div style="background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 300px;">
            <div style="color: #fbbf24; font-size: 1.2rem; margin-bottom: 10px;">⭐⭐⭐⭐⭐</div>
            <p style="font-style: italic; margin-bottom: 15px;">"Desainnya keren parah! Revisi juga cepet. Bakal order lagi buat project selanjutnya."</p>
            <div style="display: flex; align-items: center; gap: 10px; margin-top: 15px;">
    <img src="https://i.pravatar.cc/40?img=3" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;"> 
    <div>
        <p style="font-weight: bold; margin: 0;">Rudi Samo</p>
        <p style="font-size: 0.9rem; color: #666; margin: 0;">Admin Store Miqu</p>
    </div>
</div>
        </div>

        <!-- Testimoni 2 -->
        <div style="background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 300px;">
            <div style="color: #fbbf24; font-size: 1.2rem; margin-bottom: 10px;">⭐⭐⭐⭐⭐</div>
            <p style="font-style: italic; margin-bottom: 15px;">"Komunikatif banget. Hasil logo sesuai brief. Harga worth it sama kualitasnya."</p>
            <div style="display: flex; align-items: center; gap: 10px; margin-top: 15px;">
    <img src="https://i.pravatar.cc/40?img=5" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;"> 
    <div>
        <p style="font-weight: bold; margin: 0;">Sari Indah</p>
        <p style="font-size: 0.9rem; color: #666; margin: 0;">Founder Hijab Store</p>
    </div>
</div>
        </div>

        <!-- Testimoni 3 -->
        <div style="background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 300px;">
            <div style="color: #fbbf24; font-size: 1.2rem; margin-bottom: 10px;">⭐⭐⭐⭐⭐</div>
            <p style="font-style: italic; margin-bottom: 15px;">"Udah 3x repeat order. Nggak pernah kecewa. Recommended designer!"</p>
            <div style="display: flex; align-items: center; gap: 10px; margin-top: 15px;">
    <img src="https://i.pravatar.cc/40?img=12" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;"> 
    <div>
        <p style="font-weight: bold; margin: 0;">Bambang Red</p>
        <p style="font-size: 0.9rem; color: #666; margin: 0;">Owner Kaos Trif</p>
    </div>
</div>
        </div>

    </div>
</section>
</body>
</html>
    '''
@app.route('/kirim', methods=['POST'])
def kirim():
    nama = request.form['nama']
    email = request.form['email'] 
    pesan = request.form['pesan']
    
    print("=== PESAN BARU ===")
    print(f"Nama: {nama}")
    print(f"Email: {email}")
    print(f"Pesan: {pesan}")
    print("==================")
    
    return "Terima kasih! Pesan Anda sudah terkirim."
    app = app
if __name__ == '__main__':
    app.run(host=0'.0.0.0.0', port=5000)
