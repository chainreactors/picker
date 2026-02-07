---
title: 幽灵文件夹 目录影子攻击劫持WordPress搜索引擎优化
url: https://www.anquanke.com/post/id/314773
source: 安全客-有思想的安全新媒体
date: 2026-02-06
fetch_date: 2026-02-07T04:07:54.250928
---

# 幽灵文件夹 目录影子攻击劫持WordPress搜索引擎优化

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 幽灵文件夹 目录影子攻击劫持WordPress搜索引擎优化

阅读量**17523**

发布时间 : 2026-02-06 11:09:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/ghost-folders-directory-shadowing-hack-hijacks-wordpress-seo/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款新型隐秘恶意软件攻击活动正针对 WordPress 网站展开攻击，在网站管理员毫不知情的情况下，将受信任的网页变成网络博彩广告的展示板。Sucuri 公司的安全分析师普佳・斯里瓦斯塔瓦详细披露了这种名为**目录影子**的复杂攻击手法，攻击者通过在服务器上创建实体文件夹，劫持网站的合法网址。

该攻击的阴险之处在于，普通访客和管理员均无法发现异常。报告指出：“谷歌搜索结果中显示的不再是网页原本的标题和描述，而是赌场、博彩相关内容”，但网站管理员自行查看时，页面显示却一切正常。

此次攻击的核心，利用了**网页服务器的文件优先级规则**。攻击者会创建与 WordPress 网站现有固定链接完全匹配的实体目录 —— 例如创建一个真实的 /about-us/ 文件夹，以此劫持[example.com/about-us/](https://example.com/about-us/)这个虚拟网址。

由于 Apache、Nginx 这类服务器会优先加载实体文件，最终展示的将是攻击者植入的内容，而非原本的 WordPress 网页。斯里瓦斯塔瓦解释道：“此次攻击的全新点就在于目录影子的利用…… 攻击者借此可以完全劫持特定网页，且无需修改 WordPress 的实际配置”。

研究人员在这些隐藏文件夹中发现了三个文件：

* index.php：攻击的核心控制脚本
* indexx.php：网页原始内容的干净副本，用于展示给普通访客
* readme.txt：包含恶意垃圾广告内容的文件

这款恶意软件内置了识别搜索引擎爬虫的专属逻辑，会通过检查请求的用户代理字符串中是否包含 Googlebot 等关键词，决定向请求方展示何种内容。

报告指出：“当检测到请求来自谷歌相关的用户代理时，恶意软件会加载 readme.txt 文件中的内容，并直接输出到浏览器中”。

这份 readme.txt 文件本身也极具欺骗性，内含 600 多行 HTML 代码，被打造成高权重电商网站的样式，**盗用了 Etsy 平台的层叠样式表和元数据**，让自动化检测系统认为其是合法页面。这一手段成功欺骗谷歌搜索引擎，将该页面判定为印尼博彩网站的高评分商品列表并纳入索引。

要清除该恶意程序，管理员需跳出 WordPress 后台进行排查，修复步骤为**删除与网站固定链接镜像的恶意实体目录**。

斯里瓦斯塔瓦建议网站管理员提高警惕：“在服务器中发现这类垃圾广告内容需立即引起重视…… 此次攻击最明显的特征，就是服务器中出现了与 WordPress 网页固定链接同名的目录”。完成清理后，向搜索引擎提交重新索引申请是恢复网站信誉的关键步骤。

本文翻译自securityonline [原文链接](https://securityonline.info/ghost-folders-directory-shadowing-hack-hijacks-wordpress-seo/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314773](/post/id/314773)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/ghost-folders-directory-shadowing-hack-hijacks-wordpress-seo/)

如若转载,请注明出处： <https://securityonline.info/ghost-folders-directory-shadowing-hack-hijacks-wordpress-seo/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1010**

* 粉丝
* **6**

### TA的文章

* ##### [网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令](/post/id/314749)

  2026-02-06 11:13:00
* ##### [黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷](/post/id/314748)

  2026-02-06 11:12:32
* ##### [ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证](/post/id/314757)

  2026-02-06 11:12:01
* ##### [印度最高法院就WhatsApp数据共享作出里程碑式隐私裁决 判定其行为违规](/post/id/314774)

  2026-02-06 11:11:35
* ##### [PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵](/post/id/314778)

  2026-02-06 11:11:11

### 相关文章

* ##### [网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令](/post/id/314749)

  2026-02-06 11:13:00
* ##### [黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷](/post/id/314748)

  2026-02-06 11:12:32
* ##### [ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证](/post/id/314757)

  2026-02-06 11:12:01
* ##### [印度最高法院就WhatsApp数据共享作出里程碑式隐私裁决 判定其行为违规](/post/id/314774)

  2026-02-06 11:11:35
* ##### [PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵](/post/id/314778)

  2026-02-06 11:11:11
* ##### [Xcode 26.3落地macOS苹果正式引入智能体式AI编码功能](/post/id/314784)

  2026-02-06 11:10:45
* ##### [RapidFort完成4200万美元A轮融资 深耕自动化漏洞修复领域](/post/id/314788)

  2026-02-06 11:10:18

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)