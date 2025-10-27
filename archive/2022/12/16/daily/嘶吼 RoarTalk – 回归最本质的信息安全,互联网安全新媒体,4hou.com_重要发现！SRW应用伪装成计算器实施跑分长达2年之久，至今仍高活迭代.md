---
title: 重要发现！SRW应用伪装成计算器实施跑分长达2年之久，至今仍高活迭代
url: https://www.4hou.com/posts/gX4j
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-16
fetch_date: 2025-10-04T01:38:49.853105
---

# 重要发现！SRW应用伪装成计算器实施跑分长达2年之久，至今仍高活迭代

重要发现！SRW应用伪装成计算器实施跑分长达2年之久，至今仍高活迭代 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 重要发现！SRW应用伪装成计算器实施跑分长达2年之久，至今仍高活迭代

360反诈中心
[新闻](https://www.4hou.com/category/news)
2022-12-15 11:06:07

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)156865

收藏

导语：跑分界的超强“伪装者”，把IP、秘钥、端口号技术全用上了

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669732783727522.png "1669732783727522.png")

早前，我们发现过博彩产业为方便博彩代理人员管理下线人员，为其定制开发博彩代理APP，该应用伪装成一个可正常使用的计算器应用，当在该计算器中输入特定指令时，页面会展示真正的博彩代理登录界面。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669732784145369.png "1669732178371771.png")

此类伪界面手段近期也在一款跑分应用中出现，通过同源追溯，发现该应用衍生产业链存活至今已达2年，且应用不断在进行迭代，最新版本为4.3。

**下面，以跑分客的视角，来看看这个跑分应用到底是怎么“跑起来”的**

根据情报显示，跑分流程分以下这么几步：

第一步，跑分客需要访问指定的网址，获得本地ip，并将ip提供给上线进行加白

第二步，登录指定的卡商网站，将跑分客的银行信息（银行卡号、所属省市、所属支行、取款密码、U盾密码、登录密码、身份证号码）录入至平台，选择类型（U盾、跑分-银行卡、手机短信-纯收款等）

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669732784207200.png "1669732183108235.png")

第三步，手机安装该应用，并授予短信权限

第四步，打开该应用，输入密钥，点击实现短信同步

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669732785181754.png "1669732211201226.png")

这个操作之后，就意味着跑分客收到的所有银行短信，都会被自动同步给跑分平台。

也不难看出，整个过程攻防措施也是相当严密，体现在两点：

首先，ip需要人工加白，否则无法进行后续银行卡信息录入，相当于人工资质审核授权；

其次，伪装成计算器的应用，需要通过秘钥才能跳转登录页并进行短信授权；

哇哦

该跑分平台

在玩一种很新的登录验证方法

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669732786113337.png "1669732216126668.png")

**应用****背后的关联产业挖掘**

**应用分析**

通过追溯同源样本，发现应用最早于2020年开始传播，至今存活时间已长达2年之久！

**产业链挖掘**

通过梳理该产业链的IOC情报，我们发现该应用运营者的运作模式如下：

1、使用多台中国香港服务器做APP分发节点

2、为不同的用户群体定制不同的子域名+不同的端口，例如子域名shanghu（商户人员使用）、子域名kashang（卡商人员使用）、sys（支付回调使用）

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669732786163607.png "1669732246157931.png")

支付回调页面

最后，梳理一下这个产业链上下游涉及的支付通道平台、卡商以及支付通道用户之间的运作流程：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669732787910352.png "1669732250717723.png")

支付通道收集卡贩子（跑分客）手中的银行卡，并要求卡贩子（跑分客）将银行卡信息录入指定的卡商平台以及在手机（插入银行卡绑定的手机号的卡）中安装指定的计算器APP，用于监控手机的银行卡短信，并转发至支付通道终端服务器。

支付通道用户（博彩、诈骗等）开通该支付通道的API接入对应的诈骗平台，当用户在诈骗/博彩平台充值时，显示对应的充值入口（银行卡），用户在页面刷新后，重新调用接口。

整体构成了一个完整的聚合平台，可以实现以跑分客与卡商平台提供“料子”，以支付平台为中转调度出口，供支付通道用户调用，为博彩/诈骗提供跑分“一站式”服务。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?DTAtSlRv)

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

![](https://img.4hou.com/portraits/068e4092bab6e0b00b3c9e62609dd402.png)

# [360反诈中心](https://www.4hou.com/member/mx20)

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

[查看更多](https://www.4hou.com/member/mx20)

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