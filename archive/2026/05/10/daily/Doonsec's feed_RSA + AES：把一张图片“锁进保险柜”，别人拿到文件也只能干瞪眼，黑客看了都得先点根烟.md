---
title: RSA + AES：把一张图片“锁进保险柜”，别人拿到文件也只能干瞪眼，黑客看了都得先点根烟
url: https://mp.weixin.qq.com/s/BG8Q7nhxxvfRoq21jv08ew
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:54:02.936267
---

# RSA + AES：把一张图片“锁进保险柜”，别人拿到文件也只能干瞪眼，黑客看了都得先点根烟

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtibzcRx8GjWPejSa5Iux2ruCPR0MfrY1SwN2WzuIk8WbHLibIuv5eygUQria1SRnhag7wibhE3hYsTRI5ichlubG3ALSu2DMpxau2rOQl6eLc9o/0?wx_fmt=jpeg)

# RSA + AES：把一张图片“锁进保险柜”，别人拿到文件也只能干瞪眼，黑客看了都得先点根烟

原创

W不懂安全
W不懂安全

W不懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

很多人以为：

> “我把图片改个后缀、压个包、加个密码，就安全了。”

实际上：

* 改后缀 = 小学生障眼法
* 普通压缩包密码 = 彩虹表狂喜
* 微信/QQ传输 = 自动压缩画质还可能改文件

真正靠谱的方案是：

# AES 负责“暴力加密”

# RSA 负责“安全传钥匙”

#

这就是很多军工、银行、密码软件常见的组合拳。

简单来说：

* AES：负责把图片加密成“宇宙乱码”
* RSA：负责保护 AES 密钥
* 最终效果：

+ 没私钥 = 根本解不开
+ 就算拿到文件也只能看到一坨二进制垃圾
+ 理论暴力破解时间：

> 比太阳寿命长
> 比宇宙热寂还抽象
> 黑客看了都得先点根烟

本期内容直接实战。

你将得到：

✅ 图片加密器                ✅ 图片解密器
✅ RSA 公私钥系统         ✅ AES-256 加密
✅ 可直接发给别人

一、先理解整体流程

整体结构图：

```
原图 ↓AES 加密图片 ↓生成 AES 随机密钥 ↓RSA 公钥加密 AES 密钥 ↓得到：    encrypted_image.bin    encrypted_key.bin
```

别人拿到：encrypted\_image.bin 和 encrypted\_key.bin 也没用。

因为没有 RSA 私钥，就等于无法解除 AES 密钥 、无法解密图片。

这就是 “双层保险”。

二、生成 RSA 公私密钥

安装 Python 环境，我使用的是Pycharm编译器来进行编码。

先安装依赖：

```
pip install pycryptodome
```

生成 RSA 公私钥：

新建 generate\_keys.py 文件，代码如下：

```
from Crypto.PublicKey import RSA
# 生成 4096 位 RSA 密钥key = RSA.generate(4096)
# 私钥private_key = key.export_key()
with open("private.pem", "wb") as f:    f.write(private_key)
# 公钥public_key = key.publickey().export_key()
with open("public.pem", "wb") as f:    f.write(public_key)
print("RSA 密钥生成完成")
```

之后运行：

```
python generate_keys.py
```

运行之后会在目录底下生成 private.pem 和 public.pem

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXIWVibBvM3Z0ZibEfwEA9rHYATSTteutBkVeArpkMGH7lktgyyK6Xw4yGIv2LoncrsGnRu34Em78Wpbs2icIEmVxtuJYrRJklRMU/640?wx_fmt=png&from=appmsg)

注意：

| 文件 | 用途 |
| --- | --- |
| public.pem | 给别人也没事 |
| private.pem | 打死别发出去 |

因为私钥 = 保险柜的钥匙

三、开始加密（核心部分）

新建：encrypt\_image.py ，将以下代码写入其中：

```
from Crypto.Cipher import AES, PKCS1_OAEPfrom Crypto.PublicKey import RSAfrom Crypto.Random import get_random_bytesimport os
# 读取图片with open("image.jpg", "rb") as f:    image_data = f.read()
# 生成 AES 密钥aes_key = get_random_bytes(32)  # AES-256
# AES 加密cipher_aes = AES.new(aes_key, AES.MODE_GCM)
ciphertext, tag = cipher_aes.encrypt_and_digest(image_data)
# 保存加密图片with open("encrypted_image.bin", "wb") as f:    f.write(cipher_aes.nonce)    f.write(tag)    f.write(ciphertext)
# 读取 RSA 公钥with open("public.pem", "rb") as f:    public_key = RSA.import_key(f.read())
# RSA 加密 AES 密钥cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_aes_key = cipher_rsa.encrypt(aes_key)
# 保存加密后的 AES 密钥with open("encrypted_key.bin", "wb") as f:    f.write(encrypted_aes_key)
print("图片加密完成")
```

之后准备一张图片，放在项目目录中，要与 py文件 同级。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVrfiaUmbbycRLBfm3x5JnxWvV96xL846aku7PkhFVTBdHUdcOw1csgvWMNpFgbA7GgFU9ibKP7TCrricUqL65m67YnzB95nVSI1Y/640?wx_fmt=png&from=appmsg)

之后运行：

```
python encrypt_image.py
```

生成：encrypted\_image.bin 和 encrypted\_key.bin

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjXkrgjtGU2PakPopZ3Wc4PD1UlBI1JAnt6235Re3O3wc7oicf2ASk8rzce80O50bnDF3kyXPLZj58ia5ibJrXEwrJYicIcjmCZgL8g/640?wx_fmt=png&from=appmsg)

现在你的原图可以删了，这样，如果没有私钥，没人能恢复图片。

那如何解密图片呢？

新建：decrypt\_image.py ，使用以下代码解密：

```
from Crypto.Cipher import AES, PKCS1_OAEPfrom Crypto.PublicKey import RSA
# 读取 RSA 私钥with open("private.pem", "rb") as f:    private_key = RSA.import_key(f.read())
# 读取加密 AES 密钥with open("encrypted_key.bin", "rb") as f:    encrypted_aes_key = f.read()
# RSA 解密 AES 密钥cipher_rsa = PKCS1_OAEP.new(private_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)
# 读取加密图片with open("encrypted_image.bin", "rb") as f:    nonce = f.read(16)    tag = f.read(16)    ciphertext = f.read()
# AES 解密cipher_aes = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
image_data = cipher_aes.decrypt_and_verify(ciphertext, tag)
# 恢复图片with open("decrypted.jpg", "wb") as f:    f.write(image_data)
print("图片解密完成")
```

之后会生成一个 decrypted.jpg 图片，就恢复成功了。

四、为什么这套方案很强？

1、AES-256 本身就极难破解

AES-256 密钥空间：2^256

什么意思？

假设：

* 全球所有超级计算机同时爆破
* 每秒尝试万亿次
* 从宇宙大爆炸开始算

结果：还没试完

## 2、RSA 4096 位非常硬

4096 位 RSA：

* 普通人根本没算力碰瓷
* 暴力分解成本极其离谱
* 破解难度属于：

  > “国家级预算都得认真考虑电费”

3、AES + RSA 是行业经典组合

很多：

* 文件保险箱
* 安全聊天
* V\*N
* 银行系统

本质都是：RSA 传钥匙，AES 干重活

因为 RAS 不适合加密大文件，AES 才适合。

五、真正专业的人还会做什么？

这里才开始进阶玩法：

1、删除原图痕迹

仅仅删除原图是没有意义的，因为数据可能还在磁盘。

可以用：

```
sdelete    或者    shred
```

彻底覆盖。

2、给文件伪装

比如：encrypted\_image.bin

改成：

```
system.logcache.tmpvideo.dat
```

别人以为这是垃圾缓存，实际上里面锁着图片。经典的行为艺术。

3、分离传输

不要把 图片 和 密钥 一起发

正确做法是：

```
A渠道发图片B渠道发密钥
```

比如：

* 通讯软件发图片
* 邮件发密钥

这样更安全。

4、私钥离线保存

真正专业的玩法：私钥永远不联网。

放到：U盘、加密硬盘、离线设备......

因为私钥一泄露，一切都白给。

六、还能继续升级吗？

答案是：当然！！！

## 方案升级 1：密码二次加密私钥

即使别人偷到：private.pem 也打不开。

方案升级 2：图片切片

把1张图拆成  20个碎片，缺一不无法恢复。

方案升级 3：隐写术

把加密文件藏进：

* 视频
* 音频
* PNG
* GIF

别人根本不知道里面有东西。

属于：

# “你以为你看到的是猫片”

# “其实里面是机密”

七、最后重点（必须看）

如果你真想做到：

# “别人绝对打不开”

那核心不是 算法

而是：

# 私钥管理

因为：

* AES 很强
* RSA 很强

但你把私钥发别人了

那就像，给保险柜上了核弹级锁，然后把钥匙贴门上

直接喜剧。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_05.png)

本期内容到此结束。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXibu188DgR2icXAYBQtNf01bhpxic7jqf6urQPOCpmib4T38DSJQ1bdm1hkrqeCwSNPWCjicD9GAj5icWHicBWTI9sHU19kFibKaVtJ50/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

W不懂安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

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