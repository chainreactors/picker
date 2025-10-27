---
title: 警惕黑产团伙“黑猫”广撒网盗窃密币、挖矿，中招企业极多！
url: https://www.4hou.com/posts/nlYD
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-24
fetch_date: 2025-10-06T18:47:13.304408
---

# 警惕黑产团伙“黑猫”广撒网盗窃密币、挖矿，中招企业极多！

警惕黑产团伙“黑猫”广撒网盗窃密币、挖矿，中招企业极多！ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 警惕黑产团伙“黑猫”广撒网盗窃密币、挖矿，中招企业极多！

企业资讯
[漏洞](https://www.4hou.com/category/vulnerable)
2024-10-23 11:31:48

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)115409

收藏

导语：曝光新黑产团伙“黑猫”，大规模仿冒网站窃币挖矿，疑与APT组织有关。

当你在网上搜索“谷歌浏览器”时，下图中的地址可能会排在某搜索引擎结果的第一名，但你可能想不到，这是个带病毒的假官网！

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241023/1729654117475051.png "1729654117475051.png")

点击假官网，将下载一个带有“后门”的安装程序，运行程序后，后门将开始一系列网络攻击，包括：探测并窃取虚拟货币钱包，窃取浏览器信息，监听键盘等，如果你并未持有虚拟货币或者无法被窃币，后门就会释放挖矿木马组件，榨干你的最后一点价值。

微步情报局研究发现，这波攻击自7月底开始，累计仿冒网站达20余个，有数据可查的攻击已有数十万次，被攻击行业领域极其广泛，国家有关部门、高校和研究机构、汽车行业、央国企等多个领域均有大量受害单位。该攻击团伙所使用的域名资产中含有大量“heimao-\*(三位数字).com”特征域名，微步情报局据此将该团伙命名为“黑猫”。

**（一）“黑猫”团伙画像**

“黑猫”最早于2022年开始活跃，通过仿冒钓鱼网站投递各类恶意样本，包括“银狐”远控木马、变种Gh0st木马、窃密木马、XMRig挖矿木马等，受害目标为安全意识不足的机构/企业职员，通过远控主机来盗取受害者的虚拟货币并挖矿。“黑猫”的某C2地址和今年上半年APT组织“金眼狗”所使用的远控后门内置的C2地址相同，这表明“黑猫”疑似和“金眼狗”具有一定关联。

|  |  |
| --- | --- |
| 攻击特点 | 擅于使用各种提高搜索引擎排行的方式  部署钓鱼网站手法高超，使用中间下载链接来规避追踪和实时替换下载文件  以敛财盈利为主，主要目标为盗窃虚拟货币  当发现主机并无窃取价值，会下载挖矿组件进行挖矿盈利 |
| 平台 | Windows |
| 传播方式 | 部署虚假软件下载页面，并提高钓鱼网站在搜索引擎排行诱导下载 |
| 攻击地区 | 中国 |
| 攻击人群 | 下载谷歌浏览器，搜狗输入法，WPS办公软件等办公人群  数字货币持有者、行业从业人员 |
| 攻击目的 | 远控，窃密，盗取加密货币，控制肉鸡挖矿 |

表：“黑猫”攻击画像

**（二）“黑猫”常用的攻击手法**

“黑猫”的主要攻击手法是通过部署和推广虚假软件下载页面，进行窃密和盗窃虚拟货币、挖矿等攻击行为。“黑猫”投递的样本复杂多样，各种Gh0st魔改远控，银狐木马，窃密软件，XMRig挖矿木马层出不穷，且更新速度很快，投递的loader具备对各大杀软的免杀技术、反虚拟机调试、反沙箱技术，因此攻击成功率极高。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241023/1729654135333265.png "1729654135333265.png")

图：“黑猫”攻击路径示意图

“黑猫”大范围仿冒常见软件的下载网站，并通过SEO（搜索引擎优化）、SEM（搜索引擎竞价排名）等各种手段提高在搜索引擎关键字排行，诱导受害者访问钓鱼页面，并点击下载带有后门的安装程序。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241023/1729654145145719.png "1729654145145719.png")

（ToDesk搜索结果，钓鱼网站位列第二）

安装程序被受害者运行后，后门程序会窃取受害者虚拟货币钱包，浏览器信息，监听键盘等。如果受害者不具备盗币的可能，“黑猫”会释放XMRig挖矿木马组件进行挖矿。

**（三）“黑猫”仿冒的常见软件及下载地址**

“黑猫”仿冒的常见软件下载地址，高达20余个，囊括了常用办公软件、虚拟币行情交易平台、VPN/上网加速器等程序。需要警惕的是，“黑猫”具备极强的SEO（搜索引擎优化）技术，不仅会仿冒网站，还会把仿冒网站的地址顶到搜索结果的首页，甚至能常年保持在排名第一第二的位置，因此受害者极易中招。现将2024年“黑猫”仿冒的部分网站地址列表如下。

|  |  |  |
| --- | --- | --- |
| 仿冒软件名 | 假网站地址 | 搜索引擎最高排名 |
| Chrome浏览器 | http://zh-chrome.com/  https://guge-chrome.com/  https://zh-google.cn/  https://web-chrome.cn  https://chromecn.cn  https://chromem.cn | 第一，截至发稿仍生效 |
| Todesk远控软件 | https://todesk-zh.com/ | 第二，截至发稿仍生效 |
| WPS办公软件 | https://cn-wps.com | 第三，截至发稿仍生效 |
| 搜狗输入法 | https://sogou-shurufa.com | 第三，截至发稿仍生效 |
| 爱思助手 | https://i4.com.vn/ | 第四，截至发稿仍生效 |
| 爱加速vpn | https://zh-aijiasu.com/  https://ajsvpn.com/ | 第三，截至发稿仍生效 |
| MEXC数字资产一站式交易平台 | https://zh-mexc.com/ | 第七，截至发稿仍生效 |
| potato社交软件 | https://zh-potato.com/  https://potato-zh.com/ | 第十一，截至发稿仍生效 |
| 穿梭VPN | https://cs-vpn.com/  https://zh-csvpn.com/  https://transocks-vpn.com/ | 第四，截至发稿仍生效 |
| 飞连vpn | https://fl-vpn.com/ | 第一，截至发稿仍生效 |
| 快帆加速器 | https://www.qobddze.cn/ | 拓线获得，暂无排名 |
| okx欧易交易所 | https://oeokx.cn/  https://okx-client.cn/  https://zh-okex.cn/ | 第四，截至发稿仍生效 |
| gate交易所 | https://zh-gateio.cn/ | 拓线获得，暂无排名 |
| aicoin | https://www.aicoinzh.com/ | 第二，截至发稿仍生效 |
| tradingview | https://tradingview-en.com/  http://ayicoin.com  https://nbxieheng.cn/  https://zh-tradingview.cn/ | 第一，截至发稿仍生效 |
| Telegram（电报） | https://www.telegramef.com/ | 第一，截至发稿仍生效 |

**（四）处置建议**

1. 根据本文附录IOC内容进行自查，封禁相关恶意域名；

2. 对已经失陷的机器，及时隔离、清理，杜绝失陷机器外联恶意域名可能带来的监管合规问题；

3. 规范办公软件获取途径，收紧软件安装策略，禁止在办公终端上采用非官方途径进行下载安装。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?pp1jVUsl)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/aQWl)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

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