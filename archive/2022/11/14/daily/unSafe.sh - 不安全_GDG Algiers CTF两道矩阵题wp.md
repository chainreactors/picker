---
title: GDG Algiers CTF两道矩阵题wp
url: https://buaq.net/go-135435.html
source: unSafe.sh - 不安全
date: 2022-11-14
fetch_date: 2025-10-03T22:39:44.880574
---

# GDG Algiers CTF两道矩阵题wp

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/11e75445163fbfeee446dab5cbecd523.jpg)

GDG Algiers CTF两道矩阵题wp

本文为看雪论坛优秀文章看雪论坛作者ID：狗敦子gdgalgiers crypto wp两道矩阵相关的题，感觉可以整理一下下。the\_matrixpython sln.pyCyberErudites{D
*2022-11-13 17:59:38
Author: [mp.weixin.qq.com(查看原文)](/jump-135435.htm)
阅读量:20
收藏*

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FLIys7ZeazGxWUPvbfACbG6RjwibIHe4j61aQsB91AAZplgd0SpGRYLAGGrhXVnrACs9nK2VDFmVg/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：狗敦子

**gdgalgiers crypto wp**

两道矩阵相关的题，感觉可以整理一下下。

**the\_matrix**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLIys7ZeazGxWUPvbfACbGkba8VPCTkmj8Zm7XQB9hb16fyZ2QLKgpyH8qzqV5g0vd2OibGwIricyg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLIys7ZeazGxWUPvbfACbGf9Us4aIcLSPRApurUdgHVT2Q4xHwDOWDE8G9tRXZxllxxYS3w2XF2w/640?wx_fmt=png)

python sln.py

CyberErudites{Di4g0n4l1zabl3\_M4tric3s\_d4\_b3st}

franklin-last-words

```
# from sage.all import *import jsonfrom Crypto.Hash import SHA256from Crypto.Cipher import AESfrom Crypto.Util.Padding import pad p = 12143520799543738643# def read_matrix(file_name):#     data = open(file_name, 'r').read().strip()#     rows = [list(eval(row)) for row in data.splitlines()]#     return Matrix(GF(p), rows)### D = read_matrix('matrix.txt')# P = read_matrix('public_key.txt')# digD ,A = D.diagonalization()# digP = A.inverse() * P * A# vD = [digD[i][i] for i in range(12)]# vP = [digP[i][i] for i in range(12)]# print(f"vD = {vD}")vD = [37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]# print(f"vP = {vP}")vP = [6751925379844785295, 11256715989719283883, 4551561838026472495, 11383130904596697638, 8534299476177021992, 11184828239802784209, 7103104085280766875, 1622643043767580331, 11104789109564474465, 1502559189506368871, 522368022672629021, 1590703325067650792]# G = GF(p)# K = discrete_log(G(vP[11]), G(vD[11]))# print(f"K = {K}")K = 7619698002081645976 # now we can decipherkey = SHA256.new(data=str(K).encode()).digest()[:2**8]with open("encrypted_flag.txt", "r") as ff:    data_dict = json.load(ff)    iv = bytes.fromhex(data_dict["iv"])    ciphertext = bytes.fromhex(data_dict["ciphertext"])cipher = AES.new(key, AES.MODE_CBC, iv)flag = cipher.decrypt(ciphertext).decode()[:46]print(flag)# CyberErudites{Di4g0n4l1zabl3_M4tric3s_d4_b3st}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLIys7ZeazGxWUPvbfACbGwORqmGrhqswd11pORtQ0TVQKFS1yefInibuHRdxpQ9Drw5TJ2HIE6pw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLIys7ZeazGxWUPvbfACbGMibVcylz5wEmrFuv2hG7BAIATlyeIkibF6v4iaWEzsP1dOxibbeKny5WGA/640?wx_fmt=png)

python sln.py

CyberErudites{Fr4nkl1n\_W3\_n33d\_an0th3R\_S3450N\_A54P}

```
from sage.all import Matrix, IntegerModRingfrom message import N, e, ct  def poly(num):    return [(3*pow(num, 3, N)) % N, (3*pow(num, 6, N)) % N]  def v2polyv(v, num):    return (v - R_3 - pow(num, 9, N)) % N  def polyv2v(v, num):    return (v + R_3 + pow(num, 9, N)) % N  def gen(num):    V2 = Matrix(IntegerModRing(N), [poly(num)])    V1 = V2 * T_    v = (poly_C*V1[0][0] + poly_y*V1[0][1]) % N    table[polyv2v(v, num)] = chr(num)  table = {}R_3 = ct[0]prefix = b"CyberErudites{}"T = Matrix(IntegerModRing(N), [poly(int(prefix[0])), poly(int(prefix[1]))])T_ = T.inverse()# print(T_)poly_C = v2polyv(ct[1], ord('C'))poly_y = v2polyv(ct[2], ord('y'))  for num in range(32, 126):    gen(num)print("".join([table[v] for v in ct[1:]]))# CyberErudites{Fr4nkl1n_W3_n33d_an0th3R_S3450N_A54P}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EUvNq2rQycZibURG09OtYP02r4SdK1V4ysPbxQwYN8ibNrkbkufjicGAI9heEHlw7jPgFibW26C0XF5A/640?wx_fmt=png)

**看雪ID：狗敦子**

https://bbs.pediy.com/user-home-962418.htm

\*本文由看雪论坛 狗敦子 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0XCHXZ3icZXcMlqrP9xKN6J9cwRouvpXMfRrRxdE0xCpPmeqybJGOPibw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458479751&idx=1&sn=ca684920ebd23cc09080ba6eefb94165&chksm=b18e5c0d86f9d51b3b31b8a99231416b78566b3365abfbe25625aeba78a44b769576548b316f&scene=21#wechat_redirect)

看雪2022KCTF秋季赛官网：https://ctf.pediy.com/game-team\_list-18-29.htm

**#****往期推荐**

1.[CVE-2022-21882提权漏洞学习笔记](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471430&idx=1&sn=6a47d0c5c8f3f6204548e80977ecd059&chksm=b18e7c8c86f9f59a88d9b8e83c8297e0ef65034a73436998ab835531baadaa51f3d630793b95&scene=21#wechat_redirect)

2.[wibu证书 - 初探](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471429&idx=1&sn=a85188de9b9697fd1b9e708bb8bb1fdb&chksm=b18e7c8f86f9f59933d6cbf0040ed796f06e37b23f17f1ae842eb22257de02338e1a8d751f6b&scene=21#wechat_redirect)

3.[win10 1909逆向之APIC中断和实验](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471421&idx=2&sn=e83cf7220dc1c4c06a2efc78593e30cc&chksm=b18e7b7786f9f2614ecce34e23be7f71a3d3516766aabda8f25ae41c81ef359a2c245503cf86&scene=21#wechat_redirect)

4.[EMET下EAF机制分析以及模拟实现](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468723&idx=2&sn=5a830d04185d80e1b6cfa639dc6c6c15&chksm=b18e71f986f9f8ef5b3c2fec51f69751e63a5d6bdbadf43b49728ba05606fc4ac63fda378c92&scene=21#wechat_redirect)

5.[sql注入学习分享](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468108&idx=1&sn=42c8ec155e13e3882cf4aeb60cdbb982&chksm=b18e0f8686f98690c9792298abb04dd243862ff8effd545dc668c7b1c682aaacf9797d899e97&scene=21#wechat_redirect)

6.[V8 Array.prototype.concat函数出现过的issues和他们的POC们](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468074&idx=2&sn=06eb27c1649bd4e3a3e43a46a9500add&chksm=b18e0e6086f9877644ba0de33658232f99213d1b1b074342260031cb529c1b7ad1b89b2e0204&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicd7icG69uHMQX9DaOnSPpTgamYf9cLw1XbJLEGr5Eic62BdV6TRKCjWVSQ/640?wx_fmt=gif)

点击“阅读原文”，了解更多！

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MjM5NTc2MDYxMw==&mid=2458483668&idx=2&sn=064572d67c7a3deb310aaf7761c58d7b&chksm=b18e4b5e86f9c248f502b7a96da5a8e15e8e2ebef96a2a1b877ca7a19251dd792a30d95598f3#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)