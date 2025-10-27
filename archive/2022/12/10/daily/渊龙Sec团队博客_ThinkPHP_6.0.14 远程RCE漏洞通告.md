---
title: ThinkPHP<6.0.14 远程RCE漏洞通告
url: https://blog.aabyss.cn/post-168.html
source: 渊龙Sec团队博客
date: 2022-12-10
fetch_date: 2025-10-04T01:03:37.509165
---

# ThinkPHP<6.0.14 远程RCE漏洞通告

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
* ThinkPHP<6.0.14 远程RCE漏洞通告

# ThinkPHP<6.0.14 远程RCE漏洞通告

日期：2022-12-9
 [渊龙Sec团队](https://blog.aabyss.cn/author/1 "为国之安全而奋斗，为信息安全而发声！ admin@aabyss.cn")
 [安全情报](https://blog.aabyss.cn/sort/zx)
 浏览：3244次
 评论：0条

**1# 漏洞概述**
最近，ThinkPHP爆出高危漏洞，攻击者可以通过此漏洞实现任意命令执行，导致系统被攻击与控制。
![](https://s2.loli.net/2022/12/09/KMAae5rfQbIutnV.jpg)
注意，该漏洞已在9月25日的V6.0.14被修复。

**2# 影响版本**

* v6.0.0<=ThinkPHP<=v6.0.13
* v5.0.0<=ThinkPHP<=5.0.12
* v5.1.0<=ThinkPHP<=5.1.8

**3# 漏洞细节**
CVE编号：暂无
漏洞类型：任意命令执行
漏洞级别：高危
利用条件：无权限要求
交互要求：0 Click
Poc：公开
在野利用：已发现

**4# 漏洞修复**
获取官网V6.0.14的补丁包，进行升级即可。
<https://github.com/top-think/framework/releases/tag/v6.0.14>

相关链接：

* <https://tttang.com/archive/1865/>
* <https://mp.weixin.qq.com/s?__biz=MzkxMDMxNTQ3Mg==&mid=2247483831&idx=1&sn=825e82d50f4a2951fb37b472ebd2fab5&chksm=c12c1b08f65b921e0473947d94192148bb6d5ee66c6f8e052ba21d7caa5ce87b10705004fce0&mpshare=1&scene=23&srcid=1209z5Wb1p8DwqMFoT6jXoFe&sharer_sharetime=1670601195066&sharer_shareid=cf332a841f650084d7e74d4ebc15b610#rd>

本博客所有文章如无特别注明均为原创。作者：[渊龙Sec团队](https://blog.aabyss.cn/author/1 "为国之安全而奋斗，为信息安全而发声！ admin@aabyss.cn") ，复制或转载请以超链接形式注明转自 [渊龙Sec安全团队博客](/) 。
原文地址《ThinkPHP<6.0.14 远程RCE漏洞通告》

分享到：更多

### 相关推荐

* [Immunity Canvas 7.26工具包存在RCE漏洞](https://blog.aabyss.cn/post-116.html)
* [Linux sudo权限提升漏洞（CVE-2021-3156）通告](https://blog.aabyss.cn/post-112.html)
* [中国交通银行信息泄露事件：官方回复称为虚假数据](https://blog.aabyss.cn/post-105.html)
* [国家网信办：下架滴滴出行App](https://blog.aabyss.cn/post-134.html)
* [美国火眼公司遭APT攻击，红队工具遭窃取泄露](https://blog.aabyss.cn/post-102.html)
* [最新：“免费” IDA Pro 安装包里放后门！！！](https://blog.aabyss.cn/post-141.html)

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