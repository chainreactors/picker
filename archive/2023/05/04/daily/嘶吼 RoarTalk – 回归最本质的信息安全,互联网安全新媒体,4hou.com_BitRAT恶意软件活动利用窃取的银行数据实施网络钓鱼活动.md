---
title: BitRAT恶意软件活动利用窃取的银行数据实施网络钓鱼活动
url: https://www.4hou.com/posts/4KXx
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-05-04
fetch_date: 2025-10-04T11:36:56.109728
---

# BitRAT恶意软件活动利用窃取的银行数据实施网络钓鱼活动

BitRAT恶意软件活动利用窃取的银行数据实施网络钓鱼活动 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# BitRAT恶意软件活动利用窃取的银行数据实施网络钓鱼活动

布加迪
[新闻](https://www.4hou.com/category/news)
2023-05-03 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)120461

收藏

导语：据云安全公司Qualys声称，最近一起恶意软件活动背后的威胁分子一直在使用哥伦比亚银行客户的被盗信息作为网络钓鱼邮件的诱饵，目的在于用BitRAT远程访问木马感染目标。

据云安全公司Qualys声称，最近一起恶意软件活动背后的威胁分子一直在使用哥伦比亚银行客户的被盗信息作为网络钓鱼邮件的诱饵，目的在于用BitRAT远程访问木马感染目标。

该公司在调查活跃网络钓鱼攻击中的BitRAT诱饵时发现，一家未公开身份的哥伦比亚合作银行的基础设施遭到了攻击者的劫持。

总共418777条含有敏感客户数据的记录从遭到攻击的服务器中被盗，这些敏感客户数据包括姓名、电话号码、电子邮件地址、住址、哥伦比亚身份证、付款记录和工资信息。

在调查这起活动时，Qualys还发现了表明攻击者已访问客户数据的证据，包括显示攻击者使用sqlmap工具寻找SQL注入错误的日志。

Qualys表示：“此外，诱饵本身含有来自这家银行的敏感数据，以便诱饵看起来很逼真。这意味着攻击者已经获得了客户数据的访问权。”

“我们在进一步深入研究该银行的基础设施时发现了表明使用sqlmap工具来查找潜在SQLi错误的日志，还发现了实际的数据库转储内容。”

目前，从这家哥伦比亚银行的服务器上被盗的任何信息还都没有出现在Qualys监测的暗网或明网网站上。

恶意软件通过一个恶意Excel文件投放到受害者的计算机上，该恶意文件投放并执行在一个与附件捆绑的高度混淆处理的宏中编码的INF文件。.inf攻击载荷被分割成了宏中的数百个数组。反混淆例程对这些数组执行了算术运算，以重新构建攻击载荷。随后宏将攻击载荷写入到temp，并通过advpack.dll执行它。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672788862797140.png "1672788862797140.png")

图1. Excel BitRAT诱饵（来源：Qualys）

最终的BitRAT攻击载荷随后使用受攻击设备上的WinHTTP库从GitHub代码库下载，并在WinExec函数的帮助下加以执行。

在攻击的最后阶段，RAT恶意软件将其加载程序移动到Windows启动文件夹以获得持久性，并在系统重新启动后自动重启。

至少从2020年8月开始，BitRAT作为现成的恶意软件在暗网市场和网络犯罪论坛上出售，只需支付20美元即可获得长期访问权。

在支付许可证费用后，每个“客户”都可以使用各自的方法用这种恶意软件感染受害者，比如网络钓鱼、水坑攻击和木马软件。

用途广泛的BitRAT可用于实施各种恶意目的，包括：泄露数据、记录击键内容、录制视频和音频、窃取数据、DDoS攻击、加密货币挖掘、针对进程/文件/软件等运行任务以及投放额外的攻击载荷。

Qualys公司的威胁研究高级工程师Akshat Pradhan说：“现成的商用RAT一直在完善和改进其传播方法，以便感染受害者。”

“他们还增加了使用合法基础设施来托管其攻击载荷的力度，防御者需要注意到这一点。我们Qualys威胁研究部门会继续监测并记录这类威胁，了解其不断变化的策略、技术和程序（TTP）。”

**MITRE ATT&CK映射**

T1071.001 应用程序层协议：邮件协议

T1102 Web服务

T1218.011 系统二进制代理执行：Rundll32

T1218 系统二进制代理执行

T1584 攻陷基础设施

T1059.003 命令和脚本解释器：Windows命令外壳

T1140 反混淆/解码文件或信息

T1204.002 用户执行：恶意文件

T1547.001 启动或登录自动启动执行：注册表运行键/启动文件夹

本文翻译自：https://www.bleepingcomputer.com/news/security/bitrat-malware-campaign-uses-stolen-bank-data-for-phishing/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?SyvUnTUD)

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