---
title: Daily AlpacaHack B-SIDE 2/17-20 ECRSA writeup
url: https://furutsuki.hatenablog.com/entry/2026/02/21/155330
source: ふるつき
date: 2026-02-21
fetch_date: 2026-02-22T04:10:07.630872
---

# Daily AlpacaHack B-SIDE 2/17-20 ECRSA writeup

[![„Åµ„Çã„Å§„Åç](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[„Åµ„Çã„Å§„Åç](https://furutsuki.hatenablog.com/)

[Ë™≠ËÄÖ„Å´„Å™„Çã](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_medium=button&utm_campaign=subscribe_blog&utm_source=blogs_topright_button)

# [„Åµ„Çã„Å§„Åç](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v Ë®ò‰∫ã„Åå„Çà„Åã„Å£„Åü„Çâ„Çπ„Çø„Éº„Å§„Åë„Å¶„ÅÑ„Å£„Å¶„Åè„ÅÝ„Åï„ÅÑ

[2026-02-21](https://furutsuki.hatenablog.com/archive/2026/02/21)

# [Daily AlpacaHack B-SIDE 2/17-20 ECRSA writeup](https://furutsuki.hatenablog.com/entry/2026/02/21/155330)

AlpacaHack„Å®„ÅÑ„ÅÜ„Éó„É©„ÉÉ„Éà„Éï„Ç©„Éº„ÉÝ„Åß„ÅØÊØéÊó•1ÂïèCTF„ÅÆÂïèÈ°å„ÅåÂá∫È°å„Åï„Çå„ÇãDaily AlpacaHack„Å®„ÅÑ„ÅÜÂèñ„ÇäÁµÑ„Åø„ÅåË°å„Çè„Çå„Å¶„ÅÑ„Åæ„Åô„ÄÇ„Åì„ÅÆDaily AlpacaHack„Åß„ÅØCTF„Å´Âàù„ÇÅ„Å¶Ëß¶„Çå„ÇãÂàùÂøÉËÄÖ„ÄúÂêë„Åë„ÅÆÂïèÈ°å„ÅåÊèê‰æõ„Åï„Çå„Å¶„ÅÑ„Åæ„Åô„Åå„ÄÅ2026Âπ¥2Êúà„Åã„Çâ„ÅØDaily AlpacaHack B-SIDE„Å®„Åó„Å¶„ÄÅËÖïË©¶„ÅóÂïèÈ°å„ÅåÊèê‰æõ„Åï„Çå„Çã„Çà„ÅÜ„Å´„Å™„Çä„Åæ„Åó„Åü„ÄÇ

ÁßÅ„Åå‰ΩúÂïè„Åó„ÅüECRSA„Å®„ÅÑ„ÅÜÂïèÈ°å„ÇÇ„Åì„ÅÆB-SIDE„ÅÆÂïèÈ°å„Å®„Åó„Å¶2/17 - 20„ÅÆ4Êó•ÈñìÊèê‰æõ„Åï„Çå„Å¶„ÅÑ„Åæ„Åó„Åü„ÄÇ‰ªäË¶ã„Åü„Å®„Åì„Çç„Éî„ÉÉ„ÇØ„Ç¢„ÉÉ„ÉóÊúüÈñì‰∏≠„ÅØ40 solves„ÄÅÊúüÈñìÁµÇ‰∫ÜÂæå„Å´1 solve„Åó„Å¶„ÅÑ„Åü„ÅÝ„ÅÑ„Å¶„ÅÑ„Åæ„Åó„Åü„ÄÇÂèñ„ÇäÁµÑ„Çì„Åß„ÇÇ„Çâ„Å£„ÅüÁöÜÊßò„ÄÅ„ÅÇ„Çä„Åå„Å®„ÅÜ„Åî„Åñ„ÅÑ„Åæ„Åô„ÄÇ„Åì„ÅÆË®ò‰∫ã„Åß„ÅØ‰ΩúÂïèËÄÖwriteup„Å®„Åó„Å¶„ÄÅÊÉ≥ÂÆöËß£Ê≥ï„ÇíË™¨Êòé„Åó„Åæ„Åô„ÄÇ

---

ÂïèÈ°å„ÅØÊ¨°„ÅÆ„Å®„Åä„Çä„Åß„Åô„ÄÇ

```
import os

# secp521r1 patemeter
p = 0x01ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
K = GF(p)
a = K(0x01fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc)
b = K(0x0051953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00)
EC = EllipticCurve(K, (a, b))

while True:
    Q = EC.random_point()
    q = int(Q.xy()[0])
    R = 2*Q
    r = int(R.xy()[0])
    if is_prime(q) and is_prime(r):
        break

n = q*r
e = 65537
m = int.from_bytes(os.environ.get("FLAG", "Alpaca{dummy}").encode(), "big")
assert m < n
c = pow(m, e, n)

print("n = {}".format(n))
print("e = {}".format(e))
print("c = {}".format(c))
```

secp521r1„Å®„ÅÑ„ÅÜÊ•ïÂÜÜÊõ≤Á∑ö‰∏ä„ÅÆ„É©„É≥„ÉÄ„ÉÝ„Å™ÁÇπ![ Q](https://chart.apis.google.com/chart?cht=tx&chl=%20Q)„Åä„Çà„Å≥„ÄÅ„Åù„ÅÆ2ÂÄçÁÇπ![ R](https://chart.apis.google.com/chart?cht=tx&chl=%20R)„Å´„Å§„ÅÑ„Å¶„ÄÅ„Åù„Çå„Åû„Çå„ÅÆxÂ∫ßÊ®ô![ q, r](https://chart.apis.google.com/chart?cht=tx&chl=%20q%2C%20r)„ÅåÁ¥ÝÊï∞„Åß„ÅÇ„Çã„Å®„Åç„ÄÅ![ n=qr, e=65537](https://chart.apis.google.com/chart?cht=tx&chl=%20n%3Dqr%2C%20e%3D65537)„ÅÆRSAÊöóÂè∑„Åß„Éï„É©„Ç∞„ÅåÊöóÂè∑Âåñ„Åï„Çå„Å¶„ÅÑ„Åæ„Åô„ÄÇ‰Ωï„Çâ„Åã„ÅÆÊñπÊ≥ï„Åß„Åì„ÅÆRSAÊöóÂè∑„ÇíËß£Ë™≠„Åó„ÄÅÊöóÂè∑Êñá„Åã„ÇâÂπ≥Êñá„ÇíÂæ©ÂÖÉ„Åß„Åç„Çå„Å∞„Éï„É©„Ç∞„ÅåÂæó„Çâ„Çå„Åæ„Åô„ÄÇÂïèÈ°åÂêç„ÅÆÈÄö„Çä„ÄÅEC (Elliptic Curve = Ê•ïÂÜÜÊõ≤Á∑ö)„Å®RSAÊöóÂè∑„ÇíÁµÑ„ÅøÂêà„Çè„Åõ„ÅüÂïèÈ°å„Åß„Åô„ÄÇ

„Éï„É©„Ç∞„ÅØRSAÊöóÂè∑„ÅßÊöóÂè∑Âåñ„Åï„Çå„Å¶„ÅÑ„Çã„ÅÆ„Åß„ÄÅ„Åæ„ÅöRSAÊöóÂè∑„Å´„Å§„ÅÑ„Å¶ËÄÉ„Åà„Åæ„Åô„ÄÇRSAÊöóÂè∑„ÅÆÁÝ¥„ÇäÊñπ„ÅØÂâçÊèêÊù°‰ª∂„Å´„Çà„Å£„Å¶Êßò„ÄÖ„Å™„ÇÇ„ÅÆ„ÅåÁü•„Çâ„Çå„Å¶„ÅÑ„Åæ„Åô„Åå„ÄÅ„Åì„ÅÆÂïèÈ°å„Åß„ÅØ![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)„ÅÆÊßãÊàê„Åå„É©„É≥„ÉÄ„ÉÝ„Å™Á¥ÝÊï∞„Åß„ÅØ„Å™„Åè„ÄÅÁâπÂà•„Å™Êù°‰ª∂„Çí„ÇÇ„Å§Á¥ÝÊï∞![ q, r](https://chart.apis.google.com/chart?cht=tx&chl=%20q%2C%20r)„ÇíÁî®„ÅÑ„Å¶Ë°å„Çè„Çå„Å¶„ÅÑ„Çã„ÅÆ„Åß„ÄÅ![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)„ÇíÁ¥ÝÂõÝÊï∞ÂàÜËß£„Åô„Çã„Åì„Å®„Åß„ÄÅRSAÊöóÂè∑„Å´„Åä„ÅÑ„Å¶ÁßòÂåø„Åô„Åπ„Åç„Éë„É©„É°„Éº„Çø„Åß„ÅÇ„Çã![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)„ÅÆÁ¥ÝÂõÝÊï∞![ q, r](https://chart.apis.google.com/chart?cht=tx&chl=%20q%2C%20r)„ÇíÂæ©ÂÖÉ„Åó„ÄÅÂæ©Âè∑Èçµ![ d](https://chart.apis.google.com/chart?cht=tx&chl=%20d)„ÇíË®àÁÆó„Åô„Çã„Åì„Å®„Åß![ flag = c^d \mod n](https://chart.apis.google.com/chart?cht=tx&chl=%20flag%20%3D%20c%5Ed%20%5Cmod%20n)„Å®„Éï„É©„Ç∞„ÇíÊ±Ç„ÇÅ„Çã„Åì„Å®„Å´„Å™„Çä„Åù„ÅÜ„Åß„Åô„ÄÇ

„Åß„ÅØ![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)„ÇíÁ¥ÝÂõÝÊï∞ÂàÜËß£„Åô„ÇãÊñπÊ≥ï„Å´„Å§„ÅÑ„Å¶ËÄÉ„Åà„Åæ„Åô„ÄÇÂÖàËø∞„ÅÆÈÄö„Çä„ÄÅ![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)„ÅØÁâπÂà•„Å™Èñ¢‰øÇ„Çí„ÇÇ„Å§2„Å§„ÅÆÁ¥ÝÊï∞![ q, r](https://chart.apis.google.com/chart?cht=tx&chl=%20q%2C%20r)„ÅÆÁ©ç„Å™„ÅÆ„Åß„ÄÅ„Åì„ÅÆ2Á¥ÝÊï∞„ÅÆÈñ¢‰øÇ„ÇíÂà©Áî®„Åó„Å¶![ q, r](https://chart.apis.google.com/chart?cht=tx&chl=%20q%2C%20r)„ÇíÊ±Ç„ÇÅ„Çâ„Çå„Åù„ÅÜ„Åß„Åô„ÄÇ„Åù„ÅÆÈñ¢‰øÇ„Å®„ÅØ„ÄÅ![ r](https://chart.apis.google.com/chart?cht=tx&chl=%20r)„ÅØ![ q](https://chart.apis.google.com/chart?cht=tx&chl=%20q)„ÇíxÂ∫ßÊ®ô„Å®„Åô„ÇãÁÇπ„ÅÆ2ÂÄç„ÅÆ‰ΩçÁΩÆ„ÅÆÁÇπ„ÅÆxÂ∫ßÊ®ô„Åß„Åô„Åã„Çâ„ÄÅ**Ê•ïÂÜÜÊõ≤Á∑ö„ÅÆ2ÂÄçÂÖ¨Âºè**„Åß„Åù„ÅÆÈñ¢‰øÇ„ÅåË°®„Åõ„Åæ„Åô„ÄÇ

Êõ≤Á∑ö ![ y^2 \equiv x^3 + ax + b \mod p](https://chart.apis.google.com/chart?cht=tx&chl=%20y%5E2%20%5Cequiv%20x%5E3%20%2B%20ax%20%2B%20b%20%5Cmod%20p) ‰∏ä„ÅÆÁÇπ![ (x_1, y_1)](https://chart.apis.google.com/chart?cht=tx&chl=%20%28x_1%2C%20y_1%29)„ÅÆ2ÂÄçÁÇπ![ (x_2, y_2)](https://chart.apis.google.com/chart?cht=tx&chl=%20%28x_2%2C%20y_2%29)„ÇíÊ±Ç„ÇÅ„ÇãÂºè

![ x_2 \equiv \lambda^2 - x_1 - x_1 \mod p](https://chart.apis.google.com/chart?cht=tx&chl=%20x_2%20%5Cequiv%20%5Clambda%5E2%20-%20x_1%20-%20x_1%20%5Cmod%20p)
![ y_2 \equiv \lambda(x_2 - x_1) + y_1 \mod p](https://chart.apis.google.com/chart?cht=tx&chl=%20y_2%20%5Cequiv%20%5Clambda%28x_2%20-%20x_1%29%20%2B%20y_1%20%5Cmod%20p)
„Åü„ÅÝ„Åó![ \lambda \equiv \frac{3x_1^2 + a}{2y_1} \mod p](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Clambda%20%5Cequiv%20%5Cfrac%7B3x_1%5E2%20%2B%20a%7D%7B2y_1%7D%20%5Cmod%20p)

„Åì„ÅÆÂºè„Å´![ q, r](https://chart.apis.google.com/chart?cht=tx&chl=%20q%2C%20r)„ÇíÂΩì„Å¶„ÅØ„ÇÅ„Çã„Å®![ r \equiv \lambda^2 - q - q \equiv \left( \frac{3q^2 + a}{2q_y} \right) ^2 - 2q \equiv \frac{9q^4 + 6aq + a^2}{4q_y^2} - 2q \mod p](https://chart.apis.google.com/chart?cht=tx&chl=%20r%20%5Cequiv%20%5Clambda%5E2%20-%20q%20-%20q%20%5Cequiv%20%5Cleft%28%20%5Cfrac%7B3q%5E2%20%2B%20a%7D%7B2q_y%7D%20%5Cright%29%20%5E2%20-%202q%20%5Cequiv%20%5Cfrac%7B9q%5E4%20%2B%206aq%20%2B%20a%5E2%7D%7B4q_y%5E2%7D%20-%202q%20%5Cmod%20p)„Åß„Åô„ÄÇ

ÁÇπ![ Q](https://chart.apis.google.com/chart?cht=tx&chl=%20Q)„ÅÆyÂ∫ßÊ®ô„ÅØÊú™Áü•„ÅÆÂÄ§„Åß„ÄÅ„Åì„Åì„Åæ„ÅßÁôªÂÝ¥„Åó„Å¶„ÅÑ„Åæ„Åõ„Çì„Åß„Åó„Åü„Åå‰æøÂÆú‰∏ä![ q_y](https://chart.apis.google.com/chart?cht=tx&chl=%20q_y)„Å®Ë°®„Åó„Åæ„Åó„Åü„ÄÇÊ•ïÂÜÜÊõ≤Á∑ö‰∏ä„ÅÆÁÇπ„ÅØ![ y^2 \equiv x^3 + ax + b \mod p](https://chart.apis.google.com/chart?cht=tx&chl=%20y%5E2%20%5Cequiv%20x%5E3%20%2B%20ax%20%2B%20b%20%5Cmod%20p) „Å®„ÅÑ„ÅÜÈñ¢‰øÇ„ÇíÊåÅ„Å°„Åæ„Åô„Åã„Çâ„ÄÅÂÖàÁ®ã„ÅÆÂºè„ÅÆ![ q_y^2](https://chart.apis.google.com/chart?cht=tx&chl=%20q_y%5E2)„Å´„Åì„Çå„Çí‰ª£ÂÖ•„Åó„Å¶![ r \equiv \frac{9q^4 + 6aq^2 + a^2}{4(q^3 + aq + b)}  - 2q \equiv \frac{(9q^4 + 6aq^2 + a^2) - (8q^4 + 8aq^2 + 8bq)}{4(q^3 + aq + b)} \equiv \frac{q^4 - 2aq^2 - 8bq + a^2}{4(q^3 + aq + b)} \mod p](https://chart.apis.google.com/chart?cht=tx&chl=%20r%20%5Cequiv%20%5Cfrac%7B9q%5E4%20%2B%206aq%5E2%20%2B%20a%5E2%7D%7B4%28q%5E3%20%2B%20aq%20%2B%20b%29%7D%20%20-%202q%20%5Cequiv%20%5Cfrac%7B%289q%5E4%20%2B%206aq%5E2%20%2B%20a%5E2%29%20-%20%288q%5E4%20%2B%208aq%5E2%20%2B%208bq%29%7D%7B4%28q%5E3%20%2B%20aq%20%2B%20b%29%7D%20%5Cequiv%20%5Cfrac%7Bq%5E4%20-%202aq%5E2%20-%208bq%20%2B%20a%5E2%7D%7B4%28q%5E3%20%2B%20aq%20%2B%20b%29%7D%20%5Cmod%20p)„Åß„Åô[\*1](#f-3b29fa45 "ÂΩìÁÑ∂„Åì„Çì„Å™Ë®àÁÆó„ÇíÊâã„Åß„Åô„ÇãÂøÖË¶Å„ÅØ„Å™„Åè„ÄÅÂâçÊèê„Å®„Å™„ÇãÊù°‰ª∂„ÅÆÂºè„ÇíSageMath„ÇÑWolfram„Å™„Å©„Å´Á™Å„Å£Ëæº„ÇÅ„Å∞„Çà„ÅÑ„Åß„Åô")„ÄÇ„Åì„Çå„Åß![ r](https://chart.apis.google.com/chart?cht=tx&chl=%20r)„Çí![ q](https://chart.apis.google.com/chart?cht=tx&chl=%20q)„Çí‰Ωø„Å£„Å¶Ë°®„Åõ„Åæ„Åó„Åü„ÄÇ

![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)„ÇíÊîπ„ÇÅ„Å¶Ë®òËø∞„ÅóÁõ¥„Åô„Å®![ n \equiv qr \equiv q\frac{q^4 - 2aq^2 - 8bq + a^2}{4(q^3 + aq...