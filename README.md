# Osm53 Şifreleme/Şifre Çözme Sistemi

Osm53 sınıfı, üç farklı karakter kümesini kullanarak basit ama yaratıcı bir şifreleme ve çözme mekanizması sağlar.

---

## Özellikler

- *Şifreleme*: Metni, karakter indeksleri ve rastgele harflerle kodlar.
- *Şifre Çözme*: Orijinal metni geri dönüştürür.
- Destekler:
  - Küçük harfler (Türkçe karakterler dahil).
  - Büyük harfler (Türkçe karakterler dahil).
  - Özel karakterler ve semboller.
  - Sayılar (0-9).

---

## Kullanım

python
from osm53 import Osm53

# Şifreleme
veri = "Merhaba!"
sifreli = Osm53.crypt(veri)

# Şifre Çözme
cozulmus = Osm53.decrypt(sifreli)


### Örnek
python
Girdi:  "Merhaba!"
Şifreli: "65P5m21C9q0i1G0J100p"
Çözülen: "Merhaba!"


---

## Kısıtlamalar
- Eğitim amaçlıdır, üretim ortamında güvenli bir şifreleme için kullanılmamalıdır.
- Şifrelemedeki rastgele karakterler brute-force ile çözülebilir.

---

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.

---

## Yazar
[Osman YANGIN](https://github.com/Bothi98) tarafından geliştirilmiştir.