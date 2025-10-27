---
title: CentOS-WebPanel存在远程RCE漏洞通告
url: https://blog.aabyss.cn/post-169.html
source: 渊龙Sec团队博客
date: 2023-01-08
fetch_date: 2025-10-04T03:18:02.059319
---

# CentOS-WebPanel存在远程RCE漏洞通告

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
* CentOS-WebPanel存在远程RCE漏洞通告

# CentOS-WebPanel存在远程RCE漏洞通告

日期：2023-1-7
 [渊龙Sec团队](https://blog.aabyss.cn/author/1 "为国之安全而奋斗，为信息安全而发声！ admin@aabyss.cn")
 [安全情报](https://blog.aabyss.cn/sort/zx)
 浏览：2109次
 评论：0条

**1# 漏洞概述**
Control Web Panel存在一个远程命令执行漏洞，该漏洞是由于对特殊元素转义处理不恰当，允许未经身份验证的攻击者通过构造特制的请求来实现远程命令执行，进而获取服务器权限。
![](https://s2.loli.net/2023/01/07/a8HgtZnqiw1XUcR.png)
Control Web Panel官方已经发布安全更新，修复了Control Web Panel远程命令执行漏洞(CVE-2022-44877)。该漏洞允许未经身份验证的攻击者通过构造特制的请求来实现远程命令执行，进而获取服务器权限。

**2# 影响版本**
Control Web Panel 7 < v0.9.8.1147

**3# 漏洞细节**
CVE编号：CVE-2022-44877
漏洞类型：任意命令执行
漏洞级别：高危
利用条件：无权限要求
交互要求：0 Click
Poc：已公开
在野利用：已发现

**4# 漏洞修复**

目前官方已发布安全版本修复上述漏洞，建议受影响的用户升级至安全版本。

下载链接：<https://control-webpanel.com/installation-instructions>

**5# 参考资料**

* <https://github.com/numanturle/CVE-2022-44877>
* <https://nvd.nist.gov/vuln/detail/CVE-2022-44877>

本博客所有文章如无特别注明均为原创。作者：[渊龙Sec团队](https://blog.aabyss.cn/author/1 "为国之安全而奋斗，为信息安全而发声！ admin@aabyss.cn") ，复制或转载请以超链接形式注明转自 [渊龙Sec安全团队博客](/) 。
原文地址《CentOS-WebPanel存在远程RCE漏洞通告》

分享到：更多

### 相关推荐

* [Cisco Talos团队披露Microsoft Azure Sphere多个安全漏洞](https://blog.aabyss.cn/post-87.html)
* [Immunity Canvas 7.26工具包存在RCE漏洞](https://blog.aabyss.cn/post-116.html)
* [Win11高危漏洞被公开](https://blog.aabyss.cn/post-145.html)
* [突发！Spring RCE 0day高危漏洞预警](https://blog.aabyss.cn/post-163.html)
* [Fofa无法访问-透过现象看本质（附赠邀请码）](https://blog.aabyss.cn/post-154.html)
* [Linux sudo权限提升漏洞（CVE-2021-3156）通告](https://blog.aabyss.cn/post-112.html)

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