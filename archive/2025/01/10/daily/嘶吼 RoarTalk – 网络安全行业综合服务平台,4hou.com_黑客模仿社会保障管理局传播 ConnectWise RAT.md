---
title: 黑客模仿社会保障管理局传播 ConnectWise RAT
url: https://www.4hou.com/posts/NGK8
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-01-10
fetch_date: 2025-10-06T20:06:04.963073
---

# 黑客模仿社会保障管理局传播 ConnectWise RAT

黑客模仿社会保障管理局传播 ConnectWise RAT - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客模仿社会保障管理局传播 ConnectWise RAT

山卡拉
[新闻](https://www.4hou.com/category/news)
2025-01-09 10:22:26

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)102938

收藏

导语：威胁行为者利用社会工程技术部署凭证网络钓鱼活动，他们制作模仿合法实体（例如社会保障局）的电子邮件来诱骗受害者点击恶意链接。

![Social Security Administration Spoof Connectwise RAT.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250109/1736388550159380.jpg "1736388550159380.jpg")

2024 年 9 月出现了一场冒充美国社会保障局的网络钓鱼活动，它向电子邮件发送嵌入了 ConnectWise 远程访问木马 (RAT) 安装程序链接的电子邮件。

这些电子邮件伪装成更新的福利声明，采用了各种技巧，包括不匹配的链接和“查看声明”按钮，以欺骗收件人。

它最初利用ConnectWise基础设施进行命令和控制 (C2)，但后来转变为动态 DNS 服务和威胁行为者托管的域。

据观察，活动在 11 月初至中旬显著增加，并在选举日左右达到顶峰，这表明它可能与政治选举有关。

威胁行为者在针对个人的电子邮件活动中采用了复杂的欺骗策略，利用社会保障管理局合法的福利来制造假象。

通过仿政府官方网页的欺骗性链接，使用邮件诱骗收件人点击。

这可能导致恶意软件感染或数据盗窃。

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-VIq_RdGK2B0cZEztRAO-sBJh4fgsm5wcGaLJM1MsgqBrpamTrUGZvY2H7pCKCCGY1oc3SR6p-AHi6DctFEFr1XoOCk4EFGmO6-loMXGzyI_8nficoJqzOhWJ7wQgCqq_o6H1VLwslpUI1MeFuyVhwDPqzPiQZYKsfjEok_JotvQsC96RPqRvIXUsZ7sg/s1128/Hackers-Spoof-Social-Security-Administration-to-Deliver-ScreenConnect-Remote-Access-Tool_Figure1.webp)

使用品牌图像资产的欺骗社会保障管理局电子邮件示例

通过使用欺骗性的攻击，嵌入式链接能够在用户首次访问链接时将用户重定向到 ConnectWise RAT 安装程序。

然而，随后尝试访问同一链接时，用户会被重定向到合法的社会保障管理局网站，这表明使用浏览器 cookie 来追踪以前的访问。

通过在第一次访问时设置 cookie，系统可以区分初次尝试和重复尝试。

这有效地将恶意软件传递到精准用户，从而使识别恶意攻击更具挑战性。

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyCR1l7sgdIXpEl-2k21Hexm820QrbAypQ3CbVEw8625esTAL4KuD6D9nBc5JlPPsa07O4qV1IQysn-a25xaJvuDimgttDePDLo3HOK4NIVMQjoI1WObaT_Pw6Dt4wa83osS5KwrtgXoM4mNLg-KEjgL3wrlB99rSjBnoQGrLJER3kTtd7Qn5BvV4KvGrw/s962/Hackers-Spoof-Social-Security-Administration-to-Deliver-ScreenConnect-Remote-Access-Tool_Figure3.webp)

当后续尝试访问该链接时，该网站会重定向到官方网站

威胁行为者利用社会工程技术部署凭证网络钓鱼活动，他们制作模仿合法实体（例如社会保障局）的电子邮件来诱骗受害者点击恶意链接。

据Cofense Intelligence称，这些链接通常会将用户引导至伪装成官方门户的网站，要求用户提供敏感的个人信息。这些数据（包括 PII、财务信息以及母亲娘家姓氏等安全问题）会被收集起来，用于身份盗窃和账户接管。

网络钓鱼页面还可能包含远程访问木马 (RAT) 等恶意下载，从而允许攻击者远程控制受害者的设备。

这使得威胁行为者能够侵入账户、窃取资金，并可能进一步利用受害者的数字足迹。

本文翻译自：https://gbhackers.com/connectwise-rat/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?eS8iNsld)

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

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

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

[查看更多](https://www.4hou.com/member/azxO)

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