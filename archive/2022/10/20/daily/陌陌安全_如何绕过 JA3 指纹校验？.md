---
title: 如何绕过 JA3 指纹校验？
url: https://mp.weixin.qq.com/s?__biz=MzI2OTYzOTQzNw==&mid=2247487466&idx=1&sn=d6b70bb0b5d5550474acca57f15ebebf&chksm=eadc0588ddab8c9e954645ade42e024e6568747d00658e4fb2ebf4f7425449cb731002a7b97c&scene=58&subscene=0#rd
source: 陌陌安全
date: 2022-10-20
fetch_date: 2025-10-03T20:23:46.321584
---

# 如何绕过 JA3 指纹校验？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1YLJUhm0ZtnPperKia6QSGWzgevWj2t1yKnkLJBdibHt5ia6h4v0KDS3XKKVkeRTibyyYtpUwfXYa6iaCP9ONAhJTBA/0?wx_fmt=jpeg)

# 如何绕过 JA3 指纹校验？

原创

陌陌安全

陌陌安全

![](https://mmbiz.qpic.cn/mmbiz_gif/1YLJUhm0ZtkFbEJYLKgt0HcHIVD6kkKAMKjwRwlPMXYwIqF0bzFkgicZtZ81ezQXDhSXticiaIqQh0xblxy4uNM8w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

# 之前看过某些文章，很好地论证了 JA3 指纹不能作为设备指纹的特征。也让我对 JA3 指纹的具体的细节和在其他方面的应用产生了兴趣，这里我们站在攻击者的视角，以代码的角度记录下 JA3 的计算和生成自定义 JA3 指纹。

## **关于 JA3 指纹生成**

JA3 的出现由 John B. Althouse、Jeff Atkinson、Josh Atkins 三个人共同在 2017 年提出（三个人的姓名首字母都为 JA，合称即为 JA3），而 JA3 指纹的生成，则要从 TLS 建立握手开始说起。TLS 在建立握手时，以客户端发起 ClientHello 开始，告诉服务器建立一个 TLS 链接，在 RFC5246 的 7.4.4.1 章节中定义的 TLS 1.2 的 ClientHello 数据结构如下：

```
struct {
    ProtocolVersion client_version;
    Random random;
    SessionID session_id;
    CipherSuite cipher_suites<2..2^16-2>;
    CompressionMethod compression_methods<1..2^8-1>;
    select (extensions_present) {
        case false:
            struct {};
        case true:
            Extension extensions<0..2^16-1>;
    };
} ClientHello;
```

* client\_version 为本次会话中的 TLS 版本
* random 为 client 产生的随机数结构体，主要用来避免重放攻击
* session\_id 本次连接中所使用的会话 ID，这个字段主要用在会话恢复中
* cipher\_suites 为所支持的密码套件列表，具体值可以通过 openssl 查看列表

```
$ openssl ciphers -V | column -t -s " "
0x13,0x02  -  TLS_AES_256_GCM_SHA384         TLSv1.3  Kx=any       Au=any    Enc=AESGCM(256)             Mac=AEAD
0x13,0x03  -  TLS_CHACHA20_POLY1305_SHA256   TLSv1.3  Kx=any       Au=any    Enc=CHACHA20/POLY1305(256)  Mac=AEAD
0x13,0x01  -  TLS_AES_128_GCM_SHA256         TLSv1.3  Kx=any       Au=any    Enc=AESGCM(128)             Mac=AEAD
0xC0,0x2C  -  ECDHE-ECDSA-AES256-GCM-SHA384  TLSv1.2  Kx=ECDH      Au=ECDSA  Enc=AESGCM(256)             Mac=AEAD
0xC0,0x30  -  ECDHE-RSA-AES256-GCM-SHA384    TLSv1.2  Kx=ECDH      Au=RSA    Enc=AESGCM(256)             Mac=AEAD
0x00,0x9F  -  DHE-RSA-AES256-GCM-SHA384      TLSv1.2  Kx=DH        Au=RSA    Enc=AESGCM(256)             Mac=AEAD
0xCC,0xA9  -  ECDHE-ECDSA-CHACHA20-POLY1305  TLSv1.2  Kx=ECDH      Au=ECDSA  Enc=CHACHA20/POLY1305(256)  Mac=AEAD
0xCC,0xA8  -  ECDHE-RSA-CHACHA20-POLY1305    TLSv1.2  Kx=ECDH      Au=RSA    Enc=CHACHA20/POLY1305(256)  Mac=AEAD
……
```

* compression\_methods 为 client 所支持的压缩算法列表
* extensions 为 TLS 扩展，用于告知服务端一些额外信息。如 SNI (Server Name Indication) 扩展包含了所要链接的明文域名信息、supported curves 扩展为支持的椭圆曲线，supported point formats 扩展为支持的曲线格式

JA3 指纹的生成就是基于 ClientHello 数据包中五个字段，`client_version`、`cipher_suites`、`extensions`和椭圆曲线supported curves与椭圆曲线格式 supported point formats，将这些值串联在一起，然后使用 , 分隔这 5 个字段，使用 - 分隔字段中的值。最终得到了 JA3 完整字符，再经过 md5 就是指纹。

使用 cURL 请求 www.immomo.com

```
$ curl https://www.immomo.com/
```

Wireshark 过滤出 cURL 建立链接的 ClientHello 包，图中的 1-5 便是所需的 5 个字段。（Wireshark 在3.6.x 版本 添加了 JA3 plugin，使用之后版本的 Wireshark 就可以在抓包时可直接获取到 JA3 相关指纹信息）

![](https://mmbiz.qpic.cn/mmbiz_png/1YLJUhm0ZtnPperKia6QSGWzgevWj2t1y269NcEz6MaVrEWWPkpWicW27kNbz1Iq6ax54nxiaRQicB5MI0UqELCx6A/640?wx_fmt=png)

cURL 产生的 JA3 Hash Origin 为 771,4866-4867-4865-49196-49200-159-52393-52392-52394-49195-49199-158-49188-49192-107-49187-49191-103-49162-49172-57-49161-49171-51-157-156-61-60-53-47-255,0-11-10-13172-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2，MD5 后值 `f436b9416f37d134cadd04886327d3e8` 即为 JA3 Hash

使用同样的方法分别使用 Chrome、和不同操作系统下 Golang 原生 HTTP Client 向发送请求，观察对应的 JA3 原始字符和 Hash

```
func main() {
	_, err := http.DefaultClient.Get("https://immomo.com/")
	if err != nil {
		panic(err)
	}
}
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/1YLJUhm0ZtnPperKia6QSGWzgevWj2t1ykIkHTwB868zoAzne4XrhhibUAR6zibKV9KGb4o7OyWVePr34xG7km84g/640?wx_fmt=jpeg)

可以看到，Chrome 和 Chromium 的 JA3 Hash Origin 只有一个字符的微小差异，而使用 Go 发送 HTTP 请求时，哪怕是不同 Go 版本在不同操作系统上的 JA3 Hash 是完全相同的。基于此特性，TLS 指纹也就有了不同的应用。

## **TLS 指纹的应用**

### **反爬虫**

既然同一版本的库发起 TLS 连接的指纹是相同的，那么可以通过建立正常浏览器指纹和不同编程语言指纹库，就可以区分开 BOT 和正常用户，CluoudFare 和 Akamai 就是这么做的，JA3 指纹作为了识别爬虫的一个重要指标

![](https://mmbiz.qpic.cn/mmbiz_jpg/1YLJUhm0ZtnPperKia6QSGWzgevWj2t1ytkb6jKjHhtokFKAiaMxZFXiaeZIu0ibGnFHnVXCOWZXIuglkK87zJ3B2A/640?wx_fmt=jpeg)

**流量检测**

#### **C2 恶意流量检测**

360Quake 和 360netlab 利用 TLS 指纹来追踪僵尸网络和识别互联网上的 C2 服务

#### **Vmess 流量识别**

2020 年，有安全研究员提出 v2ray 服务的 TLS 指纹可被精准识别

### **空间测绘**

网络空间引擎如 Shadon、ZoomEye 也添加了对 SSL 指纹搜索的支持

## **指纹计算和修改**

### **计算 JA3 指纹**

为了能为不同的 TLS 链接生成不同的指纹，我们先自己实现下指纹计算，Wireshark 保存刚刚访问immomo.com的数据包为immomo.pcap，使用 gopacket 解析 PCAP 并设置过滤条件拿到 ClientHello 数据包。再计算出 JA3Hash

![](https://mmbiz.qpic.cn/mmbiz_jpg/1YLJUhm0ZtnPperKia6QSGWzgevWj2t1yZs3YnGdicEiaH4KJtq56z0sicjFygBeZ4CfSV9k1DNy2Kk7KHlXRUzfnA/640?wx_fmt=jpeg)

计算 JA3Hash 过程

![](https://mmbiz.qpic.cn/mmbiz_jpg/1YLJUhm0ZtnPperKia6QSGWzgevWj2t1yBs4bYDE13TiajDGKAykzA3yUvKTtcFsLZAlNGVuiayJd7pRLc7880gEQ/640?wx_fmt=jpeg)

最终结果与 Wireshark 抓包得到的一致

![](https://mmbiz.qpic.cn/mmbiz_jpg/1YLJUhm0ZtnPperKia6QSGWzgevWj2t1yE2Qa9yT0sJbOIGA2H4KW3SkLeZZaBDuf3G4JNoIx7fGwc7IEYmhwKA/640?wx_fmt=jpeg)

**生成可变的 TLS 指纹**

JA3 指纹是通过 ClientHello 中的值计算得到的，是不是通过是修改 ClientHello 中的值就能让指纹变成我们想要的值。

在 Go 发送 HTTP 请求时，会通过 net/http.Transport 处理 HTTP/HTTPS 协议的底层实现细节，其中会包含连接重用、构建请求以及发送请求等功能，对 TLS 相关处理主要为下面三个参数

```
type Transport struct {
// ...
	DialTLSContext func(ctx context.Context, network, addr string) (net.Conn, error)

	DialTLS func(network, addr string) (net.Conn, error)

	TLSClientConfig *tls.Config
// ...
}
```

refraction-networking/utls 是对 Golang TLS 库的的 fork 和重写，其中封装了 clienthello 结构体可以让用户自定义 TLS 链接时的底层数据。以 Chrome 83 版本为例，其 ClientHello 完整结构如下，红色方框即为计算 JA3 指纹所需要的数据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/1YLJUhm0ZtnPperKia6QSGWzgevWj2t1yODYZFSibfT7mk5JoITczRwYN4FV91SFLsMPdjfzMUZiatEGGc0EHziciag/640?wx_fmt=jpeg)

使用 utls 的 DialTLS 替换原始 transport，再发送请求到 www.immomo.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/1YLJUhm0ZtnPperKia6QSGWzgevWj2t1yrUD5iaMJP5ScarzZxfDXbhAEYrYOXNGHUHbS1RaRQoSdL1KicfRyHjeQ/640?wx_fmt=jpeg)

发现 JA3 的值已经变为 83 版本 Chrome 的 JA3 值，再修改 UA 为 Chrome，就能绕过常见 TLS 指纹校验了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/1YLJUhm0ZtnPperKia6QSGWzgevWj2t1ykaf11qh4hmZnKXewsCmMVgoHFLwd1Gl7sQqB9nHoUIYvJ7Bq0ofm0Q/640?wx_fmt=jpeg)

**小节**

这篇主要以代码的角度记录了下 JA3 指纹的生成和修改，可以在遇到反爬或需要藏匿流量场景时通过修改 tranport 的 TLS 配置来隐匿自己。

---

*About us*

**![](https://mmbiz.qpic.cn/mmbiz_gif/ibch48nP81TBVLhCcj3J3EXPic4CRY3X2cAiaSItIGGticFPsrR31JWs25wBqNJDuFlH6kekSGAiaxjliayum08Bia6bw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)**

**陌陌安全**

致力于以务实的工作保障陌陌旗下所有产品及亿万用户的信息安全

以开放的心态拥抱信息安全机构、团队与个人之间的共赢协作

以自由的氛围和丰富的资源支撑优秀同学的个人发展与职业成长

**/   往 期 分 享   /**

[![](https://mmbiz.qpic.cn/mmbiz_png/1YLJUhm0Ztn1L6wpcFOt1R4az6tUSicibBSUUOVglChQcibeHcUmBjsl094GyjiaAXKibIB7rqct9mQ5S1X540afxtA/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MzI2OTYzOTQzNw==&mid=2247486510&idx=1&sn=4eaac2ae2f78b04b779e7c4b94d0faec&chksm=eadc064cddab8f5ae1dfae631e6a0085a9fd44d6691e7e25854487800210874ce6843f904e4b&scene=21#wechat_redirect)

App合规实践3000问

[![](https://mmbiz.qpic.cn/mmbiz_png/1YLJUhm0Ztky4RTCZHWC0SoKJGuia0e3CWhEv0a2eT34Lp2VvMHFRVE9wic9XwYfx7S7xu1ElFiaFZ7CjWI78wbRA/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MzI2OTYzOTQzNw==&mid=2247486920&idx=1&sn=c135f85777cebd1d752fbe968e77f58f&chksm=eadc07aaddab8ebcd8cfd76509ef736b0ff043b54522f928e5301287f0313ba5c69c9b53dfee&scene=21#wechat_redirect)

App合规实践3000问之二

[![](https://mmbiz.qpic.cn/mmbiz_png/1YLJUhm0Ztn1L6wpcFOt1R4az6tUSicibBssXQSJ6jveZVIVChostfO9gzQqN5MRtlJuqupo8E35iaB5Ojvh9aAIg/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MzI2OTYzOTQzNw==&mid=2247487349&idx=1&sn=caa734fc516b07b0f27c14c8c4918fee&chksm=eadc0517ddab8c0166898ce6f26fae38d64b2862a8e5c5ed3c5e32a1fed3aff461768a101b2d&scene=21#wechat_redirect)

App合规实践3000问之三

![](https://mmbiz.qpic.cn/mmbiz_jpg/1YLJUhm0ZtkDDeHkeF8Fjz464ZHjAqr2cMkriaeWuAUvmFeln5363dEyXYThZ62JWS25vsIeraY3MiahmuaickmNg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

「陌陌安全」

扫上方二维码码关注我们，惊喜不断哦

**M   O   M   O   S   E   C   U   R   I   T   Y**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1YLJUhm0ZtlKwDGIsPegVTuyMVyYibO4uVMkKgr92KPVehbc87x9pYQH8GyZeYbsibvRnAJuJjaXWicMLR84zOtkw/0?wx_fmt=png)

陌陌安全

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
允许...