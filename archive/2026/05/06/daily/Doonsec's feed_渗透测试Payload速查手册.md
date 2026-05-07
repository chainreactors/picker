---
title: 渗透测试Payload速查手册
url: https://mp.weixin.qq.com/s/cj091LxuiMmWzGosxKTNVw
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:26:06.462913
---

# 渗透测试Payload速查手册

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVk6TJYQnRzp1V0gc1TcKxyg67TblfTePDnSe5sgIcgXd237kicoiatTyPib0KEWFAgFJrE3sCp5H81eLk8nDcah8NoxGQCAFab0GE/0?wx_fmt=jpeg)

# 渗透测试Payload速查手册

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 729，阅读大约需 4 分钟

## 前言

**一站式收集所有渗透测试场景的 Payload（攻击载荷）、绕过技巧、利用方法、工具和速查手册**，覆盖绝大多数主流漏洞与攻防场景。

* • 核心用途：**渗透测试、漏洞利用、绕过检测、红队行动、CTF 解题**

项目地址：https://github.com/swisskyrepo/PayloadsAllTheThings
![610c6533ce4870948d6b93dee110316a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmNiaHvvbfCdErMWdlrJQXmq0aIHJ4KXlzUl78oaEYYuCSe67rwo3MPB5ZiaYH4zrTJUoCA4V4sM2rg6HuXsib1aicovx3uHvlCqxw/640?from=appmsg "null")

610c6533ce4870948d6b93dee110316a.png

在线地址：https://swisskyrepo.github.io/PayloadsAllTheThings

![9fc1d86af780795e5d829071d0e08ccb.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkIJuul2MspNcCVQkSWJpGwp2El1wqD9YEjDpWPhSp6TiaM3mLZ8z4w7DJELsPLNHR97ngDuYlO2p4MwibdWibH3YVwrFwJiaWqzoY/640?from=appmsg "null")

9fc1d86af780795e5d829071d0e08ccb.png

## 主要内容

项目按**漏洞类型、攻击场景、服务/协议、绕过技巧**分类，结构清晰，以下是最核心的模块：

### 1. 主流 Web 漏洞 Payload 大全

覆盖 OWASP Top 10 所有核心漏洞，提供**现成可复制的攻击载荷**：

* • **XSS 跨站脚本**：反射型/存储型/DOM XSS、过滤绕过、无回显 XSS、各类浏览器绕过规则
* • **SQL 注入**：MySQL/MSSQL/PostgreSQL/Oracle 注入、盲注、报错注入、WAF 绕过、万能密码
* • **命令注入**：Linux/Windows 命令执行、分隔符绕过、过滤绕过（空格/关键字/特殊字符）
* • **文件上传漏洞**：WebShell 上传、后缀绕过、MIME 绕过、.htaccess/.user.ini 绕过
* • **目录遍历**：路径穿越 Payload、Windows/Linux 绝对路径读取
* • **SSRF 服务端请求伪造**：内网探测、协议绕过、端口扫描、云服务利用
* • **CSRF 跨站请求伪造**：POC 模板、绕过 Referer 技巧
* • **SSTI 模板注入**：Jinjava2/Twig/FreeMarker 等各类模板引擎利用
* • **XXE 外部实体注入**：XML 外部实体利用、无回显 XXE
* • **NoSQL 注入**：MongoDB 等非关系型数据库注入

### 2. 认证/权限绕过与登录破解

* • 弱口令字典、默认凭据大全
* • JWT 漏洞利用（伪造、未验证、密钥破解）
* • OAuth 2.0 / SAML 绕过技巧
* • 401/403 权限绕过（HTTP 头绕过、路径绕过）
* • Windows/Linux 权限提升（PrivEsc）速查手册

### 3. 服务/协议/中间件漏洞利用

针对常见服务器、数据库、中间件的渗透方法：

* • Apache/Nginx/IIS 漏洞与配置错误利用
* • Tomcat/JBoss/WebLogic 等中间件漏洞
* • Redis/Memcached/MySQL 未授权访问、RCE
* • SMB/RDP/SSH/FTP 爆破与利用
* • Docker/K8s 容器逃逸、权限滥用

### 4. WAF/防护绕过技巧（核心亮点）

专门针对**防火墙、入侵检测、安全防护**的绕过方案：

* • SQLi/XSS/命令注入 WAF 绕过
* • 字符编码、大小写混淆、注释插入绕过
* • HTTP 分割、请求走私绕过防护
* • 云 WAF（阿里云、腾讯云、Cloudflare）通用绕过思路

### 5. 红队行动（Red Team）专用资源

面向企业实战攻防的高级技巧：

* • 内网渗透：横向移动、凭证窃取、端口转发
* • 钓鱼攻击：宏病毒、Office 漏洞利用
* • 免杀技巧：Payload 编码、混淆
* • Windows/Linux 持久化驻留方法

### 6. CTF 竞赛专用速查

* • 各类题型快速解题 Payload
* • 隐写术、密码学速查表
* • 逆向/杂项常用工具与命令

### 7. 通用工具与速查手册

* • 渗透测试常用命令（Linux/Windows）
* • 反弹 Shell 大全（TCP/UDP/PHP/Java/Python 全语言）
* • 编码/解码工具（Base64、URL、Hex 等）
* • 信息收集、指纹识别脚本

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a1BOUvqnbriaKQaulUawUmcqevsicgRXaDWWcgmsbG7iaTtKE89ZwJEkPHzibEzXwcibLn8PKu1hGoicqAEIW9uQjyBw/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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