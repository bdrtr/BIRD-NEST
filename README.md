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
![Ekran Görüntüsü](https://github.com/bdrtr/BIRD-NEST/issues/1) 

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
