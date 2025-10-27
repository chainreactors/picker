---
title: 强网杯2024 solve2-apk-赛题解析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588041&idx=1&sn=066267a614cf9489ea94c308645a5603&chksm=b18c230386fbaa156cad76ce682b029ed2f3a54bf3500c51994a92dcf9aa58ad8722c3a1bdd2&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-05
fetch_date: 2025-10-06T20:08:18.647332
---

# 强网杯2024 solve2-apk-赛题解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMLIPazNGcQcrsKLia3Q2ibPxJTicLQh3VoglJibbcficAqlRMug21QQYjlAw/0?wx_fmt=jpeg)

# 强网杯2024 solve2-apk-赛题解析

Aar0n

看雪学苑

我们首先使用jeb进行分析，搜索关键词success定位到逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMhnz7JHOK9iaiadrNXyfSgS39Q99picmy2YHSSbhUia4FYNkBsG0DNBayxQ/640?wx_fmt=png&from=appmsg)

外层函数是一个魔改tea，过了前32字节检测才能进入下一个函数进行判断。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMmkCJ3icctJL3PLUUl73fgp34L0vLwn4Tw39NWKDibBvJ7Jzcmg2pfic5Q/640?wx_fmt=png&from=appmsg)

```
#include <iostream>
#include <cstdio>
#include <stdint.h>  // For uint32_t
using namespace std;

void tea_decrypt(uint32_t* v) {
    uint32_t v0 = v[0], v1 = v[1], sum = 0xC6EF3720, i;
    uint32_t delta = 0x9e3779b9;
    uint32_t k[5] = { 598323648, 1213115916, 970832168, 274853062};

    for (i = 0; i < 32; i++) {

        v1 -= (((v0 << 4) + k[2] ^ v0) + (sum ^ (v0 >> 5)) + k[3]);
        v0 -= (((v1 << 4) + k[0] ^ v1) + (sum ^ (v1 >> 5)) + k[1]);
        sum -= delta;
    }
    v[0] = v0;
    v[1] = v1;
}

uint32_t switchEndian(uint32_t num) {
    return ((num >> 24) & 0x000000FF) | // 取最高字节
           ((num >> 8) & 0x0000FF00) | // 取第二字节
           ((num << 8) & 0x00FF0000) | // 取第三字节
           ((num << 24) & 0xFF000000); // 取最低字节
}

int main() {
    uint32_t key[] = { 598323648, 1213115916, 970832168, 274853062 };

    uint32_t data[] = {
        0x5E5440B0, 2057046228, 0x4A1ED228, 0x233FE7C, 0x96461450, 0x88A670ED, 0xF79BFC89, 0x20C3D75F,0
    };

    for (int i = 0; i < 8; i += 2) {
        tea_decrypt(&data[i]);
    }

    for (int i = 0; i < 8; ++i) {
         data[i] = switchEndian(data[i]);
    }
    printf("%s",data);

    return 0;
}
// Come on you are about to get it>
```

即可得到前32位的正确数据，将后面的测试数据放在>后继续在H0.a.successWithString()中进行二轮check。

进入这个函数即可看到两个[256]的sbox，将部分数据搜索即可知为twofish算法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMic8zIhOGrEFFD0KlicVm8abdHcuxIn8elNTAibKhV2RmQp4UMwagaATSw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMDOunGp7ETIglC9g9mw60mz3XHwLStbLwFgkGZwO3Jbibfr9It449UmQ/640?wx_fmt=png&from=appmsg)

找到源码与jeb里的很相似

[link]:https://android.googlesource.com/platform/tools/base/+/master/jobb/src/main/java/Twofish/Twofish\_Algorithm.java

```
   /**
    * Use (12, 8) Reed-Solomon code over GF(256) to produce a key S-box
    * 32-bit entity from two key material 32-bit entities.
    *
    * @param  k0  1st 32-bit entity.
    * @param  k1  2nd 32-bit entity.
    * @return  Remainder polynomial generated using RS code
    */
   private static final int RS_MDS_Encode( int k0, int k1) {
      int r = k1;
      for (int i = 0; i < 4; i++) // shift 1 byte at a time
         r = RS_rem( r );
      r ^= k0;
      for (int i = 0; i < 4; i++)
         r = RS_rem( r );
      return r;
   }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMKqNasJ89nluNBWiauW6FFQ7g450C39YJYoa8bPcFLDm805OXxuK8qNQ/640?wx_fmt=png&from=appmsg)

我们在H0.a.c处下断点动调获取key：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMB2emXqU3Ul0XuMoOkIqlygYGicMmPwCbvrUYUdR0LXuOCQqcxj4ibN6A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMGvy6YVHO5LTicXicex7jEXZmXbvdfVX0HicRf7NpY0L6hicuibCJ1bUlpnQ/640?wx_fmt=png&from=appmsg)

即可得到twofish的key。

根据代码可知有两段data[16]，我们可以对v2[15]下断点得到所有的data。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMrNAbNgz1slYntQr275V5jDtBTbUrBdiaibd0sbT0h3PyX3ArRXicDGGxw/640?wx_fmt=png&from=appmsg)

```
import twofish

key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")  # key
tf = twofish.Twofish(key)
data1 = bytes([159, 46, 128, 211, 56, 34, 22, 223, 236, 150, 252, 143, 26, 34, 136, 115])
decrypted1 = tf.decrypt(data1)
print(decrypted1)
#flag{iT3N0t7H@tH
```

即可得到前半段flag，我们将前半部分flag输入进去再进行check即可得到part2的check。

> **Come on you are about to get it>flag{iT3N0t7H@tH111111111111111}**

之后有对我们传入的测试值的flag的part2的异或数据提取出来（这第二段算法是rc4，直接将加密后的值异或回去即可得到）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMDxS7YNibIFyggb1xnOrE7McqJg2oluiaZXcjqaQDWyQAVKjTPicRsINog/640?wx_fmt=png&from=appmsg)

将这段数据异或我们的输入再异或data2[16]即可还原得到第二段flag。

```
data2 = [169, 217, 118, 189, 119, 187, 86, 154, 49, 179, 222, 168, 101, 142, 26, 50]
enc1 = bytes([0xD8, 0xAD, 0x71, 0xC8, 0x76, 0xD3, 0x28, 0xFD, 0x37, 0xEA, 0xA6, 0xF7, 0x3F, 0xEC, 0x1B, 0x32])
enc2 = b'111111111111111}'
dec2 = ''.join(chr(data2[i] ^ enc1[i] ^ enc2[i]) for i in range(len(data2)))
print(dec2)
#@E6D0YOV7hInkS0}
```

这wp应该是出题人的预期解，本人走了许多弯路最终写出这份wp供大家学习。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fu2sqFLykClOFThxX08GpM8L1WksVFEc05avNFhAFDBFWolicxwEQicuccRZ2hGUnv9OZMAA8lUodQ/640?wx_fmt=png&from=appmsg)

看雪ID：Aar0n

*https://bbs.kanxue.com/user-home-985355.htm*

\*本文为看雪论坛优秀文章，由 Aar0n 原创，转载请注明来自看雪社区

# 往期推荐

1、[PWN入门-SROP拜师](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579476&idx=2&sn=4f9adc1e7d61c7357bdc85ba654f24cb&chksm=b18dc29e86fa4b88c483a581131de043b076918cd7c7436a82e9bb56bc37c8f1edf6c87d8350&scene=21#wechat_redirect)

2、[一种apc注入型的Gamarue病毒的变种](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579387&idx=1&sn=9d6fbf25f11b3d99c92c5ac8de0587d5&chksm=b18dc13186fa4827ae7a7bf909e0d2b9490c6df4417c1d7eebc27127133daa9771c212b4f310&scene=21#wechat_redirect)

3、[野蛮fuzz：提升性能](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579145&idx=1&sn=9134327916f678cfe7e2bc3371cedeaf&chksm=b18dc04386fa49557abc8c7e6ce3410dd4042ed88635c48961fda72b7fa4425698e56bb86ff6&scene=21#wechat_redirect)

4、[关于安卓注入几种方式的讨论，开源注入模块实现](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579138&idx=1&sn=fef09513ae9f594e68a503f69a312f4f&chksm=b18dc04886fa495e440990cd2dbddb24693452562e53bd8cb565063ddee921b7e288477f4eea&scene=21#wechat_redirect)

5、[2024年KCTF水泊梁山-反混淆](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579017&idx=2&sn=a97dacde8a6c913108999da8a96a667f&chksm=b18dc0c386fa49d57ce9f0ce6923690d6eb8efb3ccb8032e8c6b923184af3dd29b1b4471f9a2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMm9tEFGeP6tm5o39yicNpicmefTztxw1cjUvWZKsp16uXh9JKT11Hbz5A/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMm9tEFGeP6tm5o39yicNpicmefTztxw1cjUvWZKsp16uXh9JKT11Hbz5A/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMm9tEFGeP6tm5o39yicNpicmefTztxw1cjUvWZKsp16uXh9JKT11Hbz5A/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fu2sqFLykClOFThxX08GpMRJPrjOnHKGTE02odbliaVPllS4n6KS8e4k37YkRoUBr3ic3gqEy11A9w/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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