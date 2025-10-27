---
title: 关于针对我国用户的“银狐”木马病毒再次出现新变种并更新传播手法的预警报告
url: https://www.4hou.com/posts/XPVo
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-25
fetch_date: 2025-10-06T19:35:52.890982
---

# 关于针对我国用户的“银狐”木马病毒再次出现新变种并更新传播手法的预警报告

关于针对我国用户的“银狐”木马病毒再次出现新变种并更新传播手法的预警报告 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 关于针对我国用户的“银狐”木马病毒再次出现新变种并更新传播手法的预警报告

嘶吼
[新闻](https://www.4hou.com/category/news)
2024-12-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)106683

收藏

导语：在本次传播过程中，攻击者继续通过构造财务、税务违规稽查通知等主题的钓鱼信息和收藏链接，通过微信群直接传播包含该木马病毒的加密压缩包文件。

**一、相关病毒传播案例**

近日，国家计算机病毒应急处理中心和计算机病毒防治技术国家工程实验室依托国家计算机病毒协同分析平台（[https://virus.cverc.org.cn）](https://virus.cverc.org.cn/)在我国境内再次捕获发现针对我国用户的“银狐”木马病毒的最新变种。在本次传播过程中，攻击者继续通过构造财务、税务违规稽查通知等主题的钓鱼信息和收藏链接，通过微信群直接传播包含该木马病毒的加密压缩包文件，如图1所示。

![微信图片_20241224104241.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241224/1735008663577723.jpg "1735008147666281.jpg")

图1 钓鱼信息及压缩包文件

图1中名为“笔记”等字样的收藏链接指向文件名为“违规-记录（1）.rar”等压缩包文件，用户按照钓鱼信息给出的解压密码解压压缩包文件后，会看到以“开票-目录.exe”、“违规-告示.exe”等命名的可执行程序文件，这些可执行程序实际为“银狐”远控木马家族于12月更新传播的最新变种程序。如果用户运行相关恶意程序文件，将被攻击者实施远程控制、窃密等恶意操作，并可能被犯罪分子利用充当进一步实施电信网络诈骗活动的“跳板”。

**二、病毒感染特征**

**1.钓鱼信息特征**

本次发现攻击者使用的钓鱼信息仍然以伪造官方通知为主。结合年末特点，攻击者刻意强调“12月”、“稽查”、“违规”等关键词，借此使潜在受害者增加紧迫感从而放松警惕。在钓鱼信息之后，攻击者继续发送附带所谓的相关工作文件的钓鱼链接。

**2.文件特征**

1）文件名

对于本次发现的新一批变种，犯罪分子继续将木马病毒程序的文件名设置为与财税、金融管理等相关工作具有密切联系的名称，以引诱相关岗位工作人员点击下载运行，如：“开票-目录”、“违规-记录”、“违规-告示”等。此次发现的新变种仍然只针对安装Windows操作系统的传统PC环境，犯罪分子也会在钓鱼信息中使用“请使用电脑版”等话术进行有针对性的诱导提示。

2）文件格式

本次发现的新变种以RAR、ZIP等压缩格式（内含EXE可执行程序）为主，与之前变种不同的是，此次攻击者为压缩包设置了解压密码，并在钓鱼信息中进行提示告知，以逃避社交媒体软件和部分安全软件的检测，使其具有更强的传播能力。

3）文件HASH

34101194d27df8bc823e339d590e18f2

网络安全管理员可通过国家计算机病毒协同分析平台（[https://virus.cverc.org.cn）](https://virus.cverc.org.cn/)获得相关病毒样本的详细信息，如下：<https://virus.cverc.org.cn/#/entirety/file/searchResult?hash=34101194d27df8bc823e339d590e18f2>

**3.进程特征**

木马病毒被安装运行后，会在操作系统中创建新进程，进程名与文件名相同，并从回联服务器下载其他恶意代码直接在内存中加载执行。

**4.网络通信特征**

回联地址为：156.\*\*\*.\*\*\*.90，端口号为：1217

命令控制服务器（C2）域名为：mm7ja.\*\*\*\*\*. cn，端口号为：6666

网络安全管理员可根据上述特征配置防火墙策略，对异常通信行为进行拦截。其中与C2地址的通信过程中，攻击者会收集受害主机的操作系统信息、网络配置信息、USB设备信息、屏幕截图、键盘记录、剪切板内容等敏感数据。

**5.其他特征**

本次发现的新变种还具有主动攻击安全软件的功能，试图通过模拟用户鼠标键盘操作关闭防病毒软件。

**三、防范措施**

临近年末，国家计算机病毒应急处理中心再次提示广大企事业单位和个人网络用户提高针对各类电信网络诈骗活动的警惕性和防范意识，不要轻易被犯罪分子的钓鱼话术所诱导。结合本次发现的银狐木马病毒新变种传播活动的相关特点，建议广大用户采取以下防范措施：

1.不要轻信微信群、QQ群或其他社交媒体软件中传播的所谓政府机关和公共管理机构发布的通知及相关工作文件和官方程序（或相应下载链接），应通过官方渠道进行核实。

2.带密码的加密压缩包并不代表内容安全，针对类似此次传播的“银狐”木马病毒加密压缩包文件的新特点，用户可将解压后的可疑文件先行上传至国家计算机病毒协同分析平台[（https://virus.cverc.org.cn）](https://virus.cverc.org.cn/)进行安全性检测，并保持防病毒软件实时监控功能开启，将电脑操作系统和防病毒软件更新到最新版本。

3.一旦发现电脑操作系统的安全功能和防病毒软件在非自主操作情况下被异常关闭，应立即主动切断网络连接，对重要数据进行迁移和备份，并对相关设备进行停用直至通过系统重装或还原、完全的安全检测和安全加固后方可继续使用。

4.一旦发现微信、QQ或其他社交媒体软件发生被盗现象，应向亲友和所在单位同事告知相关情况，并通过相对安全的设备和网络环境修改登录密码，对自己常用的计算机和移动通信设备进行杀毒和安全检查，如反复出现账号被盗情况，应在备份重要数据的前提下，考虑重新安装操作系统和防病毒软件并更新到最新版本。

文章来源自：国家计算机病毒应急处理中心

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?5sWNdD1L)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/7f870371b3fa7e728a96.png
)

# [嘶吼](https://www.4hou.com/member/enZR)

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

[查看更多](https://www.4hou.com/member/enZR)

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