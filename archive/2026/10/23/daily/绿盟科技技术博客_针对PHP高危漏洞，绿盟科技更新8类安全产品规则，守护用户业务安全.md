---
title: 针对PHP高危漏洞，绿盟科技更新8类安全产品规则，守护用户业务安全
url: https://blog.nsfocus.net/%e9%92%88%e5%af%b9php%e9%ab%98%e5%8d%b1%e6%bc%8f%e6%b4%9e%ef%bc%8c%e7%bb%bf%e7%9b%9f%e7%a7%91%e6%8a%80%e6%9b%b4%e6%96%b08%e7%b1%bb%e5%ae%89%e5%85%a8%e4%ba%a7%e5%93%81%e8%a7%84%e5%88%99%ef%bc%8c/
source: 绿盟科技技术博客
date: 2026-10-23
fetch_date: 2026-10-24T06:46:04.017959
---

# 针对PHP高危漏洞，绿盟科技更新8类安全产品规则，守护用户业务安全

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)
* [登录](https://blog.nsfocus.net/wp-login.php)

* [首页](https://blog.nsfocus.net)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* 针对PHP高危漏洞，绿盟科技更新8类安全产品规则，守护用户业务安全

# 针对PHP高危漏洞，绿盟科技更新8类安全产品规则，守护用户业务安全

[0](https://blog.nsfocus.net/%E9%92%88%E5%AF%B9php%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%EF%BC%8C%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E6%9B%B4%E6%96%B08%E7%B1%BB%E5%AE%89%E5%85%A8%E4%BA%A7%E5%93%81%E8%A7%84%E5%88%99%EF%BC%8C/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-10-2317:06") 发布于 22 小时前

![](https://blog.nsfocus.net/wp-content/uploads/2026/10/security.jpeg)

阅读： 51

近日，PHP 官方发布安全更新，修复两个高危远程代码执行漏洞，编号 CVE-2026-109618 与 CVE-2026-109619。为全力保障用户业务安全，助力快速完成风险处置，绿盟科技完成 8 类安全产品的防护规则更新，并配套发布四步标准化处置清单。

据悉，这两项漏洞的 CVSS 4.0 评分均为 9.2 分，属于严重级别，并且在特定条件下未经身份验证即可被远程利用。漏洞细节与部分 POC 已经公开——攻击者不必从零研究，现成的利用方法谁都能拿来试。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/6d52f0a0f43d46bfbbee00f045b97351~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=202610231705196CF0BBC89E2482763842&x-expires=2147483647&x-signature=iVHh9X%2BilODlI%2BhCbmNzKnshZXM%3D)

造成的危害分为两级。轻的一级是进程崩溃：PHP-FPM 频繁退出，网站大面积报错或打不开，用户看到的就是 502、500 这类错误页。重的一级是攻击者以 PHP 服务账户权限执行任意代码，植入后门、挖矿、横向渗透。

根据权威互联网机构W3Techs调研：在能够识别服务器端编程语言的网站中，约 69.3% 使用 PHP。动态网站、CMS、电商、论坛，底层大多是它。判断用户业务是否受影响，只有一条标准：PHP 版本号。与网站用什么程序无关。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/a67d4159ffd94de5ac176e3e8f531670~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=202610231705196CF0BBC89E2482763842&x-expires=2147483647&x-signature=D%2B1yBoNeSL6RjcR2%2BaN1b77fisc%3D)

PHP 8.1 及更早分支已结束官方常规安全维护，没有官方补丁。这类环境有两个选择：升级到受支持版本，或确认发行版、长期支持服务商是否提供补丁。

参考链接：
https://www.php.net/archive/2026.php

### 一、补丁打完之前，靠什么顶住

补丁发出来，不等于当天就能升完。老系统要评估兼容性，容器镜像要重新构建，业务窗口要排期。这段空档，就是防护设备要顶上去的时间。

**防护分两步走：**

1）先查清哪些资产落在受影响区间，确定需要防护的对象。

2）将攻击流量挡在 PHP 之前。绿盟科技8类安全产品全面更新规则，实现PHP漏洞精准检测和实时防护。

注意：规则更新不等于补丁。规则争取的是打补丁的窗口期，不是免修补丁的理由。最终仍要把 PHP 升到修复版本。

### 二、绿盟科技 8 类产品的规则更新清单

本次更新的产品共 8 类，分成两组：4类用于防护，4 类用于检测。

分组的依据是客户最常问的两个问题。“攻击能不能挡住”，由防护组回答；“我到底中招了没有”，由检测组回答。两组规则本次都已完成更新，但起作用的阶段不同，不要互相替代。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/1a5732af9bbb420cb627b50476b56e56~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=202610231705196CF0BBC89E2482763842&x-expires=2147483647&x-signature=j%2FDcYlVTgpQhZVMq%2FfhFHy0Bi4c%3D)

2.1 **防护类：NF / WAF / IPS / NAVG**

这四类防护产品的作用是：让攻击请求在到达 PHP 之前就被识别或拦下来。

下一代防火墙NF支持入侵防护功能，已经更新PHP远程代码执行漏洞防护规则。NF部署在安全边界，能够及时拦截和阻断黑客利用PHP远程代码执行漏洞发起攻击。WAF 部署在 Web 应用前面。本次新增的规则直接对应 PHP 的会话上传进度机制漏洞。IPS 与 NAVG 部署在网络链路上，规则包各新增 3 条规则，防御PHP远程代码执行漏洞，另有 1 条既有规则同步更新。

四类产品可以叠加部署，也可以按你的网络位置选其中一类先上。优先级建议：边界安全优先更新NF，面向公网的 Web 业务先上 WAF，内网横向流量先上 IPS 与 NAVG。

升级有前置条件，动手前先核对：

**NF：**需要引擎版本为6.0.5.128及以上的所有标准版本，引擎版本低于6.0.5.128的版本请使用离线升级方式升级。

**WAF：**建议在64位系统版本 V6.0R09F00.29386582 及以上版本上升级。

**IPS、NAVG：**需要引擎版本 V56R11F01 及以上（引擎版本与表格中的规则包版本是两回事）。

版本不满足的，先升引擎再升规则。

2.2 **检测类：UTS / RSAS / TVM / WVSS**

这四类的作用是：精准检测PHP漏洞。

**UTS** 综合安全审计系统负责流量侧的威胁发现，融合多个检测引擎，通过流量的还原、检测、分析，识别针对该漏洞的恶意攻击。本次更新入侵检测规则包，覆盖PHP远程代码执行漏洞，升级需要引擎版本 V2.0R00F05 及以上，升级后固件及引擎版本不变，引擎自动重启生效，不会造成会话中断。

TVM,WVSS,RSAS负责资产漏洞的识别及管理：

**TVM** 负责漏洞的持续管理与跟踪。

**WVSS**增加PHP远程代码执行漏洞扫描插件，WVSS 的升级包版本为 V6.0R03F00.441，另有WVSS HHA 的 V6.0R04F00.4203。

**RSAS** 覆盖面更广，适合做全网资产排查；WVSS 面向 Web 场景，适合先扫对外站点。

推荐的使用顺序是两步：

* 第一步，用 RSAS 或 WVSS 把跑 PHP 的主机、容器扫一遍，标注版本与部署方式。
* 第二步，RSAS或WVSS结果会自动上传到TVM进行全生命周期的闭环处置修复。清单出来之前，你无法判断防护设备该优先部署在哪条链路上。

2.3 **安全产品规则包获取链接**

* NF：https://update.nsfocus.com/update/listNewNfDetail/v/rule\_hg6.0.5
* WAF：https://update.nsfocus.com/update/listWafV69Detail/v/rule
* IPS：https://update.nsfocus.com/update/listNewipsDetail/v/rule5.6.11\_v2
* NVAG：https://update.nsfocus.com/update/listNewnavgDetail/v/gm\_rule5.6.11\_v2
* UTS：https://update.nsfocus.com/update/listBsaUtsDetail/v/rule2.0.1
* RSAS：https://update.nsfocus.com/update/listRsasDetail/v/vulsys2
* TVM：https://update.nsfocus.com/update/listTvmDetail/v/2021101401
* WVSS：https://update.nsfocus.com/update/listWvssDetail/v/6/t/plg

### 三、四步把防护落到实处

清单看完，执行顺序是固定的：四步，少一步就有缺口。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/5241e838004a4fb8aa6d008891f94f57~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=202610231705196CF0BBC89E2482763842&x-expires=2147483647&x-signature=qtAXTLXM5Fatf25U0lvkzCLRM7w%3D)

* **第一步：查版本。**

在服务器上执行 php -v，对照上面的表格判断是否落在受影响区间。容器里的 PHP 要单独查，镜像里的版本和宿主机是两回事。同时登录各设备管理界面，核对引擎版本。

* **第二步：升 PHP。**

优先升到 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35。8.1 及更早的环境没有官方补丁，只能升版本或走发行版补丁。

补丁排不上期的，先做临时缓解。关闭会话上传进度（
session.upload\_progress.enabled = Off，仅限业务未使用上传进度跟踪时），启用严格会话模式（session.use\_strict\_mode = 1）。改完重启 PHP-FPM 与 Web 服务器。

* **第三步：上规则。**

先核对引擎前置版本，不满足的先升引擎再升规则。升级包在绿盟科技官网即可获取，按产品文档操作。

* **第四步：验证并盯守。**

用 RSAS 复扫目标资产，看能否识别出受影响版本；或者在 WAF、IPS 侧发一个测试请求，看规则是否命中。

同时盯住四个信号：工作进程异常崩溃、频繁退出、异常子进程创建、非预期文件写入。出现任何一个，都按已被尝试利用处理。

最后把扫描结果与处置清单存档。这份清单既是修复顺序的依据，也是后续审计检查的凭证。

补丁解决根因，规则争取时间。两件事都做完，这次处置才算完成。

### 四、两个最常见的问题

**1、只把 WordPress、Drupal 升到最新版，行不行？**

不行。缺陷在 PHP 底层运行引擎，更新网站程序、主题或插件动不到那一层。应用层和运行时是两层，不能混为一谈。

**2、升级规则包会不会影响业务？**

会有瞬时影响，但是可控。引擎会自动重启生效，切换瞬间会丢失 3~5 个网络探测包，表现为一次极短的抖动，属于正常现象。建议放在业务低峰期操作，升级后做一次连通性验证。

需要做的两件事：查一次 PHP 版本，升一次规则包。8 类产品的升级包已在绿盟科技官网升级包发布页就位，登录即可下载。

最后修改日期: 2026-10-23

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [绿盟科技顾杜娟博士获评 “2026中国网络安全十大人物”，前沿研发实力获行业认可](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E9%A1%BE%E6%9D%9C%E5%A8%9F%E5%8D%9A%E5%A3%AB%E8%8E%B7%E8%AF%84-2026%E4%B8%AD%E5%9B%BD%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%8D%81%E5%A4%A7%E4%BA%BA/)
* [针对PHP高危漏洞，绿盟科技更新8类安全产品规则，守护用户业务安全](https://blog.nsfocus.net/%E9%92%88%E5%AF%B9php%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%EF%BC%8C%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E6%9B%B4%E6%96%B08%E7%B1%BB%E5%AE%89%E5%85%A8%E4%BA%A7%E5%93%81%E8%A7%84%E5%88%99%EF%BC%8C/)
* [PHP远程代码执行漏洞（CVE-2026-109618/CVE-2026-109619）通告](https://blog.nsfocus.net/php%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%EF%BC%88cve-2026-109618-cve-2026-109619%EF%BC%89%E9%80%9A%E5%91%8A-2/)
* [前端在 AI Coding 的应用实践：把 AI 用成日常编码搭档](https://blog.nsfocus.net/%E5%89%8D%E7%AB%AF%E5%9C%A8-ai-coding-%E7%9A%84%E5%BA%94%E7%94%A8%E5%AE%9E%E8%B7%B5%EF%BC%9A%E6%8A%8A-ai-%E7%94%A8%E6%88%90%E6%97%A5%E5%B8%B8%E7%BC%96%E7%A0%81%E6%90%AD%E6%A1%A3/)
* [2026 TechWorld | 让智能更安全·AI自身安全专题论坛精彩回顾](https://blog.nsfocus.net/2026-techworld-%E8%AE%A9%E6%99%BA%E8%83%BD%E6%9B%B4%E5%AE%89%E5%85%A8%C2%B7ai%E8%87%AA%E8%BA%AB%E5%AE%89%E5%85%A8%E4%B8%93%E9%A2%98%E8%AE%BA%E5%9D%9B%E7%B2%BE%E5%BD%A9%E5%9B%9E%E9%A1%BE/)

## 文章导航

[上一篇文章 PHP远程代码执行漏洞（CVE-2026-109618/CVE-2026-109619）通告](https://blog.nsfocus.net/php%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%EF%BC%88cve-2026-109618-cve-2026-109619%EF%BC%89%E9%80%9A%E5%91%8A-2/)

[下一篇文章 绿盟科技顾杜娟博士获评 “2026中国网络安全十大人物”，前沿研发实力获行业认可](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E9%A1%BE%E6%9D%9C%E5%A8%9F%E5%8D%9A%E5%A3%AB%E8%8E%B7%E8%AF%84-2026%E4%B8%AD%E5%9B%BD%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%8D%81%E5%A4%A7%E4%BA%BA/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).