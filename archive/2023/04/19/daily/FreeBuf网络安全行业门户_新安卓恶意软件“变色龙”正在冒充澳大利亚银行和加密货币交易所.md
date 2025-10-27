---
title: 新安卓恶意软件“变色龙”正在冒充澳大利亚银行和加密货币交易所
url: https://www.freebuf.com/news/364003.html
source: FreeBuf网络安全行业门户
date: 2023-04-19
fetch_date: 2025-10-04T11:35:27.013079
---

# 新安卓恶意软件“变色龙”正在冒充澳大利亚银行和加密货币交易所

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

新安卓恶意软件“变色龙”正在冒充澳大利亚银行和加密货币交易所

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新安卓恶意软件“变色龙”正在冒充澳大利亚银行和加密货币交易所

2023-04-18 20:22:11

所属地 海外

##

近日，网络安全公司 Cyble 发现一种名为 Chameleon（“变色龙”）的新安卓恶意软件冒充澳大利亚政府机构 CoinSpot 加密货币交易所和 IKO 银行，通过受损网站、Discord 附件和 Bitbucket 托管服务进行分发，对澳大利亚和波兰的用户展开网络攻击。![1681817591_643e7ff70504826faa948.png!small?1681817591019](https://image.3001.net/images/20230418/1681817591_643e7ff70504826faa948.png!small?1681817591019)

Cyble 的安全研究人员表示 Chameleon 主要通过叠加注入和密钥记录、cookie 和受感染设备的短信窃取用户凭据。

## ****能够逃避安全软件检查****

该恶意软件有很强的逃避安全检查能力，一旦启动后会立即执行各种“检查”，以逃避安全软件的检测。（据悉，“检查”主要包括反仿真检查，以检测设备是否已扎根并激活调试，从而增加恶意软件应用程序在系统安全环境中运行的可能性。）

如果检查结果显示受害系统环境很“干净”，Chameleon 就会请求受害者允许其使用无障碍服务，并滥用该服务授予自身额外的权限，以期禁用 Google Play Protect。![1681817600_643e8000e602b853eceee.png!small?1681817600762](https://image.3001.net/images/20230418/1681817600_643e8000e602b853eceee.png!small?1681817600762)

请求允许使用无障碍服务（Cyble)

在与 C2 第一次连接时， 为了解最新的感染情况，Chameleon 灰发送设备版本、型号、根状态、国家和精确位置。接下来，根据恶意软件模拟的实体，它会在 WebView 中打开其合法 URL，并开始在后台加载恶意模块。

值得一提的事，这些模块包括一个 cookie 窃取器、一个键盘记录器、一个网络钓鱼页面注射器、一个锁屏 PIN/模式抓取器，以及一个可以窃取一次性密码并帮助攻击者绕过 2FA 保护的短信窃取器。![1681817610_643e800a06022559a8408.png!small?1681817610050](https://image.3001.net/images/20230418/1681817610_643e800a06022559a8408.png!small?1681817610050)

短信拦截（Cyble）

研究人员分析后发现上述恶意模块大多依赖可访问性服务滥用来按需工作，从而使 Chameleon 恶意软件能够监控屏幕内容、监控特定事件、进行干预以修改界面元素，或根据需要发送某些 API 调用。![1681870387_643f4e33e36a7578adc6f.png!small?1681870387736](https://image.3001.net/images/20230419/1681870387_643f4e33e36a7578adc6f.png!small?1681870387736)

滥用无障碍服务来检索锁屏密码（Cyble）

一部分恶意模块被用于阻止恶意软件的卸载，识别受害者何时试图删除恶意应用程序，并删除其共享的首选项变量，使其看起来好像不再存在于设备中。![1681870475_643f4e8bd4774d04d4cf9.png!small?1681870475740](https://image.3001.net/images/20230419/1681870475_643f4e8bd4774d04d4cf9.png!small?1681870475740)

自动删除共享首选项变量（Cyble）

共享的首选项变量的擦除使得 Chameleon 恶意应用程序在下次启动时重新建立与 C2 的通信，但阻止了其卸载，并使研究人员更难进行分析。

Cyble 还观察到一些代码，这些代码使 Chameleon 能够在运行时下载有效负载，并将其保存在主机上作为“.jar”文件，稍后通过 DexClassLoader 执行，但此功能目前尚未使用。![1681817634_643e80222cab738633fd1.png!small?1681817633805](https://image.3001.net/images/20230418/1681817634_643e80222cab738633fd1.png!small?1681817633805)

下载额外有效载荷的代码(Cyble)

Chameleon 作为一种新兴恶意软件威胁，可能会在未来的版本中增加更多的功能，因此网络安全专家建议安卓用户保持谨慎安装应用程序，只从官方商店下载软件，并确保其设备始终启用了Google Play Protect。

**文章来源：**

> https://www.bleepingcomputer.com/news/security/new-chameleon-android-malware-mimics-bank-govt-and-crypto-apps/

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

能够逃避安全软件检查

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)