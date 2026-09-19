---
title: 渗透测试信息打点初步总结
url: https://mp.weixin.qq.com/s/jpQhGqhDA3P7ZwLu7MVXnw
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:55:00.176343
---

# 渗透测试信息打点初步总结

# 渗透测试信息打点初步总结

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**“** 简单罗列工具和思路**，请在合法且被授权情况下进行”**

01

—

信息打点分类与内容

1. Web架构信息收集

* 操作系统：Windows / Linux

* 开发语言：ASP/ASPX、PHP、JAVA、Python、JavaScript

* 中间件容器：IIS、Apache、Nginx、Tomcat、WebLogic、WildFly（JBoss AS）

* 数据库类型：MySQL、MSSQL、Oracle、Access、DB2、Sybase、Redis、MongoDB

* 第三方软件：phpMyAdmin、vsftpd、VNC、ELK、OpenSSH

* 源码类型：

+ CMS开源（如WordPress、Discuz）

+ 闭源售卖（内部工具或加密源码）

+ 自主研发（如淘宝、京东）

2. 系统与网络信息收集

* 服务厂商：阿里云、腾讯云等云服务商或自建机房

* 网络架构：外网服务器、内网映射、反向代理

* 服务信息：FTP、SSH、SMTP、POP、Redis等协议与服务

* 阻碍信息：CDN、WAF、负载均衡、防火墙

3. APP/小程序信息收集

* 外在抓包：HTTP/HTTPS协议抓包（如FD、Burp、Charles）

* 内在提取：反编译APK/IPA，提取代码与资源（如AppInfoScanner、安卓修改大师）

* 加固处理：使用Xposed、Frida绕过加固与证书检测

* 小程序测试：通过微信端抓包分析

4. 资产泄漏与源码获取

* CMS识别：云悉、Glass、Fofa等平台

* 备份文件：目录扫描发现.zip、.tar、.bak等

* 版本控制泄露：Git、SVN、Hg、CVS、Bzr

* 配置文件泄露：

+ composer.json（PHP）

+ WEB-INF/web.xml（Java）

+ .DS\_Store（Mac）

+ .swp（Vim）

* GitHub监控：关键字搜索、语法监控

5. CDN绕过技术

* 子域名查询：未加速子域名可能直连真实IP

* 国外请求：利用CDN区域限制

* 邮件服务：通过找回密码等邮件获取真实IP

* 漏洞利用：SSRF、XSS、命令执行等让服务器主动连接

* 全网扫描：Zmap、Censys、Fofa等搜索历史IP或证书

* HOSTS绑定：获取真实IP后本地绑定绕过CDN

6. 红队工具与自动化平台

* 网络空间引擎：FOFA、Quake、Shodan、ZoomEye

* 自动化工具：

+ ARL灯塔（资产侦察灯塔）

+ Suize水泽（信息收集与热点发现）

+ Kunyu（坤舆，集成ZoomEye与S18G）

* 单点功能工具：

+ 子域名扫描：OneForAll

+ 指纹识别：Glass、Finger

+ 企业信息：企查查、Enscan

02

—

信息打点步骤

阶段一：基础信息收集

* 域名与子域名

+ 查询主域名、相似域名、子域名

+ 工具：FOFA、OneForAll、子域名爆破工具

* CMS识别与源码获取

+ 使用云悉、Glass识别CMS

+ 搜索源码：GitHub、GitLab、备份文件、版本控制泄露

* 开发语言与中间件

+ 抓包分析文件后缀、响应头

+ 工具：浏览器开发者工具、Burp Suite

阶段二：系统与网络探测

* 端口扫描

+ 工具：Nmap、Masscan

+ 目标：常见端口（21, 22, 80, 443, 3306, 6379等）

* CDN与WAF识别

+ 超级Ping工具多地测试

+ WAF识别：响应头、错误页面特征

* 真实IP获取

+ 子域名、邮件、国外请求、漏洞利用、全网扫描

阶段三：应用与资产深入

* APP/小程序分析

+ 抓包：FD、Burp、Charles

+ 反编译：AppInfoScanner、Jadx、IDA Pro

+ 脱壳：Xposed、Frida

* 资产关联与扩展

+ C段扫描、旁注查询

+ 企业信息查询：企查查、Enscan

* GitHub监控与关键词搜索

+ 设置监控任务，使用ARL灯塔或自建脚本

阶段四：自动化整合与报告

* 使用ARL灯塔、Suize水泽、Kunyu进行自动化收集

* 整合子域名、端口、服务、漏洞POC等信息

* 输出资产清单、风险点、攻击路径图

03

—

工具清单与适用范围

| 工具名称 | 类型 | 适用范围 | 备注 |
| --- | --- | --- | --- |
| **Nmap** | 端口扫描 | 所有系统 | 支持OS识别、服务版本探测 |
| **Masscan** | 端口扫描 | 所有系统 | 速度快，适合大范围扫描 |
| **FOFA** | 网络空间引擎 | Web资产 | 支持语法搜索IP、域名、中间件等 |
| **Quake** | 网络空间引擎 | 全网资产 | 360出品，类似FOFA |
| **Shodan** | 网络空间引擎 | 设备与服务 | 侧重IoT与服务器 |
| **ZoomEye** | 网络空间引擎 | 全网资产 | 知道创宇出品 |
| **ARL灯塔** | 自动化收集 | Web资产 | 支持子域名、端口、POC检测 |
| **Suize水泽** | 自动化收集 | 多源整合 | 支持子域名、IP、服务识别 |
| **Kunyu** | 自动化收集 | 集成ZoomEye | 支持漏洞检测 |
| **AppInfoScanner** | APP反编译 | Android/iOS | 提取URL、IP、关键词 |
| **安卓修改大师** | APP修改与反编译 | Android | 支持真机调试、代码修改 |
| **Xposed** | 框架绕过 | Android | 绕过证书锁定、防调试 |
| **Frida** | 动态插桩 | Android/iOS | 脱壳、Hook、调试 |
| **GitHack** | Git泄露利用 | 所有Web | Python脚本，下载.git内容 |
| **SVNHack** | SVN泄露利用 | 所有Web | 类似GitHack |
| **OneForAll** | 子域名扫描 | 所有域名 | 多接口聚合 |
| **Glass** | 指纹识别 | Web应用 | 支持CMS、中间件识别 |
| **Zmap** | 全网扫描 | 所有IP | 快速全网扫描 |
| **Censys** | 证书与IP搜索 | 全网资产 | 用于CDN绕过 |

04

—

信息打点总体思路

* 由外到内：从域名、IP、子域名开始，逐步深入至系统、服务、应用。
* 由浅入深：从公开信息（GitHub、引擎）到隐蔽信息（备份、泄露文件）。
* 多维度交叉验证：结合手工与工具、内外资产、多个引擎结果。
* 持续监控：利用Git监控、资产平台更新、漏洞情报。
* 合法合规：所有操作应在授权范围内，避免对系统造成影响。

  内容转自说说别的，侵删

![](https://mmbiz.qpic.cn/mmbiz_png/INa3lxHH4I2aV3zCmfiaj4cXeQ2HQd6s53wJS36HYI65ib48fujDK8najfWiahicsljzsdT3dfVS8HHyxaviaSd8g2g/640?wxfrom=5&wx_lazy=1&wx_fmt=png&wx_co=1)

**今日福利**

为了帮助大家早日习得网络安全核心知识，快速入行网络安全圈，给大家整理了一套***【2026最新网安资料】***网络安全工程师必备技能资料包（文末一键领取），内容有多详实丰富看下图！

Web安全👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFBODrmsTGnPTOibdIT9B5eFLTHVIgWzYafxGAesmYnfzrz52xwV3Bjhw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

渗透测试👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFVKWl2cLRTq7x9haKJerUZNO0YMhiaO8ibN1jjV0qxNLEvRKMfR90eNjQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

安全面试题👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFgrmaDLaYT1yV5lst9tKC72QrYjd5I8IN7kcOZIZSfQJJz8MdX6a1uA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

代码审计👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFxmUkTNP1iagssZL5zkjID8hibpZsRCj1OnEb4x7ZYWqpiaymSjc8O7vSQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

红队笔记👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFVZS1mB4MKAo4FoMBGyVSzq38ZXEKJCjZVaTsFtLE7tIJ3zbRWF5xeA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

入门视频👇

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgxtiaXGtk7loXV41e8AXiaORJMhqFbrtcfHvJWTia6ME2oSI9msVYJu79uCicb7foufuibEHaVg32XnWw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

以上所有资料获取请扫码

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56GWlFpAuJBpDq9xgZp8de9R91BMgAgGaf5D4gwsyWl1FR9RN64BiaJqzxqDicCAgoKtwb9LPrZm4c15qTds6Ux29Cda2avFL0mY/640?wx_fmt=png&from=appmsg)

识别上方二维码

备注：***2026安全合集***

100%免费领取

（是扫码领取，不是在公众号后台回复，别看错了哦）

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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