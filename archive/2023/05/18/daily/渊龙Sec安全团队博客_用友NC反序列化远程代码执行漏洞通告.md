---
title: 用友NC反序列化远程代码执行漏洞通告
url: https://blog.aabyss.cn/post-174.html
source: 渊龙Sec安全团队博客
date: 2023-05-18
fetch_date: 2025-10-04T11:39:11.966520
---

# 用友NC反序列化远程代码执行漏洞通告

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
* 用友NC反序列化远程代码执行漏洞通告

# 用友NC反序列化远程代码执行漏洞通告

日期：2023-5-17
 [渊龙Sec团队](https://blog.aabyss.cn/author/1 "为国之安全而奋斗，为信息安全而发声！ admin@aabyss.cn")
 [安全情报](https://blog.aabyss.cn/sort/zx)
 浏览：4658次
 评论：0条

**1# 漏洞概述**
用友 NC 是一款企业级 ERP 软件。提供了一系列的业务管理模块，包括财务会计、采购管理、销售管理、物料管理、生产计划、人力资源管理等，可以帮助企业实现信息化管理和数字化转型。
![](https://s2.loli.net/2023/05/17/Sr83Xbqfm2vsgRA.jpg)
2023 年 5 月 16 日 ， 团队情报部门和师傅发现出现用友NC相关服务出现失陷情况，紧急分析后猜测可能出现相关0Day漏洞。
![](https://s2.loli.net/2023/05/17/XRnvJa2qpIwst14.jpg)
2023 年 5 月 17 日，微步情报中心公布相关信息，获取到用友 NC 反序列化远程代码执行漏洞情报(0day)，攻击者可以通过该漏洞执行任意代码，导致系统被攻击与控制。

**2# 影响版本**

* 用友NC 版本 <= 6.5 均受影响

**3# 漏洞细节**
CVE编号：暂无
漏洞类型：反序列化远程代码执行漏洞
漏洞级别：高危
利用条件：无权限要求
交互要求：0 Click
Poc：未公开
在野利用：已发现

**4# 漏洞修复**
**4.1官方修复措施：**
官方已发布修复方案，受影响的用户建议联系用友官方获取安全补丁
<https://hc.yonyou.com/services/index.html>
<https://security.yonyou.com/#/patchList>

**4.2临时处置和应对措施：**
非必要不建议将该系统暴露在公网

**5# 参考资料**

* <https://x.threatbook.com/v5/article?threatInfoID=45579>
* <https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247498616&idx=1&sn=a241601f80501336487dce33281bf474&chksm=fe79dfe0c90e56f6f76be0e05b8880fbdd92f5a0e00f1b279c676f4b454e6d7bafaeec7784d4&mpshare=1&scene=23&srcid=0519aZPcOKUyN1kmog4NUR6E&sharer_sharetime=1684461202637&sharer_shareid=cf332a841f650084d7e74d4ebc15b610#rd>

本博客所有文章如无特别注明均为原创。作者：[渊龙Sec团队](https://blog.aabyss.cn/author/1 "为国之安全而奋斗，为信息安全而发声！ admin@aabyss.cn") ，复制或转载请以超链接形式注明转自 [渊龙Sec安全团队博客](/) 。
原文地址《用友NC反序列化远程代码执行漏洞通告》

分享到：更多

标签: [0day](https://blog.aabyss.cn/tag/0day) [漏洞](https://blog.aabyss.cn/tag/%E6%BC%8F%E6%B4%9E) [实时资讯](https://blog.aabyss.cn/tag/%E5%AE%9E%E6%97%B6%E8%B5%84%E8%AE%AF)

### 相关推荐

* [Log4j 再爆漏洞（CVE-2021-45046）](https://blog.aabyss.cn/post-148.html)
* [CISCO SD-WAN高危漏洞](https://blog.aabyss.cn/post-88.html)
* [净网大师(ADSafe)暗藏恶意代码，从众多网站劫持流量](https://blog.aabyss.cn/post-7.html)
* [2021年的6种网络安全趋势](https://blog.aabyss.cn/post-124.html)
* [锐捷 RG-UAC 信息泄露漏洞(CNVD-2021-14536)](https://blog.aabyss.cn/post-117.html)
* [披露美国中央情报局CIA攻击组织（APT-C-39）对中国关键领域长达十一年的网络渗透攻击](https://blog.aabyss.cn/post-38.html)

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