---
title: 手机指纹暴力破解攻击影响安卓和iOS设备
url: https://www.4hou.com/posts/wyKg
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-25
fetch_date: 2025-10-04T11:38:58.160439
---

# 手机指纹暴力破解攻击影响安卓和iOS设备

手机指纹暴力破解攻击影响安卓和iOS设备 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 手机指纹暴力破解攻击影响安卓和iOS设备

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-05-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)123902

收藏

导语：手机指纹暴力破解攻击影响所有安卓设备和部分iOS设备。

手机指纹暴力破解攻击影响所有安卓设备和部分iOS设备。

暴力破解攻击是指通过多次尝试的方法来破解口令、密码、密钥，以获取账户、系统、网络等的非授权访问。腾讯玄武实验室与浙江大学研究人员提出一种针对手机指纹保护的暴力破解攻击方法——BrutePrint，可暴力破解智能手机指纹以绕过用户认证，并控制设备。

研究人员利用了2个0 day漏洞来绕过智能手机上现有的针对暴力破解的防护措施，比如尝试次数限制和活性检测。这两个漏洞分别是Cancel-After-Match-Fail (CAMF，匹配失败后取消)和Match-After-Lock (MAL，锁定后匹配)。研究人员发现指纹传感器的串行外设接口(Serial Peripheral Interface，SPI)上的生物数据未得到充分的保护，可以通过中间人攻击（MITM）来劫持指纹图像。

**BrutePrint攻击**

BrutePrint攻击的原理是向目标设备提交无数次的指纹图像直到与用户定义的指纹匹配。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684812538137745.png "1684812361332672.png")

图 BrutePrint攻击

BrutePrint攻击的攻击者需要有目标设备的物理访问权限，并能够访问指纹数据库，如学术研究数据库或泄露的指纹数据库，以及大约15美元的攻击设备。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684812541350490.png "1684812387142482.png")

图 发起BrutePrint攻击所需的设备

与密码破解不同，指纹匹配使用的是参考门限而非特定值，因此攻击者可以通过操纵False Acceptance Rate (FAR，错误接受率)来增加接收门限，并更加容易得创建匹配的指纹。

BrutePrint攻击位于指纹传感器与可信执行环境（TEE）之间，利用CAMF漏洞来操纵智能手机指纹认证的多点采样和错误取消机制。CAMF在指纹数据上注入一个错误的校验和以停止认证过程。因此，攻击者可以在目标设备上不断尝试指纹输入，但手机保护机制并不会记录错误的尝试次数，最终实现无限次的尝试。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684812541269922.png "1684812415715730.png")

图 CAMF漏洞攻击逻辑

MAL漏洞使得攻击者可以推断出指纹图像的认证结果，即使设备处于锁定模式。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684812543122593.png "1684812447130820.png")

图  引发MAL漏洞的机制

锁定模式是连续多次输入指纹解锁失败的一种保护机制。在锁定时间内，设备不会接受解锁请求，但MAL漏洞可以帮助绕过这一限制。

BrutePrint攻击使用neural style transfer（神经风格迁移）系统将数据库中的所有指纹图像转换为看似是设备传感器扫描的。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684812545477535.png "1684812482192947.png")

图 根据传感器类型改进图像

**实验数据**

研究人员在10款主流智能手机上对BrutePrint和SPI MITM攻击进行了测试，并成功在所有安卓和鸿蒙设备上实现了无限制尝试次数，并在iOS设备上实现了额外的10次尝试。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684812546179309.png "1684812510701357.png")

图 测试的设备

因为在安卓设备上实现了无限的测试次数，因此只要有足够的时间，攻击者就可以暴露破解安卓设备指纹，并解锁设备。

在iOS设备中，虽然iPhone SE和iPhone 7受到CAMF漏洞的影响，但研究人员只能将指纹攻击的尝试次数增加到15次，还不足以暴露破解指纹并解锁设备。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684812538590697.png "1684812538590697.png")

图 测试结果

对于SPI MITM 攻击，所有受测的安卓设备都可以劫持用户指纹图像，但iPhone不受到该攻击的影响，因为iPhone加密了SPI上的指纹数据，所以拦截数据对攻击没有任何意义。

实验表明，如果设备中只录入了一份指纹，那么完成BrutePrint攻击所需的时间在2.9小时到13.9小时之间。如果目标设备中录入了多个指纹，那么暴力破解所需的时间会减少到0.66小时到2.78小时之间。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230523/1684812570194215.png "1684812570194215.png")

图 暴力破解指纹所需时间

**结论**

总的来看，BrutePrint在针对普通用户的攻击来说可能性不大。但对于犯罪分子和执法机构来说，BrutePrint暴力破解具有现实意义。犯罪分子可以通过暴力破解解锁被窃的设备，并提取出其中的数据。而执法机构通过暴力破解攻击可以在调查取证过程中绕过设备的安全防护。

本文翻译自：https://arxiv.org/pdf/2305.10791.pdf
https://www.bleepingcomputer.com/news/security/android-phones-are-vulnerable-to-fingerprint-brute-force-attacks/
如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?lAcZz4ua)

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