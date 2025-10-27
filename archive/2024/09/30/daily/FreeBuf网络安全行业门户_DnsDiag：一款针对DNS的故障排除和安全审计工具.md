---
title: DnsDiag：一款针对DNS的故障排除和安全审计工具
url: https://www.freebuf.com/sectool/412020.html
source: FreeBuf网络安全行业门户
date: 2024-09-30
fetch_date: 2025-10-06T18:24:50.375155
---

# DnsDiag：一款针对DNS的故障排除和安全审计工具

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

DnsDiag：一款针对DNS的故障排除和安全审计工具

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

DnsDiag：一款针对DNS的故障排除和安全审计工具

2024-09-29 14:13:33

所属地 广西

## 关于DnsDiag

DnsDiag是一款针对DNS的故障排除和安全审计工具，在该工具的帮助下，广大研究人员可以轻松检测DNS基础设施的安全性。

![](https://image.3001.net/images/20240929/1727590225_66f8ef51d9122ad58b75c.jpg!small)

你是否曾怀疑过你的 ISP 是否劫持了你的 DNS 流量？你是否曾观察到 DNS 响应有任何异常行为？你是否曾被重定向到错误的地址并怀疑你的 DNS 有问题？DnsDiag可以对你的 DNS 请求和响应执行基本审核，以确保你的 DNS 正常运行。

你可以使用DnsDiag测试任何给定 DNS 服务器对任意请求的响应时间dnsping。就像传统的 ping 实用程序一样，它为你提供了类似的 DNS 请求功能。你还可以跟踪 DNS 请求到达目的地的路径，以确保它没有被重定向或劫持。这可以通过比较发送到同一 DNS 服务器的不同 DNS 查询来实现dnstraceroute，并观察路径之间是否有任何差异。

DnsDiag的dnseval组件能够评估多个 DNS 解析器并为你的网络选择最佳 DNS 服务器。虽然强烈建议你使用自己的 DNS 解析器，并且不要信任任何第三方 DNS 服务器，但如果你需要为你的网络选择最佳 DNS 转发器，dnseval你可以从性能（延迟）和可靠性（丢失）的角度比较不同的 DNS 服务器。

## 工具要求

> dnspython>=2.6.1
>
> cymruwhois>=1.6
>
> httpx>=0.27.0
>
> cryptography>=42.0.7
>
> h2>=4.1.0

## 工具安装

由于该工具基于Python 3开发，因此我们首先需要在本地设备上安装并配置好最新版本的Python 3环境。

### 源码安装

接下来，广大研究人员可以直接使用下列命令将该项目源码克隆至本地：

```
git clone https://github.com/farrokhi/dnsdiag.git
```

然后切换到项目目录中，使用pip3命令和项目提供的requirements.txt安装该工具所需的其他依赖组件：

```
cd dnsdiag

pip3 install -r requirements.txt
```

除此之外，我们也可以使用pip命令直接安装DnsDiag：

```
pip3 install dnsdiag
```

### 发布版本安装

我们会不定期发布适用于 Windows、Mac OS X 和 Linux 的二进制软件包。你也可以从【[发布页面](https://github.com/farrokhi/dnsdiag/releases)】获取最新版本。

### Docker安装

如果你不想在本地机器上安装DnsDiag，你可以使用 Docker 镜像并在容器中运行程序。例如：

```
docker run --network host -it --rm farrokhi/dnsdiag dnsping.py
```

## 工具使用

### dnsping

DnsDiag的dnsping组件可以通过发送任意 DNS 查询指定次数来 ping DNS 解析器。使用--help可获取工具持的命令行选项。以下是一些有用的参数选项：

> --tcp、--tls和--doh可以选择使用的传输协议，默认为 UDP；
>
> --flags用于显示每个响应的响应标志（包括 EDNS ）；
>
> --dnssec可以请求 DNSSEC；
>
> --ede用于显示扩展 DNS 错误消息；
>
> --nsid用于显示名称服务器标识符 (NSID)；

除了 UDP，我们还可以分别使用 TCP、DoT（TLS 上的 DNS）和 DoH（HTTPS 上的 DNS）进行ping--tcp操作，相关选项分别为--tcp、--tls和--doh：

```
./dnsping.py -c 5 --dnssec --flags --tls --ede -t AAAA -s 8.8.8.8 brokendnssec.net
```

```
dnsping.py DNS: 8.8.8.8:853, hostname: brokendnssec.net, proto: TLS, class: IN, type: AAAA, flags: [RD]

75 bytes from 8.8.8.8: seq=1   time=113.631 ms [QR RD RA DO] SERVFAIL [EDE 10: For brokendnssec.net/soa]

75 bytes from 8.8.8.8: seq=2   time=115.479 ms [QR RD RA DO] SERVFAIL [EDE 10: For brokendnssec.net/soa]

75 bytes from 8.8.8.8: seq=3   time=90.882  ms [QR RD RA DO] SERVFAIL [EDE 10: For brokendnssec.net/soa]

75 bytes from 8.8.8.8: seq=4   time=91.256  ms [QR RD RA DO] SERVFAIL [EDE 10: For brokendnssec.net/soa]

75 bytes from 8.8.8.8: seq=5   time=94.072  ms [QR RD RA DO] SERVFAIL [EDE 10: For brokendnssec.net/soa]

--- 8.8.8.8 dnsping statistics ---

5 requests transmitted, 5 responses received, 0% lost

min=90.882 ms, avg=101.064 ms, max=115.479 ms, stddev=12.394 ms
```

### dnstraceroute

DnsDiag的dnstraceroute组件是一款路由跟踪实用程序，用于找出 DNS 请求到达目的地所经过的路径。我们可以将其与实际网络路由跟踪进行比较，并确保 DNS 流量没有路由到任何不需要的路径。

除了UDP之外，还支持TCP作为传输协议，使用--tcp标志。

```
./dnstraceroute.py --expert --asn -C -t A -s 8.8.4.4 facebook.com
```

```
dnstraceroute.py DNS: 8.8.4.4:53, hostname: facebook.com, rdatatype: A

1 192.168.0.1 (192.168.0.1) 1 ms

2 192.168.28.177 (192.168.28.177) 4 ms

3 192.168.0.1 (192.168.0.1) 693 ms

4 172.19.4.17 (172.19.4.17) 3 ms

5 dns.google (8.8.4.4) [AS15169 GOOGLE, US] 8 ms

=== Expert Hints ===

 [*] public DNS server is next to a private IP address (possible hijacking)
```

### dnseval

DnsDiag的dnseval组件一个批量 ping 实用程序，它向给定的 DNS 服务器列表发送任意 DNS 查询。此脚本用于同时比较多个 DNS 服务器的响应时间。

我们可以分别使用和dnseval来比较使用不同传输协议（如 UDP（默认）、TCP、DoT 和 DoH）的响应时间。参数选项分别为--tcp、--tls和--doh：

```
./dnseval.py --dnssec -t AAAA -f public-servers.txt -c10 ripe.net
```

```
server                   avg(ms)     min(ms)     max(ms)     stddev(ms)  lost(%)  ttl        flags                  response

----------------------------------------------------------------------------------------------------------------------------

1.0.0.1                  36.906      7.612       152.866     50.672      %0       300        QR -- -- RD RA AD --   NOERROR

1.1.1.1                  7.752       7.512       8.132       0.183       %0       298        QR -- -- RD RA AD --   NOERROR

2606:4700:4700::1001     7.661       7.169       8.102       0.240       %0       297        QR -- -- RD RA AD --   NOERROR

2606:4700:4700::1111     7.802       7.000       8.128       0.312       %0       296        QR -- -- RD RA AD --   NOERROR

195.46.39.39             14.723      7.024       78.239      22.362      %0       300        QR -- -- RD RA -- --   NOERROR

195.46.39.40             7.524       6.972       10.897      1.191       %0       300        QR -- -- RD RA -- --   NOERROR

208.67.220.220           70.519      6.694       180.229     66.516      %0       300        QR -- -- RD RA AD --   NOERROR

208.67.222.222           37.868      6.663       107.601     41.178      %0       300        QR -- -- RD RA AD --   NOERROR

2620:0:ccc::2            31.471      6.768       178.647     56.546      %0       299        QR -- -- RD RA AD --   NOERROR

2620:0:ccd::2            20.651      6.699       145.029     43.702      %0       300        QR -- -- RD RA AD --   NOERROR

216.146.35.35            19.338      6.713       131.198     39.306      %0       300        QR -- -- RD RA AD --   NOERROR

216.146.36.36            107.741     73.421      266.969     58.003      %0       299        QR -- -- RD RA AD --   NOERROR

209.244.0.3              14.717      7.015       80.329      23.058      %0       300        QR -- -- RD RA -- --   NOERROR

209.244.0.4              7.184       7.003       8.197       0.361       %0       300        QR -- -- RD RA -- --   NOERROR

4.2.2.1                  7.040       6.994       7.171       0.052       %0       299        QR -- -- RD RA -- --   NOERROR

4.2.2.2                  14.358      6.968       79.964      23.052      %0       300        QR -- -- RD RA -- --   NOERROR

4.2.2.3                  7.083       6.945       7.265       0.091       %0       299        QR -- -- RD RA -- --   NOERROR

4.2.2.4                  7.103       6.990       7.238       0.086       %0       299        QR -- -- RD RA -- --   NOERROR

4.2.2.5                  7.100       7.025       7.267       0.074       %0       299        QR -- -- RD RA -- --   NOERROR

80.80.80.80              149.924     53.310      247.395     97.311      %0       299        QR -- -- RD RA AD --   NOERROR

80.80.81.81              144.262     53.360      252.564     97.759      %0       298        QR -- -- RD RA AD --   NOERROR

8.8.4.4                  9.196       7.160       10.974      1.484       %0       299        QR -- -- RD RA AD --   NOERROR

8.8.8.8                  7.847       7.056       9.866       0.836       %0       299        QR -- -- RD RA AD --   NOERROR

2001:4860:4860::8844     31.819      7.194       155.761     50.671      %0       299        QR -- -- RD RA AD --   NOERROR

2001:4860:4860::8888     7.773       7.200       9.814       0.777       %0       298        QR -- -- RD RA AD --   NOERROR

9.9.9.9                  21.894      6.670       81.434      30.299      %0       300        QR -- -- RD RA AD --   NOERROR

2620:fe::fe              21.177      6.723       80.046      30.062      %0       300     ...