---
title: Ciphey：AI 驱动的自动解密/解码工具，Rust重构版
url: https://mp.weixin.qq.com/s/2bA9gOWD75AzCVcRuLpu7Q
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:44:51.820359
---

# Ciphey：AI 驱动的自动解密/解码工具，Rust重构版

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfM032vxPR1Sv3HNL0puA199YPr1XLbXBq9R8vMvPVkEx07l0QKyk6jAV0Kz3kCqfNkvqWnguianOian64T7N57td5o5wN305MF7g/0?wx_fmt=jpeg)

# Ciphey：AI 驱动的自动解密/解码工具，Rust重构版

仙草里没有草噜丶
仙草里没有草噜丶

泷羽Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 项目概览

Ciphey是一个由人工智能所驱动的全自动的解密解码的工具。它可以自动地进行识别并且解码几十种常见的编码以及简单的加密方式，不用你去手动地去猜测到底是什么编码。当你在CTF活动当中、处理可疑数据的时候碰到看不懂的字符串，把那个字符串交予Ciphey就好。

## 核心功能

![img](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfMW0yfdzRNkjKFbBnWNXRKgcwfjJ40maoVPRHALOsIt9rtlgyWZBlbicrLuJeE1iaDsIb0M7UdNAG3KBhAGZ6U4ibuMiaaYRRLHslc/640?wx_fmt=other&from=appmsg)

img

### 自动编码识别

支持着好几种不同的编码的方式。例如像Base64、Base32、Hex、URL编码、摩尔斯电码、凯撒密码、XOR、ROT13、Vigenere、Atbash、Braille盲文等等。你不用去操心具体用了哪一种编码，Ciphey会自己去进行尝试，一直到把明文给解密出来。

![image-20260715192123519](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOwBltHklibl5Jfnb7AUmDeBicge9OjsCq1ia5pLrQKxTOibHq4R2xVSm7LykiaSbHXa2myEia3MjWCYcuSBcaNtmjMwPXMsldxOV4Aw/640?wx_fmt=other&from=appmsg)

image-20260715192123519

### 高速解密

新版经过用Rust进行重写之后，速度就提升了足足有700%。新版相较于旧版的Python版本来讲，要快上7倍。新版具备原生的多线程支持，就算是面对多层嵌套编码这样的情况，也能够快速地去进行处理。

### 多级嵌套解码

Ciphey可以对多层嵌套的编码进行解密操作。例如像`Rot13 -> Base64 -> Rot13`这种一层一层嵌套起来的编码状况，Ciphey会一层接着一层地自动将其解开，一直到获取到明文为止。

### BERT增强明文检测

可以采用BERT模型去进行明文检测。如此操作能够使得准确率大概提升大约40%。同时还可以减少误报以及漏报的状况。而且支持配置不同敏感度的级别，从而用来适应不同种类的编码。

![image-20260715192158766](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfOOSwQZraoriceIKnwt91J9h5YFHDs5yTFXHAeGCNOZfoJbibgib5K2LmP7OHTo8KF5GHm3J2SYPt6yOEPbfA0GtXrZQut5bBcSA4/640?wx_fmt=other&from=appmsg)

image-20260715192158766

### LemmeKnow集成

里头存在着LemmeKnow，这可是PyWhat的Rust版本。它能够进行识别像IP地址、API密钥、邮箱地址、手机号码、加密货币地址这类个东西。并且它识别数据类型的速度是Python版本的33倍。

## 安装使用

### 方式一：Cargo安装（推荐）

```
cargo install ciphey
ciphey "SGVsbG8gV29ybGQh"
```

### 方式二：Docker运行

```
git clone https://github.com/Ciphey/Ciphey
cd Ciphey
docker build . -t ciphey
docker run -it ciphey
```

### 方式三：Discord机器人

要是你想要加入官方的Discord服务器，那么你就接着前往#bots那个频道之中，使用`$ciphey`这个命令来进行相关的操作事宜。

## 基础用法

简单的用法，传密文：

```
ciphey "加密后的字符串"
```

默认的超时时间设定为五秒，倘若出现了超时的情况，那么就会自动地进行停止操作，并且它还可以对于自定义的主题以及配置文件开展相关的操作。

```
# 启用BERT增强检测（首次会下载500MB模型）
ciphey --enable-enhanced-detection "密文"

# 帮助信息
ciphey --help
```

## 实际使用场景

1. **CTF比赛**：遇到Misc、Crypto题的编码题扔进去，省得一个个试
2. **日志分析**：看到可疑编码字符串不用手动查是什么编码
3. **数据处理**：批量处理URL编码、Base64编码的数据
4. **安全分析**：分析恶意样本中的编码字符串

## 优缺点

| 优点 | 缺点 |
| --- | --- |
| 全自动识别，不用手动猜编码 | 复杂现代加密无法解密（只支持编码和古典加密） |
| 速度极快，Rust版本性能优异 | 部分冷门编码可能识别失败 |
| 支持多层嵌套解码 | BERT模型较大，首次下载需要时间 |
| 支持多种输出格式，可作为库集成 |  |

## 法律与合规说明

Ciphey是一款开源的工具，他的范畴归属于安全相关领域。它仅仅会被运用到合法的安全研究、CTF学习以及经过授权的测试这类情形当中。可绝对不可以将它运用到非法的用途之上。

**项目地址**：https://github.com/Ciphey/Ciphey

**适用场景**：CTF比赛、编码识别、密文解密、日常数据处理

## 服务器推荐

阿里云九折优惠：

```
https://link.aitq.net/RcgjvF
```

腾讯云新用户专享：

```
https://link.aitq.net/mVGWtG
```

薄荷云实惠海外服务器：

```
https://link.aitq.net/RYbx8O
```

## 往期推荐

[2026 国内香港CN2低价云服务器推荐](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247510805&idx=1&sn=bc45a7094cbc1c4ee6552a4f1c350266&scene=21#wechat_redirect)

[AI中转站搭建教程，快快收藏](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247513128&idx=1&sn=3ed51ed3db822b31b3a4bc34114139bc&scene=21#wechat_redirect)

[这不辱？白嫖大厂1.5亿 Token，附使用方法](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247513099&idx=1&sn=61d87807da319a0f07bec5db71594609&scene=21#wechat_redirect)

[红日靶场官网挂了，备用网盘分享](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247513149&idx=2&sn=fec6d4b5ca9a90720cb189ee8037e2e7&scene=21#wechat_redirect)

[在云服务器、vps中安装kali，2026最新教程](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247511600&idx=1&sn=bc869fd3f883384d3d7bed204fb81961&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5975bXHXfWG2YeKibdOsJywysp4aTnLsvRodjpEhfhbPXvica7364Dn6VO7Ybtpma6IUaFciaiaZG8Sr9yJ2Dwuv1Q/0?wx_fmt=png)

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