---
title: 亚洲航空公司遭到勒索软件攻击，乘客及雇员的资料被窃取
url: https://www.4hou.com/posts/jJm4
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-26
fetch_date: 2025-10-03T23:48:27.257432
---

# 亚洲航空公司遭到勒索软件攻击，乘客及雇员的资料被窃取

亚洲航空公司遭到勒索软件攻击，乘客及雇员的资料被窃取 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 亚洲航空公司遭到勒索软件攻击，乘客及雇员的资料被窃取

布加迪
[新闻](https://www.4hou.com/category/news)
2022-11-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)154019

收藏

导语：11月11日和12日，亚洲航空集团遭到了Daixin Team团伙的勒索软件攻击。

亚洲航空集团承诺在收集个人信息时负责任，并“尽一切可能”保护隐私。请注意，这不是合同，而只是他们所表达的承诺。

11月11日和12日，亚洲航空集团遭到了Daixin Team团伙的勒索软件攻击。CISA最近就这个团伙发出了警报；该团伙告诉DataBreaches网站，他们已获得了500万乘客和所有雇员的个人数据。

DataBreaches看到了该团伙向亚洲航空集团出示的两个.csv文件。一个文件包含有名有姓的乘客的信息。第二个文件包含雇员信息，附有许多字段，包括姓名、出生日期、出生国家、位置、开始工作的日期、“秘密问题”、“答案”以及用来加密的随机字符串（salt）。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221122/1669081444196742.jpeg "1669081444196742.jpeg")

图1. 这个.csv文件貌似附有雇员数据，包含大量与个人和工作相关的信息，DataBreaches.net已作编辑处理。

据Daixin的发言人声称，亚洲航空已对这次攻击做出了回应。据称他们很快接上了头，向Daixin的谈判代表索要数据样本，在收到样本后，“非常详细地询问了如果支付赎金，我们将如何删除他们的数据。”据称亚洲航空并没有协商金额的打算，这可能表明他们从未打算支付赎金。该发言声称：“大家通常都希望协商以降低赎金金额。”目前不知道Daixin Team索要多少赎金，才肯提供解密密钥、删除他们窃取的所有数据，并将已发现和已利用的漏洞通知亚洲航空集团。

Daixin发言人强调的一点是，在锁定文件时，该团伙避免了锁定“XEN和RHEL，这些是飞行设备（雷达、空中交通管制等设备）的主机”。这番声明与Daixin Team在其他事件中向DataBreaches发表的声明相一致：他们表示，如果攻击的后果可能危及生命，他们会避免加密或销毁任何东西。

有些令人意外的是，Daixin发言人表示，亚洲航空集团网络的糟糕组织使该公司免遭进一步的攻击。虽然据称Daixin Team加密了大量资源，并删除了备份，但他们表示实际上造成的破坏没有像平时那么大：

网络组织混乱和缺乏任何标准让这个团伙颇为不屑，完全不愿意再次攻击。

该团伙拒绝长时间捡拾垃圾。正如我们的渗透测试人员所说：“让新来的攻击团伙去挑拣这些垃圾吧，他们有的是时间。”

攻击者因受害者糟糕的网络组织而放弃发起攻击，这还真是闻所未闻。DataBreaches询问Daixin的发言人，他们是否能证实亚洲航空糟糕的组织确实使这家航空公司免遭更多的攻击。发言人回应道：

是的，糟糕的组织帮助了他们。内部网络的配置没有任何规则，因此运行起来非常糟糕。似乎每个新的系统管理员都“把自己的棚屋搭在旧建筑旁边”。与此同时，网络保护非常非常薄弱。

靠无能获得安全？这会是一股潮流吗？

无论如何，Daixin告知DataBreaches，除了在他们专门的泄露网站上泄露乘客和雇员的数据外，该团伙计划在黑客论坛上私下免费提供有关亚洲航空网络的信息，“包括后门”。Daixin Team并不为未来的负面后果承担责任。

DataBreaches分别于昨天和今天上午向亚洲航空集团的数据保护主管发送了电子邮件，但截至发稿时均未收到回复。

在过去这几年，马来西亚的多家组织经常成为网络攻击的目标，黑客相关论坛上的数据库数量和泄密数量以及DataBreaches的报道证明了这一点。亚洲航空集团不是马来西亚航空业唯一一家遭到黑客入侵的公司。马来西亚航空公司在2020年和2021年都披露了数据安全事件。

自2022年1月以来，亚洲航空集团更名为Capital A Berhad，以亚洲航空的名义运营。亚洲航空是马来西亚一家跨国低成本航空公司，是马来西亚机队规模最大、目的地数量最多的航空公司。

本文翻译自：https://www.databreaches.net/airasia-victim-of-ransomware-attack-passenger-and-employee-data-acquired/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?4XLaHs95)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

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