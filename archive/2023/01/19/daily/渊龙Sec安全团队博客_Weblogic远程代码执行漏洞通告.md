---
title: Weblogic远程代码执行漏洞通告
url: https://blog.aabyss.cn/post-171.html
source: 渊龙Sec安全团队博客
date: 2023-01-19
fetch_date: 2025-10-04T04:15:05.106983
---

# Weblogic远程代码执行漏洞通告

# [渊龙Sec安全团队博客](https://blog.aabyss.cn/)

欢迎您访问渊龙Sec团队博客

* [首页](https://blog.aabyss.cn/)
* [安全资讯](https://blog.aabyss.cn/sort/zx)
* [网络安全](https://blog.aabyss.cn/sort/safe)
  + [渗透测试](https://blog.aabyss.cn/sort/5)
  + [漏洞复现](https://blog.aabyss.cn/sort/6)
  + [内网渗透](https://blog.aabyss.cn/sort/7)
  + [逆向破解](https://blog.aabyss.cn/sort/8)
  + [代码审计](https://blog.aabyss.cn/sort/9)
  + [社会工程学](https://blog.aabyss.cn/sort/14)
  + [极客硬件](https://blog.aabyss.cn/sort/16)
  + [CTF](https://blog.aabyss.cn/sort/17)
* [资源分享](https://blog.aabyss.cn/sort/fx)
  + [神兵利器](https://blog.aabyss.cn/sort/10)
  + [编程开发](https://blog.aabyss.cn/sort/program)
  + [网站源码](https://blog.aabyss.cn/sort/12)
  + [学习资料](https://blog.aabyss.cn/sort/13)
  + [故障排查](https://blog.aabyss.cn/sort/15)
* [黑科技](https://blog.aabyss.cn/sort/hkj)
* [登录](https://blog.aabyss.cn/admin)

* [推荐:团队官方靶场](http://ctf.aabyss.cn)
* [团队Github](https://github.com/Aabyss-Team/)
* [团队官网](https://www.aabyss.cn)
* [团队在线导航](https://dh.aabyss.cn)
* [AabyssZG](https://blog.zgsec.cn)
* [关注团队](https://dh.aabyss.cn)
  + [哔哩哔哩](https://space.bilibili.com/122627170)
  + [公开QQ群](https://jq.qq.com/?_wv=1027&k=xn0WTok1)
  + [Github项目](https://github.com/Aabyss-Team/)
  + [RSS订阅](http://blog.aabyss.cn/rss.php)

* [主页](https://blog.aabyss.cn/)
* [安全情报](https://blog.aabyss.cn/sort/zx)
* Weblogic远程代码执行漏洞通告

# Weblogic远程代码执行漏洞通告

日期：2023-1-18
 [渊龙Sec团队](https://blog.aabyss.cn/author/1 "为国之安全而奋斗，为信息安全而发声！ admin@aabyss.cn")
 [安全情报](https://blog.aabyss.cn/sort/zx)
 浏览：2241次
 评论：0条

**1# 漏洞概述**
WebLogic是美国Oracle公司出品的一个application server，是一个基于JAVAEE架构的中间件，WebLogic是用于开发、集成、部署和管理大型分布式Web应用、网络应用和数据库应用的Java应用服务器。
![](https://s2.loli.net/2023/01/18/6lXQDVy53vPfwMr.jpg)
WebLogic 存在远程代码执行漏洞，允许未经身份验证的攻击者通过IIOP协议网络访问并破坏易受攻击的WebLogic Server，成功的漏洞利用可导致WebLogic Server被攻击者接管，从而造成远程代码执行。

**2# 影响版本**

* Weblogic 12.2.1.3.0
* Weblogic 12.2.1.4.0
* Weblogic 14.1.1.0.0

**3# 漏洞细节**
CVE编号：CVE-2023-21839
漏洞类型：远程代码执行漏洞
漏洞级别：高危
利用条件：符合漏洞版本即可利用
交互要求：1 Click
Poc：已公开
在野利用：未发现

**4# 漏洞修复**
官方目前未放出补丁，请密切关注官方信息：
<https://www.oracle.com/security-alerts/cpujan2023.html>

**5# 参考资料**
<https://www.oracle.com/security-alerts/cpujan2023.html>

本博客所有文章如无特别注明均为原创。作者：[渊龙Sec团队](https://blog.aabyss.cn/author/1 "为国之安全而奋斗，为信息安全而发声！ admin@aabyss.cn") ，复制或转载请以超链接形式注明转自 [渊龙Sec安全团队博客](/) 。
原文地址《Weblogic远程代码执行漏洞通告》

分享到：更多

### 相关推荐

* [WannaRen勒索病毒作者主动提供解密密钥](https://blog.aabyss.cn/post-71.html)
* [Windows Active Directory域服务权限提升漏洞](https://blog.aabyss.cn/post-149.html)
* [最新变种勒索病毒紧急通告](https://blog.aabyss.cn/post-67.html)
* [圆通内鬼泄露40万条个人信息](https://blog.aabyss.cn/post-99.html)
* [SonarQube漏洞导致大量源码泄露](https://blog.aabyss.cn/post-143.html)
* [军工级“武器库”Immunity Canvas 7.26 泄露事件](https://blog.aabyss.cn/post-115.html)

### 取消回复发表评论

![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/1.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/5.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/6.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/7.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/9.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/10.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/11.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/13.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/14.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/16.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/19.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/21.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/24.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/25.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/26.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/27.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/28.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/29.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/30.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/31.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/33.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/39.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/40.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/43.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/44.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/45.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/47.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/48.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/49.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/50.png)

### 网友评论**（0）**

### AD

### 分类

* [安全资讯](http://blog.aabyss.cn/sort/zx "4 篇文章")
* [网络安全](http://blog.aabyss.cn/sort/safe "12 篇文章")
* [资源分享](http://blog.aabyss.cn/sort/fx "4 篇文章")
* [黑科技](http://blog.aabyss.cn/sort/hkj "9 篇文章")

Powered by [emlog](http://www.emlog.net "骄傲的采用emlog系统")
© 大前端优化版 By [渊龙Sec安全团队](http://www.aabyss.cn "渊龙Sec团队官网") [浙ICP备20003630号-2](https://beian.miit.gov.cn/)