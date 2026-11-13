---
title: 64%云环境受影响：Apache HTTP Server爆未认证RCE，HTTP/2一个竞争条件打穿堆内存
url: https://mp.weixin.qq.com/s/UkVimorelPpa_yv5PdYYPA
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:02:07.867886
---

# 64%云环境受影响：Apache HTTP Server爆未认证RCE，HTTP/2一个竞争条件打穿堆内存

# 64%云环境受影响：Apache HTTP Server爆未认证RCE，HTTP/2一个竞争条件打穿堆内存

零日手记
零日手记

随笔漫记安全路

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年11月11日，Apache HTTP Server发布紧急安全更新，修复一个CVSS Critical级别的远程代码执行漏洞。Wiz Research数据显示，**64%的云环境存在受影响资源**。

漏洞编号CVE-2026-119618，藏在HTTP/2模块的`assign_headers()`函数里——一个并发线程共享资源时缺乏同步的竞争条件，可被远程未认证攻击者利用触发堆内存损坏，最终实现RCE。

## 漏洞档案

| 项目 | 详情 |
| --- | --- |
| CVE | CVE-2026-119618 |
| 严重级别 | Critical |
| 影响版本 | Apache HTTP Server 2.4.55 – 2.4.70 |
| 独立模块 | mod\_h2 (GitHub) 2.0.8 – 2.0.42 |
| 补丁版本 | 2.4.71 / mod\_h2 > 2.0.42 |
| 认证要求 | **无需认证** |
| 攻击面 | 远程，通过HTTP/2连接 |
| 在野利用 | 截至发稿无公开 exploit，无在野利用报告 |
| 发现者 | Anthropic OSS Scanner (ANT-2026-MAPKT6MZ) + Google Cloud漏洞研究团队（Anthony Weems、Simon Scannann）独立发现 |

## 漏洞根因：一行代码写错了操作对象

补丁commit `5ed3928766`只有一行改动，但这一行暴露了整个问题。

漏洞出在`assign_headers()`函数中。这个函数负责将HTTP/2请求的头信息赋值到Apache内部的`request_rec`结构体。函数开头先做了一次克隆：

```
r->headers_in = apr_table_clone(r->pool, req->headers);
```

`r->headers_in`是当前请求的私有头表，`req->headers`是共享的HTTP/2请求头表。克隆之后，后续操作应该只改`r->headers_in`（私有副本），不能碰`req->headers`（共享原件）。

但漏洞代码在设置Content-Length时写错了对象：

```
// 漏洞代码 (modules/http2/h2_request.c:353)
apr_table_setn(req->headers, "Content-Length", "0");
//               ^^^^^^^^^^^ 写成了共享的 req->headers
```

```
// 修复后
apr_table_setn(r->headers_in, "Content-Length", "0");
//               ^^^^^^^^^^^^^ 改为私有的 r->headers_in
```

`req->headers`是**多线程共享的资源**。HTTP/2支持多路复用——一个连接上同时处理多个请求流，每个流在自己的线程中运行，但它们共享同一个`h2_request`结构体。当两个并发流同时执行到这行代码，都在往同一个`req->headers`表写入`Content-Length`，APR table的内部数据结构在并发写入下发生竞争，导致堆内存损坏。

堆损坏之后，攻击者可以通过精心构造的HTTP/2请求触发可预测的内存布局，将堆 corruption转化为任意代码执行——以Web服务器进程的权限运行命令。

## 攻击路径

```
攻击者发送 HTTP/2 连接
    ↓
同一连接上并发多个请求流 (stream multiplexing)
    ↓
构造特定请求：有 Content-Type 但已见 eos (no_body=true)
    ↓
多个流同时进入 assign_headers() 的 Content-Length 分支
    ↓
并发写入共享的 req->headers 表 → 竞争条件
    ↓
APR table 内部结构堆损坏
    ↓
堆 corruption → 可控内存布局 → 任意代码执行
```

关键条件：攻击者需要在一个HTTP/2连接上**同时发送多个精心构造的请求流**，让它们竞争执行到`assign_headers()`中的写入路径。触发路径需要请求同时满足：有`Content-Type`头 + 已收到EOS标记（`no_body=true`）+ 无`Content-Length`。

## 为什么影响面这么大

Wiz Research的扫描数据给出了三个数字：

* **64%** 的云环境有受影响资源
* 大量实例**公网暴露**
* 以上数据未考虑配置因素（实际暴露面可能更大）

Apache HTTP Server是全球部署量最大的Web服务器之一。2.4.55到2.4.70覆盖了2023年初至今的大多数活跃部署。只要开了HTTP/2（现代部署几乎都开了），就在射程内。

云环境尤其危险：一个被攻破的Apache容器化实例可以作为跳板，通过云元数据端点获取IAM凭证，横向移动到相邻微服务。

## 修复与临时缓解

**方案一：升级（推荐）**

```
# Debian/Ubuntu
apt update && apt upgrade apache2

# RHEL/CentOS/AlmaLinux
dnf update httpd

# 源码编译
./configure --enable-http2 && make && make install
# 确保升级到 2.4.71 或更高
httpd -v
```

**方案二：禁用HTTP/2（无法立即升级时）**

编辑Apache配置文件，移除HTTP/2协议支持，回退到HTTP/1.1：

```
# 在 httpd.conf 或 ssl.conf 中
# 找到 Protocols 行，改为：
Protocols http/1.1

# 或者注释掉整行：
# Protocols h2 h2c http/1.1
```

重启生效：

```
apachectl configtest && systemctl restart apache2
# 或 RHEL: systemctl restart httpd
```

注意：禁用HTTP/2会损失多路复用性能优势，仅作为临时止血。

## 自检：你的服务器在不在射程

```
# 1. 查版本
httpd -v   # 或 apache2 -v
# 如果 2.4.55 ≤ 版本 ≤ 2.4.70，受影响

# 2. 查是否启用了 HTTP/2
httpd -M 2>/dev/null | grep http2
# 或
apache2ctl -M 2>/dev/null | grep http2
# 输出 http2_module (shared) = 已启用

# 3. 查配置中是否声明了 HTTP/2 协议
grep -r "Protocols" /etc/apache2/ /etc/httpd/ 2>/dev/null
# 或
grep -r "h2" /etc/apache2/ /etc/httpd/ 2>/dev/null | grep -v "#"
```

三条全中：版本在范围内 + http2模块加载 + 配置声明了h2协议——立即升级或禁用HTTP/2。

## 一个细节：Anthropic的OSS扫描器又立功了

这个漏洞的两个独立发现者之一是Anthropic的OSS Scanner（漏洞编号ANT-2026-MAPKT6MZ）。加上之前Anthropic研究员报告的Linux内核TCP UAF（CVE-2026-98432，Claude写出root PoC）和OpenAI一夜间挖出948个Linux提权漏洞——AI辅助漏洞挖掘正在从实验走向工业化。

OpenSSH团队上周刚发布声明称"近期收到大量AI模型发现的安全报告，将因此加快发布节奏"。Apache HTTP Server这个Critical级别的漏洞又被AI扫描器率先发现——AI挖洞的速度已经超过了人类的补丁应用速度。

## 补丁本身：一行修复

```
- apr_table_setn(req->headers, "Content-Length", "0");
+ apr_table_setn(r->headers_in, "Content-Length", "0");
```

把写入目标从共享的`req->headers`改成私有的`r->headers_in`。一行代码，消除了竞争条件的根源——每个线程只写自己的副本，不再踩到彼此的脚。

这是典型的共享资源并发访问漏洞：克隆操作做了，但后续写入忘了用副本。CWE-362（Race Condition）+ CWE-366（共享资源同步缺陷）的经典组合。

---

参考：

* NVD: CVE-2026-119618
* oss-security公告: openwall.com/lists/oss-security/2026/11/11/13
* Wiz Research分析: wiz.io/blog/cve-2026-119618
* 补丁commit: apache/httpd@5ed3928766
* Apache安全公告: httpd.apache.org/security/vulnerabilities\_24.html

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/euBEasB1QK1mSyV63n51RYwjUnANgONCBIoG7rlnVw75VBa0K8ZtSh9RmNQBsX1ibHXx1Gw8emQgIjJAeNmdJGg/0?wx_fmt=png)

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