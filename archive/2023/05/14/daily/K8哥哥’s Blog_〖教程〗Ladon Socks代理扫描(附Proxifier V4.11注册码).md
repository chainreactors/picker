---
title: 〖教程〗Ladon Socks代理扫描(附Proxifier V4.11注册码)
url: http://k8gege.org/p/proxy.html
source: K8哥哥’s Blog
date: 2023-05-14
fetch_date: 2025-10-04T11:39:06.658862
---

# 〖教程〗Ladon Socks代理扫描(附Proxifier V4.11注册码)

[![logo](/../k8img/logo.png)

### K8哥哥](/ "K8gege")

## 没有绝对安全的系统

[K8哥哥’s Blog](http://k8gege.org)

* [Home](/)
* [Ladon](/Ladon/)
* [Code](/tags/Code/)
* [Exp](/tags/Exp/)
* [Tool](/tags/Tool/)
* [Music](https://k8music.github.io)
* [Archives](/archives/)
* [Friends](/friends/)
* [Rss](/atom.xml)

# 〖教程〗Ladon Socks代理扫描(附Proxifier V4.11注册码)

[Ladon](/categories/Ladon/)

[Proxy](/tags/Proxy/)

2023/05/13

本文于**860**
天之前发表

=============================================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

### Socks代理工具

#### windows平台

Proxifier软件是一款极其强大的socks5客户端,同时也是一款强大的站长工具。Proxifier支持TCP，UDP协议，支持Xp，Vista，Win7，支持socks4，socks5，http代理协议可以让不支持通过代理服务器工作的网络程序能通过HTTPS或SOCKS代理或代理链。

V4.11 (2022.12.16) Proxifier 现在可以记录和阻止 UDP 连接

2020年7月proxifier官方发布最新版4.0.1修复ipv6兼容问题，以及其它很多问题。 3.42支持类似chrome这样工作的69个应用程序，修复了一些第三方应用程序的兼容性。

以上更新日志，充分说明该代理工具不能保证兼容所有第3方程序，或者说兼容性不好，同样的3.31版本有人能代理Ladon，有人代理不了。

官方下载: <http://www.proxifier.com/download>

#### linux/mac平台

ProxyChains遵循GNU协议的一款适用于linux系统的网络代理设置工具。强制由任一程序发起的TCP连接请求必须通过诸如TOR 或 SOCKS4, SOCKS5 或HTTP(S) 代理。支持的认证方式包括：SOCKS4/5的用户/密码认证，HTTP的基本认证。允许TCP和DNS通过代理隧道，并且可配置多个代理。

ProxyChains代理工具非常好，真的可以兼容所有程序，不像proxifier好多程序还不定兼容，当然两者都有一定的丢包率，Ladon批量扫描功能过快超时短，可能会导致有些结果丢失，回头设置一个代理模式，提高超时放慢速度看看。

### 代理支持协议

通过以上两平台的代理工具简介，可以看出代理客户端并不支持ICMP协议。
所以使用它们代理，无法PING通内网主机。何况FRP、EW等也不支持ICMP。

#### 支持协议

1.TCP
2.UDP

#### 代理协议

1.SOCKS4
2.SOCKS5
3.HTTP(S)

### 代理工具兼容性

推荐proxifier 3.42及以上版本，最好是最新版，3.31及以前的兼容性极差，所以不推荐，我使用VM虚拟机12版本的时候，可以代理Ladon,但后面升级为15，发现很难代理，就连测试系统自带的telnet程序，都不行了。Ladon在多个虚拟机测试也是一样，但是有同事也是用3.31却可以代理使用，网上很多人也和我反应不能用。后来我看了下3.31是2016年的，就想看看官方有没更新，发现18年有个3.42版本，测试一下，兼容好多了，然后在星球发表，发表不久发现官方更新了4.0.1，只是他没写更新日志，还以为没有更新。

### Proxifier通用注册码

4.11 (2022.12.16)
4.07 (2021.11.02)
4.05 (2021.03.09)
4.03 (2020.11.04)
4.0.1 (2020.7.7)
3.4.2 (2018.8.31)
3.3.1 (2016不推荐)

Standard Edition

用户名 [k8gege.org](http://k8gege.org)
注册码 5EZ8G-C3WL5-B56YG-SCXM9-6QZAP

![使用http访问查看图片](/k8img/posts/Proxy411.PNG)

### Ladon工作原理

由于proxifier客户端不支持ICMP或者说ew等代理工具也不支持ICMP协议，所以代理后探测存活主机就不要使用Ping或OnlinePC模块了，使用扫描模块需加noping参数，非扫描模块不需要noping。探测存活主机可使用osscan、webscan、urlscan、ms17010、smbghost等模块，他们能扫出东西不也意味着主机存活吗？ping不是唯一的探测存活主机存活方式，系统防火墙默认禁ping，使用ping探测本身就会错过很多存活主机，所以实战要结合多种方式探测。假设目标防火墙只允许smb协议通过，你用nmap端口扫描的TCP包被拦截显示成关的，但用ms17010，smbghost扫出漏洞或者用smbscan就显示密码错误拒绝访问等，这不就说明445确实开放吗？不要死板的老是停留在ping和单纯的端口扫描来探测存活主机，要考虑实际环境，OnlinePC可探测到大部分存活主机，但不等于能探测到全部存活主机，当你无法渗透已扫到的存活主机，就得尝试其它模块探测更多主机。

PS：如何验证代理是否支持ICMP协议，非常简单用系统自带命令PING目标内网IP（不要PING自己的内网哦），能PING通目标存活IP，说明代理支持ICMP协议，意味你可以像挂了目标VPN一样或者像本地一样随意扫描目标内网，如果根本PING不通，老老实实扫描时加上noping参数。

### Socks代理扫描

例子：Socks5代理扫描目标10.1.2段是否存在MS17010漏洞
Ladon noping 10.1.2.8/24 MS17010

PS：再次强调，由于代理工具不支持ICMP，所以Ladon扫描类功能必须加noping参数，非扫描模块不需要。

### 实战扫描结果

Linux SSH服务识别之22端口扫描
![使用http访问查看图片](/k8img/Ladon/exe/proxy_porscan22.png)

WEB HttpBanner扫描
![使用http访问查看图片](/k8img/Ladon/exe/proxy_httpscan.png)

永恒之默漏洞 SMBghost CVE-2020-0796
![使用http访问查看图片](/k8img/Ladon/exe/proxy_smbghost.png)

OSSCAN探测目标操作系统
![使用http访问查看图片](/k8img/Ladon/exe/proxy_osscan.png)

ProtScan端口扫描
![使用http访问查看图片](/k8img/Ladon/exe/proxy_porscan.png)

### Proxifier 更新日志

#### 版本 4.11 (2022.12.16)

```
Proxifier 现在可以记录和阻止 UDP 连接
添加了一个主选项，用于控制负责 IP 地址泄漏预防的其他设置（配置文件->高级->DNS 和 IP 泄漏预防模式）
添加了阻止非 A/AAAA DNS 查询的选项（配置文件->高级->如果 DNS 通过代理，则阻止非 A/AAAA 查询）
可调整的日志窗口字体大小
日志窗口呈现问题
Proxifier、ProxyChecker 和 ServiceManager 中的多个小修复和改进
```

#### 版本 4.07 (2021.11.02)

```
Windows on ARM 支持
服务模式小优化
无人值守模式下的安装（例如 SCCM）已修复
便携式版本可能会在退出时导致其他应用程序崩溃
Windows 高对比度模式支持
```

#### 版本 4.05 (2021.03.09)

```
静默安装和卸载已修复
“无法连接到占位符（假）IP 地址”错误已修复
启用“DNS over Proxy”时改进的规则处理逻辑
对于本地主机连接，IPv4 优先于 IPv6
可自定义的假 IP 地址子网
改进了与配置文件加载相关的错误处理
在 UI 中更新和链接的文档
日志窗口自动滚动固定
改进的试用和许可证注册体验
小的 UI 优化和改进
```

#### 版本 4.03 (2020.11.04)

```
针对 IPv4 映射的 IPv6 连接修复了“无法连接到占位符（假）IP 地址”错误
使用多个手动规则（从右键单击上下文菜单创建）时崩溃
在某些情况下，启用代理名称解析后，系统连接可能无法正常工作
各种小改进
```

#### 版本 4.01 (2020.10.26)

```
发布版本
安装/卸载逻辑得到改进
拖放配置文件 (*.ppx)
负载平衡链现在可以对同一个进程使用同一个代理
```

#### 版本 4.01 测试版 3 (2020.09.29)

```
Proxifier 现在可以作为原生 Windows 服务运行
Proxifier服务管理器工具（ServiceManager.exe）介绍
Proxifier 便携版现已推出
所有二进制文件都已在发布模式下编译
由 UDP 端口 53 上的某些特定非 DNS 流量引起的 BSOD
配置文件自动更新已修复
日志性能得到改善
较小的 UI 调整和优化
```

#### 版本 4.01 测试版 2(2020.08.19)

```
无法连接到占位符（假）IP 地址错误已修复
Proxifier 退出时崩溃
详细按钮添加到连接列表窗口
不同屏幕日志和文件日志级别的正确处理
驱动程序消息：397:g_NfeFlowListSize 太大错误已修复
在重载下崩溃
窗格自动隐藏时主菜单消失
序号 381 无法定位在 ProxifierShellExt.dll 错误已修复
其他改进和优化
```

#### 版本 4.01 Beta 1

(2020.07.07)

初始发行。

### 工具下载

最新版本：<http://k8gege.org/Download>
历史版本: <https://github.com/k8gege/Ladon/releases>
Proxifier: <https://github.com/k8gege/K8tools>

### 转载声明

K8博客文章随意转载，转载请注明出处！ © K8gege <http://k8gege.org>

![](../images/k8join2.png)

扫码加入K8小密圈

转载声明：
K8博客文章随意转载，转载请注明出处！ © [K8gege](http://k8gege.org)

[上一篇

〖Tech〗Ladon RouterOS/Mikrotik路由器探测](/p/MndpInfo.html "〖Tech〗Ladon RouterOS/Mikrotik路由器探测")
[下一篇

〖Tech〗CVE-2022-36537 未授权RCE漏洞复现](/p/CVE-2022-36537.html "〖Tech〗CVE-2022-36537 未授权RCE漏洞复现")

### Table of Contents

1. [Socks代理工具](#Socks%E4%BB%A3%E7%90%86%E5%B7%A5%E5%85%B7)
   1. [windows平台](#windows%E5%B9%B3%E5%8F%B0)
   2. [linux/mac平台](#linux-mac%E5%B9%B3%E5%8F%B0)
2. [代理支持协议](#%E4%BB%A3%E7%90%86%E6%94%AF%E6%8C%81%E5%8D%8F%E8%AE%AE)
   1. [支持协议](#%E6%94%AF%E6%8C%81%E5%8D%8F%E8%AE%AE)
   2. [代理协议](#%E4%BB%A3%E7%90%86%E5%8D%8F%E8%AE%AE)
3. [代理工具兼容性](#%E4%BB%A3%E7%90%86%E5%B7%A5%E5%85%B7%E5%85%BC%E5%AE%B9%E6%80%A7)
4. [Proxifier通用注册码](#Proxifier%E9%80%9A%E7%94%A8%E6%B3%A8%E5%86%8C%E7%A0%81)
5. [Ladon工作原理](#Ladon%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86)
6. [Socks代理扫描](#Socks%E4%BB%A3%E7%90%86%E6%89%AB%E6%8F%8F)
7. [实战扫描结果](#%E5%AE%9E%E6%88%98%E6%89%AB%E6%8F%8F%E7%BB%93%E6%9E%9C)
8. [Proxifier 更新日志](#Proxifier-%E6%9B%B4%E6%96%B0%E6%97%A5%E5%BF%97)
   1. [版本 4.11 (2022.12.16)](#%E7%89%88%E6%9C%AC-4-11-2022-12-16)
   2. [版本 4.07 (2021.11.02)](#%E7%89%88%E6%9C%AC-4-07-2021-11-02)
   3. [版本 4.05 (2021.03.09)](#%E7%89%88%E6%9C%AC-4-05-2021-03-09)
   4. [版本 4.03 (2020.11.04)](#%E7%89%88%E6%9C%AC-4-03-2020-11-04)
   5. [版本 4.01 (2020.10.26)](#%E7%89%88%E6%9C%AC-4-01-2020-10-26)
   6. [版本 4.01 测试版 3 (2020.09.29)](#%E7%89%88%E6%9C%AC-4-01-%E6%B5%8B%E8%AF%95%E7%89%88-3-2020-09-29)
   7. [版本 4.01 测试版 2(2020.08.19)](#%E7%89%88%E6%9C%AC-4-01-%E6%B5%8B%E8%AF%95%E7%89%88-2-2020-08-19)
   8. [版本 4.01 Beta 1](#%E7%89%88%E6%9C%AC-4-01-Beta-1)
9. [工具下载](#%E5%B7%A5%E5%85%B7%E4%B8%8B%E8%BD%BD)

Total:

Copyright ©
2020
 |
Powered by [K8gege](//k8gege.org)