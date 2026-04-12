---
title: 信息安全-块对称加密
url: https://mp.weixin.qq.com/s/RL07C0KzdsXW6cj-VQ4M5g
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:43:36.930816
---

# 信息安全-块对称加密

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBMAJd1VLDScibP9d4uySpl8EeLiauVicJqJz5cA8nNIsyqBMSAhmceX45m3COesTGmnBiaeAyupS6p9FOVpsm0ia47ib4cUwqvvKcS0/0?wx_fmt=jpeg)

# 信息安全-块对称加密

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

**01**

**AES**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB7McnrpROLWZ9njLe9AHha3zib7XaqIkH03JrSbRianccYmM9dT3cnmCibWRgLBIpXMmqicqtIUXUFwFH9AaFPr4wlet5984PKTxI/640?wx_fmt=png&from=appmsg)

**ECB模式**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBwkePYs1ubLSt5mt9aGf9foEMcyF6RiaEicPWUibeBic4Y7ud3yQd0nmI0mTribaaiamvU4TO5mLjKZhXzB5lwZpWF8lGn1GsdYNxgQ/640?wx_fmt=png&from=appmsg)

**CBC模式**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDIan3ukRCjPnicUEJlibTTjdvrAPkfaQzXxCOmyKv9cyliakGwptKTOpz4L7Uz8xuKpiavJ9E7L6CfPLibb3xXUqULZfkjfcgkK32U/640?wx_fmt=png&from=appmsg)

1. 每次加密都会随机产生一个不同的比特序列来作为初始化向量；
2. 无法直接对中间的明文分组进行加密，如要生成密文3，必须要凑齐明文分组1、2、3，一旦加密时中间有一个比特缺失了，也会导致明文分组的长度发生变化，这样缺失比特的位置之后的密文分组也将全部无法解密了；
3. 解密过程中，只要密文分组的长度没有变化，中间有一个分组损坏了，解密时最多只有两个分组受到数据损坏的影响；

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDTLRFrheJLEZiczjZzxGbXV2NemtbVRgA4EFeDG5Ls6twiaS0nBvGauKSlmxrIu20dqjA6luC3mmjavWz3nCNj4LhZKvvpibQODk/640?wx_fmt=png&from=appmsg)

分组密码还有一种模式叫CTS模式（Cipher Text Stealing Mode），在分组密码中，当明文长度不能被分组长度整除时，最后一个分组就需要进行填充。CTS模式使用最后一个分组的前一个密文分组数据进行填充，根据最后一个分组的发送顺序不同，CTS模式有几种不同的变体，CBC-CS1、CBC-CS2、CBC-CS3；下图演示为CBC-CS3。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD1oMfDLiawUpgI1y2kqyrOYZyoiaJWUMrQh23VhGRX18jNjHBl2oKm82EgX5wesI8p2CiaVTYvLEQykvG1hOXOeYstnc7ufXdvfU/640?wx_fmt=png&from=appmsg)

**CFB模式**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDwcMCKibXHUY6H6ndx3mDQhaicqpicZY72ckHjxHtk64Vtpuj5zZtIqGjlAcScCwg0WQsAF9n1uFjx13vlzicuyibfCiacntibD7Jc5Q/640?wx_fmt=png&from=appmsg)

1. 明文分组没有通过密码算法直接进行加密。

**OFB模式**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDbaNrnAlRDUAy9sdbACf0GIPskoDfHVlRcDKCpxCjCibtGicWhB7PT7JtyZtbNSPtibz5sLys0cv96OXGTIKtIIyiaaD9ZjsfcVEE/640?wx_fmt=png&from=appmsg)

1. 密钥流是可以提前生成的，相对于CFB每次需要将密文分组作为下一个加密的输入，OFB模式更加快速，只要保证初始化向量一样，也不存在CFB的重放攻击问题；
2. 如果对密钥流的一个分组进行加密后期结果恰巧和加密前是相同的，那么这一分组之后的密钥流就会变成同一值的不断反复；

**CTR模式**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBZxn3F32HSVPV8iaVMcbWMZNuIszgQHsolcWhr4eiayRnyX411u4aWqXI1eORJMaPe3t1qUut2KpwcusGIKfmBmqR3wJPVicpEJQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAEjvvKYic4cIMqtDSLfVLSib28EXoK9nyOXhhuukicpKzqJLEplUMlFJoClwV5tU8JiaOpreriae9pbC1IpldbQF6DyCcSzaSiaD3F0/640?wx_fmt=png&from=appmsg)

1. 加密和解密使用了完全相同的结构，在程序实现上比较容易；
2. 可以以任意顺序对分组进行加密和解密，因此在加密和解密时需要用到的计数器的值可以由nonce和分组序号直接计算出来，即可以并行计算。
3. 每次加密时都会生成一个不同的nonce值作为计数器的初始值，当分组长度为128bit时，计数器的初始值可能是像下面这样的形式：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDq2KJloSNs8PL8w1ZEYVV16Ve2Wym4ujuVhicnpEOiaaF2p8Iv2WY3GAMc3DC9yjQ5mvrG4Cj9qTsH4l7GJw0WHzic1Pr8lrazos/640?wx_fmt=png&from=appmsg)

前8字节为nonce，每次加密时都不一样，后8字节为分组序号，这部分是累加的。

GCM模式（基于CTR）和CCM（CBC Counter Mode）

在CTR模式生成密文的同时生成用于认证的信息。GCM的缺点在于计算量大，导致性能和电量开销比较大，因此使用GCM最好使用硬件支持，基于硬件的GCM，性能还是明显优于chacha20。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAfEtqFUuAktCRCIqsEHl3zwusndEvuzGDic8h6UhVMOdGIMuuUVVcOLDX22FQe06HO1dvkbibPIWyPK6U8C4KyX21ib6LFnTc4Bw/640?wx_fmt=png&from=appmsg)

以默认的ECB模式为例：

AES/ECB为分组密码，分组密码也就是把明文分成一组一组的，每组长度相等，每次加密一组数据，直到加密完整个明文。在AES标准规范中，分组长度只能是128位，也就是说，每个分组为16个字节（每个字节8位）。密钥的长度可以使用128位、192位或256位。密钥的长度不同，推荐加密轮数也不同；AES的加密公式为C = E(K,P)，在加密函数E中，会执行一个轮函数，并且执行10次这个轮函数，每轮的轮密钥也不一样，这个轮函数的前9次执行的操作是一样的，只有第10次有所不同。也就是说，一个明文分组会被加密10轮

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAJk3yQ4JSlXAXQ8UK3fW2lGKMGQV23WH6wV7M0gBOjCj3XdQ1N6ib6bV4iaibfvO57V8gWKcMiah1qgHGDk88j4r5fW6IPLVvVH8U/640?wx_fmt=png&from=appmsg)

加密过程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaALlBBdmH5fOEia3RLATfAKEPkkOkS7d3GC7mc1hqNZcPCTNxHYzVkShpnhOYu9fkZdFh4p7BGniaoSE0genZZY5WhBwDg77jrvE/640?wx_fmt=png&from=appmsg)

**02**

**SM4**

SM4是中国无线局域网国家标准中使用的一种对称加密算法，128bit块加密；

1. SM4有一个s-box，而AES有两个s-box，一个用于加密，一个用于解密，但s-box的设计是相似的，均使用inversion-based mapping；
2. AES-128和SM4具有这些操作，常见的有XOR、S-box查找（AES128有160个，SM4有128）和循环移位。此外，与SM4相比，AES-128还具有modular multiplications；
3. SM4的加解密算法是一样的，但是AES128加解密算法是不一样的；

来源：CSDN@qq\_24925595

https://blog.csdn.net/qq\_24925595/article/details/104918589?spm=1001.2014.3001.5502

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦...