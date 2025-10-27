---
title: 关于针对我国用户的“银狐”木马病毒出现新变种的预警报告
url: https://www.4hou.com/posts/MXWR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-20
fetch_date: 2025-10-06T19:33:39.566935
---

# 关于针对我国用户的“银狐”木马病毒出现新变种的预警报告

关于针对我国用户的“银狐”木马病毒出现新变种的预警报告 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 关于针对我国用户的“银狐”木马病毒出现新变种的预警报告

企业资讯
[新闻](https://www.4hou.com/category/news)
2024-12-19 14:16:39

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)109425

收藏

导语：国家计算机病毒应急处理中心和计算机病毒防治技术国家工程实验室依托国家计算机病毒协同分析平台在我国境内发现针对我国用户的“银狐”木马病毒最新变种。

**一、相关病毒传播案例**

近日，国家计算机病毒应急处理中心和计算机病毒防治技术国家工程实验室依托国家计算机病毒协同分析平台在我国境内发现针对我国用户的“银狐”（又名：“游蛇”、“谷堕大盗”等）木马病毒最新变种。攻击者通过构造财务、税务等主题的钓鱼网页，通过微信群传播该木马病毒的下载链接。如图1、图2所示。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241219/1734577236151540.png "1734576933520166.png")

   图1 钓鱼信息及链接(1)

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241219/1734577237214035.png "1734576977276605.png")

图2 钓鱼信息及链接(2)

用户点击上述钓鱼链接后，钓鱼网页会根据用户终端类型进行跳转，如果用户使用手机终端访问，则会提示用户使用电脑终端进行访问，用户使用电脑终端访问链接后会下载文件名为“金稅四期（电脑版）-uninstall.msi”的安装包文件或“金稅五期（电脑版）-uninstall.zip”的压缩包文件（内含同文件名的可执行程序文件），实际为“银狐”木马病毒家族的最新变种程序。如果用户运行相关程序文件，将被攻击者实施远程控制、窃密、网络诈骗等恶意活动并充当进一步攻击的“跳板”。

**二、病毒感染特征**

**1.钓鱼信息特征**

钓鱼信息可能通过微信群、QQ群等社交媒体或电子邮件发送，信息通常为犯罪分子伪造的官方通知，主题通常涉及财税或金融管理等公共管理部门发布的最新政策和工作通知等，并附所谓的对接相关工作所需专用程序的下载链接。

**2. 文件特征**

1）文件名

犯罪分子通常会将木马病毒程序的文件名设置为与财税、金融管理部门相关工作具有显著关联，且对相关岗位工作人员具有较高辨识度的名称，如：“金稅四期（电脑版）”、“金稅五期（电脑版）”等，并以此为诱饵欺骗企业中的财务管理人员或个体经营者。由于目前该木马病毒程序的变种大多只针对安装Windows操作系统的传统PC环境，犯罪分子也会在文件名中设置“电脑版”、“PC版”等关键词以诱导受害用户在相应环境下安装。

2）文件格式

目前已知的该木马病毒常用文件格式以MSI安装包格式和ZIP、RAR等压缩包格式（内含MSI或EXE等可执行程序）为主。

3）文件HASH

cf8088b59ee684cbd7d43edcc42b2eec

f3cad147e35f236772b5e10f4292ba6e

网络安全管理员可通过国家计算机病毒协同分析平台获得相关病毒样本的详细信息，如下:

<https://virus.cverc.org.cn/#/entirety/file/searchResult?hash=cf8088b59ee684cbd7d43edcc42b2eec>

<https://virus.cverc.org.cn/#/entirety/file/searchResult?hash=f3cad147e35f236772b5e10f4292ba6e>

**3.系统驻留特征**

木马病毒被安装后，会在操作系统中注册名为“UserDataSvc\_[字母与数字随机组合]”的系统服务，实现开机自启动和持久驻留，如图3所示。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241219/1734577238137714.png "1734577021208696.png")

图3 注册系统服务实现系统持久驻留

**4.网络通信特征**

回联地址为：154.\*\*.\*\*.95

命令控制服务器（C2）域名为：8848.\*\*\*\*\*\*\*\*.zip

其中与C2地址的通信内容中，会包含受害主机的操作系统信息、用户名、CPU信息、内存信息以及内网IP地址等数据，如下：

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241219/1734577239384209.png "1734577065941726.png")

**三、防范措施**

国家计算机病毒应急处理中心提示广大企事业单位，特别是从事电商业务的中小微企业以及个体经营者和个人网络用户，临近年末，各类财税和金融业务繁忙，从事相关业务的工作人员务必提高警惕，防范以计算机病毒为作案工具的电信网络诈骗活动。建议广大用户采取以下防范措施：

1.不要轻信微信群、QQ群或其他社交媒体软件中传播的所谓政府主管部门或金融机构发布的通知，应通过官方渠道进行核实。

2.不要从微信群、QQ群或其他社交媒体软件的聊天群组中传播的网络链接（或二维码）下载所谓的官方程序。

3.一旦发现微信、QQ或其他社交媒体软件发生被盗现象，应向亲友和所在单位及同事告知相关情况，并通过相对安全的设备和网络环境修改登录密码，并对自己常用的计算机和移动通信设备进行杀毒和安全检查，如反复出现账号被盗情况，应在备份重要数据的前提下，考虑重新安装操作系统和安全软件并更新到最新版本。

4.对安全性未知的可疑文件，可访问国家计算机病毒协同分析平台（[https://virus.cverc.org.cn](https://virus.cverc.org.cn/)）进行提交检测。

文章来源自： 国家计算机病毒应急处理中心

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?g4MWnEec)

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

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

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

[查看更多](https://www.4hou.com/member/aQWl)

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