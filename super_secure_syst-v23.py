# Super Secure Syst v23 - API Connector + Sensor Real-Time
# Practical Application Game - Tron Neural Grid
# Cara pakai: python super_secure_syst_v23.py
# Nanti buka: http://localhost:8000/api/sensor/live
# Game index.html otomatis ambil data dari sini, kalau gagal pakai simulasi.

import json, random, time, os
from http.server import BaseHTTPRequestHandler, HTTPServer

def load_json(name, default):
    try:
        with open(name, encoding="utf-8") as f:
            return json.load(f)
    except:
        return default

def sensor_live(market="Rumah Tangga"):
    # Data sensor dunia nyata - kalau hardware belum nyambung, pakai simulasi
    # Nanti ganti bagian ini dengan baca serial ESP32-S3 / TCS34725 / MQ-135 / SHT41 / IMX219 / MLX90640
    return {
        "timestamp": time.time(),
        "market": market,
        "temp": round(36 + random.random(), 1),
        "mq135": random.randint(20, 45),
        "sht41_temp": round(24 + random.random()*3, 1),
        "sht41_humidity": random.randint(85, 98),
        "tcs34725": {"r": random.randint(100, 200), "g": random.randint(100, 200), "b": random.randint(100, 200)},
        "imx219": "deteksi: kaktus / api / orang",
        "mlx90640": round(28 + random.random()*35, 1),
        "esp32_s3": "ONLINE - WiFi ke HP / Laptop",
        "kapasitor": "cadangan daya OK",
        "lampu": "ON - cahaya memancar",
        "status": "AKTIF BERFUNGSI",
        "pts": 84729,
    }

def dino_auto():
    # Logika reel @kedotronic - Dinosaur Game Arduino
    # Sensor gelap = ada kaktus -> Servo tekan SPASI
    cahaya = random.randint(200, 800)
    if cahaya < 400:
        return "LOMPAT! Kaktus terdeteksi! Servo tekan SPASI!"
    return "Jalan... tidak ada halangan"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/sensor/live"):
            data = sensor_live()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        elif self.path.startswith("/api/dino"):
            data = {"dino": dino_auto(), "score": random.randint(0, 1000)}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        elif self.path.startswith("/api/peralatan"):
            data = load_json("peralatan.json", {})
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        elif self.path.startswith("/api/kontrak"):
            data = load_json("kontrak.json", {})
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Super Secure Syst v23 - API jalan! Coba /api/sensor/live")
    def log_message(self, *a):
        pass

if __name__ == "__main__":
    print("Super Secure Syst v23 jalan di http://localhost:8000")
    print("Coba: /api/sensor/live  /api/dino  /api/peralatan  /api/kontrak")
    # Test sensor 3x biar keliatan
    for i in range(3):
        print(sensor_live())
        print(dino_auto())
        time.sleep(0.5)
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
