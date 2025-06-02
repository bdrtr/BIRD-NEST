# BirdNest Detector

Python3, YOLOv8 ve PySide5 kullanarak canlı videolarda kuş yuvalarını tespit eden görüntü işleme uygulaması.

---

## Özellikler

- Canlı video akışında gerçek zamanlı kuş yuvası tespiti  
- YOLOv8 ile yüksek doğruluklu nesne algılama  
- PySide5 tabanlı kullanıcı dostu grafik arayüzü  
- Kamera veya video dosyasından görüntü alma desteği  

---

## Gereksinimler

- Python 3.8+  
- PySide5  
- Ultralytics YOLOv8  
- OpenCV (cv2)  
- NumPy  
- GPU destekliyorsa CUDA (opsiyonel, hızlandırma için)  

---
![Ekran Görüntüsü](https://private-user-images.githubusercontent.com/69633060/449999647-f8b5e5cb-f625-40a4-a9f1-63e590927a3c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDg4NDY1ODQsIm5iZiI6MTc0ODg0NjI4NCwicGF0aCI6Ii82OTYzMzA2MC80NDk5OTk2NDctZjhiNWU1Y2ItZjYyNS00MGE0LWE5ZjEtNjNlNTkwOTI3YTNjLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA2MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNjAyVDA2MzgwNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTkzYmVjYjEwYTc4OTI5OGJkNDc4ZGIxYjVjNTNhODYwMDc0ZmYyNzFlZmVkYzEzMDI1OWViYjYxMTE5MjQ4MjEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.bqt8ilBuCmZTXZE40kRrGW1WIX2x6-5B44bXWCuDzMA) 

## Kurulum

1. Depoyu klonlayın veya dosyaları indirin:

```bash
git clone https://github.com/kullaniciAdi/BirdNestDetector.git
cd BirdNestDetector
```
2. Sanal Ortam
   ```bash
   python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

   ```
3. Gerekli paketler
   `pip install -r requirements.txt`
   
Dikkat Edilmesi Gerekenler
- Kameranızın bilgisayarınıza bağlı ve erişilebilir olduğundan emin olun.

- YOLOv8 modeli büyük olabilir; GPU hızlandırması için CUDA desteği önerilir.

- Gerçek zamanlı performans donanımınıza bağlıdır.

Lisans
MIT Lisansı ile lisanslanmıştır.

@bdrtr
