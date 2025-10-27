---
title: 2024年羊城杯粤港澳大湾区网络安全大赛WP-Crypto AK篇
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247507880&idx=1&sn=495dd4e366e2d027f33bfb9d2213a377&chksm=fa520a16cd258300b2780bbebd9a4bb47f4053a92e8b6c75fc80a2701ae5189ea458852da9fe&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-08-31
fetch_date: 2025-10-06T18:08:09.997139
---

# 2024年羊城杯粤港澳大湾区网络安全大赛WP-Crypto AK篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgIicsWDGeC3KNzyHaU3vYibqtwuuyzsKTRapJUyIUkILHicpibAfpPpzNSw/0?wx_fmt=jpeg)

# 2024年羊城杯粤港澳大湾区网络安全大赛WP-Crypto AK篇

原创

NEURON

山石网科安全技术研究院

## TH\_Curve

题目定义了曲线的加法和乘法，根据x3,y3的计算公式，可以发现这是Hessian curves，已知p,a和曲线上的两个点，可以解出d。

```
p = 10297529403524403127640670200603184608844065065952536889
a = 2
G = (8879931045098533901543131944615620692971716807984752065, 4106024239449946134453673742202491320614591684229547464)
gx,gy=G[0],G[1]
PR.<d>=PolynomialRing(Zmod(p))
f=a*gx^3+gy^3+1-d*gx*gy
ret=f.roots()
print(ret)
```

曲线方程可以写成三次齐次方程的形式，然后构建出椭圆曲线直接求DLP：

```
d=8817708809404273675545317762394593437543647288341187200
Q = (6784278627340957151283066249316785477882888190582875173, 6078603759966354224428976716568980670702790051879661797)
from Crypto.Util.number import *
import gmpy2
p = 10297529403524403127640670200603184608844065065952536889
a = 2
P=(8879931045098533901543131944615620692971716807984752065, 4106024239449946134453673742202491320614591684229547464)

R.<x,y,z> = Zmod(p)[]
cubic = a*x^3 + y^3 + z^3 - d*x*y*z
E = EllipticCurve_from_cubic(cubic,morphism=True)
P = E(P)
Q = E(Q)
m = P.discrete_log(Q)
m=525729205728344257526560548008783649
print(long_to_bytes(m))
```

## BabyCurve

这个题目给的条件有点多了。

通过遍历求出来bc：

```
def mul_curve(n, P, K):
    R = (0, 0)
    while n > 0:
        if n % 2 == 1:
            R = add_curve(R, P, K)
        P = add_curve(P, P, K)
        n = n // 2
    return R
a = 46
d = 20
p1 = 826100030683243954408990060837
K1 = (a, d, p1)
G1 = (560766116033078013304693968735, 756416322956623525864568772142)
P1 = (528578510004630596855654721810, 639541632629313772609548040620)
Q1 = (819520958411405887240280598475, 76906957256966244725924513645)
for i in range(0,1000):
    P1_c=mul_curve(i,G1,K1)
    if P1_c==P1:
        print(i)
        break

for i in range(0,1000):
    Q1_b=mul_curve(i,G1,K1)
    if Q1_b==Q1:
        print(b)
        break
```

拿到bc之后，我们有G，P，直接ecdlp求解key，然后正常aes解密就行。

```
p = 770311352827455849356512448287
E = EllipticCurve(GF(p), [-35, 98])
G = E(584273268656071313022845392380, 105970580903682721429154563816)
P = E(401055814681171318348566474726, 293186309252428491012795616690)
print(P.log(G))
```

```
import hashlib
from Crypto.Util.number import *
from Crypto.Cipher import AES
k=2951856998192356
key = hashlib.sha256(str(k).encode()).digest()[:16]
iv= 0xbae1b42f174443d009c8d3a1576f07d6
ciphertest= 0xff34da7a65854ed75342fd4ad178bf577bd622df9850a24fd63e1da557b4b8a4
iv=long_to_bytes(iv)
ciphertest=long_to_bytes(ciphertest)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertest = cipher.decrypt(ciphertest)
print(ciphertest)
# b'DASCTF{THe_C0rv!_1s_Aw3s0me@!!}\x01'
```

## RSA\_loss

参考这个文章编写：

> bcactf-4.0/rsa-is-broken/rsa-broken-sol.py at main · BCACTF/bcactf-4.0 · GitHub
>
> https://github.com/BCACTF/bcactf-4.0/blob/main/rsa-is-broken/rsa-broken-sol.py

```
from Crypto.Util.number import *
import math
import re
c = 356435791209686635044593929546092486613929446770721636839137
p = 898278915648707936019913202333
q = 814090608763917394723955024893
e=65537
n=p*q
#b'X\xee\x1ey\x88\x01dX\xf6i\x91\x80h\xf4\x1f!\xa7"\x0c\x9a\x06\xc8\x06\x81\x15'

# the idea is that our retrieved m is in fact equivalent to the original m mod n
# so we add multiples of n to retrieve the flag
# but this is inefficient so we have to narrow it down using format
# The flag ends with }, so 7D = 125 mod 256
d = inverse(e,(p-1)*(q-1))
m = pow(c, d, n)
while m % 256 != 125:
    m += n
jump = n * 256
# the flag starts with bcactf{
# we essentially want to try one possible flag length at a time
# by jumping up to the next one starting with bcactf
# 0 is the smallest char (by code) that can appear in the flag
target = b'DASCTF{' + b'0'*math.floor(math.log(m, 256)-7)
md = long_to_bytes(m)
while re.fullmatch(b'[0-9a-zA-Z_{}]+', md) == None:
    if md[0:7] == b'DASCTF{':
        m += jump
        # print(md)
    else:
        m += jump * math.ceil((bytes_to_long(target) - m)/jump)
        target += b'0'
        # print(math.log(m,2))
    md = long_to_bytes(m)
print(md)
# b'DASCTF{o0p5_m3ssaGe_to0_b1g_nv93nd0}'
```

## TheoremPlus

这个最开始感觉像是威尔逊定理这个地方让他跑的慢一些，并且后面模起来看起来跟素数有关，就跑了一组看看。

```
def decode_e(e):
    if e > 1:
        mul = 1
        for i in range(1, e):
            mul *= i
        if e - mul % e - 1 == 0:
            mulmod = mul % e - e
        else:
            mulmod = mul % e
        return mulmod + decode_e(e - 1)
    else:
        return 0
for e in range(100):
    print(abs(decode_e(e)))
```

```
for e in range(150):
    if isPrime(e):
        num=num+1
print(num)
```

经过测试之后发现，稳定的情况下是，这个含有的素数个数，也就是质数量-2。

所以我们直接拉到sage里面求这个质数量：

```
print(len(prime_range(703440151))-2)
```

然后我们拿到的e之后直接解rsa就行：

```
e=36421873
from Crypto.Util.number import *
from gmpy2 import *
n = 18770575776346636857117989716700159556553308603827318013591587255198383129370907809760732011993542700529211200756354110539398800399971400004000898098091275284235225898698802555566416862975758535452624647017057286675078425814784682675012671384340267087604803050995107534481069279281213277371234272710195280647747033302773076094600917583038429969629948198841325080329081838681126456119415461246986745162687569680825296434756908111148165787768172000131704615314046005916223370429567142992192702888820837032850104701948658736010527261246199512595520995042205818856177310544178940343722756848658912946025299687434514029951
c = 2587907790257921446754254335909686808394701314827194535473852919883847207482301560195700622542784316421967768148156146355099210400053281966782598551680260513547233270646414440776109941248869185612357797869860293880114609649325409637239631730174236109860697072051436591823617268725493768867776466173052640366393488873505207198770497373345116165334779381031712832136682178364090547875479645094274237460342318587832274304777193468833278816459344132231018703578274192000016560653148923056635076144189403004763127515475672112627790796376564776321840115465990308933303392198690356639928538984862967102082126458529748355566
p=iroot(n,2)[0]
p=next_prime(p)
q=n//p
phi=(p-1)*(q-1)
d=inverse(e,phi)
m=pow(c,d,n)
print(long_to_bytes(m))
# b'DASCTF{Ot2N63D_n8L6kJt_f40V61m_zS1O8L7}'
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过