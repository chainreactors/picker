---
title: Threema 加密通信APP多安全漏洞
url: https://www.4hou.com/posts/ykLE
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-20
fetch_date: 2025-10-04T04:20:49.305566
---

# Threema 加密通信APP多安全漏洞

Threema 加密通信APP多安全漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Threema 加密通信APP多安全漏洞

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-01-19 11:20:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)233875

收藏

导语：​研究人员在端到端加密通信APP Threema发现多个安全漏洞。

研究人员在端到端加密通信APP Threema发现多个安全漏洞。

Threema是一款瑞士的加密通信APP，有超过100万用户和7000本地部署用户。其中，Threema重要用户包括瑞士政府和军方，以及德国总理。Threema广告宣称是其他即使通信应用的安全可替代产品。

![Threema app on a blue and green background](https://img.4hou.com/uploads/ueditor/php/upload/image/20230119/1674092629132432.jpg)

**Threema攻击**

瑞士苏黎世联邦理工学院 (ETH Zurich) 研究人员共涉及了7种针对Threema协议的安全攻击，可打破Threema APP的通信隐私，包括窃取私有密钥、删除消息、破解认证、欺骗服务器等。

**·** 临时密钥入侵假冒（Ephemeral key compromise impersonation）：攻击者窃取临时密钥伪装成客户端。Threema貌似重用了临时密钥，即临时密钥不是一次性的。

**·**Vouch box 伪造：攻击者可诱使用户发送有效的vouch box，然后用它来假冒客户端。

**·**消息重排和删除：恶意服务器可转发来自用户的消息，攻击者可以对消息重新排序，此外，服务器还可以将消息删除。

**·**重放和反射攻击：Threema安卓版本的消息nonce数据库是不可迁移的，因此可以实现消息重放和反射攻击。

**·**Kompromat攻击：恶意服务器可以诱使客户端在初始化注册协议阶段与服务器会话时和在端到端协议中与其他用户会话时使用的密钥。

**·**通过Threema ID export克隆：攻击者可在其设备上克隆其他用户的账户，但要求用户设备是未锁定的。

**·**压缩侧信道：研究人员在Threema加密方法中发现一个安全漏洞，允许攻击者通过控制用户名和安卓设备上的多个备份来提取用户的私钥。但攻击过程需要几个小时。

**Threema回应**

ETH Zurich研究人员于2022年10月3日将研究成果报告给Threema。11月29日，Threema发布了新的更加安全的协议——Ibex，来解决潜在的安全问题。但是Threema称ETH Zurich研究的Threema协议其已不再使用，并称其研究发现并不会对其产品带来任何影响。比如，通过Threema ID export实现克隆攻击已在2021年修复。Vouch box伪造攻击依赖社会工程攻击，需要目标用户的参与。其他攻击还需要对设备的物理访问，且要求Threema设备未锁定。

研究论文参见：<https://breakingthe3ma.app/files/Threema-PST22.pdf>

PoC和其他技术细节参见：<https://breakingthe3ma.app/>

本文翻译自：https://www.bleepingcomputer.com/news/security/threema-claims-encryption-flaws-never-had-a-real-world-impact/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mC3dWmTw)

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