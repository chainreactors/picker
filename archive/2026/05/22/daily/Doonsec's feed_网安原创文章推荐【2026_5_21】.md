---
title: 网安原创文章推荐【2026/5/21】
url: https://mp.weixin.qq.com/s/T3BTKK-0b7J3H83MMlEUJw
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:37:13.536190
---

# 网安原创文章推荐【2026/5/21】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CZMNsicRfJABaFVKA4LbSf0bMPNP9ghV0EDS6hs1C1K0AtlciaauVVlRFHkVfLTsCiaSqiccdQDAtDOxXns7b0siczVoeIkib010dU56bwicyFn8TY/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/5/21】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 2026-05-21 微信公众号精选安全技术文章总览

> 洞见网安 2026-05-21

---

### 0x1 [AICryptoProxy：AI 驱动的 JS 逆向分析渗透测试自动化代理框架](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247487498&idx=1&sn=51e3e0504cabac72ad0d233710fe1ba3&scene=21#wechat_redirect "AICryptoProxy：AI 驱动的 JS 逆向分析渗透测试自动化代理框架")

> 0x八月 2026-05-21 21:13:05

![](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODy2r5aDicarErZJB0gS8Mf1TcxVvT2aIfSK9J3odXP8JQOMlYpdbkLewLicS5hRP2WApoEdY7aqG01RLAuCyZgbibibOACIWHficqn0/640?wx_fmt=jpeg)

AICryptoProxy是一个基于Claude Code和MCP（Mitmproxy Control Protocol）的智能渗透测试框架，旨在通过AI技术自动化前端JavaScript加密逻辑的逆向分析。该框架能够在几十秒内自动搜索脚本、断点追踪并提取加密关键字、Key和算法参数，生成mitmproxy的加解密脚本。AICryptoProxy支持两种模式：直接加解密模式和JSRPC零逆向桥接模式，适用于不同场景的加密分析。框架还提供了一键启动命令，无需手动调试代理脚本，并支持动态Key适配。此外，它构建了从浏览器到服务器的完整加解密链路，使得测试人员可以在Burp Suite中操作明文请求，而服务器端接收到的仍是加密数据包。该工具适用于网络安全学习和研究，但禁止用于非法渗透测试。

AI应用

渗透测试

自动化工具

JavaScript逆向

mitmproxy

网络安全

代码审计

Python开发

---

### 0x2 [邮件钓鱼免杀完全指南（2026 实战版）六、企业级防御体系建设](https://mp.weixin.qq.com/s?__biz=MzkyNTQyMzk0MA==&mid=2247485304&idx=1&sn=0d83f071a9597c8c0d07286cf6f58e87&scene=21#wechat_redirect "邮件钓鱼免杀完全指南（2026 实战版）六、企业级防御体系建设")

> IceByte-Sec 2026-05-21 20:44:53

![](https://mmbiz.qpic.cn/mmbiz_jpg/P8tspoQj3VokH6lk57DUUsXg1JkB104kCcC0iaKsPwApUmR4m9loKpzoDDYwwT3O4E3zu7pziajZwJUt8ENQ1mfIGOEefjLSiauMBQGn2tmPQ4/640?wx_fmt=jpeg)

本文详细分析了企业邮件钓鱼的攻击链和防御体系，涵盖了从 OSINT 信息收集、邮件认证绕过、VHD 武器化到 ClickFix 与 HTML Smuggling 的攻击技术。文章强调了纵深防御的重要性，并提供了 MITRE ATT&CK 钓鱼技术的完整映射。在防御体系建设方面，文章深入探讨了安全邮件网关（SEG）的部署与优化、终端检测与响应（EDR）规则建设、网络层检测（NDR）、身份层防护（IAM/MFA）以及钓鱼模拟平台与安全意识培训。此外，还介绍了 NDR/SIEM 集成与威胁狩猎、事件响应（IR）Playbook以及分层防御体系总览。文章最后指出，企业邮件钓鱼攻防是一个永无止境的博弈过程，防御方需要持续进化以应对攻击者的不断创新。

---

### 0x3 [Cisco 安全工作负载中的关键漏洞威胁企业 API 安全](https://mp.weixin.qq.com/s?__biz=Mzg4ODI5MzAzMw==&mid=2247487068&idx=1&sn=d793a3a6fa32a3cb57c1a32b578c5e5f&scene=21#wechat_redirect "Cisco 安全工作负载中的关键漏洞威胁企业 API 安全")

> 安全圈的那点事儿 2026-05-21 19:29:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7OoXGyicHiaoTV9Pyeoa3dTTia6B0tAk2rEr3ZRHlAVo2VPtWMlhibVVQybzaiawMRoEqeVL6QiabuwmRxdobDUWAZgyoh0Xiaem2YibA0/640?wx_fmt=jpeg)

思科近期披露了一个严重的安全漏洞，编号为 CVE-2026-20223，该漏洞可能使未经身份验证的攻击者获得对敏感企业环境的高级管理访问权限。该漏洞源于内部 REST API 端点的不正确身份验证和验证，攻击者可以通过发送特制的 API 请求来利用此漏洞，从而可能获得站点管理员的权限，并完全控制受影响的环境。该漏洞影响了 Cisco 安全工作负载集群软件，无论是 SaaS 还是本地部署。思科已发布补丁，并强烈建议用户立即升级到修复后的版本。由于漏洞的严重性和缺乏身份验证要求，存在被迅速利用的高风险，组织应采取紧急措施来保护其系统。

CVE-2026-20223

思科安全工作负载

API安全

身份验证漏洞

高级管理访问权限

跨租户影响

补丁管理

SaaS部署

本地部署

安全事件响应

---

### 0x4 [BadIIS恶意软件劫持IIS服务器，将用户重定向到非法网站](https://mp.weixin.qq.com/s?__biz=Mzg4ODI5MzAzMw==&mid=2247487067&idx=1&sn=610abb32d09722c30ac58e051fe299c6&scene=21#wechat_redirect "BadIIS恶意软件劫持IIS服务器，将用户重定向到非法网站")

> 安全圈的那点事儿 2026-05-21 19:20:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7N8V9u26lmzqh24DGLU5ME7xSMic5a9kfhEiaUvWY7mSicMUSWfNdn91s4icsiapefFmOyus96PmQqXIuSiae4ZvvXWVl01AvKgYEOac/640?wx_fmt=jpeg)

BadIIS恶意软件的新变种被发现在劫持微软IIS网络服务器，将用户重定向到非法网站。这种恶意软件由使用别名“lwxat”的开发者维护，并从2021年9月持续至2026年1月。该恶意软件具有结构化和迭代的开发过程，包括快速更新和规避技术。它能够绕过防病毒解决方案，如Norton，并修复可能导致病毒暴露的操作错误。BadIIS主要用于SEO欺诈和网络流量操纵，能够重定向合法用户到恶意网站，充当反向代理，注入垃圾内容，并篡改网站元数据以提高排名。Talos发现，BadIIS是一个通用恶意软件，由多个组织共享或出售。该恶意软件还附带构建工具和辅助工具，用于自动化部署和确保持久性。新版本实现了两阶段安装过程，并在服务器重启后恢复。BadIIS的攻击遍及亚太地区以及欧洲、北美和南非，表明网络服务器恶意软件的产业化趋势。

恶意软件攻击

IIS服务器安全

网络犯罪即服务（MaaS）

SEO欺诈

逆向工程

安全漏洞利用

威胁情报

安全工具技术

---

### 0x5 [运维、安全同行务必转发！ActiveMQ 潜伏13年高危漏洞无认证可入侵](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247490078&idx=1&sn=5e83da18a5b1a5bc8218edfbf09c2536&scene=21#wechat_redirect "运维、安全同行务必转发！ActiveMQ 潜伏13年高危漏洞无认证可入侵")

> POP Star安全 2026-05-21 19:00:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/HJOl681LKxq19gkCIvJicMR2sXFrViaMO5OIibicFXyQRgDqfT34NJjBMbktkhGctUtWblcSO3ib6ykoiaBehicicnyc4lbzNrVVQGpwdLH4H95KMe4/640?wx_fmt=jpeg)

转发提醒你的运维同事，这可能是你的服务器上最安静的“定时炸弹”。

---

### 0x6 [Next.js 服务器端请求伪造漏洞 | CVE-2026-44578复现&研究](https://mp.weixin.qq.com/s?__biz=MzE5ODMzOTgwMg==&mid=2247484622&idx=1&sn=a83a205f7fa1880f07370f03cbb63b96&scene=21#wechat_redirect "Next.js 服务器端请求伪造漏洞 | CVE-2026-44578复现&研究")

> 404号浪漫 2026-05-21 18:10:35

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eefCd8vibaic2BGwN1k9Dxt3TQDiaMcfWZJcGic5RkGvWygg6Cm5iaj1dtW8eGfsUqOOaWJXDOgT3RhaCQzlX0XSKzCVpA3S1bfEOysPI6Jpybaw/640?wx_fmt=jpeg)

该文章详细介绍了 Next.js 服务器中存在的 SSRF（服务器端请求伪造）漏洞（CVE-2026-44578），该漏洞影响了 Next.js 版本 13.4.13 到 15.5.15 和 16.0.0 到 16.2.5。文章首先介绍了漏洞的背景和影响，指出攻击者可以利用该漏洞通过构造特制的 WebSocket 升级请求，迫使 Next.js 服务器向任意内部或外部地址发起请求，从而绕过网络边界防护，实现内网探测、敏感信息窃取以及云环境元数据服务访问等恶意行为。接着，文章提供了漏洞的环境搭建步骤，包括创建漏洞版 Next.js 项目并构建 Docker 镜像，启动容器，并在容器内创建验证 HTTP 服务。文章还详细分析了漏洞的复现步骤和流量特征，并深入探讨了漏洞的原理，指出漏洞源于 Next.js 在处理 WebSocket 升级请求时，未应用与普通 HTTP 请求一致的安全检查策略，导致服务器会代理未经充分验证的外部目标请求。最后，文章给出了修复建议，包括升级到最新版本，以及采取临时防护措施，如限制访问、管理接口业务限制、出站流量限制和流量审查等。

---

### 0x7 [开发者工作站沦陷：史上最高调的IDE扩展供应链攻击深度解析](https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247518853&idx=1&sn=fb5ae035cbd63c76999e90466b739e55&scene=21#wechat_redirect "开发者工作站沦陷：史上最高调的IDE扩展供应链攻击深度解析")

> 奇安信威胁情报中心 2026-05-21 17:47:41

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOqicQyickj7IIHoVBjG1ptHBicgAlJ4Ytm3IQCdsL9mbd8eZtibUKO7KYrh6gazX635ZlwU5xfdqByiaD1Hhl6AmwfT3VHJCtNibMqiaEY/640?wx_fmt=jpeg)

2026年5月，GitHub遭受了一起历史性的供应链攻击，攻击者通过一款名为Nrwl Angular Console的Visual Studio Code扩展植入木马，进而攻陷GitHub员工的工作站，窃取了约3800个私有仓库的源代码。这次攻击揭示了IDE扩展作为攻击向量的重要性，以及开发者工作站在供应链安全中的关键地位。攻击者利用了VS Code扩展的特权权限，通过恶意代码在开发者打开项目时自动执行，进而收集本地凭证和云服务凭证，实现横向移动。该事件涉及威胁组织TeamPCP，其历史攻击记录表明其对开发者工具供应链的持续关注。文章强调了开发者工作站安全的重要性，并提出了加固开发者防线和重新定义供应链安全边界的建议。

供应链攻击

开发者工具安全

Visual Studio Code扩展安全

内部威胁

数据泄露

横向移动

云安全

威胁情报

安全意识

安全策略

---

### 0x8 [AI赋能安全&&一句话进行js逆向&&配合mitmproxy进行简单测试](https://mp.weixin.qq.com/s?__biz=Mzk1NzgzMjkxOQ==&mid=2247490723&idx=1&sn=5c9c5d4290f66307a08b71cf56e76042&scene=21#wechat_redirect "AI赋能安全&&一句话进行js逆向&&配合mitmproxy进行简单测试")

> 陌笙不太懂安全 2026-05-21 17:01:06

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboSMlf0r7wUQM5RFNJTeN1GvGj42Wp7J03g8gPGVV3xEEjJXibTxqpicjBhJZ0ux2kjVjJ8ykXpvvSyiblYVGwOQJwzjhofKxplic1U/640?wx_fmt=jpeg)

本文详细介绍了如何利用AI技术简化前端加密（特别是登录参数加密）的JS逆向流程。文章以一个edusrc登录页面为例，展示了通过自然语言指令让AI自动分析加密参数、生成Python加密脚本以及联动Burp和mitmproxy进行自动化爆破测试的方法。传统JS逆向需要大量时间定位加密逻辑、调试堆栈等，而AI辅助工具可以大幅简化这一过程。文章还介绍了所需的环境配置，包括安装TRAE、Google Chrome浏览器、Node.js、npm以及mitmproxy等工具，并提供了具体的操作步骤和指令示例。通过结合AI能力和代理工具，可以将原本耗时几十分钟的JS逆向工作压缩到几分钟内完成，从而提高测试效率。

---

### 0x9 [[前沿技术] OAuth 2.0 授权码劫持](https://mp.weixin.qq.com/s?__biz=Mzg5NTgzMTgyNQ==&mid=2247484123&idx=2&sn=03f270786557d8b498a44670363e3e40&scene=21#wechat_redirect "[前沿技术] OAuth 2.0 授权码劫持")

> Pik安全实验室 2026-05-21 15:21:13

![](https://mmbiz.qpic.cn/mmbiz_jpg/BasqgWRklkR4k3D9RNvfiagmxTJk7Z5iafV3703iaz6eyed5QOUzSwuI69xW9Ewibsba15GRK5zqmdtia5swn9ib6bq58dIAuzR704ysxpTLY4libQ/640?wx_fmt=jpeg)

本文深入探讨了OAuth 2.0授权框架的安全问题，特别是授权码劫持这一关键攻击面。OAuth 2.0是互联网广泛使用的授权框架，但配置不当可能导致账户劫持。文章首先回顾了OAuth 2.0的Authorization Code Flow流程，然后详细分析了redirect\_uri劫持、CSRF绑定绕过、PKCE缺失以及scope提升等攻击手法。最后，文章提出了修复这些漏洞的建议，包括严格白名单校验redirect\_uri、强制使用state参数、使用PKCE以及最小权限scope。文章强调这些内容仅用于安全研究和学习，并提醒读者非法使用后果自负。

OAuth 2.0 安全

授权码劫持

认证机制

CSRF攻击

网络安全漏洞

防御策略

---

### 0xa [PHP-文件操作类代码审计](https://mp.weixin.qq.com/s?__biz=Mzk1NzcxMTMyOQ==&mid=2247484930&idx=1&sn=3e5ce7fb2f287c9ec8d911a0cb67599d&scene=21#wechat_redirect "PHP-文件操作类代码审计")

> 嵩艺 2026-05-21 13:41:24

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3CSuJ7WYnWaHRPMviaChG0g1BlaCtjibBu2EZB2yOVvGCaP5l9yzvEEXGtlO1pxOv7Moe89mXY9VicOQtGVdxwDwO3Hia0M7OrAGLo1icH1YibjXY/640?wx_fmt=jpeg)

本文主要介绍了网络安全学习者在进行文件类挖掘和脆弱性分析时的思路和方法。文章首先强调了仅供学习和参考，禁止非法活动，并声明不承担违法犯罪责任。接着，文章详细阐述了文件类挖掘的思路，包括查看文件路径、分析代码中的变量（特别是可控变量）以及检查变量前后的过滤机制。此外，文章还指出了文件安全挖掘的关键点，如脚本文件名、应用功能点和操作关键字（如文件上传、下载、包含、删除等）。文章建议结合黑白盒测试方法，从函数入手寻找功能点或从功能点定位对应函数。以emlog\_pro 1day漏洞（CNVD-2023-74536）为例，分析了该漏洞的环境要求、服务器和浏览器推荐，并提出了从搜索$\_FILES和MOVE\_uploaded\_file等关键词寻找突破口的方法。最后，文章以lmxcms1.40版本为例，分析了任意文件删除漏洞，并强调了在学习和实践过程中要注意身体健康。

---

### 0xb [SRC每日漏洞复现学习系列（第6篇）信息泄露漏洞+ 漏洞报告模板](https://mp.weixin.qq.com/s?...