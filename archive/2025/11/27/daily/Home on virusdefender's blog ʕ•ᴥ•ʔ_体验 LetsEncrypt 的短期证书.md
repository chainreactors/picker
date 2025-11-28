---
title: 体验 LetsEncrypt 的短期证书
url: https://strcpy.me/index.php/archives/806/
source: Home on virusdefender's blog ʕ•ᴥ•ʔ
date: 2025-11-27
fetch_date: 2025-11-28T03:12:34.240928
---

# 体验 LetsEncrypt 的短期证书

[## virusdefender's blog ʕ•ᴥ•ʔ](/)[Home](/)
[Blog](/blog/)
[About](/about/)

# 体验 LetsEncrypt 的短期证书

*2025-11-27*

在今年 2 月份的时候，LetsEncrypt 就发布了[一篇文章](https://letsencrypt.org/2025/01/16/6-day-and-ip-certs)称要推出六天的短期证书，而目前 LetsEncrypt 的默认证书还是 90 天的。

为何要使用有效期更短的证书呢，这个主要有两个重要的原因：

## 证书吊销机制不可靠

证书吊销一直是依赖 OCSP 或 CRL 机制，但是都需要是客户端主动的去检查，否则对证书有效性没有任何的影响。

### CRL（证书吊销列表）

CA 定期生成一个签名的列表，其中包含所有已被吊销但尚未过期的证书序列号。客户端在验证证书时，会下载这个列表，并检查目标证书的序列号是否在其中。
如果在，则说明该证书已被吊销，不应信任。

缺点包括

* 体积大：随着吊销证书增多，CRL 文件会变得很大，影响性能。
* 存在时效性问题：两次更新之间的窗口期内吊销的证书无法被及时发现。

### OCSP（在线证书状态协议）

客户端向 CA 指定的 OCSP 响应服务器发送一个查询请求，包含目标证书的序列号等信息，OCSP 服务器实时返回该证书的状态。

缺点包括

* 每次查询都会暴露用户正在访问哪个网站
* 依赖网络和服务器可用性：如果 OCSP 服务器宕机或响应慢，可能导致连接延迟甚至失败。某些客户端可能会忽略 OCSP 错误继续连接。

其改进版为 OCSP Stapling，即服务器主动从 CA 获取 OCSP 响应，并在 TLS 握手时一并发送给客户端。避免了客户端直接连接 OCSP 服务器，提升性能和隐私。

短期证书的主要优势在于，它们能显著缩短潜在的风险暴露时间，因为这类证书会相对较快地过期。这降低了对证书吊销机制的依赖。因为上述吊销机制一直不够可靠，所以短期证书将不包含 CRL 或者 OCSP 的配置信息。

此外，短期证书实际上要求必须实现自动化管理，实现证书签发的自动化也对于安全性至关重要。

## 支持 IP 证书

虽然说 IP 和域名的 SSL 的验证和签发本质都是一样的，但是过去只有少数几家 CA 小规模提供此类服务。

IP 证书很少见最重要的原因是 IP 地址的所有权的变动比域名频繁多了，比如你在某个云厂商创建了一个新的虚拟机，分配了一个 IP 地址，在释放虚拟机的时候，如果你同时选择了释放 IP 的话，这个 IP 可能随时就被其他人所占用。这时候已经签发的长期有效的 IP 地址的证书可能就存在安全隐患了，而使用短期证书即可以匹配 IP 生命周期也可能比较短的场景。

另外大多数互联网服务运营商并不期望终端用户会直接通过 IP 地址访问他们的网站。在某些情况下，当多个网站或设备共享同一个 IP 地址时，仅靠 IP 地址甚至无法正常建立连接。因此，为这样的 IP 地址申请证书几乎没有实际意义。

## 申请短期证书

前不久，LetsEncrypt 宣布短期证书和 IP 证书即将生产环境可用，同时开放了测试申请，于是我将本站的证书也替换为了短期证书，通过 GitHub Actions 脚本自动申请和部署。

根据 [LetsEncrypt Profiles](https://letsencrypt.org/docs/profiles/) 的文档，只要在相关的 ACME 工具中添加类似 `profile=shortlived` 的参数即可，比如 `acme.sh` 工具的命令行大概就是

```
1acme.sh --issue --dns dns_ali \
2    -d strcpy.me -d '*.strcpy.me' \
3    --server letsencrypt --certificate-profile shortlived
```

部署 SSL 证书之后通过 openssl 查看

```
1openssl s_client -showcerts -servername strcpy.me -connect strcpy.me:443 2>/dev/null | \
2    openssl x509 -inform pem -noout -text
```

```
 1Certificate:
 2    Data:
 3        Version: 3 (0x2)
 4        Serial Number:
 5            06:ed:2f:d5:60:37:ff:b9:34:f9:48:c1:1e:38:d2:89:9a:1d
 6        Signature Algorithm: ecdsa-with-SHA384
 7        Issuer: C=US, O=Let's Encrypt, CN=E8
 8        Validity
 9            Not Before: Nov 27 01:06:01 2025 GMT
10            Not After : Dec  3 17:06:00 2025 GMT
```

可以看到本站的证书是 11 月 27 日申请的，有效期至 12 月 3 日，也就是六天。

---

[#安全](https://strcpy.me/tags/%E5%AE%89%E5%85%A8/)
|
微信打赏 |
转载必须注明原文链接

![](/assets/blog/images/utils/wx_pay_2024.jpg)

## 欢迎评论

昵称

邮箱

评论内容

提交

ᕦʕ •ᴥ•ʔᕤ

提交中...

Made with [Hugo ʕ•ᴥ•ʔ Bear](https://github.com/janraasch/hugo-bearblog/)