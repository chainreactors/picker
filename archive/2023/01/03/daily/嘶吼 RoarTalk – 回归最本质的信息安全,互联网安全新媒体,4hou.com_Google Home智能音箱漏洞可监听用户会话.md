---
title: Google Home智能音箱漏洞可监听用户会话
url: https://www.4hou.com/posts/zlGy
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-03
fetch_date: 2025-10-04T02:54:36.634087
---

# Google Home智能音箱漏洞可监听用户会话

Google Home智能音箱漏洞可监听用户会话 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Google Home智能音箱漏洞可监听用户会话

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-01-02 11:40:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)149904

收藏

导语：安全研究人员Matt在Google Home智能音箱设备中发现了一个安全漏洞。

**漏洞概述**

2016年，谷歌发布Google Home智能音箱产品。2021年，安全研究人员Matt在Google Home智能音箱设备中发现了一个安全漏洞，攻击者利用该漏洞可以在受害者设备中安装后门装好，并通过互联网远程发送命令给受害者设备、访问麦克风数据量、在受害者网络中发起任意HTTP请求，甚至可能暴露WiFi密码，使攻击者访问受害者的其他设备。

研究人员在Google Home mini智能音箱测试时发现，使用Google Home app添加的新账号可以通过云API远程发送命令。

研究人员通过Nmap扫描发现了Google Home的本地http API端口，然后设置代理进行加密的HTTPS流量抓包，以期获取用户认证token。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672390989199484.png "1672390495165805.png")

图 HTTPS流量抓包

在目标设备上添加新用户需要2个步骤，首先需要设备名、证书、本地API的cloud ID。有了这个信息，就可以发送链接请求到谷歌服务器。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672390990170205.png "1672390534654607.png")

图 包含设备ID数据的链接请求

整个攻击的流程如下：

**·** 攻击者想要监听无线网络范围内的Google Home，但无需知道受害者的WiFi密码；

**·**攻击者通过谷歌公司的Mac地址前缀来发现受害者的Google Home设备；

**·**攻击者发送deauth包使设备从网络端口，并进入设置模式；

**·**攻击者连接到设备的设置网络，并请求受害者设备信息，包括设备名、证书、cloud ID等；

**·**攻击者连接到互联网，并使用获得的设备信息将其账号与受害者设备链接起来；

**·**攻击者就可以通过互联网来监听受害者设备了。

研究人员在GitHub上发布了3个PoC，包括植入恶意用户、通过麦克风进行监听，在受害者网络中发起任意http请求，在受害者设备上读写任意文件。PoC代码参见：<https://github.com/DownrightNifty/gh_hack_PoC>

在受害者设备上植入恶意账户就可以通过Google Home speaker执行以下操作：

**·**进行在线购物；

**·**远程开锁或解锁车辆；

**·**通过暴力破解PIN码的方式解锁用户智能门锁。

此外，攻击者还可以滥用"call [phone number]"命令来在特定时间激活麦克风，拨通攻击者号码，并发送麦克风数据流，实现对用户的监听。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672390990115902.png "1672390562150138.png")

图 获取用户麦克风数据

在拨打电话过程中，设备的LED灯会变蓝。如果受害者注意到LED灯的变化，可能会认为设备在进行固件升级。

此外，攻击者还可以在受害者设备上播放音乐、重命名设备、重启设备、忘记设备保存的WiFi网络密码、进行蓝牙或WiFi配对等。

**漏洞补丁**

Matt于2021年1月发现了该漏洞，并在3月将漏洞报告给了谷歌，谷歌已于2021年4月修复了该漏洞。Matt也获得了谷歌的10.75万美元漏洞奖励。

完整技术分析参见：https://downrightnifty.me/blog/2022/12/26/hacking-google-home.html

本文翻译自：https://www.bleepingcomputer.com/news/security/google-home-speakers-allowed-hackers-to-snoop-on-conversations/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?09h1NGQv)

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