---
title: 上千个Docker hub镜像泄露认证密钥和私钥
url: https://www.4hou.com/posts/BXOQ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-27
fetch_date: 2025-10-04T11:51:03.038308
---

# 上千个Docker hub镜像泄露认证密钥和私钥

上千个Docker hub镜像泄露认证密钥和私钥 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 上千个Docker hub镜像泄露认证密钥和私钥

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-07-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)326744

收藏

导语：​上千个Docker hub镜像泄露认证密钥和私钥。

上千个Docker hub镜像泄露认证密钥和私钥。

Docker Hub 是Docker社区的基于云的仓库，用于保存、分享和分发Docker镜像。这些容器创建的模板中包含在Docker中部署应用所有必要的软件代码、运行状态、库和环境变量、配置文件。

**镜像密钥泄露**

近日，德国亚琛工业大学(RWTH-Aachen University)研究人员发现上千个Docker Hub上的镜像暴露了机密密钥、软件、在线平台和用户。研究人员分析了Docker Hub中337171个镜像，聚集了1647300层的数据集，发现有8.5%的镜像（28621个Docker镜像）中包含敏感数据，包括52107个有效的私有密钥、3158个不同API秘密信息。

注：以上数据不包括测试密钥、示例API秘密和无效的匹配

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689568947198732.png "1689568819192460.png")

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689568949153224.png "1689568854190763.png")

暴露的密钥中95%是私钥，90%是API秘密，表明这可能是无意间泄露的。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689568950379951.png "1689568906563288.png")

受影响最大的是Docker Hub，秘密暴露的是9.0%，来自私有注册的进行暴露了6.3%的秘密。这一差异表明Docker hub用户对容器安全的理解不如搭建私有仓库的用户。

**泄露密钥的使用**

然后，研究人员利用泄露的密钥可以进行下一步攻击活动。研究人员根据暴露的私钥发现了22082个被入侵的证书，其中包括7546个私有CA签发的证书和1060个公有CA签发的证书。而这些CA签发的证书被大量用户使用，并且被广泛接受。截止论文发布，仍有141个CA签名的证书状态是有效的。

为进一步确定暴露的密钥的影响，研究人员通过Censys数据库分析发现有275269个主机使用这些被入侵的密钥。包括：

可能传输隐私敏感物联网数据的8,674 MQTT和 19 AMQP主机；

保存机密数据的6,672 FTP、426 PostgreSQL、3 Elasticsearch,和3 MySQL实例；

216台用户电信服务的SIP主机；

用于邮件服务的8,165 SMTP、1,516 POP3、1,798 IMAP服务器；

240 SSH服务器和24 Kubernetes实例，使用泄露的密钥可以引发远程shell访问、僵尸网络扩张、以及进一步数据访问。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689568946127633.png "1689568946127633.png")

对于API的暴露，研究发现大多数的容器(2,920个)属于亚马逊AWS这类云服务器提供商，其中部分属于Stripe这样的金融服务。

考虑到白帽伦理，研究人员未对服务终端验证暴露的API秘密，因此其对服务终端的影响尚不明确。

本文翻译自：https://www.bleepingcomputer.com/news/security/thousands-of-images-on-docker-hub-leak-auth-secrets-private-keys/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?fae8bdMS)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/e7OO)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)